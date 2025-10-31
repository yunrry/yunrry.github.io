# FLIK: 여행코스 추천 서비스 개발기 (백엔드 2편)
**Raspberry Pi 위에서 돌아가는 카드 스와이프 & 여행코스 추천 서비스 – 도메인 설계와 배포 자동화**


---

## ⚙ 배포 자동화

Raspberry Pi 환경에서 안정적인 배포를 위해 **CI/CD + Docker + Nginx**를 활용했다.

### 1. CI/CD (GitHub Actions)

* `push` → 자동 빌드, 테스트, Docker 이미지 생성
* `main` 브랜치 → Blue/Green 배포 트리거

```yaml
#root/.github/workflows/deploy.yml 샘플
name: FLIK CI/CD
on: [push]
env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  RASPBERRY_PI_HOST: ${{ secrets.RASPBERRY_PI_HOST }}
  RASPBERRY_PI_USER: ${{ secrets.RASPBERRY_PI_USER }}
  MYSQL_ROOT_PASSWORD: ${{ secrets.MYSQL_ROOT_PASSWORD }}
  MYSQL_DATABASE: ${{ secrets.MYSQL_DATABASE }}
  #--생략--
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK
        uses: actions/setup-java@v3
        with:
          java-version: '21'
      - name: Cache Gradle packages
        uses: actions/cache@v4
      - name: Test Flik Server
        run: |
          chmod +x gradlew
          ./gradlew clean test -Dspring.profiles.active=test --parallel --max-workers=4
  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
      - name: Build with Gradle
        run: ./gradlew clean build
      - name: Build Docker image
        run: docker build -t flik:latest .
      - name: Push Docker image
        run: docker tag flik:latest myregistry/flik:latest && docker push myregistry/flik:latest
```

---

### 2. Blue/Green 배포

* Nginx를 **로드밸런서**로 설정
* Blue/Green upstream proxy로 **무중단 배포** 구현
* 새 이미지를 배포 후 **Health Check → Traffic Switch**

```nginx
upstream flik-app {
   	 server flik-blue:8080 max_fails=3 fail_timeout=30s;
    	 # server flik-green:8080 max_fails=3 fail_timeout=30s;
      }
```

* Health Check 후 트래픽 전환 (주석 스위치)
* 문제 발생 시 이전 버전으로 **빠른 롤백 가능**

---

### 3. SSL / CDN

* Cloudflare를 이용한 **도메인 등록 + SSL 인증서 적용**
* 외부 API 연동 및 클라이언트 요청 시 HTTPS 통신 보장


---  


  
  
## 🧪 테스트 전략
서비스코드를 작성한 후 테스트코드를 작성하는 것은 내키지 않는다.  
테스트하면 코드가 다 꺠질것 같은 두려움 떄문일까. 이미 구현이 끝난 코드라고 생각하는 안일함 때문일까.   
어떤쪽도 맞는 심리인 것 같다. 수정하기 귀찮고 다음 테스크로 빨리 넘어가고 싶으니...

하지만 테스트는 필요한 과정이다. 조잡하게 코드를 짜다보면 어디서 구멍이 날지 모른다.  
그래서 나는 최대한 **TDD**를 도입하여 선 테스트코드 후 서비스코드 작성 전략을 취하고자 한다.   
즉 요구기능 CRUD 구현은 단위 테스트부터 작성 -> 테스트가 모두 커버되도록 구현한다. 
1. 기능 요구사항 작성
2. 테스트 목표 : CRUD 정상작동 확인. 크리티컬한 예외 발생 확인. 커버리지 80%이상
3. 테스트 케이스 작성 by AI (요구사항과 목표 입력)
4. 테스트 코드 작성 -> 테스트를 만족하는 서비스 구현

* **단위 테스트**: 핵심 비즈니스 로직, 도메인 이벤트 검증 (JUnit 5 + TestContainers)
* **통합 테스트**: REST API + DB + Redis 동작 확인 (MockMVC + Docker Compose)
* **성능 테스트**: 병목 예상 상황 시나리오 설정 -> 부하 테스트 실행 (Jmeter)

**TDD** 테스트 주도 개발(Test-Driven Development)

---



## 🏗 도메인 설계

FLIK의 핵심 기능은 **“스와이프 탐색 → 장소 카드 저장 → 코스 생성”** 이다.
이를 기반으로 도메인을 설계하고, **DDD 원칙**을 준수했다.

