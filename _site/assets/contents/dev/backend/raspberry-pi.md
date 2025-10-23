# Rasberry Pi

Rasberry Pi ARM 서버 스펙 확인
### CPU 정보
```bash
# CPU 상세 정보
cat /proc/cpuinfo

# CPU 아키텍처 확인
lscpu

# 간단한 CPU 정보
nproc  # CPU 코어 수
```

### 메모리 정보
```bash
# 메모리 사용량 (사람이 읽기 쉬운 형태)
free -h

# 상세 메모리 정보
cat /proc/meminfo
```

### 저장장치 정보
```bash
# 디스크 사용량
df -h

# 블록 디바이스 정보
lsblk

# 저장장치 상세 정보
sudo fdisk -l
```

### 시스템 전체 정보
```bash
# 라즈베리파이 모델 확인
cat /proc/device-tree/model

# 시스템 정보 요약
uname -a

# 하드웨어 정보 (설치되어 있다면)
sudo dmidecode

# 온도 확인 (라즈베리파이 특화)
vcgencmd measure_temp
```

### 네트워크 정보
```bash
# 네트워크 인터페이스
ip addr show
# 또는
ifconfig
```

### 종합 시스템 정보
```bash
# 시스템 전반적인 정보 (설치되어 있다면)
neofetch
# 또는
screenfetch
```
  
가장 기본적으로는 `cat /proc/cpuinfo`, `free -h`, `df -h` 명령어로 CPU, 메모리, 저장공간을 빠르게 확인할 수 있다.

**예시**
```
processor    : 0
BogoMIPS    : 108.00
Features    : fp asimd evtstrm crc32 cpuid
CPU implementer    : 0x41
CPU architecture: 8
CPU variant    : 0x0
CPU part    : 0xd08
CPU revision    : 3
processor    : 1
BogoMIPS    : 108.00
Features    : fp asimd evtstrm crc32 cpuid
CPU implementer    : 0x41
CPU architecture: 8
CPU variant    : 0x0
CPU part    : 0xd08
CPU revision    : 3
processor    : 2
BogoMIPS    : 108.00
Features    : fp asimd evtstrm crc32 cpuid
CPU implementer    : 0x41
CPU architecture: 8
CPU variant    : 0x0
CPU part    : 0xd08
CPU revision    : 3
processor    : 3
BogoMIPS    : 108.00
Features    : fp asimd evtstrm crc32 cpuid
CPU implementer    : 0x41
CPU architecture: 8
CPU variant    : 0x0
CPU part    : 0xd08
CPU revision    : 3
Revision    : c03112
Serial        : 1000000087363260
Model        : Raspberry Pi 4 Model B Rev 1.2
yoon@rasp
```

CPU 정보 분석  
기본 구성:
- 코어 수: 4개 (processor 0, 1, 2, 3)
- 아키텍처: ARM64 (CPU architecture: 8)
- CPU 타입: Cortex-A72 (CPU part: 0xd08)

상세 스펙:
- 제조사: ARM Holdings (CPU implementer: 0x41)
- BogoMIPS: 108.00 - 대략적인 성능 지표
지원 기능:  
- fp: 부동소수점 연산
- asimd: Advanced SIMD (벡터 연산)
- evtstrm: 이벤트 스트림
- crc32: CRC32 체크섬 하드웨어 가속
- cpuid: CPU 식별  

하드웨어 정보:
- 모델: Raspberry Pi 4 Model B Rev 1.2
- 리비전: c03112 (하드웨어 버전 코드)
- 시리얼: 1000000087363260


## 버퍼/캐시의 상세 사용 내역 확인

### 1. 상세 메모리 정보
```bash
cat /proc/meminfo
```
이 명령어로 버퍼, 캐시별 세부 항목을 볼 수 있다.

### 2. slabtop으로 커널 캐시 확인
```bash
sudo slabtop
```
커널이 사용하는 메모리 슬랩 캐시 정보를 실시간으로 보여준다.

### 3. vmstat으로 버퍼/캐시 모니터링
```bash
vmstat 1
```
실시간으로 버퍼/캐시 변화를 모니터링할 수 있다.

### 4. /proc/slabinfo 확인
```bash
cat /proc/slabinfo
```
커널 메모리 할당 상세 정보를 보여준다.

### 5. 페이지 캐시 상태 확인
```bash
# 파일 시스템 캐시 정보
cat /proc/sys/vm/drop_caches  # 현재 설정값

# 캐시 사용량 상세
awk '/^Cached|^Buffers|^MemFree|^MemTotal/ {print $1 $2}' /proc/meminfo
```

**예시**
```
MemTotal:        3882436 kB
MemFree:         3286172 kB
MemAvailable:    3696616 kB
Buffers:           64552 kB
Cached:           397672 kB
SwapCached:            0 kB
Active:           128808 kB
Inactive:         362904 kB
Active(anon):      39236 kB
Inactive(anon):        0 kB
Active(file):      89572 kB
Inactive(file):   362904 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:        524284 kB
SwapFree:         524284 kB
Zswap:                 0 kB
Zswapped:              0 kB
Dirty:                 4 kB
Writeback:             0 kB
AnonPages:         29588 kB
Mapped:            38696 kB
Shmem:              9740 kB
KReclaimable:      29684 kB
Slab:              54332 kB
SReclaimable:      29684 kB
SUnreclaim:        24648 kB
KernelStack:        2672 kB
PageTables:         1600 kB
SecPageTables:         0 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     2465500 kB
Committed_AS:     204972 kB
VmallocTotal:   261087232 kB
VmallocUsed:       12184 kB
VmallocChunk:          0 kB
Percpu:              720 kB
CmaTotal:         524288 kB
CmaFree:          505884 kB
```

버퍼/캐시 상세 분석  
총 480MB (버퍼+캐시) 내역:  
📁 파일 시스템 캐시 (397MB)  
- Cached: 397,672 kB (약 388MB) - 가장 큰 부분
    - Active(file): 89,572 kB (87MB) - 최근 사용된 파일 캐시
    - Inactive(file): 362,904 kB (354MB) - 덜 활성화된 파일 캐시

💾 디스크 버퍼 (64MB)
- Buffers: 64,552 kB (63MB) - 블록 디바이스 I/O 버퍼

🔧 커널 메모리 (54MB)
- Slab: 54,332 kB (53MB) - 커널 객체 캐시
    - SReclaimable: 29,684 kB (29MB) - 회수 가능한 슬랩
    - SUnreclaim: 24,648 kB (24MB) - 회수 불가능한 슬랩

📋 기타 시스템 메모리
- AnonPages: 29,588 kB (29MB) - 익명 페이지 (프로세스 메모리)
- Mapped: 38,696 kB (38MB) - 메모리 매핑된 파일
- Shmem: 9,740 kB (9.5MB) - 공유 메모리

  
<br>

현재 내가 사용하고있는 RaspberryPi OS : **Debian GNU/Linux**
```
Linux raspberrypi 6.12.34+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.34-1+rpt1~bookworm (2025-06-26) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Oct 23 05:33:46 2025 from 59.13.106.248

Wi-Fi is currently blocked by rfkill.
Use raspi-config to set the country before use.
```

<br><br>
---
`#RaspberryPi` `#ARM`