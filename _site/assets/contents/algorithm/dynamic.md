
# 동적계획법 (Dynamic Programming)

동적계획법(DP)은 큰 문제를 작은 부분 문제로 나누어 해결하고, 그 결과를 저장하여 재사용하는 최적화 기법입니다. 중복 계산을 제거하여 지수 시간을 다항 시간으로 줄입니다.

---

## 🎯 DP 핵심 개념

### DP란?

**Dynamic Programming = 동적 계획법**

```

핵심 아이디어:

1. 큰 문제를 작은 문제로 분할
2. 작은 문제의 답을 저장 (Memoization)
3. 저장된 답을 재사용
4. 중복 계산 제거

```

---

### DP vs 분할정복 vs 그리디

| 특성 | DP | 분할정복 | 그리디 |
|------|-------|---------|--------|
| **부분 문제** | 중복됨 | 독립적 | 최선의 선택 |
| **저장** | 필수 | 불필요 | 불필요 |
| **최적해** | 보장 | 보장 | 보장 안 됨 |
| **예시** | 피보나치 | 병합정렬 | 거스름돈 |

---

### DP가 가능한 조건

**1. 최적 부분 구조 (Optimal Substructure)**
```

큰 문제의 최적해가 작은 문제의 최적해로 구성됨

예: 최단 경로 A → C 최단 경로 = A → B 최단 경로 + B → C 최단 경로

```

**2. 중복 부분 문제 (Overlapping Subproblems)**
```

같은 부분 문제가 여러 번 반복됨

예: 피보나치 수열 fib(5) = fib(4) + fib(3) fib(4) = fib(3) + fib(2) ↑ 중복 계산!

````

---

## 🔄 DP 접근법

### Top-Down (하향식) - Memoization

**재귀 + 메모이제이션**

{% raw %}
```java
public class TopDown {
    private int[] memo;
    
    // 피보나치 예제
    public int fib(int n) {
        if (memo == null) {
            memo = new int[n + 1];
            Arrays.fill(memo, -1);
        }
        
        // Base Case
        if (n <= 1) return n;
        
        // 이미 계산됨
        if (memo[n] != -1) {
            return memo[n];
        }
        
        // 계산 후 저장
        memo[n] = fib(n - 1) + fib(n - 2);
        return memo[n];
    }
    
    public static void main(String[] args) {
        TopDown td = new TopDown();
        System.out.println(td.fib(10));  // 55
    }
}
````

{% endraw %}

**장점:**

- 직관적, 재귀와 유사
- 필요한 부분만 계산

**단점:**

- 재귀 호출 오버헤드
- Stack Overflow 위험

---

### Bottom-Up (상향식) - Tabulation ⭐ 추천

**반복문 + 테이블**

{% raw %}

```java
public class BottomUp {
    // 피보나치 예제
    public int fib(int n) {
        if (n <= 1) return n;
        
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    public static void main(String[] args) {
        BottomUp bu = new BottomUp();
        System.out.println(bu.fib(10));  // 55
    }
}
```

{% endraw %}

**장점:**

- 반복문으로 구현 (빠름)
- Stack Overflow 없음
- 코딩테스트에서 선호

**단점:**

- 모든 부분 문제 계산
- 점화식 찾기 어려움

---

## 📝 DP 문제 풀이 단계

### Step 1: DP 문제인지 확인

```
✅ DP 문제 특징:
- 최적값 구하기 (최댓값, 최솟값, 개수)
- 여러 경우의 수가 존재
- 작은 문제로 나눌 수 있음
- 중복 계산 발생

❌ DP가 아닌 경우:
- 그리디로 해결 가능
- 단순 시뮬레이션
- 문자열 처리만
```

---

### Step 2: 상태 정의

```
dp[i] = i번째 상태에서의 최적값

예시:
- dp[i] = i번째 계단까지 가는 최소 비용
- dp[i][j] = (i,j) 위치까지의 경로 수
- dp[i][j] = 첫 i개, 무게 j일 때 최대 가치
```

---

### Step 3: 점화식 도출

```
현재 상태를 이전 상태로 표현

예시:
- dp[i] = dp[i-1] + dp[i-2]  (피보나치)
- dp[i] = min(dp[i-1], dp[i-2]) + cost[i]  (계단)
- dp[i][j] = dp[i-1][j-1] + 1  (LCS)
```

