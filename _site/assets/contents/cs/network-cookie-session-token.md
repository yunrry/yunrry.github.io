# 7. 쿠키 vs 세션 vs 토큰

## 📊 비교표

| 구분 | 쿠키 | 세션 | 토큰(JWT) |
|------|------|------|-----------|
| **저장 위치** | 클라이언트 | 서버 | 클라이언트 |
| **보안** | 낮음 ❌ | 높음 ✅ | 중간 |
| **용량** | 4KB | 제한 없음 | 수 KB |
| **속도** | 빠름 ✅ | 느림 (서버 조회) | 빠름 ✅ |
| **확장성** | 좋음 ✅ | 나쁨 (서버 부하) ❌ | 좋음 ✅ |
| **만료** | 설정 가능 | 설정 가능 | 설정 가능 |
| **자동 전송** | ✅ (Same Origin) | ✅ (Session ID) | ❌ (수동) |

---

## 🍪 쿠키 (Cookie)

### 개념

```
클라이언트(브라우저)에 저장되는 작은 데이터 파일
- Key-Value 형태
- 서버가 생성하여 클라이언트에 전달
- 매 요청마다 자동으로 서버에 전송
```

### 동작 과정

```
1. 로그인 요청
Client                    Server
   |                         |
   | POST /login            |
   | username=admin         |
   |----------------------->|
   |                         |
   |  Set-Cookie:           |
   |  sessionId=abc123      |
   |<-----------------------|
   |                         |
(쿠키 저장: sessionId=abc123)

2. 이후 요청 (자동으로 쿠키 전송)
   |                         |
   | GET /profile           |
   | Cookie: sessionId=abc123|
   |----------------------->|
   |                         |
```

### 쿠키 생성

```javascript
// 서버 (Node.js Express)
res.cookie('username', 'admin', {
  maxAge: 3600000,  // 1시간 (밀리초)
  httpOnly: true,    // JavaScript 접근 불가
  secure: true,      // HTTPS만
  sameSite: 'strict' // CSRF 방지
});
```

### 쿠키 속성

```
1. Expires / Max-Age:
   - 만료 시간
   - 설정 안 하면 세션 쿠키 (브라우저 종료 시 삭제)

2. Domain:
   - 쿠키가 전송될 도메인
   - 예: domain=example.com

3. Path:
   - 쿠키가 전송될 경로
   - 예: path=/admin

4. Secure:
   - HTTPS에서만 전송
   
5. HttpOnly:
   - JavaScript로 접근 불가
   - XSS 공격 방지

6. SameSite:
   - Strict: 같은 사이트에서만
   - Lax: GET 요청은 허용
   - None: 모든 사이트 (Secure 필수)
```

### 쿠키 종류

```
1. 세션 쿠키 (Session Cookie):
   - 브라우저 종료 시 삭제
   - 만료 시간 없음

2. 영구 쿠키 (Persistent Cookie):
   - 만료 시간까지 유지
   - 브라우저 종료해도 남음

3. 보안 쿠키 (Secure Cookie):
   - HTTPS에서만 전송

4. HttpOnly 쿠키:
   - JavaScript 접근 불가
```

### 장단점

```
장점:
✅ 자동 전송
✅ 구현 간단
✅ 서버 부하 없음

단점:
❌ 보안 취약 (클라이언트 저장)
❌ 용량 제한 (4KB)
❌ XSS 공격 위험
❌ 모바일 앱에서 사용 어려움
```

---

## 🔐 세션 (Session)

### 개념
```
서버에 저장되는 사용자 정보
- 클라이언트는 Session ID만 보관
- 실제 데이터는 서버에 안전하게 저장
- 쿠키를 이용해 Session ID 전달
```

### 동작 과정

```
1. 로그인
Client                    Server
   |                         |
   | POST /login            |
   | username=admin         |
   | password=1234          |
   |----------------------->|
   |                         |
   |                    (세션 생성)
   |                    Session Store:
   |                    sessionId: abc123
   |                    user: {id:1, name:"admin"}
   |                         |
   |  Set-Cookie:           |
   |  sessionId=abc123      |
   |<-----------------------|
   |                         |
(쿠키 저장: sessionId=abc123)

2. 인증된 요청
   |                         |
   | GET /profile           |
   | Cookie: sessionId=abc123|
   |----------------------->|
   |                         |
   |                    (세션 조회)
   |                    Session Store에서
   |                    abc123 찾기
   |                    → user 정보 반환
   |                         |
   |  User Profile Data     |
   |<-----------------------|
   |                         |

3. 로그아웃
   |                         |
   | POST /logout           |
   | Cookie: sessionId=abc123|
   |----------------------->|
   |                         |
   |                    (세션 삭제)
   |                    Session Store에서
   |                    abc123 제거
   |                         |
   |  Set-Cookie:           |
   |  sessionId=; expires=0 |
   |<-----------------------|
   |                         |
```

