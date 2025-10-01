# Stack, Queue, Deque

Stack, Queue, Deque는 데이터의 삽입과 삭제 순서가 정해진 **선형 자료구조**입니다. 각각의 특성을 이해하고 적절히 활용하는 것이 중요합니다.

---

## 📦 Stack (스택)

### LIFO (Last In First Out) 구조

**나중에 들어간 것이 먼저 나온다**

```
삽입(push):          제거(pop):
     ↓                  ↑
  [  C  ] ← top      [  C  ] ← top
  [  B  ]            [  B  ]
  [  A  ]            [  A  ]
  -------            -------
```

**실생활 예시:**
- 접시 쌓기
- 브라우저 뒤로가기
- Ctrl+Z (실행 취소)

---

### Java에서 Stack 구현

{% raw %}
```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        
        // 삽입 (push) - O(1)
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack);  // [1, 2, 3]
        
        // 조회 (peek) - 제거하지 않고 맨 위 확인 - O(1)
        System.out.println(stack.peek());  // 3
        
        // 제거 (pop) - O(1)
        System.out.println(stack.pop());   // 3
        System.out.println(stack.pop());   // 2
        System.out.println(stack);         // [1]
        
        // 비어있는지 확인
        System.out.println(stack.isEmpty());  // false
        
        // 크기
        System.out.println(stack.size());     // 1
        
        // 요소 검색 (1-based index, top부터)
        stack.push(10);
        stack.push(20);
        System.out.println(stack.search(20)); // 1 (top)
        System.out.println(stack.search(10)); // 2
        System.out.println(stack.search(1));  // 3
    }
}
```
{% endraw %}

---

### Stack 주요 메서드

| 메서드 | 설명 | 시간복잡도 |
|--------|------|------------|
| `push(E item)` | 요소 삽입 | O(1) |
| `pop()` | 맨 위 요소 제거 및 반환 | O(1) |
| `peek()` | 맨 위 요소 조회 (제거 X) | O(1) |
| `isEmpty()` | 비어있는지 확인 | O(1) |
| `search(Object o)` | 요소 위치 검색 (1-based) | O(n) |
| `size()` | 크기 반환 | O(1) |

---

### ⚠️ Stack 사용 시 주의사항

**Java의 Stack 클래스는 레거시!**

{% raw %}
```java
// ❌ 권장하지 않음 (Vector 기반, 동기화 오버헤드)
Stack<Integer> stack = new Stack<>();

// ✅ 권장: Deque 인터페이스 사용
Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);
stack.push(2);
stack.pop();
```
{% endraw %}

**이유:**
- `Stack`은 `Vector`를 상속받아 불필요한 동기화 오버헤드
- `Deque`가 더 일관된 API 제공
- 성능도 `ArrayDeque`가 더 좋음

---

### Stack 실전 활용

#### 1. 괄호 검증 (Valid Parentheses)

{% raw %}
```java
public boolean isValidParentheses(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '{' || c == '[') {
            stack.push(c);
        } else {
            if (stack.isEmpty()) return false;
            
            char top = stack.pop();
            if (c == ')' && top != '(') return false;
            if (c == '}' && top != '{') return false;
            if (c == ']' && top != '[') return false;
        }
    }
    
    return stack.isEmpty();
}

// 테스트
System.out.println(isValidParentheses("()[]{}"));    // true
System.out.println(isValidParentheses("([)]"));      // false
System.out.println(isValidParentheses("{[]}"));      // true
```
{% endraw %}

---

#### 2. 후위 표기법 계산 (Postfix Evaluation)

{% raw %}
```java
public int evalRPN(String[] tokens) {
    Deque<Integer> stack = new ArrayDeque<>();
    
    for (String token : tokens) {
        if (token.equals("+")) {
            stack.push(stack.pop() + stack.pop());
        } else if (token.equals("-")) {
            int b = stack.pop();
            int a = stack.pop();
            stack.push(a - b);
        } else if (token.equals("*")) {
            stack.push(stack.pop() * stack.pop());
        } else if (token.equals("/")) {
            int b = stack.pop();
            int a = stack.pop();
            stack.push(a / b);
        } else {
            stack.push(Integer.parseInt(token));
        }
    }
    
    return stack.pop();
}

// 테스트: ["2", "1", "+", "3", "*"] → (2 + 1) * 3 = 9
String[] tokens = {"2", "1", "+", "3", "*"};
System.out.println(evalRPN(tokens));  // 9
```
{% endraw %}