---

### Step 4: 초기값 설정

```
Base Case 설정

예시:
- dp[0] = 0
- dp[1] = 1
- dp[0][0] = 1
```

---

### Step 5: 계산 순서 결정

```
Bottom-Up: 작은 문제부터
for i = 1 to n:
    dp[i] = ...

Top-Down: 재귀로 자동
```

---

## 🔢 1차원 DP

### 예제 1: 피보나치 수열

{% raw %}

```java
public class Fibonacci {
    // Bottom-Up
    public int fib(int n) {
        if (n <= 1) return n;
        
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    // 공간 최적화 O(1)
    public int fibOptimized(int n) {
        if (n <= 1) return n;
        
        int prev2 = 0, prev1 = 1;
        
        for (int i = 2; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
}
```

{% endraw %}

**시간복잡도**: O(n)  
**공간복잡도**: O(n) → O(1) 최적화 가능

---

### 예제 2: 계단 오르기 (LeetCode 70)

{% raw %}

```java
public class ClimbingStairs {
    // 1칸 또는 2칸씩 올라갈 수 있을 때
    // n번째 계단에 도달하는 방법의 수
    
    public int climbStairs(int n) {
        if (n <= 2) return n;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;  // 1칸
        dp[2] = 2;  // 1+1 or 2
        
        for (int i = 3; i <= n; i++) {
            // 이전 계단에서 1칸 or 2칸 전에서 2칸
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    public static void main(String[] args) {
        ClimbingStairs cs = new ClimbingStairs();
        System.out.println(cs.climbStairs(5));  // 8
        // 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1,
        // 1+2+2, 2+1+2, 2+2+1
    }
}
```

{% endraw %}

**점화식**: `dp[i] = dp[i-1] + dp[i-2]`

---

### 예제 3: 계단 오르기 (비용 포함)

{% raw %}

```java
public class MinCostClimbingStairs {
    // 각 계단마다 비용이 있을 때 최소 비용
    // LeetCode 746
    
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        
        // 0번 또는 1번 계단에서 시작 가능
        dp[0] = 0;
        dp[1] = 0;
        
        for (int i = 2; i <= n; i++) {
            // 1칸 전에서 올라오기 or 2칸 전에서 올라오기
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], 
                            dp[i - 2] + cost[i - 2]);
        }
        
        return dp[n];
    }
    
    // 공간 최적화
    public int minCostOptimized(int[] cost) {
        int prev2 = 0, prev1 = 0;
        
        for (int i = 2; i <= cost.length; i++) {
            int current = Math.min(prev1 + cost[i - 1], 
                                  prev2 + cost[i - 2]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    public static void main(String[] args) {
        MinCostClimbingStairs mc = new MinCostClimbingStairs();
        int[] cost = {10, 15, 20};
        System.out.println(mc.minCostClimbingStairs(cost));  // 15
        // 1번 계단(15) → 꼭대기
    }
}
```

{% endraw %}

---

### 예제 4: 집 도둑 (House Robber)

{% raw %}

```java
public class HouseRobber {
    // 인접한 집은 털 수 없을 때 최대 금액
    // LeetCode 198
    
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < n; i++) {
            // 현재 집 털기 vs 안 털기
            dp[i] = Math.max(dp[i - 1],           // 안 털기
                            dp[i - 2] + nums[i]); // 털기
        }
        
        return dp[n - 1];
    }
    
    // 공간 최적화
    public int robOptimized(int[] nums) {
        int prev2 = 0, prev1 = 0;
        
        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    public static void main(String[] args) {
        HouseRobber hr = new HouseRobber();
        int[] nums = {2, 7, 9, 3, 1};
        System.out.println(hr.rob(nums));  // 12
        // 2 + 9 + 1 = 12
    }
}
```

{% endraw %}

**점화식**: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

---

### 예제 5: 최장 증가 부분 수열 (LIS)

{% raw %}

```java
public class LongestIncreasingSubsequence {
    // LeetCode 300
    
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);  // 최소 길이 1
        
        int maxLen = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // nums[i]가 더 크면 증가 수열 연장 가능
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        
        return maxLen;
    }
    
    public static void main(String[] args) {
        LongestIncreasingSubsequence lis = new LongestIncreasingSubsequence();
        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println(lis.lengthOfLIS(nums));  // 4
        // [2, 3, 7, 101] 또는 [2, 3, 7, 18]
    }
}
```