### 세션 저장소

```
1. 메모리 (개발 환경):
   - 빠름
   - 서버 재시작 시 삭제
   - 단일 서버만 가능

2. Redis (추천):
   - 빠름 (인메모리 DB)
   - 영구 저장 가능
   - 여러 서버 공유 가능

3. 데이터베이스:
   - 영구 저장
   - 느림
   - 안정적

4. 파일 시스템:
   - 간단
   - 느림
   - 관리 어려움
```

### 세션 구현 예시

```javascript
// Node.js Express + Redis
const session = require('express-session');
const RedisStore = require('connect-redis')(session);
const redis = require('redis');

const redisClient = redis.createClient();

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'my-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24, // 1일
    httpOnly: true,
    secure: true
  }
}));

// 로그인
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  // 인증 확인
  if (authenticate(username, password)) {
    // 세션에 사용자 정보 저장
    req.session.user = {
      id: 1,
      username: username
    };
    res.send('Login success');
  }
});

// 인증 확인
app.get('/profile', (req, res) => {
  if (req.session.user) {
    res.json(req.session.user);
  } else {
    res.status(401).send('Unauthorized');
  }
});

// 로그아웃
app.post('/logout', (req, res) => {
  req.session.destroy();
  res.send('Logout success');
});
```

### 장단점

```
장점:
✅ 보안성 높음 (서버 저장)
✅ 용량 제한 없음
✅ 서버에서 제어 가능

단점:
❌ 서버 메모리/저장소 사용
❌ 서버 부하 증가
❌ 확장성 낮음 (여러 서버 시)
❌ Redis 등 추가 인프라 필요
```

---

## 🎫 토큰 (JWT - JSON Web Token)

### 개념

```
JSON 형태의 자체 포함 토큰
- 서버에 저장하지 않음
- 토큰 자체에 정보 포함
- 서명으로 무결성 검증
```

### JWT 구조

```
Header.Payload.Signature

예:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

1. Header (헤더):
{
  "alg": "HS256",      // 알고리즘
  "typ": "JWT"         // 타입
}

2. Payload (페이로드):
{
  "sub": "1234567890", // 사용자 ID
  "name": "John Doe",  // 사용자 이름
  "iat": 1516239022,   // 발급 시간
  "exp": 1516242622    // 만료 시간
}

3. Signature (서명):
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

### 동작 과정

```
1. 로그인 (토큰 발급)
Client                    Server
   |                         |
   | POST /login            |
   | username=admin         |
   | password=1234          |
   |----------------------->|
   |                         |
   |                    (JWT 생성)
   |                    Header + Payload + Signature
   |                         |
   |  Response:             |
   |  {                     |
   |    token: "eyJhbG..."  |
   |  }                     |
   |<-----------------------|
   |                         |
(토큰 저장: localStorage/sessionStorage)

2. 인증된 요청
   |                         |
   | GET /profile           |
   | Authorization:         |
   | Bearer eyJhbG...       |
   |----------------------->|
   |                         |
   |                    (토큰 검증)
   |                    1. 서명 확인
   |                    2. 만료 확인
   |                    3. Payload 추출
   |                         |
   |  User Profile Data     |
   |<-----------------------|
   |                         |

3. 로그아웃
   |                         |
   | POST /logout           |
   |----------------------->|
   |                         |
(토큰 삭제: localStorage에서 제거)
```

### JWT 생성/검증 코드

```javascript
// Node.js
const jwt = require('jsonwebtoken');
const SECRET_KEY = 'my-secret-key';

// 토큰 생성
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  if (authenticate(username, password)) {
    const payload = {
      id: 1,
      username: username
    };
    
    const token = jwt.sign(
      payload,
      SECRET_KEY,
      { expiresIn: '1h' }  // 1시간 후 만료
    );
    
    res.json({ token });
  }
});

// 토큰 검증 미들웨어
function verifyToken(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  
  if (!token) {
    return res.status(401).send('No token');
  }
  
  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).send('Invalid token');
  }
}

