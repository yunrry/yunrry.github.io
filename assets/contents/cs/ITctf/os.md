# OS 운영체제

## 운영체제 종류
### Windows
- Microsoft 개발
- GUI 기반
- 상용 OS
- 널리 사용 (개인/기업)
- NTFS 파일 시스템
- .exe 실행 파일

### UNIX
- 벨 연구소 개발
- 다중 사용자/멀티태스킹
- 이식성 높음 (C언어)
- **계층 구조:**
  - **커널(Kernel)**: 하드웨어 제어, 프로세스/메모리 관리
  - **쉘(Shell)**: 사용자-커널 인터페이스, 명령어 해석기
  - **유틸리티(Utility)**: 각종 응용 프로그램
  - **파일 시스템**: 계층적 트리 구조, /(root)부터 시작
- 쉘 종류: Bourne Shell(sh), C Shell(csh), Korn Shell(ksh), Bash
- 서버용

### Linux
- 오픈 소스
- UNIX 기반
- 리누스 토르발스 개발
- 배포판 다양 (Ubuntu, CentOS 등)
- 무료
- 서버/임베디드 시스템

### macOS
- Apple 개발
- UNIX 기반
- GUI 우수
- Mac 전용
- 안정성/보안성
- Darwin 커널

### Android
- Google 개발
- Linux 커널 기반
- 모바일 OS
- 오픈 소스
- Java/Kotlin
- 다양한 제조사

### iOS
- Apple 개발
- UNIX 기반
- iPhone/iPad 전용
- 폐쇄형
- 보안 강화
- App Store


## 프로세스(Process)

### 프로세스 상태(Process State)

**5-State Model:**
- **생성(New)**: 프로세스 생성 중
- **준비(Ready)**: CPU 할당 대기
- **실행(Running)**: CPU 할당받아 실행
- **대기(Waiting/Blocked)**: I/O 완료 대기
- **종료(Terminated)**: 실행 완료

### PCB (Process Control Block)
프로세스 관리 정보 저장
- 프로세스 ID(PID)
- 프로세스 상태
- 프로그램 카운터(PC)
- CPU 레지스터
- 메모리 관리 정보
- 스케줄링 정보
- I/O 상태 정보

### 문맥 교환(Context Switching)
- CPU를 다른 프로세스로 전환
- PCB 저장/복원
- 오버헤드(Overhead) 발생

### 프로세스 스케줄링 큐
- **작업 큐(Job Queue)**: 시스템 내 모든 프로세스
- **준비 큐(Ready Queue)**: 메모리에서 실행 대기
- **대기 큐(Device Queue)**: I/O 대기

### CPU 스케줄링 알고리즘

**비선점(Non-preemptive):**
- **FCFS**: 먼저 온 순서
- **SJF**: 실행 시간 짧은 순
- **HRN**: 대기 시간 고려 우선순위
- **Priority**: 우선순위

**선점(Preemptive):**
- **RR(Round Robin)**: 시간 할당량(Time Quantum)
- **SRT**: 남은 시간 짧은 순
- **MLQ**: 다단계 큐
- **MLFQ**: 다단계 피드백 큐

### 프로세스 동기화

**임계 영역(Critical Section):**
공유 자원 접근 코드

**해결 조건:**
- 상호 배제(Mutual Exclusion)
- 진행(Progress)
- 한정 대기(Bounded Waiting)

**동기화 기법:**
- **Mutex**: 상호 배제
- **Semaphore**: 정수형 변수 (P, V 연산)
- **Monitor**: 고수준 동기화

### 교착상태(Deadlock)

**발생 조건(4가지 동시 만족):**
- 상호 배제(Mutual Exclusion)
- 점유와 대기(Hold and Wait)
- 비선점(No Preemption)
- 순환 대기(Circular Wait)

**해결 방법:**
- **예방(Prevention)**: 4가지 조건 중 하나 제거
- **회피(Avoidance)**: 은행원 알고리즘(Banker's Algorithm)
- **탐지(Detection)**: 자원 할당 그래프
- **회복(Recovery)**: 프로세스 종료/자원 선점

### 스레드(Thread)
- 프로세스 내 실행 단위
- 코드/데이터/힙 영역 공유
- 스택 영역 독립
- 문맥 교환 오버헤드 적음

### IPC (Inter-Process Communication)
- **파이프(Pipe)**: 단방향 통신
- **메시지 큐(Message Queue)**: 메시지 전달
- **공유 메모리(Shared Memory)**: 메모리 공유
- **소켓(Socket)**: 네트워크 통신