{% endraw %}

**시간복잡도**: O(n²)  
**점화식**: `dp[i] = max(dp[j] + 1)` where `j < i and nums[j] < nums[i]`

---

### 예제 6: 동전 교환 (Coin Change)

{% raw %}

```java
public class CoinChange {
    // 최소 동전 개수로 금액 만들기
    // LeetCode 322
    
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);  // 불가능한 큰 값
        dp[0] = 0;  // 0원은 0개
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
    
    public static void main(String[] args) {
        CoinChange cc = new CoinChange();
        int[] coins = {1, 2, 5};
        System.out.println(cc.coinChange(coins, 11));  // 3
        // 5 + 5 + 1 = 11
    }
}
```

{% endraw %}

**점화식**: `dp[i] = min(dp[i], dp[i - coin] + 1)`

---

## 📊 2차원 DP

### 예제 1: 최장 공통 부분 수열 (LCS)

{% raw %}

```java
public class LongestCommonSubsequence {
    // LeetCode 1143
    
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    // 문자가 같으면 이전 LCS + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    // 다르면 한쪽을 제외한 최대값
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
    
    // LCS 문자열 역추적
    public String getLCSString(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        // DP 테이블 채우기
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // 역추적
        StringBuilder lcs = new StringBuilder();
        int i = m, j = n;
        
        while (i > 0 && j > 0) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                lcs.append(text1.charAt(i - 1));
                i--;
                j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
        
        return lcs.reverse().toString();
    }
    
    public static void main(String[] args) {
        LongestCommonSubsequence lcs = new LongestCommonSubsequence();
        System.out.println(lcs.longestCommonSubsequence("abcde", "ace"));  // 3 (ace)
        System.out.println(lcs.getLCSString("abcde", "ace"));  // "ace"
    }
}
```

{% endraw %}

**점화식**:

```
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

---

### 예제 2: 편집 거리 (Edit Distance)

{% raw %}

```java
public class EditDistance {
    // LeetCode 72
    // 문자열을 같게 만드는 최소 연산 수
    // 연산: 삽입, 삭제, 교체
    
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        // 초기값: 한쪽이 빈 문자열
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;  // word1[0..i] → "" = i번 삭제
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;  // "" → word2[0..j] = j번 삽입
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    // 문자가 같으면 연산 불필요
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(
                        Math.min(
                            dp[i - 1][j] + 1,      // 삭제
                            dp[i][j - 1] + 1),     // 삽입
                        dp[i - 1][j - 1] + 1       // 교체
                    );
                }
            }
        }
        
        return dp[m][n];
    }
    
    public static void main(String[] args) {
        EditDistance ed = new EditDistance();
        System.out.println(ed.minDistance("horse", "ros"));  // 3
        // horse → rorse (교체) → rose (삭제) → ros (삭제)
    }
}
```

{% endraw %}

---

### 예제 3: 0-1 배낭 문제 (Knapsack)

{% raw %}

```java
public class Knapsack {
    // 무게 제한이 있을 때 최대 가치
    
    public int knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        // dp[i][w] = 처음 i개 물건, 무게 w일 때 최대 가치
        int[][] dp = new int[n + 1][capacity + 1];
        
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                // 현재 물건을 넣을 수 없는 경우
                if (weights[i - 1] > w) {
                    dp[i][w] = dp[i - 1][w];
                } else {
                    // 넣기 vs 안 넣기
                    dp[i][w] = Math.max(
                        dp[i - 1][w],  // 안 넣기
                        dp[i - 1][w - weights[i - 1]] + values[i - 1]  // 넣기
                    );
                }
            }
        }
        
        return dp[n][capacity];
    }
    
    // 공간 최적화 O(capacity)
    public int knapsackOptimized(int[] weights, int[] values, int capacity) {
        int[] dp = new int[capacity + 1];
        
        for (int i = 0; i < weights.length; i++) {
            // 뒤에서부터 갱신 (덮어쓰기 방지)
            for (int w = capacity; w >= weights[i]; w--) {
                dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
            }
        }
        
        return dp[capacity];
    }
    
    public static void main(String[] args) {
        Knapsack ks = new Knapsack();
        int[] weights = {1, 3, 4, 5};
        int[] values = {1, 4, 5, 7};
        int capacity = 7;
        
        System.out.println(ks.knapsack(weights, values, capacity));  // 9
        // 물건 1(무게3, 가치4) + 물건 2(무게4, 가치5) = 무게7, 가치9
    }
}
```

{% endraw %}

**점화식**:

```
if weights[i-1] > w:
    dp[i][w] = dp[i-1][w]
