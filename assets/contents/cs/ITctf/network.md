# 네트워크
> 두 대 이상의 컴퓨터를 연결하여 자원을 공유하는 것 (전화선이나 케이블, 무선)  
> 설치 구조: 장치들의 물리적 위치에 따라 {`망형` `링형` `성형(중앙집중))`}-PtP, {`버스형` `계층형(트리,분산)` `망형`}
> 지리적 범위에 따라 `LAN`(Local Area Network) or `WAN`(Wide Area Network)으로 분류  
-> 네트워크는 **네트워크 엑세스 계층(데이터링크+물리계층)** 부터 시작된다. 


### 프로토콜
데이터 교환을 위한 표준 **통신규약**  
구문+의미+시간  
Syntex+Semantics+Timing
<br/> <br/>
___   


**예제 1**  
( )이란 TCP/IP프로토콜을 기반으로 하여 전 세계 수많은 컴퓨터와 네트워크들이 연결된 광범위한 컴퓨터 통신망이다.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 인터넷
</div>
</details>

<br/> <br/>
___   


**TCP vs IP**  

TCP : OSI 전송 계층, 연결형-가상회선  
IP : OST 네트워크 계층, 비연결형-데이터그램  
TCP/IP -> 서로 다른 컴퓨터끼리 데이터 주고받는 프로토콜 : OSI7계층 ->4계층으로 함축
<br/> <br/>
___   


## IP 주소 클래스(IP Address Class)

### 클래스 구분

| 클래스 | 첫 옥텟 범위 | 기본 서브넷 마스크 | 네트워크/호스트 비트 | 용도 |
|--------|-------------|-------------------|---------------------|------|
| A | 1~126 | 255.0.0.0 (/8) | 8/24 | 대규모 네트워크 |
| B | 128~191 | 255.255.0.0 (/16) | 16/16 | 중규모 네트워크 |
| C | 192~223 | 255.255.255.0 (/24) | 24/8 | 소규모 네트워크 |
| D | 224~239 | - | - | 멀티캐스트(Multicast) |
| E | 240~255 | - | - | 예약(연구용) |

**특수 주소:**
- 127.x.x.x: 루프백(Loopback)
- 0.0.0.0: 디폴트 라우트(Default Route)

### 사설 IP(Private IP)

- A클래스: 10.0.0.0 ~ 10.255.255.255
- B클래스: 172.16.0.0 ~ 172.31.255.255
- C클래스: 192.168.0.0 ~ 192.168.255.255

---

## 서브네팅(Subnetting)

### 개념
하나의 네트워크를 여러 서브넷으로 분할

### 서브넷 마스크(Subnet Mask)
네트워크 부분과 호스트 부분 구분

**표기법:**
- 10진수: 255.255.255.0
- CIDR: /24

### 계산 공식

```
서브넷 개수 = 2^n (n: 빌린 비트 수)
호스트 개수 = 2^m - 2 (m: 호스트 비트 수, -2는 네트워크/브로드캐스트 주소)
```

### 예제

**192.168.1.0/24를 4개 서브넷으로 분할**

1. 필요 비트: 2² = 4 → 2비트 필요
2. 새 서브넷 마스크: /26 (255.255.255.192)
3. 각 서브넷 호스트: 2⁶ - 2 = 62개

**결과:**
- 192.168.1.0/26 (0~63)
- 192.168.1.64/26 (64~127)
- 192.168.1.128/26 (128~191)
- 192.168.1.192/26 (192~255)

### CIDR 블록

| CIDR | 서브넷 마스크 | 사용 가능 호스트 |
|------|--------------|----------------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /30 | 255.255.255.252 | 2 (P2P 연결용) |
___   

<br/> <br/>

**예제 2**
- ( )는 현재 사용하는 IP주소 체계인 IPv4의 주소 부족 문제를 해결
- 128 비트
- IPv4에 비해 전송 속도 빠름
- 인증성, 기밀성, 데이터 무결성 => 보안문제 해결
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> IPv6
유 멀 애

</div>
</details>

<br/> <br/>
___   



**예제 3**
- ( )는 숫자로 된 IP 주소를 문자 형태로 표현한 것
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 도메인 네임

</div>
</details>

<br/> <br/>
___   


**예제 4**
- 도메인 네임을 IP주소로 변환하는 시스템
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> DNS

</div>
</details>

<br/> <br/>
___   


## OSI
> IOS에서 제안한 통신 규약
### 물 데 네 / 전 쎄 표 응!
(하위      ->       상위)

### 물리 계층
`실제접속`
`리피터` `허브`
### 데이터링크 계층
- 인접한 개방 시스템들 간 -> 연결설정, 유지 및 종료 담당 for 신뢰성&효율적인 정보전송
- 흐름 제어
- 프레임 동기화
- 오류제어
- 순서제어  
`HDLC` `LAPB` `LLC` `MAC` `LAPD` `PPP` `랜카드` `브리지` `스위치`
### 네트워크 계층
- 네트워크 연결을 설정, 유지 해제
- 경로설정(라우팅 Routing), 트래픽 제어, 패킷 정보 전송
- 표준 종류 : `X.25` `IP`
- 장비 : `라우터`

