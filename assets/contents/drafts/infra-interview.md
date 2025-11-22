# Infra Interview



### 1. 사용해보신(직접설치해본) 리눅스 배포판과 사용해보신 배포판의 차이점에 대해서 느낀점 위주로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Redhat 계열 : RHEL, CentOS, Fedora 등 
Debian 계열 : Debian, Ubuntu, Mint 등
제조사, 커널 버전, package installer (yum<dnf>, apt) 등등
</div>
</details>

<br/><br/>
___


### 2. 웹브라우저에서 daum.net에 접속했을 때 발생하는 일련의 과정과 브라우저에서 "안전한 페이지(자물쇠마크)"로 표기되는 이유에 대해서 아시는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 물리 - 데이터링크 - 네트워크 - 전송 - 세션 - 표현 - 응용 계층 별로 순서대로 이야기 한다.
OSI7 계층의 목적인 "프로토콜을 기능별로 나눈다"에 대해 설명한다.
자물쇠 마크는 https 보안을 위한 SSL(TLS) 프로토콜을 사용하기 때문이며, 
OSI 7 layer 에서 Session 계층과 연관이 있다고 말하면 가산점
</div>
</details>

<br/><br/>
___


### 3. TCP에서 3-Handshake에 대해서 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 클라이언트와 서버가 연결을 수립하는 과정.
3-Handshake에 대해 패킷을 보내는 주체와 대상을 순서에 맞게 설명한다 (SYN - SYN + ACK - ACK)
</div>
</details>

<br/><br/>
___


### 4. OSI 7 Layer에 대해서 아는대로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Physical - Data Link - Network - Transport - Session - Presentation - Application 
과 각각의 특징에 대해서 설명한다
TCP/IP 스택과의 연계성을 토대로 설명이 가능한지
</div>
</details>

<br/><br/>
___


### 5. 리눅스 시스템의 전원인가 후에 부팅이 완료되는 시점까지의 과정을 아는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 시간 순서대로 POST 과정, 부트로더, 커널 역할, run-level, init (systemd) 프로세스에 대한 설명을 포함하여 답변
</div>
</details>

<br/><br/>
___


### 6. 공인IP와 사설IP의 차이점에 대해서 설명해주세요. 네트워크 클래스(a,b,c)별로 사설IP 대역을 알고 계신가요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 공인IP : ISP가 공급하는 전세계에서 유일한 주소를 가지는 외부 공개 IP주소
사설IP : 특정 조직 (회사, 가정 등등) 내에서 별도로 할당된 내부용 IP주소
Class (사설 기준) A : 10.X.X.X, B : 172.16.X.X , C: 192.168.X.X 
CIDR을 알고 있는지 여부도 가산점
</div>
</details>

<br/><br/>
___


### 7. 리눅스의 Page Cache에 대해서 아는대로 설명해주세요. 그리고 Swap이 발생하는 이유

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Page Cache는 파일 데이터에 대한 읽기, 쓰기에 대한 I/O 작업을 빠르게 하기 위해서 커널에서 사용하고 있는 영역으로 free 명령어의 "cached"에 해당하는 영역이다. 
Swap은 메모리 사용량이 높아짐으로 인해 시스템의 메모리가 부족하게 되었을때, priority가 (nice) 낮은 프로세스를 swap 영역으로 옮기며, 메모리가 아닌 디스크 영역으로 성능저하가 발생함
THP, Huge Page에 대한 부분도 설명하면 가산점
Swap 설명때 NUMA Zone(Node)을 언급하면 가산점
</div>
</details>

<br/><br/>
___


### 8. 지원자가 알고 있는 파일시스템이 어떤것이 있는지와, 그 파일시스템의 특징을 설명해주세요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> ext3,4 , xfs, ntfs, fat32, exfat, nfs, cifs, zfs 등 언급 하며
특히 linux에서 통상적으로 쓰는 ext, xfs 관련 파일 시스템을 언급하면서 저널링 파일시스템(커밋 전 변경 사항을 저널에 기록)이며 그 특징을 언급하면 가산점
VFS에 대한 이해를 토대로 하면 가산점
</div>
</details>