---

#### 3. 일일 온도 (Daily Temperatures)

{% raw %}
```java
public int[] dailyTemperatures(int[] temperatures) {
    int n = temperatures.length;
    int[] answer = new int[n];
    Deque<Integer> stack = new ArrayDeque<>();  // 인덱스 저장
    
    for (int i = 0; i < n; i++) {
        // 현재 온도가 스택의 온도보다 높으면
        while (!stack.isEmpty() && 
               temperatures[i] > temperatures[stack.peek()]) {
            int idx = stack.pop();
            answer[idx] = i - idx;  // 날짜 차이
        }
        stack.push(i);
    }
    
    return answer;
}

// 테스트
int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
int[] result = dailyTemperatures(temps);
// [1, 1, 4, 2, 1, 1, 0, 0]
```
{% endraw %}

---

## 🎯 Queue (큐)

### FIFO (First In First Out) 구조

**먼저 들어간 것이 먼저 나온다**

```
삽입(offer):                제거(poll):
                ↓                        ↑
  front → [A][B][C] ← rear    front → [A][B][C] ← rear
```

**실생활 예시:**
- 줄서기 (대기열)
- 프린터 출력 대기
- BFS 알고리즘

---

### Java에서 Queue 구현

{% raw %}
```java
import java.util.*;

public class QueueExample {
    public static void main(String[] args) {
        // LinkedList로 구현
        Queue<Integer> queue = new LinkedList<>();
        
        // 삽입 (offer) - O(1)
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        System.out.println(queue);  // [1, 2, 3]
        
        // 조회 (peek) - 제거하지 않고 맨 앞 확인 - O(1)
        System.out.println(queue.peek());  // 1
        
        // 제거 (poll) - O(1)
        System.out.println(queue.poll());  // 1
        System.out.println(queue.poll());  // 2
        System.out.println(queue);         // [3]
        
        // 비어있는지 확인
        System.out.println(queue.isEmpty());  // false
        
        // 크기
        System.out.println(queue.size());     // 1
    }
}
```
{% endraw %}

---

### Queue 주요 메서드

| 메서드 | 설명 | 예외 발생 | 시간복잡도 |
|--------|------|-----------|------------|
| **offer(E e)** | 요소 삽입 | false 반환 | O(1) |
| **add(E e)** | 요소 삽입 | 예외 발생 | O(1) |
| **poll()** | 맨 앞 요소 제거 및 반환 | null 반환 | O(1) |
| **remove()** | 맨 앞 요소 제거 및 반환 | 예외 발생 | O(1) |
| **peek()** | 맨 앞 요소 조회 | null 반환 | O(1) |
| **element()** | 맨 앞 요소 조회 | 예외 발생 | O(1) |

**권장:** 예외 대신 null을 반환하는 `offer()`, `poll()`, `peek()` 사용

---

### Queue 구현체 선택

{% raw %}
```java
// 1. LinkedList - 일반적인 Queue
Queue<Integer> queue1 = new LinkedList<>();

// 2. ArrayDeque - 더 빠름 (추천!)
Queue<Integer> queue2 = new ArrayDeque<>();

// 3. PriorityQueue - 우선순위 큐
Queue<Integer> queue3 = new PriorityQueue<>();
```
{% endraw %}

---

### Queue 실전 활용

#### 1. BFS (너비 우선 탐색)

{% raw %}
```java
public void bfs(int[][] graph, int start) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[graph.length];
    
    queue.offer(start);
    visited[start] = true;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                queue.offer(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}
```
{% endraw %}

---

#### 2. 최근 요청 횟수 (Sliding Window)