else:
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
```

---

### 예제 4: 최소 경로 합

{% raw %}

```java
public class MinimumPathSum {
    // LeetCode 64
    // 왼쪽 위 → 오른쪽 아래 최소 합
    
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        
        // 초기값
        dp[0][0] = grid[0][0];
        
        // 첫 행
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }
        
        // 첫 열
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        
        // 나머지
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        
        return dp[m - 1][n - 1];
    }
    
    // 공간 최적화 O(n)
    public int minPathSumOptimized(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n];
        
        dp[0] = grid[0][0];
        for (int j = 1; j < n; j++) {
            dp[j] = dp[j - 1] + grid[0][j];
        }
        
        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        
        return dp[n - 1];
    }
    
    public static void main(String[] args) {
        MinimumPathSum mps = new MinimumPathSum();
        int[][] grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
        };
        System.out.println(mps.minPathSum(grid));  // 7
        // 1 → 3 → 1 → 1 → 1 = 7
    }
}
```

{% endraw %}

---

### 예제 5: 고유 경로

{% raw %}

```java
public class UniquePaths {
    // LeetCode 62
    // m×n 격자에서 (0,0) → (m-1, n-1) 경로 수
    
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        // 첫 행, 첫 열은 경로가 1가지
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // 위에서 + 왼쪽에서
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        return dp[m - 1][n - 1];
    }
    
    // 공간 최적화
    public int uniquePathsOptimized(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        
        return dp[n - 1];
    }
}
```

{% endraw %}

---

## 🎯 DP 패턴 정리

### 패턴 1: 선형 DP

{% raw %}

```java
// 1차원 배열
int[] dp = new int[n];
dp[0] = 초기값;

for (int i = 1; i < n; i++) {
    dp[i] = f(dp[i-1], dp[i-2], ...);
}
```

{% endraw %}

**예시**: 피보나치, 계단 오르기, 집 도둑

---

### 패턴 2: 구간 DP

{% raw %}

```java
// 구간 [i, j]
int[][] dp = new int[n][n];

for (int len = 1; len <= n; len++) {
    for (int i = 0; i + len <= n; i++) {
        int j = i + len - 1;
        dp[i][j] = f(dp[i][k], dp[k+1][j]);
    }
}
```

{% endraw %}

**예시**: 행렬 곱셈 순서, 팰린드롬

---

### 패턴 3: 격자 DP

{% raw %}

```java
// 2D 격자
int[][] dp = new int[m][n];

for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        dp[i][j] = f(dp[i-1][j], dp[i][j-1]);
    }
}
```

{% endraw %}

**예시**: 최소 경로 합, 고유 경로

---

### 패턴 4: 배낭 DP

{% raw %}

```java
// 배낭 문제
int[][] dp = new int[n + 1][capacity + 1];

for (int i = 1; i <= n; i++) {
    for (int w = 1; w <= capacity; w++) {
        if (weight[i-1] <= w) {
            dp[i][w] = max(dp[i-1][w], 
                          dp[i-1][w-weight[i-1]] + value[i-1]);
        } else {
            dp[i][w] = dp[i-1][w];
        }
    }
}
```

{% endraw %}

**예시**: 0-1 배낭, 동전 교환

---

### 패턴 5: 문자열 DP

{% raw %}

```java
// 두 문자열 비교
int[][] dp = new int[m + 1][n + 1];

for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        if (s1[i-1] == s2[j-1]) {
            dp[i][j] = dp[i-1][j-1] + 1;
        } else {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
}
```

{% endraw %}

**예시**: LCS, 편집 거리

---

## 💡 DP 최적화 기법

### 1. 공간 최적화 (Rolling Array)

{% raw %}

```java
// Before: O(n) 공간
int[] dp = new int[n];
for (int i = 1; i < n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
}

