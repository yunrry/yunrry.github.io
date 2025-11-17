# 13. 방화벽 (Firewall)

## 📌 개념

```
네트워크 트래픽을 감시하고 제어하는 보안 시스템
- 허용된 트래픽만 통과
- 악의적인 트래픽 차단
- 내부 네트워크 보호
```

### 기본 원리

```
인터넷 ──> [방화벽] ──> 내부 네트워크
           필터링

허용:
✔ HTTP (80)
✔ HTTPS (443)
✔ SSH (22) - 특정 IP만

차단:
✘ 알 수 없는 포트
✘ 의심스러운 IP
✘ 악성 패킷
```

---

## 🛡️ 방화벽 종류

### 1. 패킷 필터링 방화벽 (Packet Filtering)

#### 개념
```
OSI 3, 4계층에서 동작
- IP 주소, 포트 번호 기반 필터링
- 가장 기본적인 방화벽
```

#### 동작 방식
```
패킷 헤더 검사:
- 출발지 IP
- 목적지 IP
- 출발지 Port
- 목적지 Port
- 프로토콜 (TCP/UDP)

규칙과 비교하여 허용/차단
```

#### 규칙 예시
```
Rule 1:
- 출발지: Any
- 목적지: 192.168.1.10
- 포트: 80
- 프로토콜: TCP
- 동작: 허용 ✔

Rule 2:
- 출발지: Any
- 목적지: 192.168.1.10
- 포트: 23 (Telnet)
- 프로토콜: TCP
- 동작: 차단 ✘

Rule 3:
- 출발지: 192.168.1.0/24
- 목적지: Any
- 포트: Any
- 프로토콜: Any
- 동작: 허용 ✔
```

#### 장단점
```
장점:
✔ 빠른 속도
✔ 간단한 구조
✔ 저렴

단점:
✘ 상태 추적 안 함
✘ 애플리케이션 레벨 검사 불가
✘ 우회 공격 취약

사용:
- 기본적인 네트워크 보안
- 라우터 내장 방화벽
```

---

### 2. 상태 기반 검사 방화벽 (Stateful Inspection)

#### 개념
```
연결 상태 추적
- TCP 3-Way Handshake 확인
- 세션 테이블 유지
- 패킷의 맥락 파악
```

#### 동작 방식
```
1. 연결 추적:
Client → Server (SYN)
방화벽: 세션 테이블에 기록

2. 응답 확인:
Server → Client (SYN+ACK)
방화벽: 세션 테이블 확인
→ 요청에 대한 정상 응답인지 검증

3. 연결 완료:
Client → Server (ACK)
방화벽: 세션 확인, 연결 완료

4. 데이터 전송:
양방향 트래픽 허용
세션 테이블 기반 검증
```

#### 세션 테이블
```
출발지IP:Port | 목적지IP:Port | 상태 | 시간
--------------|--------------|------|------
192.168.1.10:50000 | 8.8.8.8:80 | ESTABLISHED | 14:30
192.168.1.20:50001 | 1.1.1.1:443 | SYN_SENT | 14:31
192.168.1.30:50002 | 93.184.216.34:80 | CLOSED | 14:29

상태:
- SYN_SENT: 연결 시도
- ESTABLISHED: 연결 완료
- FIN_WAIT: 종료 대기
- CLOSED: 종료됨
```

#### 장단점
```
장점:
✔ 연결 상태 추적
✔ 더 안전
✔ 정교한 제어

단점:
✘ 패킷 필터링보다 느림
✘ 메모리 사용 (세션 테이블)
✘ 여전히 애플리케이션 검사 불가

사용:
- 대부분의 현대 방화벽
- 기업 네트워크
```

---

### 3. 애플리케이션 레벨 방화벽 (Application Level Gateway)

#### 개념
```
OSI 7계층에서 동작
- HTTP, FTP, DNS 등 프로토콜 검사
- 패킷 내용 분석
- 가장 강력한 보안
```

#### 동작 방식
```
HTTP 요청 예시:

GET /admin.php?cmd=delete HTTP/1.1
Host: example.com
User-Agent: SQLMap

방화벽 검사:
1. URL 검사: /admin.php ✘ (관리자 페이지)
2. 파라미터 검사: cmd=delete ✘ (위험한 명령)
3. User-Agent: SQLMap ✘ (해킹 도구)

결과: 차단 ✘

정상 요청:
GET /products HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0

결과: 허용 ✔
```

