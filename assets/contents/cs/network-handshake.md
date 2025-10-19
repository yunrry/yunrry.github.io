# 4. 3-Way Handshake & 4-Way Handshake

## 📌 3-Way Handshake (연결 수립)

### 개념
```
TCP 연결을 수립하는 3단계 과정
SYN → SYN+ACK → ACK
```

### 동작 과정

```
Client                    Server

[CLOSED]                 [LISTEN]
   |                         |
   |  1. SYN (seq=100)      |
   |----------------------->|
   |                    [SYN_RCVD]
   |                         |
   | 2. SYN+ACK (seq=200,   |
   |     ack=101)            |
   |<-----------------------|
[ESTABLISHED]               |
   |                         |
   |  3. ACK (ack=201)      |
   |----------------------->|
   |                  [ESTABLISHED]
   |                         |
   
연결 수립 완료! ✅
```

### 상세 설명

```
1단계: SYN (Client → Server)
- Client가 연결 요청
- SYN 플래그 = 1
- Sequence Number = 100 (랜덤)
- 상태: CLOSED → SYN_SENT

2단계: SYN+ACK (Server → Client)
- Server가 요청 수락
- SYN 플래그 = 1
- ACK 플래그 = 1
- Sequence Number = 200 (랜덤)
- Acknowledgment Number = 101 (100+1)
- 상태: LISTEN → SYN_RCVD

3단계: ACK (Client → Server)
- Client가 확인 응답
- ACK 플래그 = 1
- Acknowledgment Number = 201 (200+1)
- 상태: SYN_SENT → ESTABLISHED
- Server 상태: SYN_RCVD → ESTABLISHED

연결 수립 완료!
```

### 왜 3-Way인가?

```
❌ 2-Way만으로는 부족:
Client: "연결하자!" (SYN)
Server: "OK!" (SYN+ACK)
→ Client가 살아있는지 확인 불가

✅ 3-Way로 양방향 확인:
Client: "연결하자!" (SYN)
Server: "OK, 너도 받았어?" (SYN+ACK)
Client: "응, 받았어!" (ACK)
→ 양쪽 모두 확인 ✅
```

---

## 📌 4-Way Handshake (연결 종료)

### 개념
```
TCP 연결을 종료하는 4단계 과정
FIN → ACK → FIN → ACK
```

### 동작 과정

```
Client                    Server

[ESTABLISHED]         [ESTABLISHED]
   |                         |
   |  1. FIN (seq=300)      |
   |----------------------->|
[FIN_WAIT_1]                |
   |                    [CLOSE_WAIT]
   |                         |
   |  2. ACK (ack=301)      |
   |<-----------------------|
[FIN_WAIT_2]                |
   |                         |
   |    (Server 작업 완료)   |
   |                         |
   |  3. FIN (seq=400)      |
   |<-----------------------|
   |                  [LAST_ACK]
[TIME_WAIT]                 |
   |                         |
   |  4. ACK (ack=401)      |
   |----------------------->|
   |                   [CLOSED]
   |                         |
(2MSL 대기)                 |
   |                         |
[CLOSED]

연결 종료 완료! ✅
```

### 상세 설명

```
1단계: FIN (Client → Server)
- Client가 연결 종료 요청
- FIN 플래그 = 1
- Sequence Number = 300
- 상태: ESTABLISHED → FIN_WAIT_1

2단계: ACK (Server → Client)
- Server가 종료 요청 확인
- ACK 플래그 = 1
- Acknowledgment Number = 301
- 상태: ESTABLISHED → CLOSE_WAIT
- Client 상태: FIN_WAIT_1 → FIN_WAIT_2

(Server가 남은 데이터 전송 완료)

3단계: FIN (Server → Client)
- Server가 연결 종료 준비 완료
- FIN 플래그 = 1
- Sequence Number = 400
- 상태: CLOSE_WAIT → LAST_ACK
- Client 상태: FIN_WAIT_2 → TIME_WAIT

4단계: ACK (Client → Server)
- Client가 최종 확인 응답
- ACK 플래그 = 1
- Acknowledgment Number = 401
- Server 상태: LAST_ACK → CLOSED
- Client 상태: TIME_WAIT → (2MSL 대기) → CLOSED

연결 종료 완료!
```

### TIME_WAIT 상태

```
왜 바로 종료 안 하고 대기하는가?

이유 1: 지연 패킷 처리
- 네트워크에 남아있는 패킷 처리
- 같은 포트로 즉시 재연결 시 문제 방지

이유 2: 마지막 ACK 재전송
- Server가 ACK를 못 받으면 FIN 재전송
- 이때 다시 ACK 전송 가능

대기 시간:
2MSL (Maximum Segment Lifetime)
= 2 × 최대 세그먼트 생존 시간
= 보통 1~4분
```

### 왜 4-Way인가?

```
Server의 Half-Close 지원:

Client: "나는 보낼 데이터 없어" (FIN)
Server: "OK, 받았어" (ACK)
        "근데 나는 아직 보낼 게 있어"
        (데이터 전송 계속)
        "이제 나도 끝!" (FIN)
Client: "알았어!" (ACK)

→ 양방향 독립적 종료 가능 ✅
```

---

## 💬 면접 답변 예시

### 3-Way Handshake

**짧은 답변:**
```
TCP 연결 수립 과정입니다.

1. SYN: Client → Server 연결 요청
2. SYN+ACK: Server → Client 수락
3. ACK: Client → Server 확인

양방향 통신 가능 확인 후 연결 수립합니다.
```

**상세 답변:**
```
3-Way Handshake는 TCP 연결을 수립하는 
3단계 과정입니다.

과정:
1. SYN (Client → Server):
   - Client가 연결 요청
   - SYN 플래그 = 1
   - 초기 Sequence Number 전송
   
2. SYN+ACK (Server → Client):
   - Server가 요청 수락
   - SYN, ACK 플래그 = 1
   - 자신의 Sequence Number 전송
   - Client의 Seq+1을 ACK로 응답
   
3. ACK (Client → Server):
   - Client가 최종 확인
   - ACK 플래그 = 1
   - Server의 Seq+1을 ACK로 응답

이유:
- 양방향 통신 가능 확인
- 초기 Sequence Number 교환
- 신뢰성 있는 연결 수립

2-Way로는 부족:
- Client가 살아있는지 확인 불가
- Server의 응답을 Client가 받았는지 미확인
```

### 4-Way Handshake

**짧은 답변:**
```
TCP 연결 종료 과정입니다.

1. FIN: Client → Server 종료 요청
2. ACK: Server → Client 확인
3. FIN: Server → Client 종료 준비 완료
4. ACK: Client → Server 최종 확인

양방향 독립적 종료를 지원합니다.
```

**상세 답변:**
```
4-Way Handshake는 TCP 연결을 종료하는 
4단계 과정입니다.

과정:
1. FIN (Client → Server):
   - Client가 연결 종료 요청
   - 더 이상 보낼 데이터 없음
   
2. ACK (Server → Client):
   - Server가 종료 요청 확인
   - 아직 보낼 데이터가 있을 수 있음
   
3. FIN (Server → Client):
   - Server도 종료 준비 완료
   - 남은 데이터 전송 완료
   
4. ACK (Client → Server):
   - Client가 최종 확인
   - TIME_WAIT 상태로 2MSL 대기

TIME_WAIT 이유:
- 지연 패킷 처리
- 마지막 ACK 유실 대비
- 같은 포트 즉시 재사용 방지

Half-Close:
- 한쪽만 먼저 종료 가능
- 상대방은 계속 데이터 전송 가능
```