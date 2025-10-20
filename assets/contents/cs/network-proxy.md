# 11. 프록시 (Proxy)

## 📌 개념

```
클라이언트와 서버 사이의 중계 서버
- 요청을 대신 전달
- 응답을 대신 받음
- 중간에서 다양한 기능 수행
```

### 기본 구조

```
직접 연결:
Client ───────────> Server

프록시 사용:
Client ──> Proxy ──> Server
         중계 서버
```

---

## 🔵 Forward Proxy (포워드 프록시)

### 개념

```
클라이언트를 대신하여 요청
- 클라이언트 측 프록시
- 클라이언트를 숨김
- 서버는 프록시만 봄
```

### 구조

```
[Client1]  ┐
[Client2]  ├─> [Forward Proxy] ──> [Server]
[Client3]  ┘
 
클라이언트 여러 명 → 프록시 1개 → 서버

서버 입장:
- 클라이언트 IP 모름
- 프록시 IP만 보임
```

### 동작 과정

```
1. Client → Forward Proxy
   "google.com 접속해줘"

2. Forward Proxy → Server (google.com)
   프록시가 대신 요청

3. Server → Forward Proxy
   응답 전달

4. Forward Proxy → Client
   응답 전달

Client는 Server와 직접 통신 안 함 ✅
```

### 주요 기능

#### 1. 익명성 (Anonymity)

```
클라이언트 IP 숨김

Client (192.168.1.10)
  ↓
Proxy (203.0.113.5)
  ↓
Server

Server가 보는 IP: 203.0.113.5 (프록시)
실제 Client IP: 192.168.1.10 (숨겨짐) ✅

사용:
- 익명 브라우징
- 우회 접속
```

#### 2. 캐싱 (Caching)

```
자주 요청되는 콘텐츠 저장

첫 요청:
Client → Proxy → Server (느림)
        └─ 응답 저장

이후 요청:
Client → Proxy (캐시에서 즉시 응답) ✅
        X Server (요청 안 함)

장점:
- 빠른 응답
- 서버 부하 감소
- 대역폭 절약
```

#### 3. 접근 제어 (Access Control)

```
특정 사이트 차단

예: 회사 네트워크
- facebook.com 차단 ❌
- youtube.com 차단 ❌
- 업무 사이트만 허용 ✅

프록시가 URL 필터링
```

#### 4. 로깅 (Logging)

```
모든 요청 기록

로그:
- 사용자: user1
- 시간: 2025-10-19 14:30:00
- URL: google.com
- 크기: 1.2MB

용도:
- 사용 패턴 분석
- 보안 감사
- 트래픽 모니터링
```

---

## 🔴 Reverse Proxy (리버스 프록시)

### 개념

```
서버를 대신하여 응답
- 서버 측 프록시
- 서버를 숨김
- 클라이언트는 프록시만 봄
```

### 구조

```
[Client] ──> [Reverse Proxy] ──> ┌─ [Server1]
                                 ├─ [Server2]
                                 └─ [Server3]

클라이언트 → 프록시 1개 → 서버 여러 개

클라이언트 입장:
- 실제 서버 IP 모름
- 프록시 IP만 보임
```

### 동작 과정

```
1. Client → Reverse Proxy
   "example.com 접속"

2. Reverse Proxy → Server (실제 서버 선택)
   Server1, Server2, Server3 중 선택

3. Server → Reverse Proxy
   응답 전달

4. Reverse Proxy → Client
   응답 전달

Client는 실제 Server를 모름 ✅
```

### 주요 기능

#### 1. 로드 밸런싱

```
여러 서버에 트래픽 분산

Client1 → Reverse Proxy → Server1
Client2 → Reverse Proxy → Server2
Client3 → Reverse Proxy → Server3
Client4 → Reverse Proxy → Server1

알고리즘:
- Round Robin
- Least Connections
- IP Hash

효과:
- 부하 분산
- 고가용성
```

#### 2. SSL 종료 (SSL Termination)

