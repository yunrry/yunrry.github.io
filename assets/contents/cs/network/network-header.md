## 헤더(Header)란?

헤더는 네트워크 통신에서 데이터 패킷의 앞부분에 붙는 **제어 정보(control information)**이다.    
실제 전송하려는 데이터(페이로드)와 함께 전송되며, 데이터를 올바른 목적지로 전달하고 처리하는 데 필요한 메타데이터를 포함한다.   

## OSI 7계층별 주요 헤더

### 1. **데이터 링크 계층 (Layer 2) - 이더넷 헤더**
- **출처**: IEEE 802.3 표준
- **주요 필드**:
  - 목적지 MAC 주소 (6 bytes)
  - 출발지 MAC 주소 (6 bytes)
  - 타입/길이 (2 bytes)
  - FCS (Frame Check Sequence)

### 2. **네트워크 계층 (Layer 3) - IP 헤더**

**IPv4 헤더** (RFC 791):
- Version (4 bits): IP 버전
- IHL (4 bits): 헤더 길이
- Type of Service (8 bits): QoS
- Total Length (16 bits): 전체 패킷 크기
- Identification, Flags, Fragment Offset: 단편화 관련
- TTL (Time To Live, 8 bits): 패킷 생존 시간
- Protocol (8 bits): 상위 프로토콜 (TCP=6, UDP=17)
- Header Checksum: 오류 검출
- **출발지 IP 주소 (32 bits)**
- **목적지 IP 주소 (32 bits)**

**IPv6 헤더** (RFC 2460):
- 더 단순화된 구조 (40 bytes 고정)
- 128비트 주소 체계

### 3. **전송 계층 (Layer 4)**

**TCP 헤더** (RFC 793):
- 출발지 포트 (16 bits)
- 목적지 포트 (16 bits)
- Sequence Number (32 bits): 순서 번호
- Acknowledgment Number (32 bits): 확인 응답 번호
- Flags: SYN, ACK, FIN, RST 등
- Window Size: 흐름 제어
- Checksum: 오류 검출

**UDP 헤더** (RFC 768):
- 출발지 포트 (16 bits)
- 목적지 포트 (16 bits)
- Length (16 bits)
- Checksum (16 bits)
- TCP보다 훨씬 단순 (8 bytes만)

### 4. **응용 계층 (Layer 7)**

**HTTP 헤더** (RFC 7230-7235):
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

## 헤더의 역할

1. **주소 지정**: 출발지와 목적지 식별
2. **라우팅**: 패킷 경로 결정
3. **오류 검출**: Checksum을 통한 데이터 무결성 검증
4. **흐름 제어**: 네트워크 혼잡 관리
5. **프로토콜 식별**: 상위 계층 프로토콜 구분

## 캡슐화 (Encapsulation)

데이터가 각 계층을 거치며 해당 계층의 헤더가 추가되는 과정:
```
[응용 계층 데이터]
↓
[TCP 헤더][데이터]
↓
[IP 헤더][TCP 헤더][데이터]
↓
[이더넷 헤더][IP 헤더][TCP 헤더][데이터][이더넷 트레일러]
```

## 참고 문헌
- **Tanenbaum, A. S., & Wetherall, D. J.**    
  (2010). *Computer Networks* (5th ed.). Pearson - 네트워크 기초 이론   
- **Stevens, W. R.**    
  (1994). *TCP/IP Illustrated, Volume 1: The Protocols*. Addison-Wesley - TCP/IP 프로토콜 상세 설명   
- **IETF RFCs**: RFC 791 (IPv4), RFC 793 (TCP), RFC 768 (UDP), RFC 2460 (IPv6)

