# 14. VPN (Virtual Private Network)

## 📌 개념

```
공용 네트워크를 통해 안전한 사설 네트워크 연결을 제공
- 암호화된 터널
- 안전한 원격 접속
- 지리적 제약 우회
```

### 기본 원리

```
VPN 없이:
Client ──────────> Server
     인터넷 (평문)
     누구나 볼 수 있음 ✘

VPN 사용:
Client ──[암호화 터널]──> VPN Server ──> Server
        누구도 볼 수 없음 ✔
```

---

## 🔐 VPN 동작 방식

### 터널링 (Tunneling)

```
1. 캡슐화 (Encapsulation):
   원본 패킷을 암호화하여 새 패킷으로 감쌈

   원본: [IP Header | Data]
   ↓ 암호화
   VPN: [New IP | VPN Header | [Encrypted Original Packet]]

2. 전송:
   암호화된 패킷을 인터넷으로 전송

3. 역캡슐화 (Decapsulation):
   VPN 서버가 암호화 해제
   원본 패킷 복원
```

### 연결 과정

```
1. 인증 (Authentication):
   Client → VPN Server
   사용자명/비밀번호, 인증서

2. 키 교환 (Key Exchange):
   암호화 키 생성 및 교환
   보안 채널 수립

3. 터널 생성 (Tunnel Establishment):
   암호화된 터널 생성
   가상 IP 할당

4. 데이터 전송:
   모든 트래픽이 터널을 통해 전송
   암호화/복호화 자동

5. 종료:
   세션 종료
   터널 닫힘
```

---

## 🔧 VPN 프로토콜

### 1. PPTP (Point-to-Point Tunneling Protocol)

```
가장 오래된 VPN 프로토콜

특징:
- 포트: TCP 1723
- 암호화: MPPE (약함)
- 빠른 속도
- 설정 간단

장점:
✔ 빠름
✔ 널리 지원
✔ 간단한 설정

단점:
✘ 약한 보안 (취약점 많음)
✘ 방화벽 차단 쉬움

권장: 사용 안 함 ✘
```

### 2. L2TP/IPsec

```
L2TP (Layer 2 Tunneling Protocol)
+ IPsec (Internet Protocol Security)

특징:
- 포트: UDP 500, 1701, 4500
- 암호화: IPsec (AES)
- 이중 캡슐화 (느림)

장점:
✔ 강력한 암호화
✔ 널리 지원
✔ 안정적

단점:
✘ 느린 속도 (이중 캡슐화)
✘ 방화벽 통과 어려움

사용:
- 기업 VPN
```

### 3. OpenVPN ⭐

```
오픈소스 VPN 프로토콜

특징:
- 포트: UDP 1194 또는 TCP 443
- 암호화: OpenSSL (AES-256)
- 매우 안전
- 유연한 설정

장점:
✔ 강력한 보안
✔ 오픈소스
✔ 방화벽 우회 쉬움
✔ 크로스 플랫폼

단점:
✘ 클라이언트 소프트웨어 필요
✘ 설정 복잡

사용:
- 개인 VPN (추천) ✔
- 기업 VPN
```

### 4. IKEv2/IPsec

```
Internet Key Exchange version 2

특징:
- 포트: UDP 500, 4500
- 암호화: IPsec (AES)
- 빠른 재연결
- 모바일 친화적

장점:
✔ 빠른 속도
✔ 안정적
✔ 네트워크 전환 시 자동 재연결
✔ 모바일 최적화

단점:
✘ 제한적 플랫폼 지원
✘ 방화벽 차단 가능

사용:
- 모바일 VPN
- Windows, iOS 기본 지원
```

### 5. WireGuard ⭐⭐

```
최신 VPN 프로토콜 (2020)

특징:
- 포트: UDP (커스터마이징 가능)
- 암호화: ChaCha20, Poly1305
- 매우 빠름
- 간단한 코드 (4,000줄)

장점:
✔ 최고의 속도
✔ 강력한 보안
✔ 간단한 설정
✔ 배터리 효율적
✔ 현대적 암호화

단점:
✘ 비교적 새로움
✘ 일부 플랫폼 지원 부족

사용:
- 개인 VPN (최신 추천) ✔
- 차세대 표준
```

---

## 🌐 VPN 유형