### 전송 계층
- 종단시스템(End to End)간 투명한 데이터 전송 (연결, 전송, 연결해제)
- 7계층의 상위3 하위3 사이의 인터페이스
- 주소설정, 다중화, 오류제어, 흐름제어
- **`TCP`**, **`UDP`**
<details class="answer-box">
<summary>TCP</summary>
<div markdown="1">

- `흐름제어` `혼잡제어` `오류제어`
- 연결 지향적, 신뢰성있는 데이터 전송 보장  
- 가상 회선 방식
- 3-Way Handshake(연결)
    - 클라이언트 -> 서버 SYN 패킷 보냄(Synchronization-동기화 요청)
    - 서버 -> 클라이언트 SYN/ACK 패킷 보냄 (연결수락)
    - 클라이언트 -> 서버 ACK 패킷 보냄 (연결완료)
- 4-Way Handshake(연결 종료)
```
클라이언트                    서버
   |                          |
   |-------- FIN ----------->|  1. 클라이언트 종료 요청
   |                          |
   |<------- ACK ------------|  2. 서버 확인 응답
   |                          |
   |<------- FIN ------------|  3. 서버 종료 준비 완료
   |                          |
   |-------- ACK ----------->|  4. 클라이언트 최종 확인
   |                          |
```
1. **FIN**: 클라이언트가 연결 종료 요청
2. **ACK**: 서버가 종료 요청 확인 (아직 데이터 전송 중일 수 있음)
3. **FIN**: 서버가 모든 데이터 전송 완료 후 종료 준비됨
4. **ACK**: 클라이언트가 최종 확인

**TIME_WAIT 상태**
- 마지막 ACK 전송 후 클라이언트는 일정 시간(2MSL) 대기
- 지연된 패킷(Packet) 처리 및 ACK 재전송 대비  

**3-Way vs 4-Way 차이**
- **3-Way**: 연결 시작 (SYN, SYN+ACK, ACK)
- **4-Way**: 연결 종료 (FIN, ACK, FIN, ACK) - 서버의 데이터 전송 완료 시간 필요

</div>
</details>

- 장비 : `게이트웨이`
### 쎼션 계층
- 송수신측간 관련성 유지, 대화 제어
- 대화 {생성, 관리, 종료}에 토큰 사용
- 소동기점, 대동기점 
- 소: ACK 안받음
### 표현 계층
- 응용에게 받은거 세션에게 전달시 데이터를 통신에 적당한 형태로 변환
- 세션에게 받은거 응용에게 맞게 변환
- 코드 변환, 데이터 암호화, 압축, 구문 검색, 포맷변환, 문맥관리
### 응답 계층
- 응용프로그램(사용자)가 OSI 환경에 접근할수 있도록함
- 응프 간의 정보 교한, 사서함, 파일 전송, 가상 터미널 등을 제공


<br/> <br/>
___   


## TCP/IP계층
### 응용 계층 (세+표+응)
- 응용프로그램간 데이터 송수신
- `TELNET` `FTP` `SMTP` `SNMP` `DNS` `HTTP`
### 전송 계층 (전송)
- 호스트 간 신뢰성 있는 통신
- `TCP` `UDP` `RTCP`
### 인터넷 계층 (네트워크)
- 주소지정, 경로설정
- `IP` `ICMP` `IGMP` `RARP`

### 네트워크 액세스 계층 (물+데)
- 실제 데이터 송수신
- `Ethernet` `IEEE 802` `HDLC` `X.25` `RS-232C` `ARQ`



<br/> <br/>
___   

## 네트워크 신기술

사물인터넷 - `IoT`  
사물 통신 - `M2M`  
중앙컴퓨터, 언제어디서나 - `클라우드 컴퓨팅`  
지리적 분산 컴퓨터들을 연결 - `그리드 컴퓨팅`  
클라우드 서비스들이나 그 자원들을 연결 - `인터클라우드 컴퓨팅`  
특수목적, 대규모 디바이스 최적화 - `메시 네트워크`  
스마트 그리드, 저전력 장거리 통신 - `와이선`  
콘텐츠 자체의 정보와 라우터 기능만으로 데이터 전송 - `NDN`


<br/> <br/>
___   


## 계층/프로토콜 예상 문제

**문제** 1  
전송 계층(Transport Layer)의 대표적인 두 프로토콜(Protocol)의 이름을 쓰시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> TCP(Transmission Control Protocol), UDP(User Datagram Protocol)

</div>
</details>

**문제** 2  
연결 지향적이며 신뢰성 있는 데이터 전송을 보장하는 프로토콜은?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> TCP(Transmission Control Protocol)

</div>
</details>

**문제** 3  
TCP의 3-Way Handshake 과정을 순서대로 나열하시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 1. SYN (클라이언트 → 서버)
> 2. SYN + ACK (서버 → 클라이언트)
> 3. ACK (클라이언트 → 서버)