// After: O(1) 공간
int prev2 = 0, prev1 = 1;
for (int i = 2; i <= n; i++) {
    int current = prev1 + prev2;
    prev2 = prev1;
    prev1 = current;
}
```

{% endraw %}

---

### 2. 2D → 1D 최적화

{% raw %}

```java
// Before: O(m×n) 공간
int[][] dp = new int[m][n];
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        dp[i][j] = dp[i-1][j] + dp[i][j-1];
    }
}

// After: O(n) 공간
int[] dp = new int[n];
for (int i = 0; i < m; i++) {
    for (int j = 1; j < n; j++) {
        dp[j] += dp[j-1];
    }
}
```

{% endraw %}

---

### 3. 메모이제이션 범위 축소

{% raw %}

```java
// HashMap으로 필요한 것만 저장
Map<String, Integer> memo = new HashMap<>();

public int dp(int i, int j) {
    String key = i + "," + j;
    if (memo.containsKey(key)) {
        return memo.get(key);
    }
    
    int result = calculate(i, j);
    memo.put(key, result);
    return result;
}
```

{% endraw %}

---

## 🎨 심화 예제

### 예제 1: 정규표현식 매칭

{% raw %}

```java
public class RegularExpressionMatching {
    // LeetCode 10
    // '.' = 모든 문자, '*' = 0개 이상
    
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        
        // 빈 문자열은 빈 패턴과 매칭
        dp[0][0] = true;
        
        // p가 a*b*c* 형태일 때 빈 문자열과 매칭
        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char sc = s.charAt(i - 1);
                char pc = p.charAt(j - 1);
                
                if (pc == '*') {
                    // * 앞 문자 0개 사용
                    dp[i][j] = dp[i][j - 2];
                    
                    // * 앞 문자가 매칭되면 1개 이상 사용 가능
                    char prevPC = p.charAt(j - 2);
                    if (prevPC == '.' || prevPC == sc) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                } else {
                    // 일반 문자 또는 '.'
                    if (pc == '.' || pc == sc) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                }
            }
        }
        
        return dp[m][n];
    }
    
    public static void main(String[] args) {
        RegularExpressionMatching rem = new RegularExpressionMatching();
        System.out.println(rem.isMatch("aa", "a"));      // false
        System.out.println(rem.isMatch("aa", "a*"));     // true
        System.out.println(rem.isMatch("ab", ".*"));     // true
        System.out.println(rem.isMatch("aab", "c*a*b")); // true
    }
}
```

{% endraw %}

---

### 예제 2: 단어 분할

{% raw %}

```java
public class WordBreak {
    // LeetCode 139
    // 문자열을 사전 단어들로 나눌 수 있는가?
    
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;  // 빈 문자열
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                // [0, j)가 분할 가능하고 [j, i)가 사전에 있으면
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[n];
    }
    
    public static void main(String[] args) {
        WordBreak wb = new WordBreak();
        List<String> dict = Arrays.asList("leet", "code");
        System.out.println(wb.wordBreak("leetcode", dict));  // true
    }
}
```

{% endraw %}

---

### 예제 3: 팰린드롬 분할

{% raw %}

```java
public class PalindromePartitioning2 {
    // LeetCode 132
    // 최소 분할 횟수로 팰린드롬 만들기
    
    public int minCut(String s) {
        int n = s.length();
        
        // isPalin[i][j] = s[i..j]가 팰린드롬인가?
        boolean[][] isPalin = new boolean[n][n];
        
        // 팰린드롬 판단 (짧은 것부터)
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;
                if (len == 1) {
                    isPalin[i][j] = true;
                } else if (len == 2) {
                    isPalin[i][j] = s.charAt(i) == s.charAt(j);
                } else {
                    isPalin[i][j] = s.charAt(i) == s.charAt(j) && isPalin[i + 1][j - 1];
                }
            }
        }
        
        // dp[i] = s[0..i]를 팰린드롬으로 만드는 최소 분할
        int[] dp = new int[n];
        
        for (int i = 0; i < n; i++) {
            if (isPalin[0][i]) {
                dp[i] = 0;  // 전체가 팰린드롬
            } else {
                dp[i] = i;  // 최악: i번 분할
                for (int j = 0; j < i; j++) {
                    if (isPalin[j + 1][i]) {
                        dp[i] = Math.min(dp[i], dp[j] + 1);
                    }
                }
            }
        }
        
        return dp[n - 1];
    }
    
    public static void main(String[] args) {
        PalindromePartitioning2 pp = new PalindromePartitioning2();
        System.out.println(pp.minCut("aab"));  // 1 (aa | b)
        System.out.println(pp.minCut("a"));    // 0
    }
}
```

{% endraw %}

---

### 예제 4: 계란 떨어뜨리기

{% raw %}

```java
public class EggDrop {
    // LeetCode 887
    // k개 계란, n층에서 최소 시도 횟수
    
