
# LeetCode 862. Shortest Subarray with Sum at Least K

## 📋 문제 이해

**목표**: 합이 k 이상인 **가장 짧은** 부분 배열의 길이 찾기

**핵심 난점**:
- **음수가 있음** → 일반 슬라이딩 윈도우 불가능
- 합이 커졌다가 음수 때문에 다시 작아질 수 있음

---

## 💡 핵심 아이디어

### 1. Prefix Sum 활용

```

부분 배열 [i, j]의 합 = prefixSum[j+1] - prefixSum[i]

합 >= k 조건: prefixSum[j+1] - prefixSum[i] >= k → prefixSum[i] <= prefixSum[j+1] - k

```

**문제 변환**:
> "각 j에 대해, prefixSum[i] <= prefixSum[j] - k를 만족하는
> 가장 큰 i를 찾아라"

---

### 2. 단조 증가 Deque

**왜 단조 증가?**

```

deque에 prefixSum이 증가하는 순서로 인덱스 저장

예시: prefixSum = [0, 1, -1, 2] indices = [0, 1, 2, 3]

i=2일 때 prefixSum[2]=-1 < prefixSum[1]=1 → 1을 제거!

이유: 2를 선택하면 더 짧은 부분 배열 가능 (2에서 시작 vs 1에서 시작)

````

---

## ✨ 최적 풀이

### 방법 1: Prefix Sum + 단조 Deque (추천 ⭐⭐⭐⭐⭐)

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        
        // 1. Prefix Sum 계산 (long 타입 - overflow 방지)
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        // 2. 단조 증가 Deque
        Deque<Integer> deque = new ArrayDeque<>();
        int minLength = Integer.MAX_VALUE;
        
        for (int i = 0; i <= n; i++) {
            // 3. 조건 만족하는 부분 배열 찾기
            // prefixSum[i] - prefixSum[deque.peekFirst()] >= k
            while (!deque.isEmpty() && 
                   prefixSum[i] - prefixSum[deque.peekFirst()] >= k) {
                minLength = Math.min(minLength, i - deque.pollFirst());
            }
            
            // 4. 단조 증가 유지
            // 현재 prefixSum보다 큰 값들 제거
            while (!deque.isEmpty() && 
                   prefixSum[i] <= prefixSum[deque.peekLast()]) {
                deque.pollLast();
            }
            
            deque.offerLast(i);
        }
        
        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}
````

**시간복잡도**: O(n) **공간복잡도**: O(n)

---

## 🔍 상세 동작 과정

### Example 3: `nums = [2, -1, 2], k = 3`

**Step 1: Prefix Sum 계산**

```
nums       = [2, -1,  2]
indices    = [0,  1,  2]
prefixSum  = [0,  2,  1,  3]
             ↑   ↑   ↑   ↑
          i=0  i=1 i=2 i=3
```

**Step 2: Deque로 처리**

```java
i=0: prefixSum[0]=0
  deque: [0]
  minLength: ∞

i=1: prefixSum[1]=2
  // 조건 확인: 2 - 0 = 2 < 3 → 불만족
  // 단조성 확인: 2 > 0 → OK
  deque: [0, 1]
  minLength: ∞

i=2: prefixSum[2]=1
  // 조건 확인: 1 - 0 = 1 < 3 → 불만족
  // 단조성 확인: 1 <= 2 → 1 제거!
  deque: [0]
  deque: [0, 2]
  minLength: ∞

i=3: prefixSum[3]=3
  // 조건 확인: 3 - 0 = 3 >= 3 → 만족! ✓
  minLength = min(∞, 3-0) = 3
  deque에서 0 제거
  
  // 다시 확인: deque = [2]
  // 3 - 1 = 2 < 3 → 불만족
  
  // 단조성: 3 > 1 → OK
  deque: [2, 3]
  
답: 3
```

---

### Example 상세: `nums = [84, -37, 32, 40, 95], k = 167`

**Prefix Sum**:

```
nums      = [84, -37, 32, 40, 95]
prefixSum = [0, 84, 47, 79, 119, 214]
            ↑   ↑   ↑   ↑   ↑    ↑
         i=0  i=1 i=2 i=3 i=4  i=5