### 1. Site-to-Site VPN

```
두 네트워크를 연결

본사 ←[VPN 터널]→ 지사

예:
본사 (서울): 192.168.1.0/24
지사 (부산): 192.168.2.0/24

VPN 연결 후:
본사 직원 → 지사 서버 직접 접속 가능

장점:
✔ 네트워크 통합
✔ 투명한 접속

사용:
- 기업 지사 연결
- 데이터센터 연결
```

### 2. Remote Access VPN (Client-to-Site)

```
개별 클라이언트가 네트워크에 연결

재택근무자 ←[VPN]→ 회사 네트워크

예:
집 (공인 IP: 203.0.113.5)
↓ VPN 연결
회사 (가상 IP: 192.168.1.100 할당)

접속:
- 회사 파일 서버
- 사내 시스템
- 프린터 등

장점:
✔ 원격 근무
✔ 안전한 접속

사용:
- 재택근무
- 출장
```

### 3. Personal VPN

```
개인 프라이버시 보호

사용자 ←[VPN]→ VPN 제공자 ←→ 인터넷

효과:
- IP 주소 숨김
- 위치 변경
- 트래픽 암호화

장점:
✔ 익명성
✔ 지리적 제약 우회
✔ 공용 WiFi 보안

사용:
- 넷플릭스 지역 제한 우회
- 토렌트
- 공용 WiFi 사용 시
```

---

## 💻 VPN 설정 예시

### OpenVPN 서버 설정 (Linux)

```bash
# OpenVPN 설치
apt-get install openvpn easy-rsa

# 인증서 생성
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
./easyrsa init-pki
./easyrsa build-ca
./easyrsa gen-req server nopass
./easyrsa sign-req server server
./easyrsa gen-dh
openvpn --genkey --secret ta.key

# 서버 설정
# /etc/openvpn/server.conf
port 1194
proto udp
dev tun

ca ca.crt
cert server.crt
key server.key
dh dh.pem
tls-auth ta.key 0

server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"

keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun

status openvpn-status.log
verb 3

# 시작
systemctl start openvpn@server
```

### OpenVPN 클라이언트 설정

```
# client.ovpn
client
dev tun
proto udp
remote your-server-ip 1194

resolv-retry infinite
nobind
persist-key
persist-tun

ca ca.crt
cert client.crt
key client.key
tls-auth ta.key 1

cipher AES-256-CBC
verb 3
```

### WireGuard 설정

```bash
# 서버 설정
# /etc/wireguard/wg0.conf
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = SERVER_PRIVATE_KEY

[Peer]
PublicKey = CLIENT_PUBLIC_KEY
AllowedIPs = 10.0.0.2/32

# 클라이언트 설정
[Interface]
Address = 10.0.0.2/24
PrivateKey = CLIENT_PRIVATE_KEY
DNS = 8.8.8.8

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = your-server-ip:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25

# 시작
wg-quick up wg0
```

---

## 🔐 VPN 보안 및 성능

### 보안 고려사항

```
1. 강력한 암호화:
   - AES-256
   - ChaCha20

2. 인증:
   - 사용자명/비밀번호
   - 인증서 (권장)
   - 2단계 인증

3. 킬 스위치 (Kill Switch):
   - VPN 연결 끊기면 인터넷 차단
   - 데이터 유출 방지

4. DNS 누수 방지:
   - VPN DNS 사용 강제
   - 실제 IP 노출 방지

5. 로그 정책:
   - No-log 정책
   - 프라이버시 보호
```

### 성능 최적화

```
1. 프로토콜 선택:
   속도: WireGuard > IKEv2 > OpenVPN (UDP) > OpenVPN (TCP)
   보안: 모두 안전 (최신 프로토콜)

2. 서버 위치:
   - 가까운 서버 선택
   - 지연시간 감소

3. 암호화 수준:
   - AES-128 vs AES-256
   - 성능 vs 보안 균형

4. 프로토콜:
   - UDP: 빠름 (손실 허용)
   - TCP: 느림 (신뢰성)

5. 하드웨어:
   - AES-NI 지원 CPU
   - 하드웨어 가속
```

---

## 🌍 상용 VPN 서비스

### 주요 제공자