{% raw %}
```java
class RecentCounter {
    private Queue<Integer> queue;
    
    public RecentCounter() {
        queue = new LinkedList<>();
    }
    
    public int ping(int t) {
        queue.offer(t);
        
        // 3000ms 이전 요청은 제거
        while (queue.peek() < t - 3000) {
            queue.poll();
        }
        
        return queue.size();
    }
}

// 사용
RecentCounter counter = new RecentCounter();
System.out.println(counter.ping(1));     // 1
System.out.println(counter.ping(100));   // 2
System.out.println(counter.ping(3001));  // 3
System.out.println(counter.ping(3002));  // 3
```
{% endraw %}

---

#### 3. 큐를 이용한 스택 구현

{% raw %}
```java
class MyStack {
    private Queue<Integer> queue;
    
    public MyStack() {
        queue = new LinkedList<>();
    }
    
    public void push(int x) {
        queue.offer(x);
        
        // 새로 추가한 요소를 맨 앞으로
        int size = queue.size();
        for (int i = 1; i < size; i++) {
            queue.offer(queue.poll());
        }
    }
    
    public int pop() {
        return queue.poll();
    }
    
    public int top() {
        return queue.peek();
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}
```
{% endraw %}

---

## 🔄 Deque (덱, Double-Ended Queue)

### 양쪽 끝에서 삽입/삭제 가능

```
        addFirst()              addLast()
             ↓                      ↓
  front → [A][B][C][D] ← rear
             ↑                      ↑
        removeFirst()          removeLast()
```

**특징:**
- Stack + Queue 기능 모두 가능
- 양쪽에서 O(1) 삽입/삭제

---

### Java에서 Deque 구현

{% raw %}
```java
import java.util.*;

public class DequeExample {
    public static void main(String[] args) {
        Deque<Integer> deque = new ArrayDeque<>();
        
        // 앞에 추가
        deque.addFirst(1);
        deque.addFirst(2);
        System.out.println(deque);  // [2, 1]
        
        // 뒤에 추가
        deque.addLast(3);
        deque.addLast(4);
        System.out.println(deque);  // [2, 1, 3, 4]
        
        // 앞에서 제거
        System.out.println(deque.removeFirst());  // 2
        
        // 뒤에서 제거
        System.out.println(deque.removeLast());   // 4
        
        System.out.println(deque);  // [1, 3]
        
        // 조회
        System.out.println(deque.peekFirst());  // 1
        System.out.println(deque.peekLast());   // 3
    }
}
```
{% endraw %}

---

### Deque 주요 메서드

| 기능 | 앞(First) | 뒤(Last) |
|------|-----------|----------|
| **삽입** | `addFirst(e)` / `offerFirst(e)` | `addLast(e)` / `offerLast(e)` |
| **제거** | `removeFirst()` / `pollFirst()` | `removeLast()` / `pollLast()` |
| **조회** | `getFirst()` / `peekFirst()` | `getLast()` / `peekLast()` |

**Stack으로 사용:**
{% raw %}
```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);      // addFirst()
stack.push(2);
stack.pop();        // removeFirst()
stack.peek();       // peekFirst()
```
{% endraw %}

**Queue로 사용:**
{% raw %}
```java
Deque<Integer> queue = new ArrayDeque<>();
queue.offer(1);     // addLast()
queue.offer(2);
queue.poll();       // removeFirst()
queue.peek();       // peekFirst()
```
{% endraw %}

---

### Deque 구현체

{% raw %}
```java
// 1. ArrayDeque - 배열 기반 (가장 빠름, 추천!)
Deque<Integer> deque1 = new ArrayDeque<>();

// 2. LinkedList - 연결 리스트 기반
Deque<Integer> deque2 = new LinkedList<>();
```
{% endraw %}

**ArrayDeque vs LinkedList:**
- **ArrayDeque**: 메모리 효율적, 캐시 친화적, 더 빠름
- **LinkedList**: 중간 삽입/삭제 시 유리 (Deque로는 거의 사용 안 함)

---

### Deque 실전 활용

#### 1. Sliding Window Maximum

