
# 프로그래머스: 기능개발 (Level 2)

## 📊 결과
- **소요시간**: 25분
- **통과**: 11/11 테스트 케이스
- **평균 Runtime**: 0.11ms
- **평균 Memory**: 81MB

---

## 💻 코드

```java
import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Integer> stack = new ArrayDeque<Integer>();
        Deque<Integer> counts = new ArrayDeque<Integer>();
        
        for(int i=0; i<progresses.length; i++){
            int day = (100-progresses[i])/speeds[i];
            if((100-progresses[i])%speeds[i]>0) day++;
            if(!stack.isEmpty()){
                int prev = stack.peek();
                if(prev>day) day=prev;
            }    
            stack.push(day);
        }
        
        int count=1;
        int len=0;
        int back=stack.pop();
        while(!stack.isEmpty()){
            int curr=stack.pop();
            if(back == curr){
              count++;  
            } else {
                len++; 
                counts.push(count);
                count=1;
            }   
            back = curr;
        }
        len++; 
        counts.push(count);
        
        int[] answer = new int[len];
        for(int i=0; i<len; i++){
            answer[i]= counts.pop();
        }
        
        return answer;
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

1. **올림 처리 정확**: `if((100-progresses[i])%speeds[i]>0) day++`
2. **배포일 조정**: 앞 작업이 늦으면 뒤 작업도 같은 날 배포
3. **그룹핑 로직**: 같은 날 배포되는 기능 카운트
4. **모든 테스트 통과**

### 🔴 개선점

1. **Stack 남용**: 문제는 Queue 개념인데 Stack 사용
2. **불필요한 역순 처리**: Stack에 넣었다가 다시 pop
3. **변수명**: `stack` → `days`, `counts` → `result`
4. **복잡한 2단계 처리**: 계산과 그룹핑을 한번에 가능

---

## ✨ 최적화된 풀이

### 방법 1: Queue 사용 (직관적)

```java
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();
        
        // 1. 각 기능의 완료일 계산
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            queue.offer(days);
        }
        
        // 2. 배포 그룹 계산
        List<Integer> result = new ArrayList<>();
        int prevDay = queue.poll();
        int count = 1;
        
        while (!queue.isEmpty()) {
            int currentDay = queue.poll();
            
            if (currentDay <= prevDay) {
                // 같은 날 배포
                count++;
            } else {
                // 다른 날 배포
                result.add(count);
                count = 1;
                prevDay = currentDay;
            }
        }
        result.add(count);
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}
```

---

### 방법 2: 한 번의 순회로 처리

```java
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();
        int maxDay = 0;  // 현재 배포일
        int count = 0;
        
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            
            if (days > maxDay) {
                // 새로운 배포일
                if (count > 0) {
                    result.add(count);
                }
                maxDay = days;
                count = 1;
            } else {
                // 같은 배포일
                count++;
            }
        }
        result.add(count);
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}
```

**시간복잡도**: O(n)  
**공간복잡도**: O(1) (결과 제외)

---

## 🔍 동작 과정

### 예시: `progresses=[93,30,55]`, `speeds=[1,30,5]`

**Step 1: 완료일 계산**

```
기능 0: (100-93)/1 = 7일
기능 1: (100-30)/30 = 2.33 → 3일
기능 2: (100-55)/5 = 9일
```

**Step 2: 배포 그룹핑**

```
days: [7, 3, 9]

i=0: maxDay=7, count=1
i=1: 3 <= 7 → count=2 (같은 날 배포)
i=2: 9 > 7 → result=[2], maxDay=9, count=1

최종: result=[2, 1]
```

**의미**:

- 1차 배포(7일): 기능 0, 1 (2개)
- 2차 배포(9일): 기능 2 (1개)

---

## 💡 핵심 개념

### 배포 규칙

```
앞 기능이 완료되어야 뒤 기능도 배포 가능
→ 뒤 기능이 먼저 완료되어도 대기

예: [7일, 3일, 9일]
- 기능1은 3일에 완료되지만 7일까지 대기
- 7일에 기능0, 1 함께 배포
```

### Math.ceil 활용

```java
// 원본: 나누기 + 나머지 체크
int day = (100-progresses[i])/speeds[i];
if((100-progresses[i])%speeds[i]>0) day++;

// 개선: Math.ceil
int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
```

---

## 🎯 개선 후 코드

```java
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int maxDay = 0;
        int count = 0;
        
        for (int i = 0; i < progresses.length; i++) {
            // 완료일 계산 (올림)
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            
            if (days > maxDay) {
                // 새로운 배포일 → 이전 그룹 저장
                if (count > 0) answer.add(count);
                maxDay = days;
                count = 1;
            } else {
                // 기존 배포일에 포함
                count++;
            }
        }
        answer.add(count);  // 마지막 그룹
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
```

**개선 효과**:

- Stack 제거 → 직관적
- 한 번의 순회로 처리
- 코드 간결화



## 최적 성능 코드

java

```java
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] temp = new int[progresses.length];
        int idx = 0;
        int maxDay = 0;
        int count = 0;
        
        for (int i = 0; i < progresses.length; i++) {
            int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            
            if (days > maxDay) {
                if (count > 0) temp[idx++] = count;
                maxDay = days;
                count = 1;
            } else {
                count++;
            }
        }
        temp[idx++] = count;
        
        return Arrays.copyOf(temp, idx);
    }
}
```

**개선점**:

- ArrayList 제거 (boxing/unboxing 오버헤드 없음)
- `Math.ceil` → 정수 연산으로 변경
- Stream API 제거

---

## 📚 관련 문제

1. **[프로그래머스] 다리를 지나는 트럭** ⭐⭐
2. **[프로그래머스] 프린터** ⭐⭐
3. **[LeetCode 933] Number of Recent Calls** ⭐

---

## 🏷️ Keywords

#Queue #Stack #프로그래머스 #배포그룹핑 #Math.ceil #FIFO #Level2