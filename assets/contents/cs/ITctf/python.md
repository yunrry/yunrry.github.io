# Python

## 문자열(String)

```python
s = "Hello"

# 검색
s.find('e')        # 1 (없으면 -1)
s.index('e')       # 1 (없으면 에러)
s.count('l')       # 2

# 변환
s.upper()          # "HELLO"
s.lower()          # "hello"
s.replace('l','L') # "HeLLo"
s.strip()          # 공백 제거
s.split(',')       # 리스트로 분할

# 판별
s.isdigit()        # 숫자 여부
s.isalpha()        # 알파벳 여부
s.startswith('H')  # 시작 문자
s.endswith('o')    # 끝 문자
```

## 리스트(List)

```python
lst = [1, 2, 3]

# 추가
lst.append(4)      # 끝에 추가
lst.insert(1, 5)   # 인덱스 1에 추가
lst.extend([6,7])  # 리스트 합치기

# 삭제
lst.remove(2)      # 값 2 삭제
lst.pop()          # 마지막 삭제 후 반환
lst.pop(0)         # 인덱스 0 삭제 후 반환

# 정렬
lst.sort()         # 오름차순 정렬
lst.sort(reverse=True)  # 내림차순
lst.reverse()      # 역순

# 기타
lst.count(1)       # 1의 개수
lst.index(3)       # 3의 인덱스
len(lst)           # 길이
```

## 튜플(Tuple)

```python
t = (1, 2, 3)

# 불변(Immutable) - 수정 불가
t.count(1)         # 1의 개수
t.index(2)         # 2의 인덱스
```

## 딕셔너리(Dictionary)

```python
d = {'a': 1, 'b': 2}

# 접근
d['a']             # 1
d.get('a')         # 1 (없으면 None)
d.get('c', 0)      # 0 (기본값)

# 추가/수정
d['c'] = 3
d.update({'d': 4})

# 삭제
d.pop('a')         # 'a' 삭제 후 값 반환
del d['b']

# 조회
d.keys()           # 키 목록
d.values()         # 값 목록
d.items()          # (키, 값) 튜플 목록
'a' in d           # 키 존재 여부
```

## 집합(Set)

```python
s = {1, 2, 3}

# 추가/삭제
s.add(4)
s.remove(1)        # 없으면 에러
s.discard(1)       # 없어도 에러 안남
s.clear()          # 전체 삭제

# 집합 연산
s1 | s2            # 합집합
s1 & s2            # 교집합
s1 - s2            # 차집합
s1 ^ s2            # 대칭 차집합
```

## 형변환

```python
int("10")          # 10
float("3.14")      # 3.14
str(100)           # "100"
list("abc")        # ['a', 'b', 'c']
tuple([1,2])       # (1, 2)
set([1,1,2])       # {1, 2}
```

## 주요 내장 함수

```python
len(obj)           # 길이
max(lst)           # 최댓값
min(lst)           # 최솟값
sum(lst)           # 합계
sorted(lst)        # 정렬된 새 리스트
reversed(lst)      # 역순 이터레이터
enumerate(lst)     # (인덱스, 값)
zip(a, b)          # 병렬 묶기
map(func, lst)     # 함수 적용
filter(func, lst)  # 필터링
```

## 슬라이싱

```python
lst[start:end:step]
lst[1:4]           # 1~3
lst[:3]            # 0~2
lst[2:]            # 2~끝
lst[::2]           # 2칸씩
lst[::-1]          # 역순
```


## Python List 파싱 문법 정리

### 1. 기본 리스트 생성 및 접근
```python
# 리스트 생성
lst = [1, 2, 3, 4, 5]

# 인덱싱 (0부터 시작)
lst[0]      # 1
lst[-1]     # 5 (뒤에서 첫 번째)
lst[-2]     # 4 (뒤에서 두 번째)

# 슬라이싱: lst[start:end:step]
lst[1:4]    # [2, 3, 4] (1번 인덱스부터 3번 인덱스까지)
lst[:3]     # [1, 2, 3] (처음부터 2번 인덱스까지)
lst[2:]     # [3, 4, 5] (2번 인덱스부터 끝까지)
lst[::2]    # [1, 3, 5] (2칸씩 건너뛰기)
lst[::-1]   # [5, 4, 3, 2, 1] (역순)
```
```python
# 슬라이싱 심화: [start:end:step]

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# step 활용
lst[1::2]    # [1, 3, 5, 7, 9] - 1번 인덱스부터 끝까지 2칸씩
lst[::3]     # [0, 3, 6, 9] - 처음부터 끝까지 3칸씩
lst[2:8:2]   # [2, 4, 6] - 2번부터 7번까지 2칸씩

# 음수 step (역순)
lst[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - 전체 역순
lst[::-2]    # [9, 7, 5, 3, 1] - 끝부터 2칸씩 역순
lst[5:1:-1]  # [5, 4, 3, 2] - 5번부터 2번까지 역순
```

### 2. 리스트 메서드
```python
lst = [1, 2, 3]

# 추가
lst.append(4)       # [1, 2, 3, 4] - 끝에 추가
lst.insert(1, 10)   # [1, 10, 2, 3, 4] - 특정 위치에 추가
lst.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6] - 리스트 합치기

# 삭제
lst.remove(10)      # 첫 번째 10 삭제
lst.pop()           # 마지막 요소 삭제 후 반환
lst.pop(0)          # 0번 인덱스 삭제 후 반환

# 정렬
lst.sort()          # 오름차순 정렬 (원본 변경)
lst.sort(reverse=True)  # 내림차순 정렬
sorted(lst)         # 정렬된 새 리스트 반환 (원본 유지)

# 기타
lst.reverse()       # 역순으로 뒤집기
lst.count(2)        # 2의 개수
lst.index(3)        # 3의 인덱스
len(lst)            # 리스트 길이
```