</div>
</details>

**문제** 4  
TCP 연결 종료 시 사용하는 4-Way Handshake의 첫 번째 단계에서 전송되는 플래그(Flag)는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> FIN (Finish)

</div>
</details>

**문제** 5  
UDP의 특징으로 옳지 않은 것은?

<보기>
1. 비연결형 프로토콜
2. 흐름 제어 기능 제공
3. 오버헤드가 적음
4. 실시간 스트리밍에 적합

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 2번
> 
> UDP는 흐름 제어(Flow Control), 혼잡 제어(Congestion Control), 오류 제어(Error Control) 기능이 없음

</div>
</details>

**문제** 6  
전송 계층에서 포트 번호(Port Number)의 범위는? (10진수)

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 0 ~ 65535 (16비트, 2¹⁶)

</div>
</details>

**문제** 7    
Well-Known Port에 해당하는 범위는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 0 ~ 1023
> 
> - HTTP: 80
> - HTTPS: 443
> - FTP: 20, 21
> - SSH: 22
> - Telnet: 23
> - SMTP: 25
> - DNS: 53

</div>
</details>

**문제** 8  
TCP가 제공하는 흐름 제어(Flow Control) 기법의 이름을 쓰시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 슬라이딩 윈도우(Sliding Window)

</div>
</details>

**문제** 9  
수신자의 처리 속도를 고려하여 데이터 전송량을 조절하는 것은 ( A )이고, 네트워크 혼잡도를 고려하여 전송량을 조절하는 것은 ( B )이다. A와 B에 들어갈 용어를 쓰시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> A: 흐름 제어(Flow Control)
> B: 혼잡 제어(Congestion Control)

</div>
</details>

**문제** 10  
TCP 혼잡 제어 알고리즘 4가지를 쓰시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 1. Slow Start (느린 시작)
> 2. Congestion Avoidance (혼잡 회피)
> 3. Fast Retransmit (빠른 재전송)
> 4. Fast Recovery (빠른 회복)

</div>
</details>

**문제** 11 (서술형)  
TCP와 UDP의 차이점을 연결성, 신뢰성, 속도, 용도 관점에서 비교 설명하시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> **TCP:**
> - 연결성: 연결 지향(Connection-oriented)
> - 신뢰성: 높음 (오류 검출, 재전송)
> - 속도: 느림 (오버헤드 큼)
> - 용도: 파일 전송, 이메일, 웹 브라우징
> 
> **UDP:**
> - 연결성: 비연결형(Connectionless)
> - 신뢰성: 낮음 (오류 검출만)
> - 속도: 빠름 (오버헤드 작음)
> - 용도: 실시간 스트리밍, DNS, VoIP

</div>
</details>

**문제** 12  
다음 중 TCP 헤더(Header)에 포함되지 않는 필드는?

<보기>
1. Source Port
2. Sequence Number
3. TTL (Time To Live)
4. Window Size

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 3번
> 
> TTL은 IP 헤더(Network Layer)에 포함

</div>
</details>

**문제** 13  
전송 계층의 PDU(Protocol Data Unit) 명칭은?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 세그먼트(Segment)

</div>
</details>

**문제** 14  
다음 설명에 해당하는 TCP 플래그를 쓰시오.

"수신한 데이터에 대한 확인 응답을 나타내며, Acknowledgment Number 필드가 유효함을 의미한다."

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> ACK (Acknowledgment)

</div>
</details>

**문제** 15  
TCP에서 순서가 틀린 데이터를 재정렬하기 위해 사용하는 번호는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 순서 번호(Sequence Number)

</div>
</details>

**문제** 16  
수신 측이 한 번에 받을 수 있는 데이터 크기를 알려주는 TCP 헤더 필드는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Window Size (윈도우 크기)

</div>
</details>

**문제** 17  
다음 중 UDP를 사용하는 프로토콜이 아닌 것은?

<보기>
1. DNS
2. DHCP
3. TFTP
4. SMTP

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 4번
> 
> SMTP는 TCP 기반 (포트 25)

</div>
</details>

**문제** 18 (서술형)  
Stop-and-Wait와 Sliding Window의 차이점을 설명하시오.

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> **Stop-and-Wait:**
> - 한 번에 하나의 프레임만 전송
> - ACK 받은 후 다음 프레임 전송
> - 효율성 낮음
> 
> **Sliding Window:**
> - 윈도우 크기만큼 연속 전송 가능
> - ACK 없이도 다음 프레임 전송
> - 효율성 높음
> - 윈도우 크기 = 패킷의 최대치

</div>
</details>

**문제** 19  
TCP 연결에서 양쪽이 동시에 FIN을 보내 연결을 종료하는 상황을 무엇이라 하는가?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Simultaneous Close (동시 종료)

</div>
</details>

**문제** 20  
데이터의 무결성을 검증하기 위해 TCP와 UDP 헤더에 공통으로 포함되는 필드는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Checksum (체크섬)

</div>
</details>