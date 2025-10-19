# 네트워크 완벽 정리 - 로드밸런서 & IP 주소

---

# 9. 로드밸런서 (Load Balancer)

## 📌 개념

```
여러 서버에 트래픽을 분산시키는 장치/소프트웨어
- 서버 부하 분산
- 고가용성 (High Availability)
- 확장성 (Scalability)
```

### 기본 구조

```
         Client
            |
            | 요청
            ↓
      ┌──────────┐
      │ Load     │
      │ Balancer │
      └──────────┘
       /    |    \
      /     |     \
     ↓      ↓      ↓
[Server1][Server2][Server3]

트래픽을 여러 서버에 분산 ✅
```

---

## 🎯 로드밸런서의 역할

### 1. 부하 분산

```
문제:
- 단일 서버에 모든 요청 집중
- 서버 과부하, 응답 지연

해결:
Client1 → Server1
Client2 → Server2
Client3 → Server3
Client4 → Server1
...

각 서버가 균등하게 처리 ✅
```

### 2. 고가용성 (HA)

```
문제:
- 서버 1대 장애 → 서비스 중단

해결:
Server1 장애 발생
    ↓
로드밸런서가 감지
    ↓
Server1 제외
    ↓
Server2, Server3로만 트래픽 전송

서비스 지속 ✅
```

### 3. Health Check (헬스 체크)

```
주기적으로 서버 상태 확인

방법:
- HTTP 요청: GET /health
- TCP 연결 확인
- Ping

응답:
- 200 OK → 정상
- Timeout/Error → 비정상

비정상 서버는 자동 제외 ✅
```

### 4. 확장성

```
수평 확장 (Scale-Out):

트래픽 증가
    ↓
서버 추가 (3대 → 5대)
    ↓
로드밸런서가 자동으로 분산
    ↓
처리 용량 증가 ✅

서버 추가/제거가 쉬움
```

---

## 🔄 로드밸런싱 알고리즘

### 1. Round Robin (라운드 로빈)

```
순서대로 분배

동작:
요청1 → Server1
요청2 → Server2
요청3 → Server3
요청4 → Server1 (다시 처음부터)
요청5 → Server2
...

장점:
✅ 구현 간단
✅ 균등 분배

단점:
❌ 서버 성능 차이 고려 안 함
❌ 세션 유지 어려움

사용:
- 서버 성능이 동일할 때
- Stateless 애플리케이션
```

### 2. Weighted Round Robin (가중 라운드 로빈)

```
서버 성능에 따라 가중치 부여

설정:
Server1: 가중치 3
Server2: 가중치 2
Server3: 가중치 1

동작:
Server1에 3번 할당
Server2에 2번 할당
Server3에 1번 할당
(총 6번 중)

예:
요청1 → Server1
요청2 → Server1
요청3 → Server1
요청4 → Server2
요청5 → Server2
요청6 → Server3

장점:
✅ 서버 성능 차이 반영

사용:
- 서버 스펙이 다를 때
```

### 3. Least Connections (최소 연결)

```
현재 연결 수가 가장 적은 서버에 할당

상태:
Server1: 10개 연결
Server2: 5개 연결  ← 선택
Server3: 8개 연결

새 요청 → Server2 (연결 수 가장 적음)

장점:
✅ 실시간 부하 고려
✅ 긴 요청 처리에 유리

단점:
❌ 연결 수 추적 필요
❌ 약간 복잡

사용:
- 요청 처리 시간이 다양할 때
- 긴 커넥션 유지 (WebSocket 등)
```

### 4. Weighted Least Connections

```
최소 연결 + 가중치

상태:
Server1 (가중치 2): 10개 연결 → 비율 10/2 = 5
Server2 (가중치 1): 5개 연결 → 비율 5/1 = 5
Server3 (가중치 3): 12개 연결 → 비율 12/3 = 4 ← 선택

새 요청 → Server3 (비율이 가장 낮음)

장점:
✅ 성능 차이 + 현재 부하 모두 고려
```

### 5. IP Hash

```
클라이언트 IP 주소를 해시하여 서버 선택

동작:
hash(Client IP) % 서버 수 = 서버 인덱스

예:
Client A (IP: 192.168.1.10)
hash(192.168.1.10) % 3 = 1
→ 항상 Server1

Client B (IP: 192.168.1.20)
hash(192.168.1.20) % 3 = 2
→ 항상 Server2

장점:
✅ 같은 클라이언트는 같은 서버
✅ 세션 유지 쉬움

단점:
❌ 서버 추가/제거 시 재분배
❌ 특정 서버에 부하 집중 가능

사용:
- 세션 기반 애플리케이션
- Stateful 서비스
```

