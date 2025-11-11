# zip() 메소드

## 기본 개념

`zip()`은 여러 개의 iterable 객체를 받아서 각 객체의 같은 인덱스 요소들을 튜플로 묶어주는 함수다.

## 기본 사용법

```python
# 두 리스트 묶기
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

result = zip(names, ages)
print(list(result))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

## 다양한 활용

### 1. 여러 리스트 동시 순회
```python
progresses = [93, 30, 55]
speeds = [1, 30, 5]

for p, s in zip(progresses, speeds):
    print(f"진행도: {p}, 속도: {s}")
# 진행도: 93, 속도: 1
# 진행도: 30, 속도: 30
# 진행도: 55, 속도: 5
```

### 2. 리스트 컴프리헨션과 함께
```python
progresses = [93, 30, 55]
speeds = [1, 30, 5]

# 각 작업의 남은 진행도 계산
remaining = [100 - p for p, s in zip(progresses, speeds)]
print(remaining)  # [7, 70, 45]
```

### 3. 딕셔너리 생성
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

dic = dict(zip(keys, values))
print(dic)  # {'a': 1, 'b': 2, 'c': 3}
```

### 4. 리스트 언패킹 (unzip)
```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

## 중요 특징

### 1. 길이가 다른 경우
```python
# 짧은 쪽 기준으로 묶임
a = [1, 2, 3]
b = ['a', 'b']

print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]
```

### 2. zip_longest (itertools)
```python
from itertools import zip_longest

a = [1, 2, 3]
b = ['a', 'b']

# 긴 쪽 기준, 빈 곳은 None
print(list(zip_longest(a, b)))
# [(1, 'a'), (2, 'b'), (3, None)]

# fillvalue 지정
print(list(zip_longest(a, b, fillvalue=0)))
# [(1, 'a'), (2, 'b'), (3, 0)]
```

### 3. 반환 타입
```python
result = zip([1, 2], ['a', 'b'])
print(type(result))  # <class 'zip'>

# 사용하려면 list(), tuple() 등으로 변환
print(list(result))  # [(1, 'a'), (2, 'b')]
```

## 실전 예제

### 행렬 전치
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print(transposed)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# 리스트로 변환
transposed = [list(row) for row in zip(*matrix)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### 두 리스트 비교
```python
list1 = [1, 2, 3, 4]
list2 = [1, 2, 4, 4]

# 같은 위치의 값이 다른 인덱스 찾기
diff_idx = [i for i, (a, b) in enumerate(zip(list1, list2)) if a != b]
print(diff_idx)  # [2]
```

### 여러 리스트 합치기
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

# 각 인덱스별 합
sums = [sum(values) for values in zip(a, b, c)]
print(sums)  # [12, 15, 18]
```

## 성능 고려사항

```python
# zip()은 이터레이터를 반환 (메모리 효율적)
result = zip(range(1000000), range(1000000))  # 빠름

# list로 변환하면 메모리 사용
result_list = list(zip(range(1000000), range(1000000)))  # 느림

# 대용량 데이터는 필요할 때만 순회
for a, b in zip(big_list1, big_list2):
    # 메모리 효율적
    process(a, b)
```

## 자주 하는 실수

```python
# ❌ 잘못된 사용
progresses = [93, 30, 55]
speeds = [1, 30, 5]

# zip()만 호출하면 zip 객체만 반환됨
result = zip(progresses, speeds)
print(result)  # <zip object at 0x...>

# ✅ 올바른 사용
result = list(zip(progresses, speeds))
print(result)  # [(93, 1), (30, 30), (55, 5)]

# 또는 직접 순회
for p, s in zip(progresses, speeds):
    print(p, s)
```

## 요약

- **목적**: 여러 iterable을 동시에 순회
- **반환**: zip 객체 (이터레이터)
- **길이**: 가장 짧은 iterable 기준
- **언패킹**: `zip(*pairs)`로 역변환 가능
- **활용**: 병렬 순회, 딕셔너리 생성, 행렬 전치 등