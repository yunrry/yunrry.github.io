
# LeetCode 141: Linked List Cycle 풀이

## 📊 결과
- **소요시간:** 5분
- **Runtime:** 471ms
- **Memory:** 44.35MB

---

## 💻 내 코드

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        List<ListNode> list = new ArrayList<ListNode>();
        
        while (head != null) {
            if (list.contains(head)) {
                return true;
            } else {
                list.add(head);
            }
            head = head.next;
        }
        
        return false;
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- 동작은 정확함
- 빠른 구현 (5분)

### ✘ 심각한 문제

1. **시간복잡도: O(n²)**
    
    ```java
    list.contains(head)  // O(n) 순회
    ```
    
    매번 전체 리스트 검색
    
2. **공간복잡도: O(n)**
    
    - 모든 노드를 리스트에 저장
    - 메모리 낭비
3. **성능: 471ms**
    
    - 최적 풀이는 0ms 가능

---

## ✨ 최적화

### Floyd's Cycle Detection (토끼와 거북이)

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                return true;
            }
        }
        
        return false;
    }
}
```

**원리:**

- slow: 1칸씩 이동
- fast: 2칸씩 이동
- 순환이 있으면 언젠가 만남

**시각화:**

```
순환 있음:
[1] -> [2] -> [3] -> [4]
             ↑          ↓
             [6] <- [5] 

slow: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3...
fast: 1 -> 3 -> 5 -> 3 -> 5 -> 3...
                  만남!
```

### HashSet 사용 (차선책)

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        
        while (head != null) {
            if (!visited.add(head)) {  // O(1) 체크
                return true;
            }
            head = head.next;
        }
        
        return false;
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|Runtime|
|---|---|---|---|
|**ArrayList**|O(n²)|O(n)|471ms|
|**HashSet**|O(n)|O(n)|4ms|
|**Two Pointer**|O(n)|O(1)|0ms|

---

## 🎯 개선 후 코드

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                return true;
            }
        }
        
        return false;
    }
}
```

**개선:** 471ms → 0ms, O(n) 공간 → O(1)

---

## 💡 핵심

**Cycle 감지 = Floyd's Algorithm**

- Two Pointer (느린/빠른)
- 순환 있으면 반드시 만남
- 공간복잡도 O(1)

---
## 🏷️ Keywords
`#LeetCode` `#LinkedList` `#Cycle` `#TwoPointer` `#Easy` `#FloydAlgorithm`