
# LeetCode 21: Merge Two Sorted Lists 풀이

## 📊 결과
- **소요시간:** 40분
- **Runtime:** 0ms (100%)
- **Memory:** 42.40MB

---

## 💻 내 코드

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode merged = dummy;
        
        while (list1 != null && list2 != null) {        
            if (list1.val > list2.val) {
                merged.next = list2;
                list2 = list2.next;
            } else {
                merged.next = list1;
                list1 = list1.next;
            }
            merged = merged.next;
        }

        if (list1 != null) {
            merged.next = list1;
        }
        if (list2 != null) {
            merged.next = list2;
        }

        return dummy.next;
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- Dummy Node 활용 - 깔끔한 구현
- 남은 노드 처리 정확
- 최적 성능 (0ms)
- 완벽한 풀이

### ✦ 개선점

거의 없음. 한 가지만:

```java
if (list1 != null) {
    merged.next = list1;
}
if (list2 != null) {
    merged.next = list2;
}
```

둘 중 하나만 실행되므로 `else if` 가능

---

## ✨ 미세 개선

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode merged = dummy;
        
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                merged.next = list1;
                list1 = list1.next;
            } else {
                merged.next = list2;
                list2 = list2.next;
            }
            merged = merged.next;
        }

        merged.next = (list1 != null) ? list1 : list2;
        
        return dummy.next;
    }
}
```

**변경점:**

- 조건 순서 변경 (`<=` 먼저)
- 삼항 연산자로 간결화

---

## 📊 성능

| 항목        | 시간     | 공간   |
| --------- | ------ | ---- |
| **시간복잡도** | O(n+m) | -    |
| **공간복잡도** | -      | O(1) |

---

## 🎯 핵심

**정렬된 리스트 병합 = Two Pointer + Dummy Node**

- 작은 값 선택하며 연결
- 남은 노드 한 번에 연결

---
## 🏷️ Keywords
`#LeetCode` `#LinkedList` `#Merge` `#TwoPointer` `#Easy` `#DummyNode`
