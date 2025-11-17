# 12. CDN (Content Delivery Network)

## 📌 개념

```
전 세계에 분산된 서버 네트워크
- 콘텐츠를 사용자와 가까운 곳에서 제공
- 빠른 속도
- 서버 부하 분산
```

### 기본 원리

```
CDN 없이:
한국 사용자 → 미국 서버 (느림) ✘
        14,000km 거리

CDN 사용:
한국 사용자 → 한국 CDN 서버 (빠름) ✔
        근거리
```

---

## 🌍 CDN 구조

### 글로벌 분산

```
Origin Server (원본 서버):
- 미국 (본사)

Edge Servers (엣지 서버):
- 서울
- 도쿄
- 싱가포르
- 프랑크푸르트
- 런던
- 뉴욕
- 시드니
...전 세계 수백 곳

사용자는 가장 가까운 Edge Server 접속 ✔
```

### 계층 구조

```
          [Origin Server]
                 |
         [Regional Cache]
          /      |      \
    [Edge]   [Edge]   [Edge]
     / \      / \      / \
  Users   Users    Users

3단계:
1. Origin: 원본 콘텐츠
2. Regional: 지역별 캐시
3. Edge: 최종 사용자와 가까움
```

---

## 🔄 CDN 동작 과정

### 첫 요청 (Cache Miss)

```
1. 사용자 요청:
   한국 사용자 → "example.com/image.jpg"

2. DNS 조회:
   example.com → 가장 가까운 CDN 서버 IP
   → 서울 CDN 서버

3. 서울 CDN 확인:
   image.jpg 있나? → 없음 (Cache Miss)

4. Origin에서 가져옴:
   서울 CDN → Origin Server (미국)
   image.jpg 다운로드

5. 캐싱 및 응답:
   서울 CDN에 저장
   사용자에게 응답

첫 요청: 느림 (Origin까지 가야 함)
```

### 이후 요청 (Cache Hit)

```
1. 사용자 요청:
   다른 한국 사용자 → "example.com/image.jpg"

2. DNS 조회:
   서울 CDN 서버

3. 서울 CDN 확인:
   image.jpg 있음! (Cache Hit) ✔

4. 즉시 응답:
   서울 CDN → 사용자
   (Origin 접속 불필요)

이후 요청: 매우 빠름 ✔
```

---

## 🎯 CDN 주요 기능

### 1. 캐싱

```
정적 콘텐츠 저장:
- 이미지 (JPG, PNG, GIF)
- 동영상 (MP4, WebM)
- CSS, JavaScript
- 폰트 파일
- 문서 (PDF)

TTL (Time To Live):
- 캐시 유효 시간 설정
- 예: 1일, 1주일, 1개월

Cache-Control 헤더:
Cache-Control: max-age=86400
→ 24시간 캐싱
```

### 2. 지리적 분산

```
Geo-Routing (지역 기반 라우팅):

한국 사용자 → 서울 CDN
일본 사용자 → 도쿄 CDN
미국 사용자 → 뉴욕 CDN

기준:
- 물리적 거리
- 네트워크 지연(Latency)
- 서버 부하

효과:
- 빠른 응답 속도
- 낮은 지연시간
```

### 3. 로드 밸런싱

```
여러 CDN 서버에 트래픽 분산

서울 CDN:
- Server 1: 60% 부하
- Server 2: 40% 부하
- Server 3: 50% 부하

새 요청 → Server 2 (부하 낮음)

효과:
- 고가용성
- 장애 대응
```

### 4. DDoS 방어

```
분산 서비스 거부 공격 방어

공격:
- 1억 개 요청/초

CDN:
- 전 세계 서버에 분산
- 각 서버: 10만 개/초
- 감당 가능 ✔

Origin Server:
- 직접 공격 안 받음
- CDN이 보호
```

### 5. SSL/TLS

```
HTTPS 지원

CDN에서 SSL 종료:
User ←[HTTPS]→ CDN ←[HTTP/HTTPS]→ Origin
      암호화          선택 가능

장점:
- 빠른 SSL 처리
- 인증서 중앙 관리
```

### 6. 압축

```
자동 압축 (Gzip, Brotli)

Origin: 10MB HTML
  ↓ CDN 압축
User: 2MB 전송

효과:
- 대역폭 절약
- 빠른 로딩
```

### 7. 이미지 최적화

```
자동 변환:
- WebP 지원 브라우저 → WebP
- 구형 브라우저 → JPEG/PNG

크기 조정:
- 원본: 4000x3000
- 모바일: 800x600 (자동 리사이징)

효과:
- 용량 감소
- 빠른 로딩
```

---

## 📊 CDN 종류

### Push CDN

```
원본 서버가 콘텐츠를 CDN에 직접 업로드

동작:
1. 개발자가 콘텐츠 업로드
2. CDN이 모든 서버에 복제
3. 사용자 요청 시 즉시 제공

장점:
- 항상 캐시됨
- 빠른 응답

단점:
- 수동 관리
- 저장 공간 사용

사용:
- 변경이 적은 콘텐츠
- 정적 사이트
```

### Pull CDN

```
사용자 요청 시 Origin에서 가져옴

동작:
1. 사용자 요청
2. CDN에 없으면 Origin에서 가져옴
3. CDN에 캐싱
4. 이후 요청은 캐시 제공

장점:
- 자동화
- 저장 공간 효율적

단점:
- 첫 요청 느림

사용:
- 대부분의 웹사이트 (일반적) ✔
```

---

## 🏢 주요 CDN 제공자

### 1. Cloudflare

```
특징:
- 무료 플랜 제공
- 글로벌 네트워크
- DDoS 방어
- DNS 서비스

위치:
- 전 세계 200+ 도시
```

