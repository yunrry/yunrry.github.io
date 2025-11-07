# 메모리 관리 - 페이지 교체 알고리즘

## 1. 주요 알고리즘

### FIFO (First In First Out)
- 가장 먼저 들어온 페이지를 먼저 교체
- 구현이 간단하지만 Belady's Anomaly 발생 가능
- 페이지 프레임 수가 증가해도 페이지 부재율이 증가할 수 있음

### LRU (Least Recently Used)
- 가장 오랫동안 사용되지 않은 페이지를 교체
- 최근 사용 시간을 추적해야 함
- 성능은 좋으나 오버헤드가 큼

### LFU (Least Frequently Used)
- 참조 횟수가 가장 적은 페이지를 교체
- 참조 횟수를 계속 카운트해야 함

### Optimal (OPT)
- 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체
- 이론상 최적이나 미래 예측이 불가능하여 실제 구현 불가
- 다른 알고리즘의 성능 비교 기준으로 사용

### Clock (Second Chance)
- FIFO + 참조 비트 사용
- 원형 큐 구조, 참조 비트가 1이면 0으로 바꾸고 기회 부여
- LRU의 근사 알고리즘

## 2. 용어 정리

- **페이지 부재(Page Fault)**: 참조하려는 페이지가 메모리에 없는 경우
- **페이지 프레임**: 물리 메모리를 고정 크기로 나눈 단위
- **작업 집합(Working Set)**: 프로세스가 일정 시간 동안 참조하는 페이지 집합
- **스래싱(Thrashing)**: 페이지 부재가 과도하게 발생하여 CPU 이용률이 급격히 떨어지는 현상

---

### 예상 문제

### 문제 1
다음 페이지 참조열에서 FIFO 알고리즘을 사용할 때, 페이지 프레임이 3개일 경우 페이지 부재 발생 횟수는?

**참조열: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5**


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 9회
> 
> **과정:**
> - 1: [1] - 부재
> - 2: [1,2] - 부재
> - 3: [1,2,3] - 부재
> - 4: [4,2,3] - 부재 (1 교체)
> - 1: [4,1,3] - 부재 (2 교체)
> - 2: [4,1,2] - 부재 (3 교체)
> - 5: [5,1,2] - 부재 (4 교체)
> - 1: [5,1,2] - 적중
> - 2: [5,1,2] - 적중
> - 3: [5,3,2] - 부재 (1 교체)
> - 4: [5,3,4] - 부재 (2 교체)
> - 5: [5,3,4] - 적중

</div>
</details>
<br/><br/>


### 문제 2
페이지 프레임 수를 늘렸는데 오히려 페이지 부재율이 증가하는 현상을 무엇이라 하는가?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Belady's Anomaly (벨레이디의 모순)
> 
> FIFO 알고리즘에서 발생 가능

</div>
</details>
<br/><br/>


### 문제 3
다음 페이지 참조열에서 LRU 알고리즘을 사용할 때, 페이지 프레임이 3개일 경우 페이지 부재 발생 횟수는?

**참조열: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3**


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 6회
> 
> **과정:**
> - 7: [7] - 부재
> - 0: [7,0] - 부재
> - 1: [7,0,1] - 부재
> - 2: [2,0,1] - 부재 (7 교체, 가장 오래전 사용)
> - 0: [2,0,1] - 적중
> - 3: [2,0,3] - 부재 (1 교체)
> - 0: [2,0,3] - 적중
> - 4: [4,0,3] - 부재 (2 교체)
> - 2: [4,0,2] - 부재 (3 교체)
> - 3: [4,3,2] - 부재 (0 교체)

</div>
</details>
<br/><br/>


### 문제 4
이론상 최적의 성능을 보이지만 미래의 페이지 참조를 알 수 없어 실제 구현이 불가능한 페이지 교체 알고리즘은?


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Optimal (OPT) 또는 MIN 알고리즘
> 
> 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체

</div>
</details>
<br/><br/>


### 문제 5
페이지 부재가 과도하게 발생하여 CPU 이용률이 급격히 떨어지고, 대부분의 시간을 페이지 교체에 소비하는 현상은?


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Thrashing (스래싱)
> 
> **발생 원인:** 다중 프로그래밍 정도가 높아 각 프로세스에 할당된 프레임 수가 작업 집합 크기보다 작을 때

</div>
</details>
<br/><br/>


### 문제 6
다음 중 LRU 알고리즘의 근사 알고리즘으로, 참조 비트를 사용하여 FIFO의 단점을 보완한 알고리즘은?


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Clock 알고리즘 (Second Chance 알고리즘)
> 
> 원형 큐 구조로 포인터가 회전하며, 참조 비트가 1인 페이지는 0으로 바꾸고 한 번의 기회를 더 줌

</div>
</details>
<br/><br/>


### 문제 7
다음 페이지 참조열에서 페이지 프레임이 4개일 때, FIFO와 LRU 중 어느 알고리즘의 페이지 부재 횟수가 더 적은가?

**참조열: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5**


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> LRU
> 
> **FIFO:** 10회
> **LRU:** 10회
> 
> 이 경우 동일하지만, 일반적으로 LRU가 더 나은 성능을 보임

</div>
</details>
<br/><br/>


### 문제 8
프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합을 무엇이라 하는가?


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Working Set (작업 집합)
> 
> 지역성(Locality) 원리에 기반하며, 이를 메모리에 유지해야 스래싱을 방지할 수 있음

</div>
</details>
<br/>