```
HTTPS 암호화/복호화를 프록시가 처리

Client ←[HTTPS]→ Reverse Proxy ←[HTTP]→ Server
        암호화               평문

장점:
- 서버 부하 감소
- 인증서 중앙 관리
- 서버는 HTTP만 처리

Reverse Proxy:
- SSL 인증서 설치
- 암호화/복호화 수행
- 평문으로 서버 전달
```

#### 3. 캐싱

```
정적 콘텐츠 캐싱

첫 요청:
Client → Reverse Proxy → Server
        └─ 이미지, CSS, JS 저장

이후 요청:
Client → Reverse Proxy (캐시 응답) ✅
        X Server

효과:
- 서버 부하 감소
- 빠른 응답
```

#### 4. 보안

```
실제 서버 보호

Client는 Reverse Proxy만 봄
  ↓
방화벽, DDoS 방어
  ↓
실제 Server (내부 네트워크)

공격:
- 프록시가 먼저 받음
- 필터링 후 서버 전달
- 서버 직접 노출 안 됨 ✅
```

#### 5. 압축

```
응답 데이터 압축

Server → Reverse Proxy (평문 10MB)
        ↓ gzip 압축
Client ← 2MB

효과:
- 대역폭 절약
- 빠른 전송
```

---

## 🆚 Forward Proxy vs Reverse Proxy

| 구분 | Forward Proxy | Reverse Proxy |
|------|---------------|---------------|
| **위치** | 클라이언트 측 | 서버 측 |
| **숨기는 대상** | 클라이언트 | 서버 |
| **용도** | 접근 제어, 익명성 | 로드밸런싱, 보안 |
| **캐싱** | 클라이언트 캐시 | 서버 캐시 |
| **설정** | 클라이언트 설정 | 서버 설정 |
| **예시** | 회사 프록시, VPN | Nginx, Apache |

---

## 💻 프록시 구현

### Nginx (Reverse Proxy)

```nginx
# nginx.conf

http {
    # 업스트림 서버 정의
    upstream backend {
        server 192.168.1.10:8080;
        server 192.168.1.11:8080;
        server 192.168.1.12:8080;
    }
    
    # 캐시 설정
    proxy_cache_path /var/cache/nginx 
                     levels=1:2 
                     keys_zone=my_cache:10m 
                     max_size=1g;
    
    server {
        listen 80;
        server_name example.com;
        
        location / {
            # 리버스 프록시 설정
            proxy_pass http://backend;
            
            # 헤더 설정
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # 캐싱
            proxy_cache my_cache;
            proxy_cache_valid 200 1h;
            proxy_cache_use_stale error timeout;
            
            # 타임아웃
            proxy_connect_timeout 30s;
            proxy_send_timeout 30s;
            proxy_read_timeout 30s;
        }
        
        # 정적 파일 캐싱
        location ~* \.(jpg|jpeg|png|gif|css|js)$ {
            proxy_pass http://backend;
            proxy_cache my_cache;
            proxy_cache_valid 200 1d;
            expires 1d;
        }
    }
    
    # HTTPS 설정
    server {
        listen 443 ssl;
        server_name example.com;
        
        ssl_certificate /etc/ssl/certs/example.com.crt;
        ssl_certificate_key /etc/ssl/private/example.com.key;
        
        location / {
            proxy_pass http://backend;
        }
    }
}
```

### Squid (Forward Proxy)

```
# squid.conf

# 포트 설정
http_port 3128

# 캐시 설정
cache_dir ufs /var/spool/squid 10000 16 256

# 접근 제어 (ACL)
acl localnet src 192.168.1.0/24
acl blocked_sites dstdomain .facebook.com
acl blocked_sites dstdomain .youtube.com

# 규칙
http_access deny blocked_sites
http_access allow localnet
http_access deny all

# 로그
access_log /var/log/squid/access.log
cache_log /var/log/squid/cache.log
```

---

## 🌐 프록시 서버 예시

### 공개 프록시

```
무료/유료 프록시 서비스:
- Squid Proxy
- Privoxy
- TinyProxy

상용 서비스:
- ProxyMesh
- Bright Data
- Smartproxy

주의:
- 보안 위험 (트래픽 감청 가능)
- 신뢰할 수 있는 서비스 사용
```

