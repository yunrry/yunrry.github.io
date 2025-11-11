# Python 필수 문법

### 1. 자료구조 기본
```python
# 리스트
arr = [1, 2, 3]
arr.append(4)
arr.pop()
arr.insert(0, 0)
arr.remove(2)
arr.sort() / arr.sort(reverse=True)
sorted(arr)

# 2차원 리스트
matrix = [[0] * m for _ in range(n)]  # ⭐

# 딕셔너리
dic = {}
dic['key'] = 'value'
dic.get('key', default_value)
if 'key' in dic:
    pass

# 집합
s = set()
s.add(1)
s.remove(1)
s1 & s2  # 교집합
s1 | s2  # 합집합
s1 - s2  # 차집합

# 큐
from collections import deque
q = deque()
q.append(1)
q.popleft()
q.appendleft(0)

# 힙
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappop(heap)
# 최대힙: -값으로 저장
```

### 2. 문자열
```python
# 기본
s = "hello"
s.upper() / s.lower()
s.split()
s.split(',')
''.join(['a', 'b', 'c'])
s.replace('old', 'new')
s.strip()

# 검사
s.isdigit()
s.isalpha()
s.isalnum()

# 슬라이싱
s[1:4]
s[::-1]  # 역순
```

### 3. 정렬
```python
# 리스트 정렬
arr.sort()
sorted(arr)

# 커스텀 정렬
arr.sort(key=lambda x: x[0])  # 첫 번째 요소 기준
arr.sort(key=lambda x: (x[0], -x[1]))  # 첫 번째 오름차순, 두 번째 내림차순

# 딕셔너리 정렬
sorted(dic.items(), key=lambda x: x[1])
```

### 4. 순회/반복
```python
# enumerate
for i, val in enumerate(arr):
    print(i, val)

# zip
for a, b in zip(arr1, arr2):
    print(a, b)

# range
for i in range(n):
    pass
for i in range(start, end, step):
    pass

# 리스트 컴프리헨션
result = [x*2 for x in arr if x > 0]
matrix = [[0]*m for _ in range(n)]
```

### 5. 수학/비트
```python
# 수학
abs(-5)
max(a, b, c)
min(a, b, c)
sum(arr)
pow(2, 3) or 2**3

import math
math.sqrt(16)
math.ceil(3.2)
math.floor(3.8)
math.gcd(12, 8)

# 비트 연산
a & b  # AND
a | b  # OR
a ^ b  # XOR
~a     # NOT
a << 1 # 왼쪽 시프트
a >> 1 # 오른쪽 시프트


## 증감 연산자: 파이썬에는 별도의 증감 연산자(++, --)가 없다.
##대신 사용하는 연산자: 변수에 값을 더하거나 빼는 연산은 복합 할당 연산자를 사용.
x += 1 # +=: 덧셈 할당 (예: x += 1은 x = x + 1과 같음)
x -= 1 # -=: 뺄셈 할당 (예: x -= 1은 x = x - 1과 같음) 

# a=3 b=2
a // b # 몫 = 1
a / b # (float) = 1.5
a % b # 나머지 = 1
```

### 6. 기타 유용한 것들
```python
# any, all
any([True, False, False])  # True
all([True, True, False])   # False

# map, filter
list(map(int, input().split()))
list(filter(lambda x: x > 0, arr))

# Counter
from collections import Counter
counter = Counter([1, 1, 2, 3, 3, 3])
counter.most_common(2)  # [(3, 3), (1, 2)]

# defaultdict
from collections import defaultdict
dic = defaultdict(int)
dic = defaultdict(list)
```

---

## 🎯 추천 문제 리스트 (난이도별)

### Level 1: 기초 구현 (10문제)
1. [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644)
2. [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)
3. [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
4. [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)
5. [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)
6. [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915)
7. [3진법 뒤집기](https://school.programmers.co.kr/learn/courses/30/lessons/68935)
8. [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301)
9. [신규 아이디 추천](https://school.programmers.co.kr/learn/courses/30/lessons/72410)
10. [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)

### Level 2: 핵심 자료구조 (15문제)
**스택/큐**
1. [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) ⭐ | <a href="#" data-content="/assets/contents/algorithm/programmers/42586.md">풀이</a>
2. [프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587)
3. [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583)
4. [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)

**해시**
5. [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) ⭐
6. [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)
7. [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

**정렬**
8. [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) ⭐
9. [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

**구현**
10. [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)
11. [괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058)
12. [문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) ⭐
13. [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)
14. [방문 길이](https://school.programmers.co.kr/learn/courses/30/lessons/49994)
15. [수식 최대화](https://school.programmers.co.kr/learn/courses/30/lessons/67257)

### Level 2: BFS/DFS 기초 (8문제)
1. [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)
2. [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) ⭐
3. [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)
4. [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)
5. [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)
6. [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302)
7. [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993)
8. [두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

### Level 2: 심화 구현 (7문제)
1. [n^2 배열 자르기](https://school.programmers.co.kr/learn/courses/30/lessons/87390)
2. [예상 대진표](https://school.programmers.co.kr/learn/courses/30/lessons/12985)
3. [멀쩡한 사각형](https://school.programmers.co.kr/learn/courses/30/lessons/62048)
4. [압축](https://school.programmers.co.kr/learn/courses/30/lessons/17684)
5. [파일명 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/17686)
6. [후보키](https://school.programmers.co.kr/learn/courses/30/lessons/42890)
7. [삼각 달팽이](https://school.programmers.co.kr/learn/courses/30/lessons/68645)

### Level 3: 필수 문제 (10문제)
1. [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)
2. [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)
3. [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) ⭐
4. [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)
5. [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) ⭐
6. [징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236)
7. [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)
8. [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)
9. [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)
10. [디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627)

---

## 코딩테스트 팁!

```python
# 입력 받기 템플릿
# 프로그래머스
def solution(param1, param2):
    answer = 0
    return answer

# 백준
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
```

**시간복잡도 기준**
- n ≤ 100: O(n³) 가능
- n ≤ 1,000: O(n²) 가능
- n ≤ 10,000: O(n log n) 필요
- n ≤ 100,000: O(n) 또는 O(n log n)
- n ≤ 1,000,000: O(n) 또는 O(log n)

**디버깅 팁**
```python
# 중간 결과 확인
print(f"idx={idx}, value={value}")

# 리스트 상태 확인
print(arr)

# 반복문 횟수 제한 (무한루프 방지)
MAX_ITER = 10000
for i in range(MAX_ITER):
    if 종료조건:
        break
```

