# 프린터 [python]

## 📊 결과

- **소요 시간**: 30분
- **실행 결과**: 전체 통과 ✅
- **성능**: 0.01~1.02ms, 9.13~9.35MB
- **문제**: [프로그래머스 - 프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587)

## 💻 내 코드

```python
from collections import deque

def getMax(q):
    cur_max=0
    for i in range(len(q)):
        cur_max = max(cur_max, q[i])
    return cur_max

def solution(priorities, location):
    q = deque(priorities)
    length = len(priorities)
    visited = [False] * length
    cur_max=getMax(q)
    order=0
    i=0
    while len(q)>0:
        i%=length
        if visited[i]:
            i+=1
            continue
        if priorities[i] >= cur_max:
            q.popleft()
            visited[i]=True
            cur_max=getMax(q)
            order+=1
            if i==location:
                return order
        else :
            q.append(q.popleft())
        i+=1
    
    answer = 0
    return answer
```

## 📝 평가

### ✔ 잘한 점

1. **deque 사용**: 큐 자료구조를 올바르게 선택해 문제를 해결했다
2. **최댓값 추적**: `cur_max`를 유지하며 우선순위 비교를 수행했다
3. **위치 추적**: `location` 문서가 언제 출력되는지 정확히 추적했다

### ✦ 개선점

1. **불필요한 복잡도**: `visited` 배열과 인덱스 관리(`i`, `i%=length`)가 불필요하다. 큐에 인덱스를 함께 저장하면 훨씬 간단하다
2. **매번 최댓값 계산**: `getMax(q)`를 매번 호출하면 O(n)이 반복되어 전체 시간복잡도가 O(n²)이 된다
3. **getMax 함수**: `max(q)`를 직접 사용하거나 힙을 쓰면 더 효율적이다
4. **불필요한 변수**: `answer = 0`은 사용되지 않는다

## ✨ 최적화된 풀이

### 풀이 1: 큐 + 인덱스 튜플
```python
from collections import deque

def solution(priorities, location):
    # (우선순위, 인덱스) 튜플로 저장
    queue = deque((p, i) for i, p in enumerate(priorities))
    order = 0
    
    while queue:
        current = queue.popleft()
        
        # 현재보다 높은 우선순위가 있으면 뒤로 보냄
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            # 출력
            order += 1
            if current[1] == location:
                return order
    
    return order
```

### 풀이 2: 우선순위 큐 활용
```python
from collections import deque

def solution(priorities, location):
    queue = deque((p, i) for i, p in enumerate(priorities))
    order = 0
    
    while queue:
        current = queue.popleft()
        
        # 최댓값과 비교 (O(n)이지만 간결함)
        if current[0] < max(queue)[0] if queue else 0:
            queue.append(current)
        else:
            order += 1
            if current[1] == location:
                return order
    
    return order
```

### 풀이 3: 정렬 활용
```python
def solution(priorities, location):
    queue = [(p, i) for i, p in enumerate(priorities)]
    # 우선순위 내림차순 정렬
    sorted_priorities = sorted(priorities, reverse=True)
    
    order = 0
    idx = 0
    
    while queue:
        current = queue.pop(0)
        
        # 현재 출력해야 할 우선순위와 비교
        if current[0] == sorted_priorities[idx]:
            order += 1
            idx += 1
            if current[1] == location:
                return order
        else:
            queue.append(current)
    
    return order
```

**성능 비교:**

| 풀이 | 시간복잡도 | 공간복잡도 | 코드 라인 |
|------|-----------|-----------|----------|
| 원본 | O(n²) | O(n) | 25줄 |
| 최적화 1 | O(n²) | O(n) | 13줄 |
| 최적화 2 | O(n²) | O(n) | 13줄 |
| 최적화 3 | O(n log n + n²) | O(n) | 17줄 |

## 💡 핵심 인사이트

1. **큐에 정보 함께 저장**: 원본 데이터를 유지하면서 인덱스도 추적해야 할 때는 튜플로 묶어서 저장한다
   ```python
   queue = deque((value, index) for index, value in enumerate(arr))
   ```

2. **any() 함수 활용**: 조건을 만족하는 요소가 하나라도 있는지 확인할 때 유용하다
   ```python
   if any(current[0] < q[0] for q in queue):
       # 더 높은 우선순위가 존재함
   ```

3. **enumerate 패턴**: 값과 인덱스를 동시에 다룰 때 필수적이다
   ```python
   for i, p in enumerate(priorities):
       queue.append((p, i))
   ```

4. **큐 vs 리스트**: 이 문제는 `pop(0)`을 사용해도 성능 차이가 크지 않지만, 큰 데이터에서는 `deque.popleft()`가 O(1)로 훨씬 빠르다

## 📚 관련 개념

**우선순위 큐 구현 방법**

```python
# 1. 리스트로 매번 최댓값 찾기 (O(n))
max_value = max(queue)

# 2. heapq 사용 (O(log n))
import heapq
heap = []
heapq.heappush(heap, -priority)  # 최대힙은 음수로
heapq.heappop(heap)

# 3. PriorityQueue (멀티스레드 환경)
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((-priority, index))
pq.get()
```

**deque 주요 메서드**

```python
from collections import deque

q = deque([1, 2, 3])

# 추가
q.append(4)         # 오른쪽: [1, 2, 3, 4]
q.appendleft(0)     # 왼쪽: [0, 1, 2, 3, 4]

# 제거
q.pop()             # 오른쪽에서 제거: 4
q.popleft()         # 왼쪽에서 제거: 0

# 회전
q.rotate(1)         # 오른쪽으로 1칸: [3, 1, 2]
q.rotate(-1)        # 왼쪽으로 1칸: [1, 2, 3]
```

## 🎓 유사 문제

**프로그래머스**
- [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) - 큐 기본
- [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583) - 시뮬레이션 큐
- [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584) - 스택/큐

**LeetCode**
- [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) - 큐 설계
- [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) - 슬라이딩 윈도우

**백준**
- [1966. 프린터 큐](https://www.acmicpc.net/problem/1966) - 동일 문제
- [2164. 카드2](https://www.acmicpc.net/problem/2164) - 큐 시뮬레이션
- [18258. 큐 2](https://www.acmicpc.net/problem/18258) - 큐 구현

**연습 포인트 체크리스트:**
- [ ] 큐에 튜플로 여러 정보 저장
- [ ] any(), all() 함수 활용
- [ ] enumerate로 인덱스-값 동시 처리
- [ ] deque vs list 성능 차이 이해
- [ ] 우선순위 큐 구현 방법

## 🏷️ Keywords

`#프로그래머스` `#프린터` `#큐` `#스택/큐` `#우선순위큐` `#Level2` `#시뮬레이션` `#deque` `#Python`