{% raw %}
```java
public int[] maxSlidingWindow(int[] nums, int k) {
    Deque<Integer> deque = new ArrayDeque<>();  // 인덱스 저장
    int[] result = new int[nums.length - k + 1];
    int idx = 0;
    
    for (int i = 0; i < nums.length; i++) {
        // 윈도우 범위를 벗어난 인덱스 제거
        while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
            deque.pollFirst();
        }
        
        // 현재 값보다 작은 값들 제거 (단조 감소 유지)
        while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
            deque.pollLast();
        }
        
        deque.offerLast(i);
        
        // 윈도우가 완성되면 최댓값 추가
        if (i >= k - 1) {
            result[idx++] = nums[deque.peekFirst()];
        }
    }
    
    return result;
}

// 테스트
int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
int[] result = maxSlidingWindow(nums, 3);
// [3, 3, 5, 5, 6, 7]
```
{% endraw %}

---

#### 2. 회문 검사 (Palindrome)

{% raw %}
```java
public boolean isPalindrome(String s) {
    Deque<Character> deque = new ArrayDeque<>();
    
    // 알파벳과 숫자만 추가
    for (char c : s.toLowerCase().toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            deque.offerLast(c);
        }
    }
    
    // 양끝에서 비교
    while (deque.size() > 1) {
        if (deque.pollFirst() != deque.pollLast()) {
            return false;
        }
    }
    
    return true;
}

// 테스트
System.out.println(isPalindrome("A man, a plan, a canal: Panama"));  // true
System.out.println(isPalindrome("race a car"));  // false
```
{% endraw %}

---

#### 3. 최근 K개 요소 유지

{% raw %}
```java
class RecentItems<T> {
    private Deque<T> deque;
    private int maxSize;
    
    public RecentItems(int k) {
        this.deque = new ArrayDeque<>();
        this.maxSize = k;
    }
    
    public void add(T item) {
        if (deque.size() == maxSize) {
            deque.pollFirst();  // 가장 오래된 항목 제거
        }
        deque.offerLast(item);  // 새 항목 추가
    }
    
    public List<T> getRecent() {
        return new ArrayList<>(deque);
    }
}

// 사용
RecentItems<String> recent = new RecentItems<>(3);
recent.add("A");
recent.add("B");
recent.add("C");
recent.add("D");  // A 제거됨
System.out.println(recent.getRecent());  // [B, C, D]
```
{% endraw %}

---

## 📊 성능 비교

### 시간복잡도

| 연산 | Stack | Queue | Deque |
|------|-------|-------|-------|
| 삽입 (앞) | - | - | O(1) |
| 삽입 (뒤) | O(1) | O(1) | O(1) |
| 제거 (앞) | - | O(1) | O(1) |
| 제거 (뒤) | O(1) | - | O(1) |
| 조회 (앞) | - | O(1) | O(1) |
| 조회 (뒤) | O(1) | - | O(1) |

---

### 공간복잡도

{% raw %}
```java
// ArrayDeque (추천)
// 내부 배열 크기는 2의 거듭제곱으로 자동 조정
// 초기 크기: 16

Deque<Integer> deque = new ArrayDeque<>();
// 메모리: 16 * 4 bytes (int) = 64 bytes

Deque<Integer> deque2 = new ArrayDeque<>(100);
// 메모리: 128 * 4 bytes = 512 bytes (다음 2의 거듭제곱)


// LinkedList
// 각 노드: 데이터 + prev + next + 객체 오버헤드
// 약 40 bytes per element

LinkedList<Integer> list = new LinkedList<>();
// 100개 저장 시: ~4KB
```
{% endraw %}

---

## 🎯 자료구조 선택 가이드

### 언제 무엇을 사용할까?

| 상황 | 선택 | 이유 |
|------|------|------|
| **후입선출(LIFO) 필요** | `ArrayDeque` (Stack으로) | Stack 클래스는 레거시 |
| **선입선출(FIFO) 필요** | `ArrayDeque` (Queue로) | 가장 빠르고 효율적 |
| **양쪽 삽입/삭제** | `ArrayDeque` | Deque의 기본 용도 |
| **우선순위가 필요** | `PriorityQueue` | 최소/최대 힙 |
| **중간 삽입/삭제** | `LinkedList` | 하지만 비추천 |
| **BFS 구현** | `LinkedList` 또는 `ArrayDeque` | 둘 다 OK |
| **DFS 구현** | `ArrayDeque` (Stack으로) | 재귀 또는 명시적 스택 |

