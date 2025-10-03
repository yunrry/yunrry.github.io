
# LeetCode 19: Remove Nth Node From End of List 풀이

## 📊 결과
- **소요시간:** 25분
- **Runtime:** 0ms (100%)
- **Memory:** 41.70MB

---

## 💻 내 코드

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null) return null;
        int sz = 1;
        ListNode temp = head;

        while (temp.next != null) {
            if (sz == 30) break;
            sz++;
            temp = temp.next;
        }
        
        if (sz == n) {
            return head.next;
        }

        ListNode target = head;
        ListNode before = head;

        for (int i = 0; i < sz - n; i++) {
            target = target.next; 
            if (i > 0) {
                before = before.next; 
            }           
        }

        before.next = target.next;
        return head;
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

- 길이 계산 후 위치 찾기
- head 삭제 케이스 처리
- 0ms 달성

### 🔴 문제점

1. **의미 없는 break**
    
    ```java
    if (sz == 30) break;  // 왜 30?
    ```
    
2. **비효율적인 Two Pass**
    
    - 전체 순회 → 다시 순회
    - One Pass로 가능
3. **복잡한 before 업데이트**
    
    ```java
    if (i > 0) {
        before = before.next;  // 왜 조건문?
    }
    ```
    

---

## ✨ 최적화

### Two Pointer (One Pass) - 최적

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;
        
        // fast를 n+1칸 앞으로
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        
        // 동시 이동
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        
        // 삭제
        slow.next = slow.next.next;
        
        return dummy.next;
    }
}
```

**핵심:** fast가 끝에 도달하면 slow는 삭제할 노드 직전

---

## 시각화

```
n = 2일 때:
[1] -> [2] -> [3] -> [4] -> [5]

1. fast를 3칸 앞으로 (n+1)
dummy  [1]   [2]   [3]
 slow              fast

2. 동시 이동
[1]    [2]   [3]   [4]   [5]  null
      slow              fast

3. slow.next 삭제
[1] -> [2] -> [3] -> [5]
```

---

## 📊 성능 비교

|방법|시간|공간|순회 횟수|
|---|---|---|---|
|**내 코드**|O(n)|O(1)|2번|
|**Two Pointer**|O(n)|O(1)|1번|

---

## 🎯 개선 후 코드

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;
        
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

**개선:** One Pass, Dummy Node로 edge case 간단 처리

---

## 💡 핵심

**뒤에서 N번째 = Two Pointer 간격 N**

- fast를 n+1칸 앞으로
- 함께 이동하면 slow는 삭제 직전 위치

---

#LeetCode #LinkedList #TwoPointer #Medium #DummyNode