### 6. Least Response Time (최소 응답 시간)

```
응답 시간이 가장 빠른 서버 선택

상태:
Server1: 평균 응답 100ms
Server2: 평균 응답 50ms  ← 선택
Server3: 평균 응답 80ms

장점:
✅ 최적의 성능
✅ 사용자 경험 향상

단점:
❌ 응답 시간 측정 필요
❌ 구현 복잡
```

---

## 🏗️ 로드밸런서 유형

### L4 로드밸런서 (Transport Layer)

```
OSI 4계층 (전송 계층)에서 동작
- IP, Port 기반 분산
- TCP/UDP 레벨

동작:
Client → LB (IP:Port 확인)
         ↓
      Server 선택 (IP, Port 기반)

특징:
✅ 빠른 속도
✅ 간단한 구조
❌ 내용 기반 라우팅 불가

정보:
- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol (TCP/UDP)

사용:
- 단순 부하 분산
- 고성능 필요
```

### L7 로드밸런서 (Application Layer)

```
OSI 7계층 (응용 계층)에서 동작
- HTTP 헤더, URL, 쿠키 등 기반 분산
- 콘텐츠 기반 라우팅

동작:
Client → LB (HTTP 요청 분석)
         ↓
      URL, Header 확인
         ↓
      Server 선택 (콘텐츠 기반)

특징:
✅ 유연한 라우팅
✅ SSL 종료 가능
✅ 캐싱, 압축 등 부가 기능
❌ 느린 속도 (패킷 분석)

정보:
- HTTP 메서드 (GET, POST)
- URL 경로
- HTTP 헤더
- 쿠키
- Body 내용

사용:
- 마이크로서비스
- 복잡한 라우팅 규칙
```

### L4 vs L7 비교

```
예시:

L4:
모든 /api/* 요청 → Server1, 2, 3 (Round Robin)
간단하지만 유연성 낮음

L7:
/api/users/*    → User Service (Server1, 2)
/api/orders/*   → Order Service (Server3, 4)
/api/products/* → Product Service (Server5, 6)

유연하지만 약간 느림
```

---

## 💻 로드밸런서 구현

### 소프트웨어 로드밸런서

#### 1. Nginx

```nginx
# nginx.conf

http {
    upstream backend {
        # 로드밸런싱 알고리즘
        least_conn;  # 최소 연결
        
        # 서버 목록 (가중치 포함)
        server 192.168.1.10:8080 weight=3;
        server 192.168.1.11:8080 weight=2;
        server 192.168.1.12:8080 weight=1;
        
        # 헬스 체크
        server 192.168.1.13:8080 backup;  # 백업 서버
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

#### 2. HAProxy

```
# haproxy.cfg

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    
    # 헬스 체크
    option httpchk GET /health
    
    # 서버 목록
    server server1 192.168.1.10:8080 check
    server server2 192.168.1.11:8080 check
    server server3 192.168.1.12:8080 check
```

### 하드웨어 로드밸서

```
상용 제품:
- F5 Networks
- Citrix NetScaler
- A10 Networks

특징:
✅ 고성능 (전용 하드웨어)
✅ 안정성
❌ 고가
❌ 유연성 낮음
```

### 클라우드 로드밸런서

```
AWS:
- ELB (Elastic Load Balancer)
  - ALB (Application Load Balancer) - L7
  - NLB (Network Load Balancer) - L4
  - CLB (Classic Load Balancer) - L4/L7

GCP:
- Cloud Load Balancing
  - HTTP(S) Load Balancing - L7
  - TCP/UDP Load Balancing - L4

Azure:
- Azure Load Balancer - L4
- Application Gateway - L7

특징:
✅ 관리 불필요 (Managed)
✅ 자동 확장
✅ 고가용성
✅ 사용한 만큼 과금
```

---

## 🔐 세션 관리 (Session Persistence)

### 문제

```
Stateful 애플리케이션에서 세션 유지 필요

Client → Server1 (로그인, 세션 생성)
Client → Server2 (세션 없음!) ❌
```

### 해결 방법

#### 1. Sticky Session (Session Affinity)

```
같은 클라이언트는 항상 같은 서버

구현:
- 쿠키 기반
- IP Hash

예:
Client A → Server1 (첫 요청)
          → Server1 (이후 모든 요청)

장점:
✅ 구현 간단
✅ 세션 공유 불필요

단점:
❌ 부하 불균형 가능
❌ 서버 장애 시 세션 손실
```

#### 2. Session Clustering

```
모든 서버가 세션 공유

