# 프로그래머스 - 기능개발 [Python]

## 📊 결과

- **소요 시간**: 30분
- **실행 결과**: 전체 통과 ✅
- **성능**: 0.01~0.09ms, 9.05~9.34MB
- **문제**: [프로그래머스 - 기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)

## 💻 내 코드

```python
def solution(progresses, speeds):
    n = len(progresses);
    answer = []
    times = []
    for i in range(n):
        times.append(int(100-progresses[i])//speeds[i])
        rem = (100-progresses[i])%speeds[i]
        if rem!=0:
            times[i] += 1          
    
    cur=times[0]
    count=0;
    for i in range(n):
        if times[i]<=cur:
            count+=1
        else :
            answer.append(count)
            cur = times[i]
            count=1
        if i == n-1:
            answer.append(count)  
    
    return answer
```

## 📝 평가

### ✔ 잘한 점

1. **핵심 로직 정확**: 각 작업의 완료 소요일을 먼저 계산한 후, 앞선 작업을 기준으로 그룹화하는 접근이 올바름
2. **올림 처리**: 나머지가 있을 때 `+1`로 일수를 올림 처리해 정확한 완료일 계산
3. **배포 그룹화**: 현재 기준일(`cur`)보다 작거나 같으면 같은 배포에 포함시키는 로직이 정확함

### ✦ 개선점

1. **불필요한 세미콜론**: Python에서는 세미콜론이 불필요함 (`n = len(progresses);`)
2. **마지막 처리 로직**: 루프 내에서 `i == n-1` 체크보다 루프 종료 후 처리가 더 명확함
3. **수식 간소화**: `math.ceil()` 또는 `(a + b - 1) // b` 패턴으로 올림을 더 간결하게 표현 가능
4. **변수명**: `times` 대신 `days`가 더 의미를 명확히 전달함

## ✨ 최적화된 풀이

```python
import math

def solution(progresses, speeds):
    # 각 작업의 완료 소요일 계산
    days = [math.ceil((100 - p) / s) for p in zip(progresses, speeds)]
    
    answer = []
    current_max = days[0]
    count = 0
    
    for day in days:
        if day <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = day
            count = 1
    
    # 마지막 그룹 추가
    answer.append(count)
    
    return answer
```

**또 다른 풀이 (math 없이):**

```python
def solution(progresses, speeds):
    # 올림: (a + b - 1) // b
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    
    answer = []
    current_max = days[0]
    count = 0
    
    for day in days:
        if day <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = day
            count = 1
    
    answer.append(count)
    return answer
```

**성능 비교:**
- 시간복잡도: O(n) → O(n) (동일)
- 공간복잡도: O(n) → O(n) (동일)
- 코드 라인 수: 17줄 → 12줄
- 가독성: 리스트 컴프리헨션과 zip으로 더 간결함

## 💡 핵심 인사이트

1. **큐 문제의 핵심**: 먼저 들어온 작업이 완료되어야 뒤 작업도 배포 가능 → FIFO 특성
2. **그룹화 패턴**: 현재 최댓값을 기준으로 이하인 값들을 묶는 패턴은 자주 등장함
3. **올림 계산 방법**:
   ```python
   # 방법 1: math.ceil
   math.ceil(a / b)
   
   # 방법 2: 나머지 체크
   result = a // b
   if a % b != 0:
       result += 1
   
   # 방법 3: 수학 공식
   (a + b - 1) // b
   ```
4. **마지막 그룹 처리**: 루프 안에서 인덱스 체크보다 루프 후 추가가 더 깔끔함

## 📚 관련 개념

**큐(Queue)**
```python
from collections import deque

# 큐 기본 연산
q = deque([1, 2, 3])
q.append(4)      # enqueue
q.popleft()      # dequeue
q[0]             # front (peek)
len(q)           # size
```

**그룹화 패턴**
```python
# 연속된 값 그룹화
arr = [1, 1, 2, 2, 2, 3]
groups = []
current = arr[0]
count = 0

for val in arr:
    if val == current:
        count += 1
    else:
        groups.append((current, count))
        current = val
        count = 1
groups.append((current, count))
# [(1, 2), (2, 3), (3, 1)]
```

## 🎓 유사 문제

**프로그래머스**
- [프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587) - 우선순위 큐
- [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583) - 시뮬레이션 + 큐
- [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584) - 스택/큐 응용

**LeetCode**
- [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) - 큐 기본
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) - 우선순위 큐

**백준**
- [1966. 프린터 큐](https://www.acmicpc.net/problem/1966) - 큐 + 우선순위
- [2164. 카드2](https://www.acmicpc.net/problem/2164) - 큐 기본

**연습 포인트 체크리스트:**
- [ ] 큐를 사용한 FIFO 처리
- [ ] 그룹화 패턴 (현재 기준값 유지)
- [ ] 올림 계산 3가지 방법
- [ ] 마지막 그룹 처리 방법
- [ ] 리스트 컴프리헨션 + zip 활용

## 🏷️ Keywords

`#프로그래머스` `#기능개발` `#큐` `#스택/큐` `#그룹화` `#Level2` `#시뮬레이션` `#Python`