#### 검사 항목
```
HTTP:
- URL 패턴
- HTTP 메서드
- 헤더
- 쿠키
- Body 내용
- SQL Injection 패턴
- XSS 패턴

FTP:
- 파일명
- 파일 크기
- 파일 타입

DNS:
- 도메인 필터링
- DNS Tunneling 감지

SMTP:
- 스팸 필터링
- 첨부 파일 검사
```

#### 장단점
```
장점:
✔ 가장 강력한 보안
✔ 애플리케이션 레벨 공격 차단
✔ 상세한 로깅

단점:
✘ 느린 속도 (깊은 검사)
✘ 높은 비용
✘ 복잡한 설정

사용:
- WAF (Web Application Firewall)
- 엔터프라이즈급 보안
```

---

### 4. 프록시 방화벽

#### 개념
```
중계 서버 역할 + 방화벽
- 클라이언트와 서버 사이 중계
- 직접 연결 차단
```

#### 동작 방식
```
Client ──> Proxy Firewall ──> Server
           검사 및 중계

1. Client → Proxy: 요청
2. Proxy: 검사 (규칙 확인)
3. Proxy → Server: 대신 요청
4. Server → Proxy: 응답
5. Proxy: 검사 (내용 확인)
6. Proxy → Client: 응답 전달

직접 연결 불가 ✔
```

#### 장단점
```
장점:
✔ 완벽한 격리
✔ 상세한 검사
✔ 익명성

단점:
✘ 매우 느림
✘ 복잡한 구성
✘ 높은 자원 사용

사용:
- 고보안 환경
- 정부 기관
```

---

### 5. 차세대 방화벽 (NGFW: Next-Generation Firewall)

#### 개념
```
기존 방화벽 + 추가 기능
- IPS (침입 방지)
- 애플리케이션 인식
- 사용자 인식
- 위협 인텔리전스
```

#### 기능
```
1. 전통적 방화벽:
   - 패킷 필터링
   - 상태 추적

2. IPS (Intrusion Prevention System):
   - 공격 패턴 탐지
   - 실시간 차단

3. 애플리케이션 제어:
   - Facebook 차단
   - YouTube 차단
   - 특정 앱만 허용

4. 사용자 인식:
   - 사용자별 정책
   - 관리자는 허용, 일반 사용자는 차단

5. SSL 복호화:
   - HTTPS 트래픽 검사
   - 암호화된 위협 탐지

6. 위협 인텔리전스:
   - 악성 IP 데이터베이스
   - 자동 업데이트
```

#### 제품
```
상용:
- Palo Alto Networks
- Fortinet FortiGate
- Cisco Firepower
- Check Point

특징:
- 통합 보안 솔루션
- 중앙 관리
- 고성능
```

---

## 🔧 방화벽 규칙 설정

### 기본 원칙

#### 1. Default Deny (기본 차단)
```
모든 트래픽을 차단하고
필요한 것만 허용

규칙:
1. HTTP 허용 (80)
2. HTTPS 허용 (443)
3. SSH 허용 (22) - 관리자 IP만
...
마지막. 모든 트래픽 차단 ✘

안전하지만 관리 필요 ✔
```

#### 2. Default Allow (기본 허용)
```
모든 트래픽을 허용하고
위험한 것만 차단

규칙:
1. Telnet 차단 (23)
2. 악성 IP 차단
...
마지막. 모든 트래픽 허용 ✔

편리하지만 위험 ✘
```

#### 권장: Default Deny ✔

---

### iptables (Linux 방화벽)

```bash
# 기본 정책 설정 (모두 차단)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 로컬호스트 허용
iptables -A INPUT -i lo -j ACCEPT

# 연결된 세션 허용 (상태 추적)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SSH 허용 (포트 22)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# HTTP/HTTPS 허용 (포트 80, 443)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 특정 IP만 MySQL 접속 허용
iptables -A INPUT -p tcp -s 192.168.1.100 --dport 3306 -j ACCEPT

# Ping 허용 (ICMP)
iptables -A INPUT -p icmp -j ACCEPT

# 로그 기록 (차단된 패킷)
iptables -A INPUT -j LOG --log-prefix "DROPPED: "

# 규칙 확인
iptables -L -n -v

# 규칙 저장
iptables-save > /etc/iptables/rules.v4
```

### UFW (Uncomplicated Firewall)