### 2. AWS CloudFront

```
특징:
- AWS 통합
- S3, EC2 연동
- Lambda@Edge

가격:
- 사용량 기반
```

### 3. Akamai

```
특징:
- 가장 오래된 CDN
- 엔터프라이즈급
- 고성능

점유율:
- 전 세계 1위
```

### 4. Fastly

```
특징:
- 실시간 캐시 제거
- VCL (Varnish Configuration Language)
- 엣지 컴퓨팅

사용:
- GitHub, Stripe
```

### 5. Google Cloud CDN

```
특징:
- Google 네트워크
- GCP 통합
- YouTube 인프라 활용
```

---

## 💻 CDN 설정 예시

### Cloudflare 설정

```
1. DNS 설정:
example.com → Cloudflare Nameserver

2. Cloudflare에서:
- SSL/TLS 설정
- 캐싱 규칙 설정
- 압축 활성화

3. 자동:
- 모든 트래픽이 Cloudflare 경유
- 정적 콘텐츠 자동 캐싱
```

### AWS CloudFront 설정

```javascript
// CloudFront Distribution 생성
{
  "Origins": [{
    "DomainName": "example.s3.amazonaws.com",
    "Id": "S3-example"
  }],
  "DefaultCacheBehavior": {
    "TargetOriginId": "S3-example",
    "ViewerProtocolPolicy": "redirect-to-https",
    "AllowedMethods": ["GET", "HEAD"],
    "CachedMethods": ["GET", "HEAD"],
    "Compress": true,
    "DefaultTTL": 86400  // 1일
  }
}
```

### Cache-Control 헤더

```
정적 리소스:
Cache-Control: public, max-age=31536000, immutable
→ 1년 캐싱, 변경 안 됨

HTML:
Cache-Control: public, max-age=3600, must-revalidate
→ 1시간 캐싱, 재검증 필요

동적 콘텐츠:
Cache-Control: no-cache, no-store, must-revalidate
→ 캐싱 안 함
```

---

## 📈 CDN 성능 측정

### 주요 지표

```
1. Hit Ratio (캐시 적중률):
   캐시 Hit / 전체 요청
   목표: 90% 이상

2. Origin 부하:
   Origin 요청 수
   목표: 최소화

3. 응답 시간:
   TTFB (Time To First Byte)
   목표: <100ms

4. 대역폭 절약:
   CDN으로 절약된 대역폭
   목표: 70% 이상
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
CDN은 전 세계에 분산된 캐시 서버 네트워크입니다.

동작:
1. 사용자 요청
2. 가장 가까운 CDN 서버 연결
3. 캐시 있으면 즉시 응답 (빠름)
4. 없으면 Origin에서 가져와 캐싱

장점:
- 빠른 속도
- 서버 부하 감소
- DDoS 방어

사용:
- 이미지, 동영상
- CSS, JavaScript
```

### 상세 답변
```
CDN (Content Delivery Network):

정의:
전 세계에 분산된 서버 네트워크로
콘텐츠를 사용자와 가까운 곳에서 제공

구성:
1. Origin Server: 원본 콘텐츠 서버
2. Edge Server: 전 세계 캐시 서버
3. DNS: 가장 가까운 서버 안내

동작 과정:

1. DNS 조회:
   - example.com 요청
   - 가장 가까운 CDN 서버 IP 반환
   - 지리적 위치, 네트워크 지연 고려

2. Cache Hit (캐시 있음):
   - Edge Server에 콘텐츠 있음
   - 즉시 응답 (매우 빠름) ✔
   - Origin 접속 불필요

3. Cache Miss (캐시 없음):
   - Edge Server에 콘텐츠 없음
   - Origin Server에서 가져옴
   - Edge Server에 캐싱
   - 사용자에게 응답
   - 다음 요청은 Cache Hit

주요 기능:

1. 지리적 분산:
   - 전 세계 수백 개 서버
   - 사용자와 가까운 곳에서 제공
   - 낮은 지연시간

2. 캐싱:
   - 정적 콘텐츠 저장
   - 이미지, 동영상, CSS, JS
   - TTL 설정으로 유효 시간 관리

3. 로드 밸런싱:
   - 여러 서버에 트래픽 분산
   - 고가용성
   - 장애 대응

4. 보안:
   - DDoS 방어 (트래픽 분산)
   - SSL/TLS 지원
   - Origin Server 보호

5. 최적화:
   - 자동 압축 (Gzip, Brotli)
   - 이미지 최적화 (WebP 변환)
   - 자동 크기 조정

장점:
✔ 빠른 로딩 속도 (물리적 거리 감소)
✔ 서버 부하 감소 (Origin 보호)
✔ 대역폭 절약 (캐싱)
✔ 고가용성 (분산 구조)
✔ DDoS 방어
✔ 글로벌 확장 용이

단점:
✘ 비용 (트래픽 기반 과금)
✘ 캐시 무효화 복잡
✘ 동적 콘텐츠에는 효과 적음

CDN 종류:

Push CDN:
- 개발자가 콘텐츠 업로드
- 모든 서버에 복제
- 변경 적은 콘텐츠

Pull CDN (일반적):
- 요청 시 자동 캐싱
- 자동화
- 대부분의 웹사이트

주요 제공자:
- Cloudflare (무료 플랜)
- AWS CloudFront
- Akamai
- Fastly
- Google Cloud CDN

실무 활용:
- 웹사이트 (정적 리소스)
- 동영상 스트리밍 (Netflix, YouTube)
- 소프트웨어 배포 (npm, Docker Hub)
- 게임 (대용량 다운로드)
- API (엣지 컴퓨팅)

설정:
- DNS를 CDN으로 변경
- Origin Server 지정
- 캐싱 규칙