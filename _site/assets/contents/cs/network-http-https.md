# 5. HTTP vs HTTPS

## 📊 비교표

| 구분 | HTTP | HTTPS |
|------|------|-------|
| **보안** | 없음 ✘ | 암호화 ✔ |
| **포트** | 80 | 443 |
| **프로토콜** | HTTP | HTTP + SSL/TLS |
| **속도** | 빠름 ✔ | 약간 느림 (암호화) |
| **인증서** | 불필요 | 필요 ✔ |
| **URL** | http:// | https:// |
| **SEO** | 불리 | 유리 ✔ |
| **신뢰도** | 낮음 | 높음 ✔ |

---

## 🔴 HTTP (HyperText Transfer Protocol)

### 특징

```
✔ 빠른 속도
✔ 간단한 구현
✘ 보안 없음
✘ 데이터 평문 전송
✘ 중간자 공격 취약

포트: 80
암호화: 없음
```

### HTTP 통신 과정

```
Client                    Server
   |                         |
   |  1. HTTP Request       |
   |  GET /index.html       |
   |----------------------->|
   |                         |
   |  2. HTTP Response      |
   |  200 OK                |
   |  <html>...</html>      |
   |<-----------------------|
   |                         |

데이터: 평문 전송 (누구나 읽을 수 있음) ✘
```

### HTTP 메시지 구조

```
요청 (Request):
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

응답 (Response):
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>
  <body>Hello World</body>
</html>
```

### HTTP 메서드

```
GET: 데이터 조회
POST: 데이터 생성
PUT: 데이터 전체 수정
PATCH: 데이터 일부 수정
DELETE: 데이터 삭제
HEAD: 헤더만 조회
OPTIONS: 지원 메서드 확인
```

### HTTP 상태 코드

```
1xx: 정보
- 100 Continue

2xx: 성공
- 200 OK
- 201 Created
- 204 No Content

3xx: 리다이렉션
- 301 Moved Permanently
- 302 Found
- 304 Not Modified

4xx: 클라이언트 오류
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found

5xx: 서버 오류
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable
```

---

## 🔒 HTTPS (HTTP Secure)

### 특징

```
✔ 데이터 암호화
✔ 무결성 보장
✔ 인증서로 신원 확인
✔ SEO 우대
✘ 약간 느림 (암호화 오버헤드)
✘ 인증서 비용

포트: 443
암호화: SSL/TLS
```

### HTTPS 통신 과정

```
Client                    Server
   |                         |
   |  1. TCP 3-Way          |
   |     Handshake          |
   |<---------------------->|
   |                         |
   |  2. SSL/TLS Handshake  |
   |  - 인증서 확인          |
   |  - 암호화 방식 협상     |
   |  - 세션 키 생성         |
   |<---------------------->|
   |                         |
   |  3. HTTP 통신 (암호화)  |
   |  GET /index.html       |
   |  (암호화된 데이터)      |
   |<---------------------->|
   |                         |

데이터: 암호화 전송 (제3자가 읽을 수 없음) ✔
```

### SSL/TLS Handshake 상세

```
1. Client Hello:
   - 지원하는 암호화 방식 목록
   - 랜덤 데이터

2. Server Hello:
   - 선택한 암호화 방식
   - 서버 인증서 (공개키 포함)
   - 랜덤 데이터

3. Client 인증서 검증:
   - CA (인증 기관) 확인
   - 유효 기간 확인
   - 도메인 확인

4. 세션 키 생성:
   - Client가 대칭키 생성
   - 서버 공개키로 암호화하여 전송

5. 암호화 통신 시작:
   - 대칭키로 데이터 암호화
   - 빠른 속도 유지
```

### 암호화 방식

```
비대칭 키 암호화 (공개키/개인키):
- 용도: 세션 키 교환
- 느림
- RSA, ECC

대칭 키 암호화:
- 용도: 실제 데이터 암호화
- 빠름
- AES, DES

하이브리드 방식:
1. 비대칭 키로 세션 키 교환 (안전)
2. 세션 키로 데이터 암호화 (빠름)
```

### SSL 인증서

```
구성 요소:
- 도메인 정보
- 공개키
- 인증 기관(CA) 서명
- 유효 기간

종류:
1. DV (Domain Validation):
   - 도메인 소유 확인만
   - 저렴, 빠름

2. OV (Organization Validation):
   - 조직 정보 확인
   - 중간 수준

3. EV (Extended Validation):
   - 엄격한 검증
   - 주소창 녹색 표시
   - 비싸고 오래 걸림

발급 기관 (CA):
- Let's Encrypt (무료)
- DigiCert
- Comodo
- GeoTrust
```

---

## 🔐 HTTPS 보안 기능

### 1. 암호화 (Encryption)

```
평문 데이터를 암호화하여 전송

예:
평문: "password123"
암호화: "3kd9fj2ksd9fj23k"

→ 중간자가 가로채도 해독 불가 ✔
```

### 2. 무결성 (Integrity)

```
데이터 변조 방지

해시 함수 사용:
- 데이터에서 해시 생성
- 수신자가 해시 재계산
- 같으면 변조 없음 ✔

예:
원본: "Hello" → 해시: abc123
변조: "World" → 해시: def456
→ 해시가 달라서 변조 감지
```

### 3. 인증 (Authentication)

```
서버의 신원 확인

인증서로 확인:
- 서버가 주장하는 도메인이 맞는가?
- 신뢰할 수 있는 CA가 발급했는가?
- 유효 기간 내인가?

→ 피싱 사이트 방지 ✔
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
HTTP:
- 평문 통신
- 포트 80
- 빠르지만 보안 없음

HTTPS:
- 암호화 통신 (SSL/TLS)
- 포트 443
- 안전하지만 약간 느림
- 인증서 필요

차이점:
- 보안: HTTPS만 암호화
- SEO: HTTPS 우대
- 신뢰도: HTTPS 높음
```

### 상세 답변
```
HTTP (HyperText Transfer Protocol):

특징:
- 평문으로 데이터 전송
- 포트 80 사용
- 빠른 속도
- 구현 간단

문제점:
- 데이터 도청 가능
- 중간자 공격 취약
- 데이터 변조 가능
- 서버 신원 확인 불가

HTTPS (HTTP Secure):

특징:
- HTTP + SSL/TLS 암호화
- 포트 443 사용
- 데이터 암호화
- 인증서로 신원 확인

동작 원리:
1. TCP 연결 수립
2. SSL/TLS Handshake:
   - 암호화 방식 협상
   - 인증서 검증
   - 세션 키 교환
3. 암호화된 HTTP 통신

암호화:
- 비대칭 키: 세션 키 교환
- 대칭 키: 데이터 암호화
- 하이브리드 방식 사용

보안 기능:
1. 암호화: 데이터 보호
2. 무결성: 변조 방지
3. 인증: 신원 확인

장점:
- 보안성 높음
- SEO 우대
- 사용자 신뢰
- 법적 요구사항 충족

단점:
- 약간의 성능 오버헤드
- 인증서 관리 필요
- 인증서 비용 (무료도 있음)

현재:
- 대부분의 웹사이트가 HTTPS 사용
- 브라우저에서 HTTP 경고 표시
- Let's Encrypt로 무료 인증서 제공
```