```bash
# 활성화
ufw enable

# 기본 정책
ufw default deny incoming
ufw default allow outgoing

# 규칙 추가
ufw allow 22/tcp         # SSH
ufw allow 80/tcp         # HTTP
ufw allow 443/tcp        # HTTPS

# 특정 IP만 허용
ufw allow from 192.168.1.100 to any port 3306

# 포트 범위 허용
ufw allow 8000:9000/tcp

# 규칙 삭제
ufw delete allow 80/tcp

# 상태 확인
ufw status verbose

# 규칙 번호로 삭제
ufw status numbered
ufw delete 3
```

---

## 🏢 방화벽 배치 위치

### 1. 네트워크 경계 (Perimeter Firewall)

```
인터넷 ──> [방화벽] ──> 내부 네트워크

역할:
- 외부 위협 차단
- 전체 네트워크 보호

위치:
- 가장 바깥쪽
- 인터넷과 내부 네트워크 사이
```

### 2. 내부 세그먼트 (Internal Firewall)

```
                [경계 방화벽]
                      |
        ┌─────────────┼─────────────┐
        |             |             |
   [영업부]      [개발부]      [인사부]
        |             |             |
    [방화벽]      [방화벽]      [방화벽]

역할:
- 부서 간 트래픽 제어
- 횡적 이동 방지

위치:
- 내부 네트워크 사이
```

### 3. 호스트 기반 (Host-based Firewall)

```
[PC/서버]
    |
[방화벽 (OS 내장)]

역할:
- 개별 장치 보호
- 세밀한 제어

예:
- Windows Firewall
- iptables (Linux)
- macOS Firewall
```

---

## 🌐 DMZ (Demilitarized Zone)

### 개념
```
내부 네트워크와 외부 네트워크 사이의 중립 지대
- 공개 서버 배치
- 내부 네트워크 보호
```

### 구조
```
인터넷
   |
[외부 방화벽]
   |
┌──DMZ──┐
│ 웹서버 │
│ 메일서버│
└────────┘
   |
[내부 방화벽]
   |
내부 네트워크
(DB, 파일서버 등)

규칙:
- 인터넷 → DMZ: 허용 (제한적)
- 인터넷 → 내부: 차단 ✘
- DMZ → 내부: 제한적 허용
- 내부 → DMZ: 허용
- 내부 → 인터넷: 허용
```

### 장점
```
✔ 내부 네트워크 보호
✔ 공격 표면 축소
✔ 침해 시 격리

예:
웹서버 해킹 당해도
내부 DB는 안전 ✔
```

---

## 🔍 방화벽 로그 및 모니터링

### 로그 종류
```
1. 허용 로그:
   2025-10-19 14:30:00 ALLOW TCP 203.0.113.5:50000 → 192.168.1.10:80

2. 차단 로그:
   2025-10-19 14:31:00 DENY TCP 198.51.100.10:12345 → 192.168.1.10:3389

3. 공격 탐지:
   2025-10-19 14:32:00 ATTACK Port Scan from 198.51.100.10

4. 정책 변경:
   2025-10-19 14:33:00 POLICY Rule 5 added by admin
```

### 모니터링 지표
```
1. 차단된 트래픽:
   - 차단 횟수
   - 차단된 IP
   - 차단된 포트

2. 허용된 트래픽:
   - 대역폭 사용량
   - 연결 수
   - 프로토콜 분포

3. 공격:
   - DDoS 시도
   - 포트 스캔
   - 무차별 대입 공격

4. 성능:
   - CPU 사용률
   - 메모리 사용률
   - 처리량 (Throughput)
```

---

## ⚠️ 방화벽 우회 공격

### 1. 터널링
```
허용된 프로토콜로 위장

예: DNS Tunneling
- DNS 쿼리로 데이터 전송
- 포트 53 (DNS)는 대부분 허용됨

대응:
- DNS 트래픽 검사
- 비정상 패턴 탐지
```

### 2. 분할 공격 (Fragmentation)
```
패킷을 작게 나눠서 전송
- 방화벽 규칙 우회

대응:
- 재조립 후 검사
- 작은 패킷 차단
```

### 3. 암호화
```
HTTPS로 악성 트래픽 숨김

대응:
- SSL 복호화
- 인증서 검사
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
방화벽은 네트워크 트래픽을 
감시하고 제어하는 보안 시스템입니다.

종류:
1. 패킷 필터링: IP, Port 기반
2. 상태 추적: 연결 상태 추적
3. 애플리케이션: 내용 검사
4. NGFW: 통합 보안

원칙:
- Default Deny (기본 차단) 권장
- 필요한 것만 허용

DMZ:
- 공개 서버 배치
- 내부 네트워크 보호
```