[Server1] ─┐
[Server2] ─┼─ 세션 복제
[Server3] ─┘

장점:
✅ 어느 서버든 가능
✅ 서버 장애에도 세션 유지

단점:
❌ 네트워크 오버헤드
❌ 서버 수 증가 시 부담
```

#### 3. Session Storage (추천) ✅

```
중앙 저장소에 세션 저장

[Server1] ─┐
[Server2] ─┼─ Redis/Memcached
[Server3] ─┘

동작:
1. Server1에서 세션 생성 → Redis 저장
2. Server2에서 세션 조회 → Redis에서 가져옴

장점:
✅ 완벽한 부하 분산
✅ 서버 추가/제거 자유
✅ 서버 장애에도 세션 유지

단점:
❌ Redis 등 추가 인프라
❌ 약간의 지연

사용:
- 대부분의 현대적 애플리케이션
```

---

## 📊 로드밸런서 모니터링

### Health Check 설정

```nginx
# Nginx
upstream backend {
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;
    
    # 헬스 체크 설정
    check interval=3000 rise=2 fall=3 timeout=1000;
    # interval: 3초마다 체크
    # rise: 2번 성공 시 정상
    # fall: 3번 실패 시 비정상
    # timeout: 1초 내 응답 없으면 실패
}
```

### 메트릭

```
모니터링 지표:

1. 서버 상태:
   - Active Servers
   - Failed Servers
   - Health Check Status

2. 트래픽:
   - Requests per Second
   - Bandwidth
   - Active Connections

3. 응답 시간:
   - Average Response Time
   - P95, P99 Latency

4. 오류율:
   - 4xx Errors
   - 5xx Errors
   - Timeout Rate

5. 분산 비율:
   - Requests per Server
   - Load Distribution
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
로드밸런서는 여러 서버에 트래픽을 
분산시키는 장치입니다.

역할:
- 부하 분산
- 고가용성 (서버 장애 대응)
- Health Check

알고리즘:
- Round Robin: 순서대로
- Least Connections: 연결 적은 곳
- IP Hash: 같은 클라이언트 → 같은 서버

유형:
- L4: IP/Port 기반 (빠름)
- L7: HTTP 내용 기반 (유연)
```

### 상세 답변
```
로드밸런서 (Load Balancer):

정의:
여러 서버에 네트워크 트래픽을 분산시켜
성능과 가용성을 향상시키는 장치/소프트웨어

주요 역할:

1. 부하 분산:
   - 트래픽을 여러 서버에 균등 분배
   - 서버 과부하 방지
   - 응답 시간 개선

2. 고가용성 (HA):
   - Health Check로 서버 상태 감시
   - 장애 서버 자동 제외
   - 무중단 서비스

3. 확장성:
   - 서버 추가/제거 용이
   - 수평 확장 (Scale-Out)
   - 트래픽 증가에 대응

로드밸런싱 알고리즘:

1. Round Robin:
   - 순서대로 분배
   - 간단, 균등 분배
   
2. Weighted Round Robin:
   - 서버 성능 반영
   - 가중치 부여
   
3. Least Connections:
   - 연결 수 가장 적은 서버
   - 실시간 부하 고려
   
4. IP Hash:
   - 클라이언트 IP 기반
   - 세션 유지

5. Least Response Time:
   - 응답 시간 가장 빠른 서버
   - 최적 성능

유형:

L4 (Transport Layer):
- IP, Port 기반
- TCP/UDP 레벨
- 빠른 속도
- 간단한 라우팅

L7 (Application Layer):
- HTTP 헤더, URL 기반
- 콘텐츠 기반 라우팅
- SSL 종료 가능
- 유연하지만 느림

세션 관리:

1. Sticky Session:
   - 같은 클라이언트 → 같은 서버
   - 구현 간단
   - 부하 불균형 가능

2. Session Storage (추천):
   - Redis 등 중앙 저장소
   - 완벽한 부하 분산
   - 고가용성

구현:

소프트웨어:
- Nginx (오픈소스)
- HAProxy (오픈소스)
- Apache mod_proxy

클라우드:
- AWS ELB (ALB, NLB)
- GCP Load Balancing
- Azure Load Balancer

Health Check:
- 주기적 상태 확인
- HTTP /health 엔드포인트
- 비정상 서버 자동 제외
- 복구 시 자동 포함

실무 활용:
- MSA (마이크로서비스)
- 대용량 트래픽 처리
- 무중단 배포 (Blue-Green)
- 지역별 라우팅 (Geo Load Balancing)
```