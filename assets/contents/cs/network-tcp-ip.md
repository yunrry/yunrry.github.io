
# 2. TCP/IP 4계층

## 📌 개념

**실제 인터넷에서 사용하는 프로토콜 스택**
- OSI 7계층을 단순화
- 실용적인 모델

---

## 🔢 4계층 구조

```
┌─────────────────────┐
│ 4. 응용 계층         │ ← OSI 5, 6, 7계층
│   (Application)     │
├─────────────────────┤
│ 3. 전송 계층         │ ← OSI 4계층
│   (Transport)       │
├─────────────────────┤
│ 2. 인터넷 계층       │ ← OSI 3계층
│   (Internet)        │
├─────────────────────┤
│ 1. 네트워크 액세스   │ ← OSI 1, 2계층
│   (Network Access)  │
└─────────────────────┘
```

---

## 📝 각 계층 상세

### 4계층: 응용 계층 (Application Layer)

```
OSI 5, 6, 7계층 통합

역할:
- 응용 프로그램 간 통신
- 사용자 인터페이스

프로토콜:
- HTTP/HTTPS (웹)
- FTP (파일)
- SMTP/POP3 (이메일)
- DNS (도메인)
- SSH (원격 접속)
- Telnet

데이터 단위: 메시지
```

### 3계층: 전송 계층 (Transport Layer)

```
OSI 4계층과 동일

역할:
- 프로세스 간 통신
- 신뢰성 보장 (TCP)
- 빠른 전송 (UDP)

프로토콜:
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

데이터 단위: 세그먼트 (TCP), 데이터그램 (UDP)
```

### 2계층: 인터넷 계층 (Internet Layer)

```
OSI 3계층과 동일

역할:
- IP 주소 지정
- 패킷 라우팅
- 경로 결정

프로토콜:
- IP (Internet Protocol)
- ICMP (Internet Control Message Protocol)
- IGMP (Internet Group Management Protocol)
- ARP (Address Resolution Protocol)

데이터 단위: 패킷
```

### 1계층: 네트워크 액세스 계층 (Network Access Layer)

```
OSI 1, 2계층 통합

역할:
- 물리적 전송
- MAC 주소 지정
- 프레임 전송

프로토콜:
- Ethernet
- WiFi (IEEE 802.11)
- PPP

데이터 단위: 프레임
```

---

## 📊 OSI vs TCP/IP

| OSI 7계층 | TCP/IP 4계층 | 주요 프로토콜 |
|-----------|-------------|--------------|
| 응용 | | HTTP, FTP |
| 표현 | 응용 | SSL/TLS |
| 세션 | | SSH |
| 전송 | 전송 | TCP, UDP |
| 네트워크 | 인터넷 | IP, ICMP |
| 데이터링크 | 네트워크 액세스 | Ethernet |
| 물리 | | UTP, 광케이블 |

---

# 3. TCP vs UDP

## 📊 비교표

| 구분 | TCP | UDP |
|------|-----|-----|
| **연결 방식** | 연결 지향 | 비연결 |
| **신뢰성** | 보장 ✅ | 보장 안 함 ❌ |
| **순서 보장** | 보장 ✅ | 보장 안 함 ❌ |
| **속도** | 느림 | 빠름 ✅ |
| **오버헤드** | 큼 (20바이트) | 작음 (8바이트) ✅ |
| **흐름 제어** | ✅ | ❌ |
| **혼잡 제어** | ✅ | ❌ |
| **재전송** | ✅ | ❌ |
| **사용 사례** | 웹, 이메일, 파일 전송 | 스트리밍, 게임, DNS |

---

## 🔵 TCP (Transmission Control Protocol)

### 특징

```
✅ 연결 지향 (Connection-Oriented)
✅ 신뢰성 보장
✅ 순서 보장
✅ 흐름 제어
✅ 혼잡 제어
❌ 느린 속도
```

### TCP 헤더 구조

