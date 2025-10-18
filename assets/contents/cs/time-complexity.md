
# 시간복잡도 기초

## 📌 Big-O 표기법

**알고리즘의 수행 시간을 입력 크기 N에 대한 함수로 표현**

### 주요 시간복잡도

```
O(1) < O(log N) < O(N) < O(N log N) < O(N²) < O(2ᴺ) < O(N!)

빠름 ←──────────────────────────────────────→ 느림
```

### 시간복잡도별 성능

```
N = 1,000,000 기준:

O(1):        1번 연산           ✅ 최고
O(log N):    약 20번            ✅ 매우 빠름
O(N):        1,000,000번        ✅ 빠름
O(N log N):  약 20,000,000번    ✅ 준수
O(N²):       1,000,000,000,000번 ❌ 느림
O(2ᴺ):       ...                ❌ 불가능
```

### 예시 코드

```c
// O(1) - 상수 시간
int getFirst(int arr[]) {
    return arr[0];  // 항상 1번
}

// O(N) - 선형 시간
int sum(int arr[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {  // n번 반복
        total += arr[i];
    }
    return total;
}

// O(N²) - 제곱 시간
void printPairs(int arr[], int n) {
    for (int i = 0; i < n; i++) {        // n번
        for (int j = 0; j < n; j++) {    // n번
            printf("%d, %d\n", arr[i], arr[j]);
        }
    }
}

// O(log N) - 로그 시간
int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == key) return mid;
        if (arr[mid] < key) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

