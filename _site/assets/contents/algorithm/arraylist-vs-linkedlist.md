# ArrayList vs LinkedList                                


Java에서 List 인터페이스를 구현하는 두 가지 주요 클래스이다. 각각의 내부 구조와 특성이 다르므로 상황에 맞게 선택해야 한다.

---

## 내부 구조

### ArrayList
- **동적 배열(Dynamic Array)** 기반
- 연속된 메모리 공간에 데이터 저장
- 인덱스로 직접 접근 가능

{% raw %}
```java
// ArrayList 내부 구조 (간단화)
public class ArrayList<E> {
    private Object[] elementData;  // 내부 배열
    private int size;               // 실제 요소 개수
    
    // 기본 용량 10
    public ArrayList() {
        this.elementData = new Object[10];
    }
}
```
{% endraw %}

**메모리 구조:**
```
인덱스:  [0] [1] [2] [3] [4] ...
데이터:  [A] [B] [C] [D] [E] ...
         ↑ 연속된 메모리 공간
```

---

### LinkedList
- **이중 연결 리스트(Doubly Linked List)** 기반
- 각 노드가 이전/다음 노드를 참조
- 메모리 공간이 연속적이지 않음

{% raw %}
```java
// LinkedList 내부 구조 (간단화)
public class LinkedList<E> {
    private Node<E> first;  // 첫 번째 노드
    private Node<E> last;   // 마지막 노드
    private int size;
    
    private static class Node<E> {
        E item;           // 데이터
        Node<E> next;     // 다음 노드 참조
        Node<E> prev;     // 이전 노드 참조
    }
}
```
{% endraw %}

**메모리 구조:**
```
[노드A] ←→ [노드B] ←→ [노드C] ←→ [노드D]
  ↓          ↓          ↓          ↓
 data      data       data       data
```

---

## 시간복잡도 비교

| 연산 | ArrayList | LinkedList | 설명 |
|------|-----------|------------|------|
| **get(index)** | O(1) | O(n) | ArrayList 압도적 우위 |
| **add(element)** | O(1)* | O(1) | 끝에 추가 |
| **add(index, element)** | O(n) | O(n) | 중간 삽입 |
| **remove(index)** | O(n) | O(n) | 중간 삭제 |
| **remove(element)** | O(n) | O(n) | 요소 찾아서 삭제 |
| **contains(element)** | O(n) | O(n) | 순차 탐색 |
| **size()** | O(1) | O(1) | 크기 반환 |

**주의:** ArrayList의 `add()`는 내부 배열이 꽉 찬 경우 O(n) (재할당 필요)

---

## 상세 연산 분석

### 1. 조회 (get)

#### ArrayList: O(1)
{% raw %}
```java
public E get(int index) {
    return (E) elementData[index];  // 배열 직접 접근
}

// 예시
ArrayList<String> list = new ArrayList<>();
list.add("A");
list.add("B");
list.add("C");
String item = list.get(1);  // 즉시 "B" 반환
```
{% endraw %}

#### LinkedList: O(n)
{% raw %}
```java
public E get(int index) {
    Node<E> x = first;
    // 처음부터 index까지 순회
    for (int i = 0; i < index; i++) {
        x = x.next;
    }
    return x.item;
}

// 예시
LinkedList<String> list = new LinkedList<>();
list.add("A");
list.add("B");
list.add("C");
String item = list.get(1);  // first → next → 반환
```
{% endraw %}

**결론:** 인덱스 접근이 많다면 **ArrayList 사용!**

---

### 2. 끝에 추가 (add)

#### ArrayList: O(1) (평균)
{% raw %}
```java
public boolean add(E e) {
    ensureCapacity();  // 용량 체크
    elementData[size++] = e;
    return true;
}

// 배열이 꽉 차면?
private void ensureCapacity() {
    if (size == elementData.length) {
        // 새 배열 생성 (1.5배 크기)
        Object[] newArray = new Object[elementData.length * 3 / 2];
        System.arraycopy(elementData, 0, newArray, 0, size);
        elementData = newArray;  // O(n) 발생!
    }
}
```
{% endraw %}

**Amortized O(1)**: 대부분은 O(1), 가끔 O(n)이지만 평균적으로 O(1)

#### LinkedList: O(1)
{% raw %}
```java
public boolean add(E e) {
    Node<E> newNode = new Node<>(e);
    if (last == null) {
        first = last = newNode;
    } else {
        last.next = newNode;
        newNode.prev = last;
        last = newNode;
    }
    size++;
    return true;
}
```
{% endraw %}

**결론:** 둘 다 빠르지만, ArrayList가 메모리 재할당 때문에 가끔 느려질 수 있음

---

### 3. 중간 삽입 (add(index, element))

#### ArrayList: O(n)
{% raw %}
```java
public void add(int index, E element) {
    // index 이후의 모든 요소를 한 칸씩 뒤로 이동
    System.arraycopy(elementData, index, 
                     elementData, index + 1, 
                     size - index);  // O(n)
    elementData[index] = element;
    size++;
}
```
{% endraw %}

