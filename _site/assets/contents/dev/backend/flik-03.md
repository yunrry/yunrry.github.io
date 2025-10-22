# FLIK: 여행코스 추천 서비스 개발기 - (백엔드 3편) 


  
# 관광지 데이터, 어떻게 요리할까 🍳

> **데이터 수집 → 정제 → 저장**까지의 설계와 시행착오

---

## 🏁 공모전 조건: TourAPI 필수 사용

FLIK은 “2025 관광데이터 공모전” 참가 조건에 따라  
**한국관광공사 TourAPI (공공데이터포털 제공)** 를 반드시 활용해야 했다.  
그래서 개발 초기엔 다음 순서로 데이터 수집 인프라를 준비했다.  

1️⃣ **API 키 발급**

* 공공데이터포털에서 *국문 관광정보 API* 사용 신청  
* 개발용 계정 기준 **일일 1,000건 트래픽 제한**  
  → 테스트 중에는 호출 제한이 금방 걸림 (batch로 제어 필요)  

2️⃣ **응답 구조 분석**

* TourAPI는 XML/JSON 응답을 모두 지원하지만,  
  구조가 깊고 key 이름이 일정하지 않아 parsing 이슈가 있었다.  
* 예: `addr1`, `addr2`, `cat1`, `cat2`, `cat3` ... 같은 다단계 필드 존재  
  → 이후 **label_depth1/2 매핑 규칙 테이블**로 관리

3️⃣ **content_type_id 별 데이터 분리 수집**  
TourAPI는 `content_type_id`에 따라 관광지 유형이 다르다.  
FLIK에서는 이를 내부적으로 **도메인별 테이블**에 매핑했다.  

| content_type_id | 수집 데이터   | 내부 저장 테이블                     |
| --------------- | -------- | ----------------------------- |
| 12              | 관광지      | `fetched_tourist_attractions` |
| 14              | 문화시설     | `fetched_cultural_facilities` |
| 15              | 축제/공연/행사 | `fetched_festivals_events`    |
| 28              | 레포츠      | `fetched_sports_recreation`   |
| 32              | 숙박       | `fetched_accommodations`      |
| 38              | 쇼핑       | `fetched_shopping`            |
| 39              | 음식점      | `fetched_restaurants`         |

---

## ⚙️ 배치 서버 설계: 데이터 수집의 심장

초기엔 FLIK 메인 서버에서 API 호출을 직접 처리했지만,  
**트래픽 제어와 스케줄링 효율**을 위해 **별도 배치 서버**를 구성했다.  

> 🎯 목적:
> 외부 API를 주기적으로 호출 → 가공 → MySQL 저장  
> (추후 Redis 캐시 및 검색엔진 확장 고려)  

### 구조 설계

```
Scheduler (Spring Batch)
   ↓
TourAPIClient (RestTemplate)
   ↓
Raw Data (JSON/XML)
   ↓
DataParser (정제 로직)
   ↓
SpotEntity (도메인 매핑)
   ↓
MySQL 저장
```

* **Scheduler**: `@Scheduled(cron="0 0 1 * * ?")`
  → 매일 새벽 1시에 수집 시작
* **TourAPIClient**: `RestTemplate` 기반 외부 호출
  → content_type_id별로 endpoint 반복 호출
* **Parser**: 공공데이터 필드 불일치 처리
  → 누락 필드 보정, `label_depth` 매핑, 주소 정제
* **Repository**: JPA 기반 영속화
  → `fetched_*` 임시테이블 → 정제 후 `spot` 본테이블로 마이그레이션

---

## 🧩 데이터 정제 로직

TourAPI 응답은 단순하지 않다.
카테고리(`cat1`, `cat2`, `cat3`)와 지역정보(`areacode`, `sigungucode`)를  
FLIK의 자체 비즈니스 분류(`역사문화`, `자연`, `카페` 등)로 **매핑**해야 했다.  

### label_depth 매핑 예시

| label_depth1 | label_depth2 | FLIK 카테고리 |
| ------------ | ------------ | --------- |
| A02          | A0201        | 역사문화      |
| A05          | A0502        | 전통시장      |
| C01          | C0112        | 카페        |
| A03          | A0302        | 테마파크      |
| A01          | A0101        | 자연        |
| A04          | A0401        | 실내여행지     |
| A06          | A0601        | 액티비티      |

> 📌 최종적으로 `spot` 테이블에는 `category` 컬럼이 FLIK 내부 분류로 저장됨.  
> API 응답의 복잡한 코드 체계를 사람이 이해할 수 있는 형태로 단순화.  

---

## ⚠️ 트러블슈팅: 우리가 부딪힌 문제들  

### 1️⃣ 응답 필드 누락  

* TourAPI 응답에서 특정 필드가 비정상적으로 null로 오는 경우 존재  
* 예: `cat3`가 없는 데이터
  → `Optional.ofNullable()` + 기본값 처리로 대응

### 2️⃣ 중복 데이터 발생

* 동일한 관광지가 content_type_id가 다르게 등록된 케이스 발견  
  → `contentid`를 기준으로 중복 필터링  

### 3️⃣ API 호출 제한 (1000건/day)

* 테스트 중 연속 요청 시 금방 제한 도달
  → content_type_id별 호출 분리 + 딜레이(`Thread.sleep`) 적용  
  → 배치 실행 시 로그 기록 (`fetch_log` 테이블)

### 4️⃣ 인코딩 문제

* 응답에 특수문자, HTML entity가 섞여 있음
  → Apache Commons `StringEscapeUtils.unescapeHtml4()` 사용  

---

## 💾 결과: 정제된 관광 데이터베이스

최종적으로 다음과 같은 형태로 정제 데이터가 저장된다.  

| 컬럼              | 설명        |
| --------------- | --------- |
| id              | PK        |
| title           | 장소명       |
| address         | 주소        |
| category        | 비즈니스 카테고리 |
| content_type_id | 원본 분류코드   |
| image_urls      | 대표 이미지    |
| description     | 설명        |
| phone           | 연락처       |
| lat/lng         | 좌표        |
| reg_date        | 등록일       |

---

## 📅 다음 이야기 예고

데이터를 가져와서 저장했다면,  
이제 그걸 “사용자에게 어떻게 보여줄지”가 남았다.    
다음 편에서는 **데이터 검색 및 추천 시스템 설계**를 다룬다.  
(사용자 스와이프 패턴 + 카테고리 벡터 기반 추천 로직)  

> 🔜 4편 예고: “나에게 맞는 여행지는 무엇일까?”

---