    public int superEggDrop(int k, int n) {
        // dp[i][j] = i번 시도, j개 계란으로 확인 가능한 최대 층수
        int[][] dp = new int[n + 1][k + 1];
        
        int moves = 0;
        while (dp[moves][k] < n) {
            moves++;
            for (int eggs = 1; eggs <= k; eggs++) {
                // 깨짐: 아래 층 확인 (계란 -1)
                // 안 깨짐: 위 층 확인 (계란 유지)
                dp[moves][eggs] = dp[moves - 1][eggs - 1] + dp[moves - 1][eggs] + 1;
            }
        }
        
        return moves;
    }
    
    public static void main(String[] args) {
        EggDrop ed = new EggDrop();
        System.out.println(ed.superEggDrop(1, 2));  // 2
        System.out.println(ed.superEggDrop(2, 6));  // 3
        System.out.println(ed.superEggDrop(3, 14)); // 4
    }
}
```

{% endraw %}

---

## 📊 DP 문제 유형별 정리

### 유형 1: 최적값 구하기

```
최대, 최소, 최댓값, 최솟값 문제

예시:
- 최장 증가 부분 수열
- 최소 경로 합
- 최대 정사각형
```

---

### 유형 2: 경우의 수

```
가능한 방법의 수

예시:
- 계단 오르기
- 고유 경로
- 동전 조합
```

---

### 유형 3: 가능 여부

```
참/거짓 판단

예시:
- 단어 분할
- 정규표현식 매칭
- 부분집합 합
```

---

### 유형 4: 문자열 DP

```
두 문자열 비교/변환

예시:
- LCS
- 편집 거리
- 와일드카드 매칭
```

---

## 🏆 추천 문제

### 1차원 DP (⭐)

1. **[백준 2579] 계단 오르기**
    - 기본 1D DP
2. **[백준 1463] 1로 만들기**
    - 최소 연산 횟수
3. **[백준 9095] 1, 2, 3 더하기**
    - 경우의 수
4. **[백준 11726] 2×n 타일링**
    - 피보나치 응용
5. **[LeetCode 70] Climbing Stairs**
    - 기초 DP
6. **[LeetCode 198] House Robber**
    - 선택 문제
7. **[LeetCode 300] Longest Increasing Subsequence**
    - LIS 기본
8. **[LeetCode 322] Coin Change**
    - 동전 문제

---

### 2차원 DP (⭐⭐)

1. **[백준 9251] LCS**
    - 최장 공통 부분 수열
2. **[백준 12865] 평범한 배낭**
    - 0-1 배낭
3. **[백준 1149] RGB거리**
    - 최소 비용
4. **[백준 11053] 가장 긴 증가하는 부분 수열**
    - LIS
5. **[LeetCode 64] Minimum Path Sum**
    - 격자 DP
6. **[LeetCode 72] Edit Distance**
    - 편집 거리
7. **[LeetCode 1143] Longest Common Subsequence**
    - LCS
8. **[LeetCode 62] Unique Paths**
    - 경로 수

---

### 심화 (⭐⭐⭐)

1. **[백준 2293] 동전 1**
    - 동전 조합
2. **[백준 11054] 가장 긴 바이토닉 부분 수열**
    - LIS 응용
3. **[백준 2225] 합분해**
    - 경우의 수
4. **[백준 1520] 내리막 길**
    - DFS + DP
5. **[LeetCode 10] Regular Expression Matching**
    - 정규표현식
6. **[LeetCode 139] Word Break**
    - 문자열 분할
7. **[LeetCode 312] Burst Balloons**
    - 구간 DP
8. **[LeetCode 887] Super Egg Drop**
    - 계란 떨어뜨리기

---

### 고급 (⭐⭐⭐⭐)

1. **[백준 2098] 외판원 순회**
    - 비트마스킹 DP
2. **[백준 1086] 박성원**
    - 비트마스킹 + 나머지
3. **[백준 2172] 팰린드롬 만들기**
    - 문자열 DP
4. **[LeetCode 115] Distinct Subsequences**
    - 부분 수열
5. **[LeetCode 1687] Delivering Boxes**
    - 최적화 DP

---

## 📚 학습 로드맵

### 1주차: 1D DP 기초

- [ ] 피보나치 수열
- [ ] 계단 오르기 (기본)
- [ ] 계단 오르기 (비용)
- [ ] 집 도둑

### 2주차: 1D DP 응용

- [ ] 최장 증가 부분 수열
- [ ] 동전 교환
- [ ] 1로 만들기
- [ ] 타일링 문제

### 3주차: 2D DP 기초

- [ ] 고유 경로
- [ ] 최소 경로 합
- [ ] 최장 공통 부분 수열
- [ ] 편집 거리

### 4주차: 2D DP 심화

- [ ] 0-1 배낭 문제
- [ ] 정규표현식 매칭
- [ ] 단어 분할
- [ ] 팰린드롬 분할

---

## 💡 실전 팁

### 1. DP 문제 인식

```
✅ DP 신호:
- "최소", "최대", "최적"
- "경우의 수"
- "가능한가?"
- 작은 문제로 나눌 수 있음