---

## 💡 실전 팁

### 1. Stack 대신 Deque 사용

{% raw %}
```java
// ❌ 비추천
Stack<Integer> stack = new Stack<>();

// ✅ 추천
Deque<Integer> stack = new ArrayDeque<>();
```
{% endraw %}

### 2. 예외 vs null 반환

{% raw %}
```java
Queue<Integer> queue = new LinkedList<>();

// 예외 발생 메서드
try {
    queue.remove();  // NoSuchElementException
} catch (Exception e) {
    // 처리
}

// null 반환 메서드 (추천)
Integer value = queue.poll();
if (value == null) {
    // 비어있음
}
```
{% endraw %}

### 3. 초기 용량 지정

{% raw %}
```java
// 크기를 알고 있다면 초기 용량 지정
Deque<Integer> deque = new ArrayDeque<>(1000);
// 재할당 횟수 감소 → 성능 향상
```
{% endraw %}

---

## 🏆 코딩테스트 단골 문제 유형

### Stack 문제
1. **괄호 검증** - LeetCode 20
2. **일일 온도** - LeetCode 739
3. **히스토그램 최대 직사각형** - LeetCode 84
4. **후위 표기법 계산** - LeetCode 150
5. **최소 스택** - LeetCode 155

### Queue 문제
1. **BFS** - 대부분의 그래프 문제
2. **최근 요청 횟수** - LeetCode 933
3. **벽 부수고 이동하기** - 백준 2206
4. **토마토** - 백준 7576
5. **숨바꼭질** - 백준 1697

### Deque 문제
1. **슬라이딩 윈도우 최댓값** - LeetCode 239
2. **회전하는 큐** - 백준 1021
3. **AC** - 백준 5430
4. **최솟값 찾기** - 백준 11003

---

## 📝 핵심 정리

### 기억해야 할 것

1. **Stack = LIFO** (후입선출)
   - 실행 취소, 괄호 검증, DFS
   - Java에서는 `ArrayDeque` 사용 권장

2. **Queue = FIFO** (선입선출)
   - 대기열, 작업 스케줄링, BFS
   - `ArrayDeque` 또는 `LinkedList` 사용

3. **Deque = 양쪽 가능**
   - Stack + Queue 기능
   - `ArrayDeque`가 가장 빠름

4. **모든 기본 연산은 O(1)**

### 빠른 선택 차트

```
필요한 기능         →  선택할 자료구조
─────────────────────────────────────
후입선출(LIFO)     →  ArrayDeque (Stack으로)
선입선출(FIFO)     →  ArrayDeque (Queue로)
양쪽 삽입/삭제     →  ArrayDeque
우선순위          →  PriorityQueue
```

---

## 📚 연습 문제

### 문제 1: 적절한 자료구조 선택
다음 상황에 적합한 자료구조를 선택하세요:

1. 웹 브라우저의 뒤로가기/앞으로가기
2. 프린터 출력 대기열
3. 최근 검색어 10개 유지
4. 괄호 짝 맞추기

**정답:**
1. 2개의 Stack (뒤로가기용, 앞으로가기용)
2. Queue
3. Deque (크기 제한)
4. Stack

---

### 문제 2: 구현 연습

{% raw %}
```java
// 두 개의 Stack으로 Queue 구현하기
class MyQueue {
    private Deque<Integer> stack1;
    private Deque<Integer> stack2;
    
    public MyQueue() {
        stack1 = new ArrayDeque<>();
        stack2 = new ArrayDeque<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
    
    public int peek() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.peek();
    }
    
    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}
```
{% endraw %}

---

#Java #자료구조 #Stack #Queue #Deque #LIFO #FIFO #알고리즘 #코딩테스트 #BFS #DFS #ArrayDeque