```
0                   16                  31
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Source Port   |   Destination Port|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Sequence Number             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|        Acknowledgment Number          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Data |R|C|E|U|A|P|R|S|F|               |
|Offset|S|W|C|R|C|S|S|Y|I|    Window    |
|     |V|R|E|G|K|H|T|N|N|               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    Checksum       |  Urgent Pointer   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

주요 필드:
- Sequence Number: 순서 번호
- Acknowledgment Number: 확인 응답 번호
- Flags: SYN, ACK, FIN 등 제어 플래그
- Window: 흐름 제어 (수신 버퍼 크기)
- Checksum: 오류 검출
```

### 흐름 제어 (Flow Control)

```
수신자의 처리 속도를 고려하여 전송 속도 조절

Window Size:
- 수신자가 받을 수 있는 데이터 크기
- ACK에 포함하여 전달

예:
송신자: 1000 바이트 전송
수신자: Window = 500 → 500바이트만 전송
수신자: 처리 완료 → Window = 1000
송신자: 1000 바이트 전송
```

### 혼잡 제어 (Congestion Control)

```
네트워크 혼잡을 방지하기 위한 전송 속도 조절

알고리즘:
1. Slow Start:
   - 처음엔 천천히 시작
   - 지수적으로 증가

2. Congestion Avoidance:
   - 임계값 도달 후 선형 증가

3. Fast Retransmit:
   - 중복 ACK 3개 수신 시 즉시 재전송

4. Fast Recovery:
   - 혼잡 발생 시 절반으로 감소
```

### 사용 사례

```
✅ 웹 브라우징 (HTTP/HTTPS)
✅ 이메일 (SMTP, POP3, IMAP)
✅ 파일 전송 (FTP)
✅ 원격 접속 (SSH, Telnet)
✅ 데이터베이스 연결

→ 신뢰성이 중요한 경우
```

---

## 🟢 UDP (User Datagram Protocol)

### 특징

```
✅ 비연결 (Connectionless)
✅ 빠른 속도
✅ 작은 오버헤드
❌ 신뢰성 보장 안 함
❌ 순서 보장 안 함
❌ 흐름 제어 없음
```

### UDP 헤더 구조

```
0                   16                  31
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Source Port   |   Destination Port|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|      Length       |     Checksum      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

주요 필드:
- Source Port: 출발지 포트
- Destination Port: 목적지 포트
- Length: 전체 길이
- Checksum: 오류 검출 (선택사항)

크기: 8바이트 (TCP 20바이트의 40%)
```

### 사용 사례

```
✅ 실시간 스트리밍 (동영상, 음악)
✅ 온라인 게임
✅ DNS (도메인 조회)
✅ DHCP (IP 할당)
✅ VoIP (인터넷 전화)
✅ IoT 센서 데이터

→ 속도가 중요하고 일부 손실 허용 가능
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
TCP:
- 연결 지향, 신뢰성 보장
- 3-Way Handshake로 연결
- 순서 보장, 재전송
- 느리지만 안전
- 웹, 이메일, 파일 전송

UDP:
- 비연결, 빠른 속도
- 신뢰성 보장 안 함
- 순서 보장 안 함
- 빠르지만 손실 가능
- 스트리밍, 게임, DNS
```

### 상세 답변
```
TCP (Transmission Control Protocol):

연결 방식:
- 3-Way Handshake로 연결 수립
- 4-Way Handshake로 연결 종료
- 연결 지향

신뢰성:
- 순서 번호로 순서 보장
- ACK로 수신 확인
- 타임아웃 시 재전송
- Checksum으로 오류 검출

제어:
- 흐름 제어 (Window Size)
- 혼잡 제어 (Slow Start 등)

단점:
- 헤더 크기 큼 (20바이트)
- 연결 수립 시간
- 느린 속도

UDP (User Datagram Protocol):

연결 방식:
- 비연결
- 사전 연결 없이 전송

특징:
- 헤더 작음 (8바이트)
- 빠른 전송
- 낮은 지연시간

단점:
- 신뢰성 보장 안 함
- 순서 보장 안 함
- 손실 가능

선택 기준:
- 신뢰성 중요 → TCP
- 속도 중요 + 일부 손실 허용 → UDP
- 실시간성 중요 → UDP
```