<br/><br/>
___


### 9. 가상머신과 컨테이너머신의 차이점이 무엇인가요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 가상머신 : 하이퍼바이저 등으로 인하여 게스트OS가 설치되어 기존 OS 환경과 독립적으로 분리하여 구성
컨테이너 : 도커, lxc 등으로 불리며, 커널을 공유하면서 리눅스의 cgroup, namespace의 기술을 이용하여 별도의 이미지를 이용하여 어플리케이션을 실행
cgroup, namespace에 대해서 디테일하게 답변 시 가산점
linux namespace의 구현체 종류도 알고 있다면 가산점
</div>
</details>

<br/><br/>
___


### 10. 로드밸런싱의 개념과 동작방식에 대해서 아는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서버에 인입되는 네트워크 트래픽을 분산시키고 서비스의 안정성을 높이기 위해서 사용하는 것.
L2, L3, L4, L7 등 모드별 동작방식에 대해 간단하게 설명한다.
DSR, inline 모드에 대한 이해. 분배방식(RR, least connection 등)을 설명하면 가산점
</div>
</details>

<br/><br/>
___


### 11. 리눅스 커널파라미터와 시스템설정파일에 대해서 알고 있는 것을 설명해주세요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 커널파라미터 : tcp 위주, file 관련 위주의 커널 파라미터를 답변
설정 파일 : /etc/security/limits.conf, /etc/sysctl.conf, /etc/pam.d/*, /etc/systemd/system.conf, /etc/init.d/* 등에 대한 내용 언급
sysfs, /proc 파일시스템에 대한 이해를 토대로 한다면 가산점
</div>
</details>

<br/><br/>
___


### 12. 시스템에서 운영체제의 역할에 대해 아는대로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 운영체제는 하드웨어 자원관리와 프로세스 관리, 사용자 편의 제공 등의 운영체제 일반론적인 답변. 
리눅스와 커널에 대해 추가로 설명할 수 있으면 가산점
</div>
</details>

<br/><br/>
___


### 13. 블록디바이스가 무엇인지 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 데이터에 접근할 때 블록을 기준으로 읽고 쓰는 장치를 의미, 적절한 블록 디바이스의 예시를 들면서 답변
디스크, CD/DVD 등의 데이터 적재시 사용하는 장치를 주로 일컬으며, /dev 에서 ls 명령어로 확인 가능.
메모리 장치도 block 디바이스임을 인지하는지도 확인 필요
</div>
</details>

<br/><br/>
___


### 14. 신문기사/방송에서 본 보안사고 기억나는거과 느낀점

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1.25대란, 7.7대란, 3.20대란 등 사회적으로 이슈가 되었던 사고에 대한 관심도와 원인을 설명하면 가산점
인터파크, 옥션, SK컴즈등 대량의 개인정보 유출사고의 원인을 설명할 수 있으면 가산점
</div>
</details>

<br/><br/>
___


### 15. 카카오톡 보안 기능을 추가한다면 어떤걸 추가하고 싶은지 말씀해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 모범답안이 정해진 항목은 아님
</div>
</details>

<br/><br/>
___


### 16. 웹서비스 이용자 계정 패스워드는 서버에서 어떻게 저장되는지 설명해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Hash 또는 Salted Hash 사용하여 해시값 저장. SHA2 해시 알고리즘을 언급하거나 PBKDF2 같은 패스워드 저장 전용 알고리즘을 답한다면 가산점
</div>
</details>

<br/><br/>
___


### 17. 웹서버 인증서가 어떻게 웹의 안전성 및 신뢰성을 확보해주는지 설명해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 루트인증서에서 도메인인증서까지 인증서 체인 유효성 검증. 전자서명이나 "Root of Trust" 를 언급하면 가산점
</div>
</details>

<br/><br/>
___


### 18. 카카오 임직원의 보안의식을 높일수 있는 방법에는 어떤것이 있는지 아는데로 말씀해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 보안교육, 캠페인, 해킹사고대비 피싱메일 모의훈련 등
참여 성과에 따른 보상과 인센티브를 지급등 동기를 부여방법을 언급하면 가산점
</div>
</details>

<br/><br/>
___


### 19. 보안솔루션을 하나 예시로 들고 설명해보시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 침입탐지시스템, 침입차단시스템, 백신, PMS, 서버접근통제시스템, DB암호화시스템 등등 언급하고 추가적인 심화 질문에 답변할 수 있으면 가산점
</div>
</details>

<br/><br/>
___


### 20. 위험, 위협, 취약점을 구분해서 설명할 수 있는가?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 위협*취약점=위험이라는 개념을 이해하면 됨, 위협은 상수, 취약점은 변수라서 취약점 관리를 통해 위험을 낮출수 있다고 답변하면 베스트
</div>
</details>

<br/><br/>
___


### 21. 보안 취약점 또는 공격(해킹)방법에 대해 들어보았거나 알고 있는 내용을 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 취약한 비밀번호/비밀번호 무작위 대입, 피싱/스미싱, 도감청 등을 쉽게 접할수 있는 해킹기법 또는 취약점 언급. XSS, SQLi, CSRF 등 전문적인 공격 기법 또는 취약점 유형을 언급하면 가산점
</div>
</details>

<br/><br/>
___


### 22. 사용해보신(직접설치해본) 리눅스 배포판과 사용해보신 배포판의 차이점에 대해서 느낀점 위주로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Redhat 계열 : RHEL, CentOS, Fedora 등 
Debian 계열 : Debian, Ubuntu, Mint 등
제조사, 커널 버전, package installer (yum<dnf>, apt) 등등
</div>
</details>

<br/><br/>
___


### 23. 웹브라우저에서 daum.net에 접속했을 때 발생하는 일련의 과정과 브라우저에서 "안전한 페이지(자물쇠마크)"로 표기되는 이유에 대해서 아시는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 물리 - 데이터링크 - 네트워크 - 전송 - 세션 - 표현 - 응용 계층 별로 순서대로 이야기 한다.
OSI7 계층의 목적인 "프로토콜을 기능별로 나눈다"에 대해 설명한다.
자물쇠 마크는 https 보안을 위한 SSL(TLS) 프로토콜을 사용하기 때문이며, 
OSI 7 layer 에서 Session 계층과 연관이 있다고 말하면 가산점
</div>
</details>

<br/><br/>
___


### 24. TCP에서 3-Handshake에 대해서 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 클라이언트와 서버가 연결을 수립하는 과정.
3-Handshake에 대해 패킷을 보내는 주체와 대상을 순서에 맞게 설명한다 (SYN - SYN + ACK - ACK)
</div>
</details>

<br/><br/>
___


### 25. OSI 7 Layer에 대해서 아는대로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Physical - Data Link - Network - Transport - Session - Presentation - Application 
과 각각의 특징에 대해서 설명한다
TCP/IP 스택과의 연계성을 토대로 설명이 가능한지
</div>
</details>

<br/><br/>
___


### 26. 리눅스 시스템의 전원인가 후에 부팅이 완료되는 시점까지의 과정을 아는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 시간 순서대로 POST 과정, 부트로더, 커널 역할, run-level, init (systemd) 프로세스에 대한 설명을 포함하여 답변
</div>
</details>

<br/><br/>
___


### 27. 공인IP와 사설IP의 차이점에 대해서 설명해주세요. 네트워크 클래스(a,b,c)별로 사설IP 대역을 알고 계신가요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 공인IP : ISP가 공급하는 전세계에서 유일한 주소를 가지는 외부 공개 IP주소
사설IP : 특정 조직 (회사, 가정 등등) 내에서 별도로 할당된 내부용 IP주소
Class (사설 기준) A : 10.X.X.X, B : 172.16.X.X , C: 192.168.X.X 
CIDR을 알고 있는지 여부도 가산점
</div>
</details>

<br/><br/>
___


### 28. 리눅스의 Page Cache에 대해서 아는대로 설명해주세요. 그리고 Swap이 발생하는 이유

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Page Cache는 파일 데이터에 대한 읽기, 쓰기에 대한 I/O 작업을 빠르게 하기 위해서 커널에서 사용하고 있는 영역으로 free 명령어의 "cached"에 해당하는 영역이다. 
Swap은 메모리 사용량이 높아짐으로 인해 시스템의 메모리가 부족하게 되었을때, priority가 (nice) 낮은 프로세스를 swap 영역으로 옮기며, 메모리가 아닌 디스크 영역으로 성능저하가 발생함
THP, Huge Page에 대한 부분도 설명하면 가산점
Swap 설명때 NUMA Zone(Node)을 언급하면 가산점
</div>
</details>

<br/><br/>
___


### 29. 지원자가 알고 있는 파일시스템이 어떤것이 있는지와, 그 파일시스템의 특징을 설명해주세요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> ext3,4 , xfs, ntfs, fat32, exfat, nfs, cifs, zfs 등 언급 하며
특히 linux에서 통상적으로 쓰는 ext, xfs 관련 파일 시스템을 언급하면서 저널링 파일시스템(커밋 전 변경 사항을 저널에 기록)이며 그 특징을 언급하면 가산점
VFS에 대한 이해를 토대로 하면 가산점
</div>
</details>

<br/><br/>
___


### 30. 가상머신과 컨테이너머신의 차이점이 무엇인가요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 가상머신 : 하이퍼바이저 등으로 인하여 게스트OS가 설치되어 기존 OS 환경과 독립적으로 분리하여 구성
컨테이너 : 도커, lxc 등으로 불리며, 커널을 공유하면서 리눅스의 cgroup, namespace의 기술을 이용하여 별도의 이미지를 이용하여 어플리케이션을 실행
cgroup, namespace에 대해서 디테일하게 답변 시 가산점
linux namespace의 구현체 종류도 알고 있다면 가산점
</div>
</details>

<br/><br/>
___


### 31. 로드밸런싱의 개념과 동작방식에 대해서 아는대로 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서버에 인입되는 네트워크 트래픽을 분산시키고 서비스의 안정성을 높이기 위해서 사용하는 것.
L2, L3, L4, L7 등 모드별 동작방식에 대해 간단하게 설명한다.
DSR, inline 모드에 대한 이해. 분배방식(RR, least connection 등)을 설명하면 가산점
</div>
</details>

<br/><br/>
___


### 32. 리눅스 커널파라미터와 시스템설정파일에 대해서 알고 있는 것을 설명해주세요

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 커널파라미터 : tcp 위주, file 관련 위주의 커널 파라미터를 답변
설정 파일 : /etc/security/limits.conf, /etc/sysctl.conf, /etc/pam.d/*, /etc/systemd/system.conf, /etc/init.d/* 등에 대한 내용 언급
sysfs, /proc 파일시스템에 대한 이해를 토대로 한다면 가산점
</div>
</details>

<br/><br/>
___


### 33. 시스템에서 운영체제의 역할에 대해 아는대로 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 운영체제는 하드웨어 자원관리와 프로세스 관리, 사용자 편의 제공 등의 운영체제 일반론적인 답변. 
리눅스와 커널에 대해 추가로 설명할 수 있으면 가산점
</div>
</details>

<br/><br/>
___


### 34. 블록디바이스가 무엇인지 설명해주세요

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 데이터에 접근할 때 블록을 기준으로 읽고 쓰는 장치를 의미, 적절한 블록 디바이스의 예시를 들면서 답변
디스크, CD/DVD 등의 데이터 적재시 사용하는 장치를 주로 일컬으며, /dev 에서 ls 명령어로 확인 가능.
메모리 장치도 block 디바이스임을 인지하는지도 확인 필요
</div>
</details>

<br/><br/>
___