### 기업 프록시

```
회사 네트워크에서 사용

목적:
- 인터넷 접근 제어
- 트래픽 모니터링
- 대역폭 관리
- 보안 강화

기능:
- 웹 필터링
- 바이러스 검사
- 사용 로그 기록
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
프록시는 클라이언트와 서버 사이의 중계 서버입니다.

Forward Proxy (클라이언트 측):
- 클라이언트를 숨김
- 접근 제어, 캐싱
- 예: 회사 프록시

Reverse Proxy (서버 측):
- 서버를 숨김
- 로드밸런싱, SSL 종료
- 예: Nginx

차이점:
- Forward: 클라이언트 보호
- Reverse: 서버 보호
```

### 상세 답변
```
프록시 (Proxy):

정의:
클라이언트와 서버 사이에서 요청을 중계하는 서버
- 중간자 역할
- 다양한 기능 수행

Forward Proxy (포워드 프록시):

위치: 클라이언트 측
역할: 클라이언트를 대신하여 요청

구조:
Client → Forward Proxy → Server

서버 입장:
- 클라이언트 IP 모름
- 프록시 IP만 보임

기능:
1. 익명성: 클라이언트 IP 숨김
2. 캐싱: 자주 요청되는 콘텐츠 저장
3. 접근 제어: 특정 사이트 차단
4. 로깅: 트래픽 모니터링
5. 압축: 데이터 압축

사용 사례:
- 회사 네트워크 (인터넷 제어)
- VPN (우회 접속)
- 웹 스크래핑

Reverse Proxy (리버스 프록시):

위치: 서버 측
역할: 서버를 대신하여 응답

구조:
Client → Reverse Proxy → Multiple Servers

클라이언트 입장:
- 실제 서버 IP 모름
- 프록시 IP만 보임

기능:
1. 로드 밸런싱:
   - 여러 서버에 트래픽 분산
   - 고가용성

2. SSL 종료:
   - HTTPS 암호화/복호화
   - 서버 부하 감소

3. 캐싱:
   - 정적 콘텐츠 저장
   - 서버 부하 감소

4. 보안:
   - 실제 서버 보호
   - DDoS 방어

5. 압축:
   - 응답 데이터 압축

사용 사례:
- 웹 서버 (Nginx, Apache)
- API Gateway
- CDN

차이점:

Forward Proxy:
- 클라이언트를 숨김
- 나가는 트래픽 제어
- 클라이언트가 설정

Reverse Proxy:
- 서버를 숨김
- 들어오는 트래픽 제어
- 서버가 설정

실무:
- Nginx: 가장 많이 사용되는 리버스 프록시
- HAProxy: 로드밸런싱 특화
- Squid: 포워드 프록시
- Apache: 범용 웹 서버/프록시

프록시 체인:
Client → Forward Proxy → Reverse Proxy → Server
익명성 강화, 다층 보안
```

---

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
한국 사용자 → 미국 서버 (느림) ❌
        14,000km 거리

CDN 사용:
한국 사용자 → 한국 CDN 서버 (빠름) ✅
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

사용자는 가장 가까운 Edge Server 접속 ✅
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
   image.jpg 있음! (Cache Hit) ✅

4. 즉시 응답:
   서울 CDN → 사용자
   (Origin 접속 불필요)

이후 요청: 매우 빠름 ✅
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
- 감당 가능 ✅

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
- 대부분의 웹사이트 (일반적) ✅
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
   - 즉시 응답 (매우 빠름) ✅
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
✅ 빠른 로딩 속도 (물리적 거리 감소)
✅ 서버 부하 감소 (Origin 보호)
✅ 대역폭 절약 (캐싱)
✅ 고가용성 (분산 구조)
✅ DDoS 방어
✅ 글로벌 확장 용이

단점:
❌ 비용 (트래픽 기반 과금)
❌ 캐시 무효화 복잡
❌ 동적 콘텐츠에는 효과 적음

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