❌ DP가 아님:
- 그리디로 해결
- 단순 구현
- 정렬 후 해결
```

---

### 2. 디버깅

{% raw %}

```java
// DP 테이블 출력
public void printDP(int[][] dp) {
    for (int i = 0; i < dp.length; i++) {
        for (int j = 0; j < dp[0].length; j++) {
            System.out.printf("%3d ", dp[i][j]);
        }
        System.out.println();
    }
}

// 경로 추적
public void printPath(int[] parent, int end) {
    List<Integer> path = new ArrayList<>();
    for (int i = end; i != -1; i = parent[i]) {
        path.add(i);
    }
    Collections.reverse(path);
    System.out.println("경로: " + path);
}
```

{% endraw %}

---

### 3. 점화식 세우는 법

```
Step 1: 작은 예시로 손으로 계산
Step 2: 패턴 찾기
Step 3: 일반화
Step 4: Base Case 확인
Step 5: 코드 작성
Step 6: 테스트
```

---

## 🎯 핵심 체크리스트

### DP 문제 풀이

- [ ] 문제가 DP인지 확인
- [ ] 상태 정의 (dp[i], dp[i][j])
- [ ] 점화식 도출
- [ ] Base Case 설정
- [ ] Top-Down vs Bottom-Up 선택
- [ ] 공간 최적화 고려

### 디버깅

- [ ] 작은 입력으로 테스트
- [ ] DP 테이블 출력
- [ ] Base Case 확인
- [ ] 인덱스 범위 확인
- [ ] 초기화 확인

---

## 📝 암기 필수 템플릿

### 1. 1D DP

{% raw %}

```java
int[] dp = new int[n];
dp[0] = 초기값;

for (int i = 1; i < n; i++) {
    dp[i] = 점화식(dp[i-1], dp[i-2], ...);
}

return dp[n-1];
```

{% endraw %}

---

### 2. 2D DP

{% raw %}

```java
int[][] dp = new int[m][n];
dp[0][0] = 초기값;

// 초기화
for (int i = 0; i < m; i++) dp[i][0] = ...;
for (int j = 0; j < n; j++) dp[0][j] = ...;

// 채우기
for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
        dp[i][j] = 점화식(dp[i-1][j], dp[i][j-1], ...);
    }
}

return dp[m-1][n-1];
```

{% endraw %}

---

### 3. 배낭 DP

{% raw %}

```java
int[][] dp = new int[n+1][capacity+1];

for (int i = 1; i <= n; i++) {
    for (int w = 1; w <= capacity; w++) {
        if (weight[i-1] <= w) {
            dp[i][w] = max(dp[i-1][w], 
                          dp[i-1][w-weight[i-1]] + value[i-1]);
        } else {
            dp[i][w] = dp[i-1][w];
        }
    }
}
```

{% endraw %}

---

#Java #DP #DynamicProgramming #동적계획법 #메모이제이션 #Memoization #점화식 #배낭문제 #Knapsack #LCS #최장공통부분수열 #알고리즘 #코딩테스트