**시각화:**
```
삽입 전: [A][B][C][D][E]
삽입 위치:     ↑ (index 2에 X 삽입)

1단계: [A][B][_][C][D][E]  // C,D,E를 한 칸씩 이동 → O(n)
2단계: [A][B][X][C][D][E]  // X 삽입
```

#### LinkedList: O(n)
{% raw %}
```java
public void add(int index, E element) {
    Node<E> node = getNode(index);  // O(n) - 해당 위치까지 순회
    
    Node<E> newNode = new Node<>(element);
    newNode.next = node;
    newNode.prev = node.prev;
    
    if (node.prev != null) {
        node.prev.next = newNode;
    }
    node.prev = newNode;
}
```
{% endraw %}

**시각화:**
```
삽입 전: [A]↔[B]↔[C]↔[D]

1. index 2까지 순회 → O(n)
2. 포인터만 수정 → O(1)
   [A]↔[B]↔[X]↔[C]↔[D]
```

**결론:** 둘 다 O(n)이지만, LinkedList는 **앞/뒤 삽입**일 때 O(1)!

---

### 4. 삭제 (remove)

#### ArrayList: O(n)
{% raw %}
```java
public E remove(int index) {
    E oldValue = (E) elementData[index];
    
    // index 이후 요소들을 앞으로 이동
    int numMoved = size - index - 1;
    if (numMoved > 0) {
        System.arraycopy(elementData, index + 1,
                         elementData, index,
                         numMoved);  // O(n)
    }
    
    elementData[--size] = null;
    return oldValue;
}
```
{% endraw %}

#### LinkedList: O(n)
{% raw %}
```java
public E remove(int index) {
    Node<E> node = getNode(index);  // O(n) - 순회
    
    // 포인터만 수정 - O(1)
    if (node.prev != null) {
        node.prev.next = node.next;
    }
    if (node.next != null) {
        node.next.prev = node.prev;
    }
    
    return node.item;
}
```
{% endraw %}

**결론:** 삭제도 마찬가지로 LinkedList는 **앞/뒤 삭제**에서 유리!

---

## 🎯 선택 기준

### ArrayList를 사용해야 할 때

1. **인덱스 접근이 빈번한 경우**
   ```java
   for (int i = 0; i < list.size(); i++) {
       String item = list.get(i);  // O(1)
   }
   ```

2. **데이터 크기가 고정되어 있거나 예측 가능한 경우**
   ```java
   ArrayList<String> list = new ArrayList<>(1000);  // 초기 용량 지정
   ```

3. **읽기 작업이 쓰기 작업보다 많은 경우**

4. **메모리 효율이 중요한 경우**
   - 노드의 prev/next 포인터 오버헤드 없음

5. **랜덤 액세스가 필요한 경우**
   ```java
   Collections.binarySearch(list, target);  // O(log n)
   ```

---

### LinkedList를 사용해야 할 때

1. **앞/뒤에서 삽입/삭제가 빈번한 경우**
   ```java
   list.addFirst(element);   // O(1)
   list.addLast(element);    // O(1)
   list.removeFirst();       // O(1)
   list.removeLast();        // O(1)
   ```

2. **Queue나 Deque로 사용할 때**
   ```java
   Deque<String> deque = new LinkedList<>();
   deque.offerFirst("A");
   deque.offerLast("B");
   deque.pollFirst();
   ```

3. **크기가 자주 변하는 경우**
   - 재할당 오버헤드 없음

4. **순차 접근만 하는 경우**
   ```java
   for (String item : list) {  // Iterator 사용
       System.out.println(item);
   }
   ```

---

## 실전 예제

### 예제 1: 성능 비교 테스트

{% raw %}
```java
import java.util.*;

public class ListPerformanceTest {
    public static void main(String[] args) {
        int n = 100000;
        
        // ArrayList 테스트
        List<Integer> arrayList = new ArrayList<>();
        long start = System.currentTimeMillis();
        
        // 끝에 추가
        for (int i = 0; i < n; i++) {
            arrayList.add(i);
        }
        System.out.println("ArrayList add: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // 중간에 삽입
        start = System.currentTimeMillis();
        for (int i = 0; i < 1000; i++) {
            arrayList.add(n / 2, i);
        }
        System.out.println("ArrayList insert: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // 인덱스 접근
        start = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            int value = arrayList.get(i);
        }
        System.out.println("ArrayList get: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        
        // LinkedList 테스트
        List<Integer> linkedList = new LinkedList<>();
        start = System.currentTimeMillis();
        
        // 끝에 추가
        for (int i = 0; i < n; i++) {
            linkedList.add(i);
        }
        System.out.println("LinkedList add: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // 중간에 삽입
        start = System.currentTimeMillis();
        for (int i = 0; i < 1000; i++) {
            linkedList.add(n / 2, i);
        }
        System.out.println("LinkedList insert: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // 인덱스 접근
        start = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            int value = linkedList.get(i);
        }
        System.out.println("LinkedList get: " + 
            (System.currentTimeMillis() - start) + "ms");
    }
}

/* 예상 출력:
ArrayList add: 5ms
ArrayList insert: 450ms
ArrayList get: 3ms

LinkedList add: 8ms
LinkedList insert: 15000ms  // 매우 느림!
LinkedList get: 8000ms      // 매우 느림!
*/
```
{% endraw %}