### 핵심 도메인

| 도메인         | 역할                               |
| ----------- | -------------------------------- |
| **Spot**    | 관광지 정보 저장, 카드 스와이프 기능과 연결        |
| **Course**  | 사용자가 선택한 Spot들을 모아 코스 생성         |
| **Auth**    | 로그인/회원 정보 관리, OAuth2 + JWT 인증 처리 |
| **User**    | 사용자의 선호 장소 저장, 사용자의 카테고리별 선호벡터 저장 |
| **Post**    | 게시글(여행기, 장소후기) |

### 도메인 모델 샘플 (`Spot`)

```java
public class Spot {
    private final Long id;
    private final String name;
    private final String address;
    private final SpotType type;
    
    // 생성자
    public Spot(Long id, String name, String address, SpotType type) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.type = type;
    }

    // 행동 메서드
    public void updateInfo(String newName, String newAddress) {
        this.name = newName;
        this.address = newAddress;
    }
}
```

* `@Setter`를 쓰지 않고 **메서드 기반 업데이트**  
for **불변성 유지 + 핵심 도메인 로직 내 구현**

---

## API 흐름

FLIK API는 **CQRS 패턴**을 적용해 읽기/쓰기 요청을 분리하기로 했다.

### 예시: 스팟 카드 스와이프 저장
1. **Client → Controller (in adapter/out)**
   `POST /api/spots/save` 요청 전달
2. **Controller → UseCase**
   `SaveSpotUseCase` 호출
3. **UseCase → Service (Core)**
   비즈니스 로직 실행: 사용자가 이미 좋아요 했는지 검증
4. **Service → Repository (out port)**
   JPA Repository 또는 Redis 캐시에 저장
5. **Controller → Response**
   `Response.success()`로 API 응답 반환

이 서비스의 핵심은 사용자의 **스와이프(장소 저장)이벤트**이다.  
'스와이프' 동작이 곧 요청이기 때문에 즉시 응답하고 비동기로 처리하는 로직을 구상했다.  
따라서 장소 저장 요청은 이벤트 발행으로 이어진다.

### 스팟 저장 이벤트 플로우
```
Client → UseCase → EventListener → DB/Service
```
1. **Client**  
   - POST `/api/spots/save` 요청 전송

2. **UseCase**  
   - `SpotSwipeEvent` 발행
   - 이벤트 발행 직후 API 응답: `Response.success()`

3. **EventListener (비동기)**  
   - 이벤트 수신 후 비동기 처리 시작
   - `isAlreadySaved` 체크
   - DB에 저장: `saveUserSpot`
   - 벡터 업데이트: `updateCategoryVector`

4. **DB/Service**  
   - 저장 완료 및 후처리 완료

```text

Client
   |
   v
+-----------------+
| UseCase         |
| (SpotSwipeEvent)|
+-----------------+
   |
   v
 Response.success()  <-- 이벤트 발행 직후 즉시 API 응답
   |
   v
+----------------------+
| EventListener (Async)|
+----------------------+
   |
   +--> check isAlreadySaved?
   |         |
   |         v
   |      already saved? ---+
   |         |               |
   |         v               |
   |     skip save           |
   |                         |
   +--> saveUserSpot         |
   +--> updateCategoryVector |
   |
   v
Listener 처리 완료

```

---

## 배운 점

1. **Hexagonal + DDD 설계** 도메인 중심 개발  
    "어디까지 추상화 해야하나?" 정답은 없다.   
    core와 port를 순회하며 도메인 객체가 어디로부터 어디로 흘러가는지 따라가다보니 역할분리의 효과를 알 수 있었다.

2. **Raspberry Pi + Docker 배포**로 실제 서버 환경을 체험  
        
3. **Blue/Green 배포**로 무중단 서비스 구현 경험  
    - blue/green 스위칭 꼬이면 컨테이너 중단하지 말고 nginx.conf를 수정하렴!   
    - 추가해야할 환경변수 꼭 체크하기 -> 자동화방법 찾기        
4. **TDD + CI/CD**로 테스트 자동화, 안정적 배포

---

## 💬 마무리

2편에서는 FLIK의 **도메인 설계, API 흐름, 배포 자동화**를 중심으로 살펴봤다.
다음 편에서는 **데이터처리 (수집/정제/저장)** 설계와 트러블슈팅을 다룰 예정이다.

> 🔜 3편 예고: “관광지 데이터 어떻게 요리할까"

---