### 3. 리스트 컴프리헨션
```python
# 기본 형태: [표현식 for 항목 in 반복가능객체 if 조건]

# 1~10의 제곱
[x**2 for x in range(1, 11)]

# 짝수만 필터링
[x for x in range(10) if x % 2 == 0]

# 중첩 리스트
[[i*j for j in range(1, 4)] for i in range(1, 4)]
```

---

## 정보처리기사 대비 실행 결과 문제

### 문제 1 
```python
lst = [10, 20, 30, 40, 50]
print(lst[1:4])
print(lst[-2])
print(lst[::2])
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[20, 30, 40]
40
[10, 30, 50]
```
</details>

---

### 문제 2 
```python
lst = [1, 2, 3, 4, 5]
lst.append(6)
lst.insert(2, 10)
lst.remove(4)
print(lst)
print(len(lst))
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[1, 2, 10, 3, 5, 6]
6
```

풀이:
- append(6): [1, 2, 3, 4, 5, 6]
- insert(2, 10): [1, 2, 10, 3, 4, 5, 6]
- remove(4): [1, 2, 10, 3, 5, 6]
</details>

---

### 문제 3 
```python
lst = [5, 2, 8, 1, 9]
lst.sort()
print(lst[2])
lst.reverse()
print(lst[-1])
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
5
1
```

풀이:
- sort(): [1, 2, 5, 8, 9]
- lst[2]: 5
- reverse(): [9, 8, 5, 2, 1]
- lst[-1]: 1
</details>

---

### 문제 4 
```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x for x in lst if x % 3 == 0]
print(result)
print(sum(result))
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />
</form>

<details>
<summary>정답 보기</summary>

```
[3, 6, 9]
18
```
</details>

---

### 문제 5 
```python
lst = [10, 20, 30, 40, 50]
a = lst.pop()
b = lst.pop(1)
print(a + b)
print(lst)
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
70
[10, 30, 40]
```

풀이:
- pop(): 50 제거 → a = 50, lst = [10, 20, 30, 40]
- pop(1): 20 제거 → b = 20, lst = [10, 30, 40]
- a + b = 70
</details>

---

### 문제 6 
```python
lst = [1, 2, 3, 4, 5]
result = [x*2 for x in lst if x > 2]
print(result)
print(lst[::-1][1:4])
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[6, 8, 10]
[4, 3, 2]
```

풀이:
- x > 2인 요소는 3, 4, 5
- 각각 2배: [6, 8, 10]
- lst[::-1] = [5, 4, 3, 2, 1]
- [1:4] = [4, 3, 2]
</details>

---

### 문제 7 
```python
lst = [[1, 2], [3, 4], [5, 6]]
print(lst[1][1])
print([item[0] for item in lst])
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
4
[1, 3, 5]
```

풀이:
- lst[1][1]: lst[1] = [3, 4], [3, 4][1] = 4
- 각 서브리스트의 첫 번째 요소: [1, 3, 5]
</details>

---

### 문제 8 
```python
lst1 = [1, 2, 3]
lst2 = lst1
lst3 = lst1[:]
lst1[0] = 100
print(lst2)
print(lst3)
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[100, 2, 3]
[1, 2, 3]
```

풀이:
- lst2 = lst1: 얕은 복사(참조 공유) → lst1과 같은 객체
- lst3 = lst1[:]: 깊은 복사(새로운 객체) → 독립적
- lst1[0] = 100 변경시 lst2도 함께 변경, lst3는 독립적
</details>

---


```python
# 슬라이싱 심화: [start:end:step]

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# step 활용
lst[1::2]    # [1, 3, 5, 7, 9] - 1번 인덱스부터 끝까지 2칸씩
lst[::3]     # [0, 3, 6, 9] - 처음부터 끝까지 3칸씩
lst[2:8:2]   # [2, 4, 6] - 2번부터 7번까지 2칸씩

# 음수 step (역순)
lst[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - 전체 역순
lst[::-2]    # [9, 7, 5, 3, 1] - 끝부터 2칸씩 역순
lst[5:1:-1]  # [5, 4, 3, 2] - 5번부터 2번까지 역순
```


#### 문제 9
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lst[1::2])
print(lst[::3])
print(lst[::-2])
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[1, 3, 5, 7]
[0, 3, 6]
[8, 6, 4, 2, 0]
```
</details>

#### 문제 10
```python
lst = [10, 20, 30, 40, 50, 60]
print(lst[1:5:2])
print(lst[4:0:-1])
print(len(lst[::2]))
```
<form class="inline-answer">
  <input type="text" placeholder="출력결과" />

</form>

<details>
<summary>정답 보기</summary>

```
[20, 40]
[50, 40, 30, 20]
3
```

풀이:
- [1:5:2]: 인덱스 1, 3 → [20, 40]
- [4:0:-1]: 인덱스 4, 3, 2, 1 → [50, 40, 30, 20]
- [::2]: [10, 30, 50] → 길이 3
</details>