```

**처리 과정**:

```java
i=0: prefixSum[0]=0
  deque: [0]

i=1: prefixSum[1]=84
  // 84 - 0 = 84 < 167
  // 84 > 0 → OK
  deque: [0, 1]

i=2: prefixSum[2]=47
  // 47 - 0 = 47 < 167
  // 47 <= 84 → 1 제거!
  deque: [0, 2]

i=3: prefixSum[3]=79
  // 79 - 0 = 79 < 167
  // 79 > 47 → OK
  deque: [0, 2, 3]

i=4: prefixSum[4]=119
  // 119 - 0 = 119 < 167
  // 119 > 79 → OK
  deque: [0, 2, 3, 4]

i=5: prefixSum[5]=214
  // 214 - 0 = 214 >= 167 ✓
  minLength = 5-0 = 5
  deque: [2, 3, 4]
  
  // 214 - 47 = 167 >= 167 ✓
  minLength = min(5, 5-2) = 3
  deque: [3, 4]
  
  // 214 - 79 = 135 < 167
  // 214 > 119 → OK
  deque: [3, 4, 5]

답: 3 (부분 배열 [32, 40, 95])
```

---

## 🎨 시각적 이해

### 왜 단조 증가 Deque?

**Case 1: prefixSum이 감소하는 경우**

```
prefixSum: [0, 5, 3, 8]
            ↑  ↑  ↑  ↑
         i=0  1  2  3

i=2일 때:
- prefixSum[2]=3 < prefixSum[1]=5
- 만약 나중에 합이 k 이상이 되면:
  - [1,?]보다 [2,?]가 항상 더 짧음!
  - 왜? 2가 1보다 오른쪽에 있으니까
- 따라서 1은 절대 답이 될 수 없음 → 제거!
```

**Case 2: 조건 만족 시 제거**

```
prefixSum: [0, 2, 5, 10]
k = 8

i=3일 때:
- 10 - 0 = 10 >= 8 ✓ → [0,3] 길이 3
- 10 - 2 = 8 >= 8 ✓ → [1,3] 길이 2
- 0 제거! (이미 사용했으니 더 이상 필요 없음)
```

---

## 📊 다른 접근법 비교

### 방법 2: Brute Force (시간 초과)

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        int minLength = Integer.MAX_VALUE;
        
        for (int i = 0; i < n; i++) {
            long sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum >= k) {
                    minLength = Math.min(minLength, j - i + 1);
                    break;
                }
            }
        }
        
        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}
```

**시간복잡도**: O(n²) **결과**: TLE (Time Limit Exceeded)

---

### 방법 3: TreeMap (느림)

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        TreeMap<Long, Integer> map = new TreeMap<>();
        int minLength = Integer.MAX_VALUE;
        
        for (int i = 0; i <= n; i++) {
            // prefixSum[i] - x >= k
            // x <= prefixSum[i] - k
            Long target = prefixSum[i] - k;
            
            // headMap: key <= target인 모든 항목
            for (Map.Entry<Long, Integer> entry : map.headMap(target, true).entrySet()) {
                minLength = Math.min(minLength, i - entry.getValue());
            }
            
            map.put(prefixSum[i], i);
        }
        
        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}
