
# LeetCode 121: Best Time to Buy and Sell Stock 풀이

## 📊 결과
- **소요시간:** 12H
- **Runtime:** 2ms (상위 85%)
- **Memory:** 62.13MB

---

## 💻 내 코드 (Try 1)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int small = prices[0];
        int big = 0;
        int max = 0;
        
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < small) {
                small = prices[i];
                big = 0;
            } else {
                big = prices[i];
            }
            
            if (max < big - small) {
                max = big - small;
            }
        }   
        
        return max;
    }
}
````

---

## 📝 평가

이거 Easy라고?? 자괴감 든다.... 
아무 생각없이 n^n 로 풀었다가 런타임 에러나서   
map 만들고 별짓 다해봤는데   
난이도는 Easy라니까 맵까지는 안쓸것같고  
점점 산으로가다가 결국 클로드한테 힌트만 달라고 했다.  

힌트 내용  
<img src="/assets/images/스크린샷 2025-10-03 오전 12.40.03.png" alt="힌트" width="600">  
<img src="/assets/images/스크린샷 2025-10-03 오전 12.40.28.png" alt="힌트" width="600">  
힌트도 정말 잘준다 AI..  
힌트를 보자마자 5분만에 풀어버렸다  
1시간 내로 못풀겠으면 힌트라도 받자 앞으로...  


### ✔ 잘한 점 
form Ai

1. **핵심 아이디어 파악**
    - "지금까지 본 최솟값"을 추적하는 접근 방식 정확
    - 한 번의 순회로 해결 (O(n))
2. **변수 네이밍**
    - `small` (최솟값), `big` (현재 가격), `max` (최대 이익)
    - 직관적이고 이해하기 쉬움
3. **시간복잡도 최적**
    - O(n) - 배열 한 번만 순회
    - 추가 공간 사용 없음 O(1)
4. **정확한 동작**
    - 모든 테스트 케이스 통과
    - 엣지 케이스 처리 완료

---

## ✦ 개선점

### 1. 불필요한 변수 `big`

```java
// ❌ 현재 코드
if (prices[i] < small) {
    small = prices[i];
    big = 0;  // 불필요한 재설정
} else {
    big = prices[i];
}
max = Math.max(max, big - small);

// ✔ 개선
max = Math.max(max, prices[i] - small);
// big 변수 없이 직접 계산 가능
```

### 2. `big = 0` 설정의 의미 불명확

```java
if (prices[i] < small) {
    small = prices[i];
    big = 0;  // 왜 0으로?
}
```

- `big`을 0으로 설정하는 것은 논리적으로 혼란스러움
- 실제로는 `big` 변수 자체가 불필요

### 3. 변수명 개선 여지

```java
// 현재
int small, big, max

// 더 명확하게
int minPrice, currentPrice, maxProfit
// 또는
int lowestBuy, maxProfit
```

---

## ✨ 최적화된 풀이

### 방법 1: 간결한 버전 (추천!)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        
        return maxProfit;
    }
}
```

**변경사항:**

- `big` 변수 제거
- `Math.min()`, `Math.max()` 활용
- 로직 더 명확해짐

---

### 방법 2: 한 줄로 더 간결하게

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        
        return maxProfit;
    }
}
```

**장점:**

- `prices[0]` 초기화 불필요
- for-each로 더 간결

---

### 방법 3: Kadane's Algorithm 변형

```java
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = prices[0];
        
        for (int price : prices) {
            // 오늘 팔면 얼마 벌까?
            int profit = price - minPrice;
            maxProfit = Math.max(maxProfit, profit);
            
            // 더 싼 날이 있으면 갱신
            minPrice = Math.min(minPrice, price);
        }
        
        return maxProfit;
    }
}
```

---

## 📊 성능 비교

|방법|시간복잡도|공간복잡도|코드 길이|가독성|
|---|---|---|---|---|
|**내 코드**|O(n)|O(1)|15줄|보통|
|**방법 1**|O(n)|O(1)|10줄|좋음 ⭐|
|**방법 2**|O(n)|O(1)|10줄|매우 좋음|
|**방법 3**|O(n)|O(1)|12줄|좋음|