---

### 예제 2: 올바른 사용 사례

{% raw %}
```java
// ArrayList - 조회가 많은 경우
public List<Product> searchProducts(String keyword) {
    List<Product> results = new ArrayList<>();  // 올바른 선택
    
    for (Product product : allProducts) {
        if (product.getName().contains(keyword)) {
            results.add(product);
        }
    }
    
    // 빈번한 인덱스 접근
    for (int i = 0; i < results.size(); i++) {
        results.get(i).updateRanking(i);  // O(1)
    }
    
    return results;
}

// LinkedList - Queue로 사용
public class TaskQueue {
    private Deque<Task> queue = new LinkedList<>();  // 올바른 선택
    
    public void addTask(Task task) {
        queue.offerLast(task);  // O(1)
    }
    
    public Task getNextTask() {
        return queue.pollFirst();  // O(1)
    }
}

// 잘못된 사용
public void processItems(List<String> items) {
    // LinkedList인데 인덱스 접근 → 비효율적
    for (int i = 0; i < items.size(); i++) {
        String item = items.get(i);  // LinkedList면 O(n²)!
        process(item);
    }
}

// 올바른 수정
public void processItems(List<String> items) {
    // Iterator 또는 for-each 사용
    for (String item : items) {  // O(n)
        process(item);
    }
}
```
{% endraw %}

---

## 📊 메모리 사용량 비교

{% raw %}
```java
// ArrayList 메모리
// 각 요소: 참조(8byte)
// 오버헤드: 배열 객체(24byte) + 미사용 공간

// LinkedList 메모리
// 각 요소: 데이터(8byte) + prev(8byte) + next(8byte) + 노드객체(16byte)
// → 요소당 40byte!

// 예: Integer 1000개 저장
ArrayList<Integer>:  8KB + 소량 오버헤드
LinkedList<Integer>: 40KB
```
{% endraw %}

**결론:** ArrayList가 메모리 효율적!

---

## 핵심 정리

### 빠른 선택 가이드

| 작업 유형 | 추천 |
|----------|------|
| 인덱스로 자주 조회 | **ArrayList** |
| 끝에만 추가/삭제 | **ArrayList** |
| 앞/뒤에 추가/삭제 | **LinkedList** |
| 중간에 자주 삽입/삭제 | **LinkedList** (단, 순차 접근 시) |
| for문으로 순회 | **ArrayList** |
| Iterator로 순회 | 둘 다 OK |
| 메모리 효율 중요 | **ArrayList** |
| Queue/Deque 필요 | **LinkedList** |

### 기억해야 할 핵심

1. **ArrayList**: 배열 기반 → 조회 빠름 (O(1))
2. **LinkedList**: 노드 기반 → 앞/뒤 삽입/삭제 빠름 (O(1))
3. **기본 선택**: 대부분의 경우 **ArrayList**가 더 나음
4. **특수 목적**: Queue/Deque가 필요하면 **LinkedList**

---

## 연습 문제

### 문제 1: 적절한 자료구조 선택
다음 상황에 적합한 List 구현체를 선택하세요:

1. 로그 파일을 순차적으로 읽고 마지막 100개만 유지
2. 학생 명단을 학번 순으로 정렬해서 자주 조회
3. 대기열(Queue) 시스템 구현
4. 페이징 처리를 위해 특정 페이지의 데이터만 조회

**정답:**
1. LinkedList (Deque로 사용)
2. ArrayList (정렬 + 조회)
3. LinkedList (Queue)
4. ArrayList (인덱스 접근)

---

### 문제 2: 성능 예측
{% raw %}
```java
List<String> list = new ArrayList<>();  // 또는 LinkedList
for (int i = 0; i < 10000; i++) {
    list.add(0, "item" + i);  // 맨 앞에 삽입
}
```
{% endraw %}

ArrayList와 LinkedList 중 어느 것이 더 빠를까요?

**정답:** LinkedList가 훨씬 빠름
- ArrayList: O(n²) - 매번 모든 요소를 이동
- LinkedList: O(n) - 노드만 연결

---

## 🔗 관련 학습

- **Vector**: 동기화된 ArrayList (레거시, 사용 비추천)
- **CopyOnWriteArrayList**: Thread-safe한 ArrayList
- **Collections.synchronizedList()**: List를 동기화
- **Stack**: Vector 기반 (대신 Deque 사용 권장)

---
## 🏷️ Keywords
`#Java` `#자료구조` `#ArrayList` `#LinkedList` `#List` `#성능비교` `#시간복잡도`  
 `#알고리즘` `#코딩테스트` `#면접준비`