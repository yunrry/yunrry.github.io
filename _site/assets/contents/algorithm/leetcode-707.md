
# LeetCode 707: Design Linked List 풀이

## 📊 결과
- **소요시간:** 4H
- **Runtime:** 10ms
- **Memory:** 45.43MB

---

## 💻 내 코드

```java
class MyLinkedList {
    Node head;
    Node tail;
    int size;

    public MyLinkedList() {
        this.size = 0;
    }
    
    public int get(int index) {
        Node temp = this.head;
        if (index >= this.size) {
            return -1;
        } else if (index == 0) {
            return temp.val;
        } else if (index == (this.size - 1)) {
            return this.tail.val;
        }
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp.val;
    }
    
    public void addAtHead(int val) {
        if (this.size == 0) {
            this.head = new Node(val);
            this.head.next = this.head;
            this.tail = this.head;
        } else {
            Node first = new Node(val);
            first.next = this.head;
            this.head = first;
        }
        this.size++;
    }
    
    public void addAtTail(int val) {
        if (this.size == 0) {
            this.head = new Node(val);
            this.head.next = this.head;
            this.tail = this.head;
        } else {
            Node last = new Node(val);
            this.tail.next = last;
            this.tail = last;
        }
        this.size++;    
    }
    
    public void addAtIndex(int index, int val) {
        if (index <= this.size) {            
            if (index == 0) {
                this.addAtHead(val);
            } else if (index == this.size) {
                this.addAtTail(val);
            } else {          
                Node temp = this.head;
                Node added = new Node(val);
                for (int i = 1; i < index; i++) { 
                    temp = temp.next;
                }
                added.next = temp.next;
                temp.next = added;
                this.size++;
            }
        }
    }
    
    public void deleteAtIndex(int index) {
        if (index < this.size && this.size > 0) {
            Node temp = this.head;
            if (index == 0) {
                this.head = null;
                if (this.size > 1) {
                    this.head = temp.next;
                }
                this.size--;
            } else {
                for (int i = 1; i < index; i++) {
                    temp = temp.next;
                }    
                Node delete = temp.next;            
                if (index == (this.size - 1)) {
                    this.tail = temp;
                    this.tail.next = null;
                } else {
                    temp.next = delete.next;
                }
                this.size--;
            }
        }
    }
}

class Node {
    int val;
    Node next;

    public Node() {}
    public Node(int val) { this.val = val; }
    public Node(Node next) { this.next = next; }
    public Node(int val, Node next) { 
        this.val = val; 
        this.next = next; 
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- Node를 별도 클래스로 분리
- head, tail, size 관리
- 엣지 케이스 처리 시도

### ✦ 개선점

1. **버그: `this.head.next = this.head`**
    
    ```java
    if (this.size == 0) {
        this.head = new Node(val);
        this.head.next = this.head;  // 순환 참조 버그!
    }
    ```
    
2. **불필요한 최적화**
    
    ```java
    else if (index == 0) {
        return temp.val;  // 이미 temp = head
    } else if (index == (this.size - 1)) {
        return this.tail.val;  // 굳이 필요 없음
    }
    ```
    
3. **deleteAtIndex 복잡**
    
    - `this.head = null` 후 다시 할당
    - 로직 불필요하게 복잡

---

## ✨ 최적화

### 개선 버전

```java
class MyLinkedList {
    Node head;
    Node tail;
    int size;

    public MyLinkedList() {
        this.size = 0;
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) return -1;
        
        Node curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.val;
    }
    
    public void addAtHead(int val) {
        Node newNode = new Node(val, head);
        head = newNode;
        
        if (size == 0) {
            tail = head;
        }
        size++;
    }
    
    public void addAtTail(int val) {
        Node newNode = new Node(val);
        
        if (size == 0) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }
    
    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        
        if (index == 0) {
            addAtHead(val);
            return;
        }
        
        if (index == size) {
            addAtTail(val);
            return;
        }
        
        Node prev = head;
        for (int i = 0; i < index - 1; i++) {
            prev = prev.next;
        }
        
        Node newNode = new Node(val, prev.next);
        prev.next = newNode;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        
        if (index == 0) {
            head = head.next;
            if (size == 1) {
                tail = null;
            }
        } else {
            Node prev = head;
            for (int i = 0; i < index - 1; i++) {
                prev = prev.next;
            }
            
            prev.next = prev.next.next;
            
            if (index == size - 1) {
                tail = prev;
            }
        }
        size--;
    }
}

class Node {
    int val;
    Node next;
    
    Node(int val) {
        this.val = val;
    }
    
    Node(int val, Node next) {
        this.val = val;
        this.next = next;
    }
}
```

---

## 📊 성능 비교

|항목|내 코드|개선 코드|
|---|---|---|
|**버그**|순환 참조|없음|
|**가독성**|복잡|명확|
|**코드 길이**|길음|간결|

---

## 💡 핵심 인사이트

### 배운 점

1. **초기화 버그**
    
    ```java
    // ❌ 순환 참조
    this.head.next = this.head;
    
    // ✔ null로 초기화
    this.head = new Node(val);  // next는 기본 null
    ```
    
2. **Linked List 핵심**
    
    - 항상 이전 노드부터 접근
    - tail 업데이트 타이밍 중요
3. **Node 생성자 활용**
    
    ```java
    new Node(val, next)  // 한 줄로 연결
    ```
    

---

## 🎯 개선 후 코드 (핵심만)

```java
public void addAtHead(int val) {
    Node newNode = new Node(val, head);  // next를 head로
    head = newNode;
    if (size == 0) tail = head;
    size++;
}

public void deleteAtIndex(int index) {
    if (index < 0 || index >= size) return;
    
    if (index == 0) {
        head = head.next;
        if (size == 1) tail = null;
    } else {
        Node prev = head;
        for (int i = 0; i < index - 1; i++) {
            prev = prev.next;
        }
        prev.next = prev.next.next;
        if (index == size - 1) tail = prev;
    }
    size--;
}
```

---

## 📚 관련 개념

### Singly Linked List vs Doubly Linked List

- 단방향: 메모리 효율적, 역방향 탐색 불가
- 양방향: 메모리 더 사용, 양방향 탐색 가능

### Sentinel Node (더미 노드)

```java
Node dummy = new Node(0);
dummy.next = head;
// 엣지 케이스 처리 간단해짐
```

---

## 🎓 다음 단계

- <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">LeetCode 206: Reverse Linked List</a>
- <a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank">LeetCode 876: Middle of the Linked List</a>

---
## 🏷️ Keywords
`#LeetCode` `#LinkedList` `#Design` `#DataStructure` `#Medium` `#포인터조작`