// 인증 필요한 라우트
app.get('/profile', verifyToken, (req, res) => {
  res.json(req.user);
});
```

### JWT Payload 표준 클레임

```
등록된 클레임 (Registered Claims):
- iss (issuer): 발급자
- sub (subject): 주제 (사용자 ID)
- aud (audience): 대상
- exp (expiration): 만료 시간
- nbf (not before): 활성 시작 시간
- iat (issued at): 발급 시간
- jti (JWT ID): 고유 식별자

공개 클레임 (Public Claims):
- 사용자 정의 (충돌 방지 필요)

비공개 클레임 (Private Claims):
- 당사자 간 합의한 정보
- 예: name, email, role
```

### Refresh Token

```
문제:
- Access Token 만료 시간이 짧음 (15분)
- 자주 재로그인 불편

해결:
Access Token + Refresh Token 방식

Access Token:
- 짧은 만료 시간 (15분)
- API 요청에 사용

Refresh Token:
- 긴 만료 시간 (7일)
- Access Token 재발급에 사용
- HttpOnly 쿠키에 저장

동작:
1. 로그인 → Access + Refresh Token 발급
2. API 요청 → Access Token 사용
3. Access Token 만료 → Refresh Token으로 재발급
4. Refresh Token도 만료 → 재로그인
```

### 장단점

```
장점:
✅ Stateless (서버 저장 불필요)
✅ 확장성 좋음 (여러 서버)
✅ 모바일 앱 친화적
✅ 서버 부하 적음
✅ CORS 문제 없음

단점:
❌ 토큰 크기 큼 (쿠키보다)
❌ 탈취 시 만료까지 유효
❌ Payload 노출 (암호화 안 됨)
❌ 강제 로그아웃 어려움
```

---

## 🔄 쿠키 vs 세션 vs 토큰 상세 비교

### 보안

```
쿠키:
- 클라이언트 저장
- JavaScript로 접근 가능 (HttpOnly 없으면)
- XSS 공격 위험
- 보안: 낮음 ❌

세션:
- 서버 저장
- Session ID만 클라이언트
- 중요 정보는 서버에
- 보안: 높음 ✅

토큰:
- 클라이언트 저장
- Payload 노출 (Base64)
- 서명으로 무결성 보장
- 보안: 중간
```

### 확장성 (Scale-Out)

```
쿠키:
- 서버 상태 없음
- 확장성: 좋음 ✅

세션:
- 서버마다 세션 다름
- Sticky Session 또는 중앙 저장소 필요
- 확장성: 나쁨 ❌

[Server1] ─┐
[Server2] ─┼─ Redis (세션 저장소)
[Server3] ─┘

토큰:
- 서버 상태 없음
- 어느 서버든 검증 가능
- 확장성: 좋음 ✅
```

### 성능

```
쿠키:
- 자동 전송
- 서버 조회 없음
- 성능: 좋음 ✅

세션:
- 매 요청마다 저장소 조회
- Redis 사용 시 빠름
- 성능: 중간

토큰:
- 서버 조회 없음
- 서명 검증만
- 성능: 좋음 ✅
```

### 만료/로그아웃

```
쿠키:
- 만료 시간 설정
- 클라이언트에서 삭제
- 제어: 약함

세션:
- 서버에서 삭제 가능
- 강제 로그아웃 가능
- 제어: 강함 ✅

토큰:
- 만료 시간 설정
- 강제 만료 어려움
- Blacklist 필요
- 제어: 약함
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
쿠키:
- 클라이언트 저장 (4KB)
- 자동 전송
- 보안 낮음

세션:
- 서버 저장 (무제한)
- Session ID만 클라이언트
- 보안 높음, 확장성 낮음

토큰 (JWT):
- 클라이언트 저장
- 자체 포함 (Payload)
- Stateless, 확장성 높음

선택:
- 단순 데이터 → 쿠키
- 전통적 웹 → 세션
- REST API, 모바일 → JWT
```

### 상세 답변
```
쿠키 (Cookie):

특징:
- 클라이언트(브라우저)에 저장
- Key-Value 형태
- 자동으로 서버에 전송

장점:
- 구현 간단
- 서버 부하 없음

단점:
- 보안 취약 (XSS 공격)
- 용량 제한 (4KB)
- 모바일 앱에서 어려움

사용:
- 언어 설정, 테마 등
- 간단한 사용자 기본 설정

세션 (Session):

특징:
- 서버에 저장
- Session ID만 클라이언트 (쿠키)
- 실제 데이터는 서버

