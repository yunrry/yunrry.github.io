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