```

**시간복잡도**: O(n²) (headMap 순회) **결과**: TLE

---

## 📊 성능 비교

|방법|시간복잡도|공간복잡도|결과|
|---|---|---|---|
|Brute Force|O(n²)|O(1)|TLE|
|TreeMap|O(n²) or O(n log n)|O(n)|TLE or Slow|
|**단조 Deque**|**O(n)**|**O(n)**|**AC ✅**|

---

## 💡 핵심 인사이트

### 1. Prefix Sum의 활용

```
부분 배열 합을 O(1)에 계산
→ 모든 가능한 부분 배열을 빠르게 검사 가능
```

### 2. 단조 Deque의 두 가지 역할

**역할 1: 불필요한 후보 제거**

```java
// prefixSum이 감소하면 제거
while (!deque.isEmpty() && 
       prefixSum[i] <= prefixSum[deque.peekLast()]) {
    deque.pollLast();
}
```

**역할 2: 조건 만족 시 즉시 제거**

```java
// 이미 답을 찾았으면 제거 (더 긴 부분 배열은 불필요)
while (!deque.isEmpty() && 
       prefixSum[i] - prefixSum[deque.peekFirst()] >= k) {
    minLength = Math.min(minLength, i - deque.pollFirst());
}
```

### 3. 왜 음수가 어려운가?

```
양수만 있으면: Two Pointer로 O(n) 가능
음수가 있으면: 합이 증가했다가 감소 → Two Pointer 불가

예: [5, -3, 8]
누적: 5 → 2 → 10
     ↑   ↓   ↑
   증가 감소 증가
```

---

## 🎯 완성 코드 (주석 포함)

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        
        // Prefix Sum 배열 (long 타입으로 overflow 방지)
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        // 단조 증가 Deque (인덱스 저장)
        Deque<Integer> deque = new ArrayDeque<>();
        int minLength = Integer.MAX_VALUE;
        
        for (int i = 0; i <= n; i++) {
            // 1. 조건을 만족하는 부분 배열 찾기
            // prefixSum[i] - prefixSum[j] >= k
            while (!deque.isEmpty() && 
                   prefixSum[i] - prefixSum[deque.peekFirst()] >= k) {
                // 최소 길이 갱신 후 제거
                // (이미 사용했으므로 더 이상 필요 없음)
                minLength = Math.min(minLength, i - deque.pollFirst());
            }
            
            // 2. 단조 증가 유지
            // 현재 prefixSum이 더 작으면 이전 것들 제거
            // 이유: 현재 위치가 더 오른쪽이면서 값도 작으므로
            // 나중에 더 짧은 부분 배열을 만들 수 있음
            while (!deque.isEmpty() && 
                   prefixSum[i] <= prefixSum[deque.peekLast()]) {
                deque.pollLast();
            }
            
            // 3. 현재 인덱스 추가
            deque.offerLast(i);
        }
        
        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}

/**
 * 시간복잡도: O(n) - 각 인덱스는 최대 1번 추가, 1번 제거
 * 공간복잡도: O(n) - prefixSum 배열과 deque
 * 
 * Runtime: 20-30ms
 * Memory: 55-60MB
 */
```

---

## 🔑 핵심 포인트

### 1. Long 타입 사용

```java
long[] prefixSum = new long[n + 1];
// nums[i]가 최대 10^5, n이 최대 10^5
// 최악의 경우: 10^5 * 10^5 = 10^10 > Integer.MAX_VALUE
```

### 2. 단조 증가의 의미

```
deque의 prefixSum 값들:
[작은 값] → [중간 값] → [큰 값]

왜? 작으면서 오른쪽에 있는 게 유리
→ 더 짧은 부분 배열 가능
```

### 3. 두 while 루프의 차이

```java
// 첫 번째: pollFirst() - 답 찾기
while (...) {
    minLength = min(minLength, i - deque.pollFirst());
}

// 두 번째: pollLast() - 불필요한 후보 제거
while (...) {
    deque.pollLast();
}
```

---

## 🎓 연습 문제

### 비슷한 문제

1. **[LeetCode 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)** ⭐⭐
    
    - 양수만 있는 버전 (Two Pointer로 가능)
2. **[LeetCode 1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)** ⭐⭐⭐⭐
    
    - DP + 단조 Deque
3. **[LeetCode 1499. Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/)** ⭐⭐⭐⭐
    
    - 단조 Deque 응용

---

## 🏷️ Keywords

#MonotonicDeque #PrefixSum #ShortestSubarray #단조큐 #누적합 #Deque #SubarraySum #Hard난이도 #슬라이딩윈도우 #음수처리 #LeetCodeHard #최적화 #O(n)알고리즘