동작:
1. 로그인 → 세션 생성
2. Session ID를 쿠키로 전달
3. 매 요청마다 세션 조회

장점:
- 보안성 높음
- 용량 제한 없음
- 강제 로그아웃 가능

단점:
- 서버 메모리/저장소 사용
- 확장성 낮음 (여러 서버 시)
- Redis 등 추가 인프라

사용:
- 전통적인 웹 애플리케이션
- 보안이 중요한 경우

토큰 (JWT):

특징:
- JSON 형태의 토큰
- Header.Payload.Signature
- 자체 포함 (Self-Contained)

동작:
1. 로그인 → JWT 발급
2. 클라이언트 저장 (localStorage)
3. Authorization 헤더로 전송
4. 서버가 서명 검증

장점:
- Stateless (서버 저장 불필요)
- 확장성 높음 (Scale-Out)
- 모바일 앱 친화적
- CORS 문제 없음

단점:
- 토큰 크기 큼
- 탈취 시 위험 (만료까지 유효)
- Payload 노출 (암호화 안 됨)
- 강제 로그아웃 어려움

보안 강화:
- Refresh Token 사용
- 짧은 만료 시간
- HTTPS 사용
- XSS/CSRF 방지

선택 기준:
- 단순 설정 저장 → 쿠키
- 전통적 웹 (단일 서버) → 세션
- REST API, MSA → JWT
- 모바일 앱 → JWT
- 보안 최우선 → 세션
- 확장성 최우선 → JWT
```

---

# 8. DNS (Domain Name System)

## 📌 개념

```
도메인 이름을 IP 주소로 변환하는 시스템
- 인터넷의 전화번호부
- 사람이 읽기 쉬운 이름 → 컴퓨터가 이해하는 IP
```

### 예시

```
www.example.com → 93.184.216.34

사람: www.example.com (기억하기 쉬움)
컴퓨터: 93.184.216.34 (실제 주소)
```

---

## 🔍 DNS 조회 과정

### 전체 흐름

```
1. 브라우저에 www.example.com 입력

2. DNS 조회 시작
   ↓
3. 로컬 캐시 확인
   ↓ (없으면)
4. Recursive DNS 서버 (ISP)
   ↓
5. Root DNS 서버
   ↓
6. TLD DNS 서버 (.com)
   ↓
7. Authoritative DNS 서버 (example.com)
   ↓
8. IP 주소 반환 (93.184.216.34)
   ↓
9. 브라우저가 해당 IP로 접속
```

### 상세 과정

```
Client                                  DNS Servers

1. www.example.com 입력
   |
2. 로컬 캐시 확인
   브라우저 캐시
   OS 캐시
   hosts 파일
   |
   (없으면)
   |
3. Recursive DNS 서버
   (ISP DNS: 168.126.63.1)
   |                         
   | "www.example.com?"      
   |------------------------>|
   |                         |
   |                    4. Root DNS 서버 질의
   |                         | "com은 어디?"
   |                         |-------------> [Root]
   |                         |               "TLD로 가"
   |                         |<------------- 
   |                         |
   |                    5. TLD DNS 서버 질의
   |                         | "example.com은 어디?"
   |                         |-------------> [.com TLD]
   |                         |               "Authoritative로 가"
   |                         |<------------- 
   |                         |
   |                    6. Authoritative DNS 질의
   |                         | "www.example.com은?"
   |                         |-------------> [example.com NS]
   |                         |               "93.184.216.34"
   |                         |<------------- 
   |                         |
   | "93.184.216.34"        |
   |<------------------------|
   |                         
7. IP 주소로 접속
   |
   | HTTP GET /
   |-----------------------> 93.184.216.34
```

---

## 🏗️ DNS 서버 계층

### 1. Root DNS 서버

```
역할:
- 최상위 DNS 서버
- TLD 서버 위치 안내

특징:
- 전 세계 13개 (A~M)
- Anycast로 복제본 수백 개
- 예: a.root-servers.net

응답:
"com 도메인은 TLD 서버로 가세요"
```

### 2. TLD DNS 서버 (Top-Level Domain)

```
역할:
- 최상위 도메인 관리
- .com, .net, .org, .kr 등

예:
.com TLD: com 도메인 관리
.kr TLD: kr 도메인 관리

응답:
"example.com은 Authoritative 서버로 가세요"
```

### 3. Authoritative DNS 서버

```
역할:
- 실제 도메인 정보 보유
- 최종 IP 주소 제공