```
1. ExpressVPN:
   - 94개국, 3000+ 서버
   - 빠른 속도
   - No-log 정책

2. NordVPN:
   - 60개국, 5400+ 서버
   - 저렴한 가격
   - Double VPN

3. Surfshark:
   - 무제한 동시 접속
   - 저렴
   - 빠른 속도

4. ProtonVPN:
   - 무료 플랜
   - 스위스 (강력한 프라이버시 법)
   - 오픈소스

5. Mullvad:
   - 익명 계정 (이메일 불필요)
   - WireGuard 지원
   - 프라이버시 중심
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
VPN은 공용 네트워크를 통해
안전한 사설 네트워크 연결을 제공합니다.

동작:
1. 암호화된 터널 생성
2. 모든 트래픽 암호화
3. VPN 서버 경유
4. 목적지 도달

장점:
- 보안 (암호화)
- 익명성 (IP 숨김)
- 원격 접속

프로토콜:
- OpenVPN (안전)
- WireGuard (빠름)
- IKEv2 (모바일)
```

### 상세 답변
```
VPN (Virtual Private Network):

정의:
공용 네트워크(인터넷)를 통해 
안전한 사설 네트워크 연결을 생성하는 기술

핵심 개념:

1. 터널링 (Tunneling):
   - 원본 패킷 암호화
   - 새 패킷으로 캡슐화
   - 안전한 터널 통과

2. 암호화 (Encryption):
   - AES-256, ChaCha20
   - 데이터 보호
   - 도청 방지

3. 인증 (Authentication):
   - 사용자 확인
   - 인증서 기반
   - 안전한 접속

동작 과정:

1. 연결 요청:
   Client → VPN Server
   인증 정보 전송

2. 인증 및 키 교환:
   - 사용자 인증
   - 암호화 키 생성
   - 보안 채널 수립

3. 터널 생성:
   - 가상 네트워크 인터페이스
   - 가상 IP 할당
   - 라우팅 설정

4. 데이터 전송:
   - 모든 트래픽 암호화
   - VPN 서버 경유
   - 목적지 전달

VPN 프로토콜:

1. PPTP:
   - 오래됨
   - 약한 보안
   - 사용 권장 안 함 ✘

2. L2TP/IPsec:
   - 강력한 암호화
   - 느린 속도
   - 기업에서 사용

3. OpenVPN:
   - 오픈소스
   - 매우 안전
   - 유연한 설정
   - 널리 사용 ✔

4. IKEv2/IPsec:
   - 빠른 속도
   - 모바일 최적화
   - 자동 재연결

5. WireGuard:
   - 최신 (2020)
   - 최고의 속도
   - 간단한 설정
   - 차세대 표준 ✔

VPN 유형:

1. Site-to-Site:
   - 네트워크 간 연결
   - 본사-지사 연결
   - 투명한 접속

2. Remote Access:
   - 개인-네트워크 연결
   - 재택근무
   - 원격 접속

3. Personal VPN:
   - 프라이버시 보호
   - IP 주소 숨김
   - 지역 제한 우회

장점:

✔ 보안:
   - 암호화된 통신
   - 공용 WiFi 안전

✔ 프라이버시:
   - IP 주소 숨김
   - 익명 브라우징

✔ 원격 접속:
   - 재택근무
   - 사내 시스템 접속

✔ 지역 제한 우회:
   - 콘텐츠 접근
   - 검열 우회

단점:

✘ 속도 저하:
   - 암호화 오버헤드
   - 경유 서버 지연

✘ 비용:
   - 상용 VPN 구독료
   - 서버 운영 비용

✘ 신뢰 문제:
   - VPN 제공자 신뢰 필요
   - No-log 정책 확인

보안 고려사항:

1. 킬 스위치:
   - VPN 끊기면 인터넷 차단
   - 데이터 유출 방지

2. DNS 누수 방지:
   - VPN DNS 사용
   - 실제 IP 노출 방지

3. 강력한 암호화:
   - AES-256
   - 최신 프로토콜

4. 인증:
   - 인증서 기반
   - 2단계 인증

실무 활용:

기업:
- 재택근무 지원
- 지사 간 연결
- 보안 통신

개인:
- 공용 WiFi 보안
- 프라이버시 보호
- 스트리밍 지역 제한 우회

클라우드:
- AWS VPN
- Azure VPN Gateway
- GCP Cloud VPN
```