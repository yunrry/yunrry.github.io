# 6. GET vs POST

## 📊 비교표

| 구분 | GET | POST |
|------|-----|------|
| **목적** | 데이터 조회 | 데이터 생성/수정 |
| **데이터 위치** | URL (Query String) | Body |
| **보안** | 낮음 (URL 노출) ✘ | 높음 (Body) ✔ |
| **캐싱** | 가능 ✔ | 불가능 |
| **북마크** | 가능 ✔ | 불가능 |
| **히스토리** | 남음 | 안 남음 |
| **길이 제한** | 있음 (2048자) | 없음 ✔ |
| **멱등성** | ✔ | ✘ |
| **속도** | 빠름 ✔ | 약간 느림 |

---

## 🔵 GET

### 특징

```
✔ 데이터 조회
✔ URL에 데이터 포함
✔ 캐싱 가능
✔ 멱등성 보장
✘ 보안 취약
✘ 길이 제한

사용: 검색, 조회, 필터링
```

### 요청 형식

```
GET /search?q=java&page=1 HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0

(Body 없음)

URL:
http://www.example.com/search?q=java&page=1
                              └─────┬─────┘
                            Query String
```

### Query String 구조

```
?key1=value1&key2=value2&key3=value3

예:
/search?q=java&category=book&sort=price

파싱:
q = "java"
category = "book"
sort = "price"
```

### 장점

```
✔ 간단함:
   - URL만으로 전달
   - 별도 Body 불필요

✔ 캐싱:
   - 브라우저 캐시
   - CDN 캐시
   - 빠른 응답

✔ 북마크/공유:
   - URL 복사만으로 공유
   - 검색 결과 공유 가능

✔ 멱등성:
   - 여러 번 요청해도 같은 결과
   - 안전함
```

### 단점

```
✘ 보안:
   - URL에 데이터 노출
   - 브라우저 히스토리에 남음
   - 로그에 기록됨
   - 비밀번호 전송 불가

✘ 길이 제한:
   - 브라우저: 약 2048자
   - 서버마다 다름
   - 긴 데이터 전송 불가

✘ 바이너리 데이터:
   - 파일 업로드 불가
   - 텍스트만 가능
```

### 사용 예시

```
✔ 올바른 사용:
GET /users/123           (사용자 조회)
GET /products?id=5       (상품 조회)
GET /search?q=java       (검색)
GET /posts?page=2        (페이징)

✘ 잘못된 사용:
GET /login?id=admin&pw=1234  (비밀번호 노출!)
GET /user/delete?id=5        (삭제는 DELETE 사용)
```

---

## 🔴 POST

### 특징

```
✔ 데이터 생성/수정
✔ Body에 데이터 포함
✔ 보안성 높음
✔ 길이 제한 없음
✘ 캐싱 불가
✘ 멱등성 없음

사용: 회원가입, 로그인, 파일 업로드
```

### 요청 형식

```
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/json
Content-Length: 52

{
  "username": "admin",
  "password": "secret123"
}

데이터: Body에 포함 (URL에 노출 안 됨) ✔
```

### Content-Type

```
1. application/json (가장 많이 사용):
{
  "name": "홍길동",
  "age": 30
}

2. application/x-www-form-urlencoded:
name=%ED%99%8D%EA%B8%B8%EB%8F%99&age=30

3. multipart/form-data (파일 업로드):
------WebKitFormBoundary
Content-Disposition: form-data; name="file"

(파일 내용)
------WebKitFormBoundary--

4. text/plain:
name: 홍길동
age: 30
```

### 장점

```
✔ 보안:
   - Body에 데이터 숨김
   - URL에 노출 안 됨
   - 히스토리에 안 남음

✔ 데이터 크기:
   - 길이 제한 없음
   - 대용량 데이터 전송 가능

✔ 다양한 형식:
   - JSON, XML, 파일 등
   - 바이너리 데이터 가능
```

### 단점

```
✘ 캐싱 불가:
   - 매번 서버 요청
   - 느릴 수 있음

✘ 북마크/공유 불가:
   - URL만으로 재현 불가

✘ 멱등성 없음:
   - 여러 번 요청 시 중복 생성 가능
   - 주의 필요
```

### 사용 예시

```
✔ 올바른 사용:
POST /users              (사용자 생성)
POST /login              (로그인)
POST /posts              (게시글 작성)
POST /upload             (파일 업로드)

✘ 잘못된 사용:
POST /users/123          (조회는 GET 사용)
POST /search             (검색은 GET 사용)
```

---

## 🎯 멱등성 (Idempotent)

### 개념

```
같은 요청을 여러 번 해도 결과가 같음

멱등: f(f(x)) = f(x)
```

### GET은 멱등

```
GET /users/123

1번 요청: {id: 123, name: "홍길동"}
2번 요청: {id: 123, name: "홍길동"}
3번 요청: {id: 123, name: "홍길동"}

→ 항상 같은 결과 ✔
```

### POST는 비멱등

```
POST /users
Body: {name: "홍길동"}

1번 요청: 사용자 1 생성
2번 요청: 사용자 2 생성 (중복!)
3번 요청: 사용자 3 생성 (중복!)

→ 매번 다른 결과 ✘
```

### HTTP 메서드별 멱등성

```
멱등:
- GET ✔
- PUT ✔
- DELETE ✔
- HEAD ✔
- OPTIONS ✔

비멱등:
- POST ✘
- PATCH ✘ (경우에 따라 다름)
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
GET:
- 데이터 조회
- URL에 데이터 (Query String)
- 캐싱 가능, 북마크 가능
- 보안 취약, 길이 제한
- 멱등성 O

POST:
- 데이터 생성/수정
- Body에 데이터
- 캐싱 불가, 북마크 불가
- 보안 좋음, 길이 제한 없음
- 멱등성 X

선택:
- 조회 → GET
- 생성/수정 → POST
```

### 상세 답변
```
GET:

특징:
- 서버 리소스 조회
- URL에 파라미터 포함 (Query String)
- 브라우저 히스토리에 남음

장점:
- 캐싱 가능 (빠른 응답)
- 북마크 가능 (URL 공유)
- 멱등성 보장 (안전)

단점:
- URL 길이 제한 (약 2048자)
- 보안 취약 (URL 노출)
- 바이너리 데이터 불가

사용 사례:
- 검색: /search?q=java
- 조회: /users/123
- 필터링: /products?category=book

POST:

특징:
- 서버 리소스 생성/수정
- Body에 데이터 포함
- 히스토리에 안 남음

장점:
- 보안성 (Body에 숨김)
- 길이 제한 없음
- 다양한 형식 (JSON, File 등)

단점:
- 캐싱 불가 (느릴 수 있음)
- 북마크 불가
- 멱등성 없음 (중복 주의)

사용 사례:
- 회원가입: POST /users
- 로그인: POST /login
- 파일 업로드: POST /upload

멱등성:
- GET: 여러 번 조회해도 같은 결과
- POST: 여러 번 요청 시 중복 생성

실무 선택 기준:
- 데이터 조회만 → GET
- 민감한 데이터 → POST
- 캐싱 필요 → GET
- 파일 업로드 → POST
- RESTful 설계 따르기
```