예:
example.com의 네임서버
- ns1.example.com
- ns2.example.com

응답:
"www.example.com = 93.184.216.34"
```

### 4. Recursive DNS 서버

```
역할:
- 사용자 대신 DNS 조회
- 캐싱

제공자:
- ISP (KT, SK, LG)
- Google (8.8.8.8)
- Cloudflare (1.1.1.1)

특징:
- 전체 조회 과정 수행
- 결과 캐싱으로 빠른 응답
```

---

## 📝 DNS 레코드 타입

### A 레코드 (Address)

```
도메인 → IPv4 주소

예:
www.example.com.  IN  A  93.184.216.34
```

### AAAA 레코드

```
도메인 → IPv6 주소

예:
www.example.com.  IN  AAAA  2606:2800:220:1:248:1893:25c8:1946
```

### CNAME 레코드 (Canonical Name)

```
도메인 → 다른 도메인 (별칭)

예:
blog.example.com.  IN  CNAME  example.com.

blog.example.com 접속 → example.com으로 리다이렉트
```

### MX 레코드 (Mail Exchange)

```
이메일 서버 지정

예:
example.com.  IN  MX  10  mail.example.com.
              우선순위↑  메일서버↑

낮을수록 우선순위 높음
```

### NS 레코드 (Name Server)

```
네임서버 지정

예:
example.com.  IN  NS  ns1.example.com.
example.com.  IN  NS  ns2.example.com.
```

### TXT 레코드

```
텍스트 정보 (SPF, DKIM, 인증 등)

예:
example.com.  IN  TXT  "v=spf1 include:_spf.google.com ~all"
```

---

## ⏱️ DNS 캐싱

### TTL (Time To Live)

```
DNS 레코드의 캐시 유효 시간 (초 단위)

예:
www.example.com.  300  IN  A  93.184.216.34
                  ↑
                 TTL (5분)

5분 동안 캐시 사용, 이후 재조회
```

### 캐시 계층

```
1. 브라우저 캐시:
   - 짧은 시간 (수 분)
   - 빠른 접근

2. OS 캐시:
   - 시스템 레벨
   - hosts 파일 우선

3. Recursive DNS 캐시:
   - ISP 서버
   - TTL 기간 동안 유지

장점:
- 빠른 응답
- DNS 서버 부하 감소

단점:
- IP 변경 시 전파 지연
- TTL 만료까지 대기
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
DNS는 도메인 이름을 IP 주소로 변환하는 시스템입니다.

조회 과정:
1. 로컬 캐시 확인
2. Recursive DNS (ISP)
3. Root DNS
4. TLD DNS (.com)
5. Authoritative DNS
6. IP 주소 반환

캐싱으로 빠른 응답, 
TTL로 유효 시간 관리합니다.
```

### 상세 답변
```
DNS (Domain Name System):

역할:
- 도메인 이름을 IP 주소로 변환
- 인터넷의 전화번호부
- www.example.com → 93.184.216.34

조회 과정:
1. 브라우저 캐시 확인
2. OS 캐시 확인
3. Recursive DNS 서버 (ISP)
4. Root DNS 서버
   - 13개 루트 서버 (A~M)
   - TLD 서버 위치 안내
5. TLD DNS 서버
   - .com, .net, .org 관리
   - Authoritative 서버 안내
6. Authoritative DNS 서버
   - 실제 IP 주소 보유
   - 최종 응답
7. IP 주소 반환 및 캐싱

DNS 레코드:
- A: IPv4 주소
- AAAA: IPv6 주소
- CNAME: 별칭
- MX: 메일 서버
- NS: 네임서버
- TXT: 텍스트 정보

캐싱:
- TTL로 유효 시간 설정
- 브라우저 → OS → Recursive DNS
- 빠른 응답, 서버 부하 감소

보안:
- DNSSEC: DNS 응답 무결성 검증
- DNS over HTTPS (DoH): 암호화
- DNS over TLS (DoT): 암호화

성능 최적화:
- CDN DNS (Cloudflare, AWS Route 53)
- Anycast로 가까운 서버 응답
- 지역별 IP 반환 (Geo DNS)
```

---

이것으로 네트워크 핵심 내용 정리가 완료되었습니다! 

다음 내용이 필요하시면 말씀해주세요:
- 로드밸런서
- IP 주소 (IPv4/IPv6, 서브넷)
- 프록시
- CDN
- 웹소켓
- gRPC
- 기타 네트워크 개념