### 상세 답변
```
방화벽 (Firewall):

정의:
네트워크 트래픽을 감시하고 제어하여
내부 네트워크를 보호하는 보안 시스템

역할:
- 허용된 트래픽만 통과
- 악의적인 트래픽 차단
- 접근 제어
- 로깅 및 모니터링

방화벽 종류:

1. 패킷 필터링 (Packet Filtering):
   계층: OSI 3, 4계층
   검사: IP, Port, 프로토콜
   장점: 빠름, 간단
   단점: 상태 추적 안 함
   사용: 기본 보안

2. 상태 기반 검사 (Stateful Inspection):
   계층: OSI 3, 4계층
   검사: 연결 상태 추적
   세션 테이블: TCP 상태 관리
   장점: 더 안전
   단점: 메모리 사용
   사용: 대부분의 현대 방화벽

3. 애플리케이션 레벨 (Application Level):
   계층: OSI 7계층
   검사: HTTP, FTP 등 프로토콜
   패턴: SQL Injection, XSS 탐지
   장점: 가장 강력
   단점: 느림
   사용: WAF (웹 방화벽)

4. 프록시 방화벽:
   역할: 중계 + 방화벽
   특징: 완벽한 격리
   장점: 상세한 검사
   단점: 매우 느림

5. NGFW (차세대 방화벽):
   기능:
   - 기존 방화벽 기능
   - IPS (침입 방지)
   - 애플리케이션 인식
   - 사용자 인식
   - SSL 복호화
   - 위협 인텔리전스
   제품: Palo Alto, Fortinet

방화벽 규칙:

Default Deny (권장):
- 기본적으로 모두 차단
- 필요한 것만 허용
- 안전하지만 관리 필요

예시:
1. HTTP 허용 (80)
2. HTTPS 허용 (443)
3. SSH 허용 (22) - 특정 IP만
4. 나머지 차단

DMZ (Demilitarized Zone):

구조:
인터넷 → 외부 방화벽 → DMZ → 내부 방화벽 → 내부

DMZ 배치:
- 웹 서버
- 메일 서버
- DNS 서버

내부 배치:
- 데이터베이스
- 파일 서버
- 업무 시스템

장점:
- 내부 네트워크 보호
- 공격 표면 축소
- 침해 시 격리

배치 위치:

1. 네트워크 경계:
   - 인터넷과 내부 사이
   - 전체 네트워크 보호

2. 내부 세그먼트:
   - 부서 간 트래픽 제어
   - 횡적 이동 방지

3. 호스트 기반:
   - 개별 PC/서버 보호
   - Windows Firewall, iptables

방화벽 우회:

1. 터널링:
   - DNS, HTTPS로 위장
   대응: 트래픽 검사

2. 분할 공격:
   - 패킷 분할
   대응: 재조립 후 검사

3. 암호화:
   - HTTPS로 숨김
   대응: SSL 복호화

실무 도구:

Linux:
- iptables (저수준)
- UFW (고수준)
- firewalld

클라우드:
- AWS Security Group
- Azure Network Security Group
- GCP Firewall Rules

모니터링:
- 차단/허용 로그
- 공격 탐지
- 성능 지표
- 정책 변경 이력

Best Practice:
- Default Deny 원칙
- 최소 권한 원칙
- 정기적인 규칙 검토
- 로그 모니터링
- 계층적 방어 (Defense in Depth)
```

---

## 📝 핵심 정리

### 프록시
```
Forward Proxy (클라이언트 측):
- 클라이언트를 숨김
- 접근 제어, 캐싱
- 회사 프록시

Reverse Proxy (서버 측):
- 서버를 숨김
- 로드밸런싱, SSL 종료
- Nginx
```

### CDN
```
전 세계 분산 캐시 서버
- 빠른 콘텐츠 전달
- 서버 부하 감소
- DDoS 방어

동작:
1. 가까운 서버 연결
2. 캐시 있으면 즉시 응답
3. 없으면 Origin에서 가져옴
```

### 방화벽
```
네트워크 트래픽 제어

종류:
1. 패킷 필터링 (기본)
2. 상태 추적 (일반적)
3. 애플리케이션 (WAF)
4. NGFW (통합)

원칙:
- Default Deny
- 최소 권한

DMZ:
- 공개 서버 격리
- 내부 보호
```

---
