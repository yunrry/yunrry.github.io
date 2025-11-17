
# 이진 탐색 (Binary Search)

## 📌 개념

**정렬된 배열에서 중간값과 비교하여 절반씩 범위를 줄여가며 탐색**

- 전제조건: **반드시 정렬된 배열**

### 💡 동작 원리

```
배열: [1, 3, 5, 7, 9, 11, 13, 15]
찾는 값: 7

1단계: 전체 범위
[1, 3, 5, 7, 9, 11, 13, 15]
         ↑ mid=9
7 < 9 → 왼쪽 절반 탐색

2단계: 왼쪽 절반
[1, 3, 5, 7]
      ↑ mid=5
7 > 5 → 오른쪽 절반 탐색

3단계: 좁혀진 범위
[7]
 ↑ mid=7
7 == 7 → 찾음! ✔

비교 횟수: 3번 (선형 탐색은 4번)
```

### 💻 구현 코드 (반복문)

```c
int binarySearch(int arr[], int n, int key) {
    int left = 0;
    int right = n - 1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        
        if (arr[mid] == key) {
            return mid;  // 찾음
        }
        
        if (arr[mid] < key) {
            left = mid + 1;  // 오른쪽 절반
        } else {
            right = mid - 1;  // 왼쪽 절반
        }
    }
    
    return -1;  // 못 찾음
}
```

### 💻 구현 코드 (재귀)

```c
int binarySearchRecursive(int arr[], int left, int right, int key) {
    if (left > right) {
        return -1;  // 못 찾음
    }
    
    int mid = (left + right) / 2;
    
    if (arr[mid] == key) {
        return mid;  // 찾음
    }
    
    if (arr[mid] < key) {
        // 오른쪽 절반 재귀
        return binarySearchRecursive(arr, mid + 1, right, key);
    } else {
        // 왼쪽 절반 재귀
        return binarySearchRecursive(arr, left, mid - 1, key);
    }
}

// 호출
int result = binarySearchRecursive(arr, 0, n - 1, key);
```

### 상세 동작 예시

```c
arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
key = 13

1단계:
left=0, right=9, mid=4
arr[4]=9
13 > 9 → left = mid + 1 = 5

2단계:
left=5, right=9, mid=7
arr[7]=15
13 < 15 → right = mid - 1 = 6

3단계:
left=5, right=6, mid=5
arr[5]=11
13 > 11 → left = mid + 1 = 6

4단계:
left=6, right=6, mid=6
arr[6]=13
13 == 13 → 찾음! ✔

비교 횟수: 4번
```

### 📊 시간복잡도

```
최선: O(1)      - 첫 비교에서 찾음
평균: O(log N)  - 절반씩 줄어듦
최악: O(log N)  - 끝까지 찾음

공간복잡도:
- 반복문: O(1)
- 재귀: O(log N) (스택)

비교: 선형 탐색 O(N)
```

### 성능 비교

```
배열 크기 | 선형 탐색 | 이진 탐색
----------|----------|----------
10        | 최대 10번 | 최대 4번
100       | 최대 100번 | 최대 7번
1,000     | 최대 1,000번 | 최대 10번
1,000,000 | 최대 1,000,000번 | 최대 20번 ✔

1,000,000개 중에서 20번 비교로 찾음!
```

### 로그 계산

```
N개 원소에서 이진 탐색:
- 1회: N개
- 2회: N/2개
- 3회: N/4개
- k회: N/2^k개

N/2^k = 1
→ 2^k = N
→ k = log₂N

예: N = 1,024
log₂(1024) = 10
최대 10번 비교
```

---

## 🎯 이진 탐색 응용

### 1. 하한 (Lower Bound)

**key 이상인 첫 번째 원소의 인덱스**

```c
// key 이상인 첫 위치
int lowerBound(int arr[], int n, int key) {
    int left = 0;
    int right = n;
    
    while (left < right) {
        int mid = (left + right) / 2;
        
        if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid;  // 같아도 왼쪽 탐색
        }
    }
    
    return left;
}
```

**예시:**

```
arr[] = {1, 3, 3, 3, 5, 7, 9}
key = 3

결과: 인덱스 1 (첫 번째 3의 위치)
```

### 2. 상한 (Upper Bound)

**key 초과인 첫 번째 원소의 인덱스**

```c
// key 초과인 첫 위치
int upperBound(int arr[], int n, int key) {
    int left = 0;
    int right = n;
    
    while (left < right) {
        int mid = (left + right) / 2;
        
        if (arr[mid] <= key) {  // 같아도 오른쪽
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

**예시:**

```
arr[] = {1, 3, 3, 3, 5, 7, 9}
key = 3

결과: 인덱스 4 (3 다음 위치, 5의 인덱스)
```

### 3. 중복 원소 개수

```c
// key의 개수 세기
int countOccurrences(int arr[], int n, int key) {
    int lower = lowerBound(arr, n, key);
    int upper = upperBound(arr, n, key);
    
    return upper - lower;
}
```

**예시:**

```
arr[] = {1, 3, 3, 3, 5, 7, 9}
key = 3

lower = 1
upper = 4
개수 = 4 - 1 = 3개 ✔
```

---

## ⚠️ 주의사항

### 1. 오버플로우 방지

```c
// ✘ 오버플로우 가능
int mid = (left + right) / 2;

// ✔ 안전한 방법
int mid = left + (right - left) / 2;

예:
left = 2,000,000,000
right = 2,000,000,000

(left + right) = 4,000,000,000
→ int 범위 초과! (약 21억)

left + (right - left) / 2
= 2,000,000,000 + 0
= 2,000,000,000 ✔
```

### 2. 정렬 필수

```c
int arr[] = {5, 2, 8, 1, 9};  // 정렬 안 됨 ✘

// 반드시 정렬 후 사용
qsort(arr, n, sizeof(int), compare);

// 그 후 이진 탐색
int result = binarySearch(arr, n, key);
```

### 3. 경계 조건

```c
// 빈 배열
int arr[] = {};
int result = binarySearch(arr, 0, key);
// → -1 반환 (올바름)

// 단일 원소
int arr[] = {5};
int result = binarySearch(arr, 1, 5);
// → 0 반환 (올바름)
```

---
