

# LeetCode 206: Reverse Linked List 풀이

## 📊 결과
- **소요시간:** 30분
- **Runtime:** 0ms (100%)
- **Memory:** 42.57MB

---

## 💻 내 코드

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode cur = new ListNode(head.val);
        
        while (head != null) {
            if (head.next == null) break;
            ListNode dummy = new ListNode(head.next.val);
            dummy.next = cur; 
            cur = dummy; 
            head = head.next; 
        }
        
        return cur;
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

- 역순 연결 개념 이해
- 0ms 달성

### 🔴 문제점

1. **불필요한 노드 생성**
    
    ```java
    ListNode cur = new ListNode(head.val);  // 새 노드 생성
    ListNode dummy = new ListNode(head.next.val);  // 또 생성
    ```
    
    메모리 낭비 - 기존 노드 재사용 가능
    
2. **복잡한 로직**
    
    - `if (head.next == null) break` 불필요
    - 반복문 조건으로 처리 가능

---

## ✨ 최적화

### 방법 1: Iterative (포인터 조작)

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next;  // 다음 노드 저장
            curr.next = prev;           // 역방향 연결
            prev = curr;                // prev 이동
            curr = next;                // curr 이동
        }
        
        return prev;
    }
}
```

**시각화:**

```
초기: null <- [1] -> [2] -> [3]
      prev   curr

1단계: null <- [1]   [2] -> [3]
              prev   curr

2단계: null <- [1] <- [2]   [3]
                     prev   curr

3단계: null <- [1] <- [2] <- [3]
                            prev  curr(null)
```

### 방법 2: Recursive

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        
        return newHead;
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|특징|
|---|---|---|---|
|**내 코드**|O(n)|O(n)|새 노드 생성|
|**Iterative**|O(n)|O(1)|최적|
|**Recursive**|O(n)|O(n)|스택 사용|

---

## 🎯 개선 후 코드

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
}
```

**핵심:** 노드 생성 대신 포인터만 조작

---

## 💡 핵심

**Linked List 역순 = 포인터 방향 뒤집기**

- 새 노드 생성 불필요
- prev, curr, next 3개 포인터로 해결

---

#LeetCode #LinkedList #Reverse #Easy #포인터조작