---

## 💡 핵심 인사이트

### 배운 점

1. **Greedy 알고리즘**
    
    - 각 지점에서 최선의 선택
    - "지금까지 최솟값"만 기억하면 충분
2. **불필요한 변수 제거**
    
    - `big` 변수는 중간 계산용
    - 직접 계산하면 코드 간결
3. **Math 함수 활용**
    
    - `Math.min()`, `Math.max()` 사용
    - if-else보다 깔끔
4. **Dynamic Programming 관점**
    
    - 이전 상태(최솟값)만 유지
    - 현재 위치에서 최적해 계산

### 핵심 개념

**문제의 본질:**

```
최대 이익 = max(현재 가격 - 지금까지 최저 가격)
```

**왜 이렇게 풀 수 있나?**

- 최저가에 사서 최고가에 팔면 됨
- 최저가는 항상 최고가보다 먼저 나와야 함
- 각 시점에서 "오늘 팔면 얼마?"를 계산

---

## 🎯 개선 후 코드 (추천)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.length; i++) {
            // 더 싼 날이 있으면 갱신
            minPrice = Math.min(minPrice, prices[i]);
            
            // 오늘 팔면 얼마 벌까?
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        
        return maxProfit;
    }
}
```

**개선 사항:**

- ✂️ `big` 변수 제거 (33% 코드 감소)
- 📈 가독성 향상
- 🎯 로직 더 명확
- 🚀 성능 동일

---

## 📚 관련 개념

### Greedy Algorithm (탐욕 알고리즘)

- 각 단계에서 최선의 선택
- 전체 최적해를 보장하는 경우에만 사용
- 이 문제: "지금까지 최저가"가 항상 최선

### Dynamic Programming 연관

- **상태:** `dp[i]` = i번째 날까지의 최대 이익
- **전이:** `dp[i] = max(dp[i-1], prices[i] - minPrice)`
- 공간 최적화: 이전 상태만 필요 → O(1)

### Kadane's Algorithm

- 최대 부분 배열 합 문제
- 이 문제도 유사한 패턴
- 차이: 음수 이익은 0으로 처리

---

## 🎓 다음 단계

### 비슷한 문제

1. <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/" target="_blank">LeetCode 122: Best Time to Buy and Sell Stock II</a> (Medium)
    
    - 여러 번 거래 가능
2. <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/" target="_blank">LeetCode 123: Best Time to Buy and Sell Stock III</a> (Hard)
    
    - 최대 2번 거래
3. <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/" target="_blank">LeetCode 188: Best Time to Buy and Sell Stock IV</a> (Hard)
    
    - 최대 k번 거래
4. <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/" target="_blank">LeetCode 309: Best Time to Buy and Sell Stock with Cooldown</a> (Medium)
    
    - 쿨다운 있음
5. <a href="https://leetcode.com/problems/maximum-subarray/" target="_blank">LeetCode 53: Maximum Subarray</a> (Medium)
    
    - Kadane's Algorithm

### 프로그래머스

- <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42584" target="_blank">프로그래머스: 주식가격</a> (Level 2)

### 연습 포인트

- [ ] 불필요한 변수 제거 습관화
- [ ] Greedy vs DP 판단 기준 이해
- [ ] Math 함수 활용 익숙해지기
- [ ] 코드 간결성과 가독성 균형 찾기

---

## 🏆 추가 최적화

### Stream API 버전 (참고용)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int[] minPrice = {Integer.MAX_VALUE};
        int[] maxProfit = {0};
        
        Arrays.stream(prices).forEach(price -> {
            minPrice[0] = Math.min(minPrice[0], price);
            maxProfit[0] = Math.max(maxProfit[0], price - minPrice[0]);
        });
        
        return maxProfit[0];
    }
}
```

**주의:** 가독성은 떨어지고 성능도 느림. 실전에서는 비추천!

---
## 🏷️ Keywords
`#LeetCode` `#Greedy` `#DynamicProgramming` `#알고리즘` `#코딩테스트` `#Java`  
 `#Easy` `#배열순회` `#최적화`
