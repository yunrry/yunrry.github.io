# 사이버 공격 기법 암기

## DoS/DDoS 공격

**SYN Flooding**
- TCP 3-Way Handshake 악용
- SYN 패킷만 전송, ACK 응답 안 함
- 서버 연결 대기 큐 포화

**UDP Flooding**
- UDP 패킷 대량 전송
- 비연결형 프로토콜 악용
- 대역폭 소진

**Smurf**
- ICMP Echo Request를 브로드캐스트
- 출발지 IP를 피해자로 위조
- 증폭된 응답으로 공격

**TearDrop**
- IP 단편화(Fragmentation) 악용
- 중첩되는 Offset 값 설정
- 재조립 과정에서 시스템 마비

**Land Attack**
- 송신 IP = 수신 IP로 설정
- 송신 포트 = 수신 포트
- 무한 루프로 시스템 다운

**Ping of Death**
- 최대 크기(65,535바이트) 초과 ICMP
- 단편화 후 재조립 시 버퍼 오버플로
- 시스템 크래시

---

## 애플리케이션 공격

**SQL Injection**
- 입력값에 SQL 쿼리 삽입
- DB 인증 우회, 데이터 탈취
- `' OR '1'='1` 등 사용

**XSS (Cross-Site Scripting)**
- 악성 스크립트를 웹 페이지에 삽입
- 사용자 브라우저에서 실행
- 쿠키 탈취, 세션 하이재킹

**CSRF (Cross-Site Request Forgery)**
- 사용자가 의도하지 않은 요청 전송
- 인증된 세션 악용
- 송금, 정보 변경 등 수행

**Buffer Overflow**
- 버퍼 크기 초과 데이터 입력
- 메모리 영역 침범
- 임의 코드 실행

---

## 네트워크 공격

**MITM (Man In The Middle)**
- 통신 중간에서 데이터 가로채기
- 도청, 변조, 위조
- ARP Spoofing으로 구현

**Session Hijacking**
- 정상 세션 가로채기
- 세션 ID 탈취 후 사용
- 인증 우회

**Sniffing**
- 네트워크 패킷 도청
- 평문 데이터 수집
- Promiscuous Mode 사용

**Spoofing**
- IP/MAC/DNS 주소 위조
- 신뢰 관계 악용
- 출처 은닉

**Pharming**
- DNS 테이블 변조
- 가짜 사이트로 유도
- 개인정보 탈취

---

## 시스템 침투

**Brute Force**
- 모든 조합 시도
- 시간 소요 많음
- 단순하지만 효과적

**Dictionary Attack**
- 사전 파일 기반 공격
- 일반 단어, 흔한 비밀번호
- Brute Force보다 빠름

**Rainbow Table**
- 미리 계산된 해시 테이블
- 해시값 → 원본 역산
- 시간-공간 트레이드오프

**Key Logger**
- 키보드 입력 기록
- 하드웨어/소프트웨어 방식
- 비밀번호, 개인정보 탈취

**Rootkit**
- 관리자 권한 획득 후 은닉
- 시스템 깊숙이 침투
- 탐지 어려움


**Bootkit (부트킷)**
- 부트 영역(MBR/UEFI) 감염 악성코드
- OS 로딩 전 실행
- Rootkit보다 깊은 레벨, 탐지 매우 어려움

**Backdoor**
- 정상 인증 우회 통로
- 지속적 접근 가능
- 숨겨진 계정, 포트

**Trojan Horse**
- 정상 프로그램으로 위장
- 내부에 악성 코드
- 사용자가 직접 실행

---

## 고급 지속 위협

**APT (Advanced Persistent Threat)**
- 특정 조직 표적 장기 공격
- 단계: 침투 → 검색 → 수집 → 유출
- 지능적, 은밀함

**Zero-Day Attack**
- 공개되지 않은 취약점 공격
- 패치 존재 안 함
- 방어 매우 어려움

**Ransomware**
- 파일 암호화 후 금전 요구
- 확장자 변경, 백업 삭제
- WannaCry, Petya 등

## 기타
- **Social Engineering**: 사회공학기법
- **Phishing**: 피싱
- **Worm**: 웜
- **Virus**: 바이러스
- **DRDoS**: 분산 반사 서비스 거부

**암기 팁**: DoS계 → 앱계 → 네트워크계 → 시스템계 순서


## 사이버 공격 기법 상세

### Social Engineering (사회공학기법)
- **Phishing**: 이메일 위장
- **Spear Phishing**: 특정 대상 공격
- **Whaling**: 고위직 표적
- **Smishing**: SMS 피싱
- **Vishing**: 음성 피싱
- **Qishing**: QR코드 피싱
- **Pretexting**: 신뢰 관계 위장
- **Baiting**: 미끼(USB 등)
- **Tailgating**: 물리적 무단 출입
- **Shoulder Surfing**: 어깨 넘어 훔쳐보기
- **Dumpster Diving**: 쓰레기통 뒤지기

### Worm (웜)
- **자가 복제**: 독립 실행
- **네트워크 전파**: 자동 확산
- **Morris Worm**: 최초 웜
- **Code Red**: IIS 취약점
- **Nimda**: 다중 경로 감염
- **Blaster**: Windows RPC 공격

### Virus (바이러스)
- **숙주 필요**: 파일/부트 감염
- **Macro Virus**: 문서 매크로
- **Boot Sector Virus**: 부트 영역
- **File Infector**: 실행 파일
- **Polymorphic Virus**: 변형
- **Stealth Virus**: 은폐

### DRDoS (Distributed Reflection DoS)
- **반사 공격**: 응답 증폭
- **DNS Amplification**: DNS 서버 악용
- **NTP Amplification**: NTP 서버 악용
- **SSDP Reflection**: UPnP 프로토콜
- **Memcached Attack**: 캐시 서버
- **IP 위조**: 출발지 스푸핑


## 보안 용어

**Logic Bomb (논리 폭탄)**
- 특정 조건 충족 시 실행되는 악성 코드
- 날짜, 이벤트 등을 트리거로 설정
- 시한폭탄처럼 작동

**Spyware (스파이웨어)**
- 사용자 몰래 정보 수집
- 웹 브라우징, 키 입력, 파일 등 감시
- 광고/마케팅 목적 또는 악의적 사용

**Honeypot (허니팟)**
- 공격자 유인용 가짜 시스템
- 공격 패턴 분석, 정보 수집
- 방어 기법 (함정)

**Bug Bounty (버그 바운티)**
- 취약점 발견 시 보상 제도
- 합법적 화이트햇 해커 활용
- 보안 강화 목적
