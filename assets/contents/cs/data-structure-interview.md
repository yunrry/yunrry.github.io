# 자료구조 면접/서술

## 1. 스택 2개로 큐 구현

### 📌 핵심 아이디어

**두 개의 스택(stack1, stack2)을 사용하여 FIFO 동작 구현**

---

### 💡 동작 원리

### 구조
```
stack1 (enqueue용)    stack2 (dequeue용)
┌─────┐              ┌─────┐
│     │              │     │
│     │              │     │
└─────┘              └─────┘
```

### 규칙
1. **Enqueue**: stack1에 push
2. **Dequeue**: 
   - stack2가 비어있으면 → stack1의 모든 원소를 stack2로 이동
   - stack2에서 pop

---

## 💻 구현 코드 (C언어)

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

typedef struct {
    Stack stack1;  // enqueue용
    Stack stack2;  // dequeue용
} QueueWithStacks;

// 스택 기본 연산
void initStack(Stack* s) {
    s->top = -1;
}

int isEmpty(Stack* s) {
    return s->top == -1;
}

void push(Stack* s, int value) {
    if (s->top >= MAX_SIZE - 1) return;
    s->data[++(s->top)] = value;
}

int pop(Stack* s) {
    if (isEmpty(s)) return -1;
    return s->data[(s->top)--];
}

// 큐 초기화
void initQueue(QueueWithStacks* q) {
    initStack(&q->stack1);
    initStack(&q->stack2);
}

// Enqueue: stack1에 push
void enqueue(QueueWithStacks* q, int value) {
    push(&q->stack1, value);
}

// Dequeue: stack2에서 pop
int dequeue(QueueWithStacks* q) {
    // stack2가 비어있으면 stack1의 원소를 모두 이동
    if (isEmpty(&q->stack2)) {
        while (!isEmpty(&q->stack1)) {
            int value = pop(&q->stack1);
            push(&q->stack2, value);
        }
    }
    
    // stack2가 여전히 비어있으면 큐가 빈 것
    if (isEmpty(&q->stack2)) {
        return -1;  // 에러
    }
    
    return pop(&q->stack2);
}
```

---

## 📊 동작 예시

### 예시 1: 기본 동작

```
초기 상태:
stack1: []
stack2: []

1. enqueue(1)
stack1: [1]
stack2: []

2. enqueue(2)
stack1: [1, 2]
stack2: []

3. enqueue(3)
stack1: [1, 2, 3]
stack2: []

4. dequeue() → stack2가 비어있음
   stack1의 모든 원소를 stack2로 이동:
   
   stack1에서 pop: 3, 2, 1 순서로
   stack2에 push: 3, 2, 1 순서로
   
   결과:
   stack1: []
   stack2: [3, 2, 1]  (top이 1)
   
   stack2에서 pop() → 1 반환

5. dequeue() → stack2가 비어있지 않음
   stack2: [3, 2]
   2 반환

6. enqueue(4)
   stack1: [4]
   stack2: [3]

7. dequeue()
   stack2: [3] → 3 반환
   
8. dequeue() → stack2가 비어있음
   stack1의 4를 stack2로 이동
   stack2: [4] → 4 반환
```

---

## 🎯 시간복잡도 분석

### Enqueue
```
시간복잡도: O(1)
- stack1에 push만 하면 됨
```

### Dequeue
```
최선의 경우: O(1)
- stack2에 원소가 있으면 바로 pop

최악의 경우: O(N)
- stack2가 비어있어서 stack1의 모든 원소(N개)를 이동

분할 상환 분석 (Amortized): O(1)
- 각 원소는 최대 2번만 이동 (stack1→stack2, stack2에서 pop)
- N번의 연산에 대해 총 2N번의 작업 → O(1)
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
두 개의 스택을 사용합니다.
- stack1은 enqueue 전용
- stack2는 dequeue 전용

Enqueue 시 stack1에 push하고,
Dequeue 시 stack2가 비어있으면 stack1의 모든 원소를 
stack2로 옮긴 후 pop합니다.

이렇게 하면 FIFO 순서가 보장됩니다.
```

### 상세 답변
```
스택은 LIFO 구조인데, 두 개를 사용하면 큐의 FIFO를 구현할 수 있습니다.

동작 원리:
1. Enqueue는 항상 stack1에 push
2. Dequeue는 stack2에서 pop
   - stack2가 비어있으면 stack1의 모든 원소를 뒤집어서 이동

왜 동작하는가?
- stack1에서 stack2로 이동할 때 순서가 뒤집힙니다
- 두 번 뒤집으면 원래 순서로 복원됩니다
- 따라서 먼저 들어온 원소가 먼저 나갑니다

시간복잡도:
- Enqueue: O(1)
- Dequeue: 분할 상환 O(1)
  (최악의 경우 O(N)이지만, 각 원소는 최대 2번만 이동)

공간복잡도: O(N) (두 스택 합쳐서)
```

---

# 2. HashMap 동작 원리

## 📌 HashMap이란?

**Key-Value 쌍을 저장하는 자료구조로, 해시 함수를 사용하여 평균 O(1)의 검색/삽입/삭제 성능 제공**

---

## 💡 동작 원리

### 1. 기본 구조

```
HashMap 내부:
┌─────────────────┐
│ 배열 (Bucket)    │
├─────────────────┤
│ [0] → NULL      │
│ [1] → NULL      │
│ [2] → (k3, v3)  │
│ [3] → NULL      │
│ [4] → (k1, v1)  │
│ [5] → NULL      │
│ [6] → (k2, v2)  │
│ [7] → NULL      │
└─────────────────┘
```

### 2. 해시 함수

```
hash(key) → index

예시:
key = "apple"
hash("apple") = 12345
index = 12345 % 8 = 5

→ 배열의 5번 인덱스에 저장
```

---

## 🔧 주요 연산

### 1. Put (삽입)

```java
public void put(K key, V value) {
    // 1. 해시 코드 계산
    int hash = key.hashCode();
    
    // 2. 배열 인덱스 계산
    int index = hash % buckets.length;
    
    // 3. 해당 인덱스에 저장
    buckets[index] = new Entry(key, value);
}
```

### 2. Get (조회)

```java
public V get(K key) {
    // 1. 해시 코드 계산
    int hash = key.hashCode();
    
    // 2. 배열 인덱스 계산
    int index = hash % buckets.length;
    
    // 3. 해당 인덱스에서 값 반환
    Entry entry = buckets[index];
    return entry != null ? entry.value : null;
}
```

---

## ⚠️ 해시 충돌 (Hash Collision)

### 충돌이란?

**서로 다른 키가 같은 인덱스를 가리키는 현상**

```
hash("apple") % 8 = 5
hash("banana") % 8 = 5  ← 충돌!

둘 다 인덱스 5를 가리킴
```

---

## 🛠️ 해시 충돌 해결 방법

### 방법 1: 체이닝 (Chaining) ⭐

**같은 인덱스에 여러 원소를 연결 리스트로 저장**

```
Bucket 배열:
[0] → NULL
[1] → NULL
[2] → (k3, v3) → NULL
[3] → NULL
[4] → NULL
[5] → (apple, 100) → (banana, 200) → NULL  ← 연결 리스트
[6] → (k2, v2) → NULL
[7] → NULL
```

#### 구현 (Java)

```java
class HashMap<K, V> {
    private static class Entry<K, V> {
        K key;
        V value;
        Entry<K, V> next;  // 연결 리스트
        
        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private Entry<K, V>[] buckets;
    
    public void put(K key, V value) {
        int index = hash(key);
        Entry<K, V> entry = buckets[index];
        
        // 이미 키가 존재하는지 확인
        while (entry != null) {
            if (entry.key.equals(key)) {
                entry.value = value;  // 값 업데이트
                return;
            }
            entry = entry.next;
        }
        
        // 새 노드를 맨 앞에 삽입
        Entry<K, V> newEntry = new Entry<>(key, value);
        newEntry.next = buckets[index];
        buckets[index] = newEntry;
    }
    
    public V get(K key) {
        int index = hash(key);
        Entry<K, V> entry = buckets[index];
        
        // 연결 리스트 순회
        while (entry != null) {
            if (entry.key.equals(key)) {
                return entry.value;
            }
            entry = entry.next;
        }
        
        return null;  // 못 찾음
    }
}
```

#### 시간복잡도

```
평균: O(1)
- 충돌이 적으면 연결 리스트 길이가 짧음

최악: O(N)
- 모든 원소가 한 인덱스에 몰림
- 연결 리스트를 끝까지 순회

실제로는:
- Java 8+: 연결 리스트 길이가 8 이상이면 Red-Black Tree로 변환
- 최악의 경우 O(log N)으로 개선
```

---

### 방법 2: 개방 주소법 (Open Addressing)

**충돌 시 다른 빈 버킷을 찾아 저장**

#### 2-1. 선형 탐사 (Linear Probing)

```
충돌 시 바로 다음 인덱스 확인

index = hash(key) % size
충돌 시: (index + 1) % size
또 충돌: (index + 2) % size
...

예시:
hash("apple") % 8 = 5
[5]가 차있음 → [6] 확인
[6]이 차있음 → [7] 확인
[7]이 비어있음 → 저장!
```

**문제점: 클러스터링 (Clustering)**
```
[3][4][5][6][7] 모두 차있으면
다음 삽입도 이 영역에 몰림 → 성능 저하
```

#### 2-2. 제곱 탐사 (Quadratic Probing)

```
충돌 시 제곱수만큼 이동

index = hash(key) % size
충돌 시: (index + 1²) % size = (index + 1) % size
또 충돌: (index + 2²) % size = (index + 4) % size
또 충돌: (index + 3²) % size = (index + 9) % size

클러스터링 완화 ✔
```

#### 2-3. 이중 해싱 (Double Hashing)

```
두 개의 해시 함수 사용

index = hash1(key) % size
충돌 시: (index + hash2(key)) % size
또 충돌: (index + 2 * hash2(key)) % size

최소 클러스터링 ✔
```

---

## 📊 체이닝 vs 개방 주소법 비교

| 구분 | 체이닝 | 개방 주소법 |
|------|--------|------------|
| **구현** | 간단 ✔ | 복잡 |
| **메모리** | 추가 메모리 (포인터) | 배열만 사용 ✔ |
| **캐시 효율** | 낮음 (포인터 추적) | 높음 (연속 메모리) ✔ |
| **삭제** | 쉬움 ✔ | 복잡 (재배치 필요) |
| **로드팩터** | 1 이상 가능 ✔ | 1 미만만 가능 |
| **최악 성능** | O(N), Java 8+는 O(log N) | O(N) |

---

## 🔄 리사이징 (Resizing)

### 로드 팩터 (Load Factor)

```
로드 팩터 = (저장된 원소 수) / (버킷 크기)

예: 16개 버킷에 12개 원소 저장
→ 로드 팩터 = 12/16 = 0.75
```

### 리사이징 기준

```
Java HashMap:
- 기본 로드 팩터: 0.75
- 로드 팩터 초과 시 → 버킷 크기 2배 확장

예: 16 → 32 → 64 → 128 ...
```

### 리사이징 과정

```
1. 새로운 큰 배열 생성 (2배 크기)
2. 모든 원소를 새 배열로 재배치 (rehashing)
   - 해시값은 동일하지만 인덱스가 변경됨
   - index = hash % newSize

시간복잡도: O(N)
- 모든 원소를 다시 삽입해야 함

분할 상환: O(1)
- 리사이징은 가끔만 발생
```

---

## 💬 면접 답변 예시

### 짧은 답변
```
HashMap은 해시 함수로 키를 배열 인덱스로 변환하여
평균 O(1)에 데이터를 저장/조회합니다.

충돌 발생 시:
1. 체이닝: 같은 인덱스에 연결 리스트로 저장
2. 개방 주소법: 다른 빈 버킷을 찾아 저장

Java는 체이닝 방식을 사용하며,
로드 팩터가 0.75 초과 시 배열 크기를 2배로 확장합니다.
```

### 상세 답변
```
HashMap 동작 원리:

1. 데이터 저장:
   - 키의 hashCode() 호출
   - 해시값을 배열 크기로 나눈 나머지가 인덱스
   - 해당 인덱스에 (key, value) 저장

2. 해시 충돌 해결:
   
   체이닝 (Java 사용):
   - 같은 인덱스에 연결 리스트로 저장
   - Java 8+: 리스트 길이 8 이상이면 Red-Black Tree 변환
   - 최악 O(N) → O(log N)으로 개선
   
   개방 주소법:
   - 선형 탐사: 다음 인덱스 순차 확인
   - 제곱 탐사: 제곱수만큼 이동
   - 이중 해싱: 두 번째 해시 함수 사용

3. 리사이징:
   - 로드 팩터(원소수/버킷크기)가 임계값(0.75) 초과 시
   - 배열 크기를 2배로 확장
   - 모든 원소를 재배치 (rehashing)

시간복잡도:
- 평균: O(1)
- 최악: O(N) (체이닝), O(log N) (Java 8+ 트리화)

공간복잡도: O(N)
```

---

# 3. BST vs AVL Tree vs Red-Black Tree

## 📊 비교 표

| 구분 | BST | AVL Tree | Red-Black Tree |
|------|-----|----------|----------------|
| **균형** | 없음 | 엄격한 균형 | 느슨한 균형 |
| **높이** | 최악 O(N) | 최대 1.44 log N | 최대 2 log N |
| **탐색** | 최악 O(N) | **O(log N)** | **O(log N)** |
| **삽입** | 평균 O(log N) | O(log N), 회전 많음 | **O(log N), 회전 적음** |
| **삭제** | 평균 O(log N) | O(log N), 회전 많음 | **O(log N), 회전 적음** |
| **회전 빈도** | 없음 | 높음 (2회전 이내) | 낮음 (3회전 이내) |
| **사용 사례** | 단순 구현 | 검색 많음 | 삽입/삭제 많음 |
| **구현** | 간단 ✔ | 복잡 | 매우 복잡 |

---

## 1️⃣ BST (Binary Search Tree)

### 특징
```
✔ 왼쪽 < 루트 < 오른쪽
✘ 균형 보장 없음
✘ 편향 트리 가능
```

### 구조 예시

```
균형 잡힌 BST:
         50
        /  \
      30    70
     / \    / \
   20  40 60  80

높이: 3
탐색: O(log N) ✔

편향된 BST (최악):
    10
      \
       20
         \
          30
            \
             40
              \
               50

높이: 5
탐색: O(N) ✘ (연결 리스트와 동일)
```

### 장단점

```
장점:
✔ 구현이 간단
✔ 평균적으로 O(log N) 성능
✔ 중위 순회 시 정렬된 결과

단점:
✘ 최악의 경우 O(N)
✘ 순차 삽입 시 편향 트리
✘ 균형 보장 없음
```

---

## 2️⃣ AVL Tree

### 특징

```
✔ 자가 균형 이진 탐색 트리
✔ 모든 노드의 BF (Balance Factor) ∈ {-1, 0, 1}
✔ 가장 엄격한 균형 조건

BF = (왼쪽 서브트리 높이) - (오른쪽 서브트리 높이)
```

### 균형 인수 예시

```
✔ 균형 잡힌 AVL:
         50 (BF=0)
        /  \
      30    70 (BF=0)
     / \      \
   20  40     80

✘ 불균형 (BF=2):
         50 (BF=2)
        /
      30 (BF=1)
     /
   20

→ 회전 필요!
```

### 회전 종류

#### LL 회전 (Right Rotation)
```
    30             20
   /       →      /  \
  20             10   30
 /
10
```

#### RR 회전 (Left Rotation)
```
10                 20
  \       →       /  \
   20           10   30
     \
      30
```

#### LR 회전 (Left-Right)
```
  30           30           20
 /      →     /      →     /  \
10           20           10   30
  \         /
   20      10
```

#### RL 회전 (Right-Left)
```
10           10            20
  \    →       \     →    /  \
   30           20       10   30
  /              \
20               30
```

### 장단점

```
장점:
✔ 항상 O(log N) 보장
✔ 검색 성능이 가장 우수
✔ 높이가 가장 낮음 (최대 1.44 log N)

단점:
✘ 삽입/삭제 시 회전 빈번
✘ 구현 복잡
✘ 오버헤드 (BF 저장)
```

### 사용 사례

```
✔ 데이터베이스 인덱스 (검색 중심)
✔ 읽기 작업이 99%
✔ 실시간 시스템 (예측 가능한 성능)
```

---

## 3️⃣ Red-Black Tree

### 특징

```
✔ 자가 균형 이진 탐색 트리
✔ 각 노드는 빨강 또는 검정
✔ AVL보다 느슨한 균형
✔ 회전 빈도 낮음
```

### 규칙 (5가지)

```
1. 모든 노드는 빨강 또는 검정
2. 루트는 검정
3. 모든 리프(NULL)는 검정
4. 빨강 노드의 자식은 검정
   (빨강-빨강 연속 불가)
5. 모든 경로의 검정 노드 수 동일
   (Black Height 일정)
```

### 구조 예시

```
       [20B]
      /     \
   [10R]   [30B]
   /  \     /  \
[5B] [15B] [25R] [40B]

B = Black, R = Red

규칙 확인:
✔ 루트(20)는 검정
✔ 빨강 노드(10, 25)의 자식은 검정
✔ 모든 경로의 검정 노드 수 = 3
```

### 회전 및 색 변경

```
삽입/삭제 시:
1. BST 규칙대로 삽입/삭제
2. 새 노드는 빨강으로 삽입
3. Red-Black 규칙 위반 시:
   - 색 변경 (Recoloring)
   - 회전 (Rotation)
```

### 장단점

```
장점:
✔ 삽입/삭제가 AVL보다 빠름
✔ 회전 횟수 적음 (최대 3회)
✔ 최악의 경우도 O(log N)
✔ 실무에서 가장 많이 사용

단점:
✘ AVL보다 높이가 높음 (최대 2 log N)
✘ 검색이 AVL보다 약간 느림
✘ 구현이 매우 복잡
```

### 사용 사례

```
✔ Java TreeMap, TreeSet
✔ C++ STL map, set
✔ Linux 커널 (프로세스 스케줄링)
✔ 삽입/삭제가 빈번한 경우
```

---

## 🎯 상세 비교

### 1. 높이 비교

```
같은 N개 노드 저장 시:

BST 높이:
- 평균: 1.39 log N
- 최악: N (편향 트리)

AVL 높이:
- 최대: 1.44 log N ✔ (가장 낮음)

Red-Black 높이:
- 최대: 2 log N
```

### 2. 연산 비교

```
1000개 노드 기준:

        | BST     | AVL      | RB-Tree
--------|---------|----------|----------
검색    | 평균 10 | 최대 14  | 최대 20
        | 최악 1000| ✔       |
삽입    | 평균 10 | 14(회전) | 20(회전적음) ✔
삭제    | 평균 10 | 14(회전) | 20(회전적음) ✔
```

### 3. 회전 빈도

```
삽입 1000번 기준:

AVL Tree: 평균 500번 회전
Red-Black: 평균 200번 회전 ✔

→ RB-Tree가 삽입/삭제에 유리
```

---

## 💬 면접 답변 예시

### 짧은 답변

```
BST: 기본 이진 탐색 트리, 균형 보장 없음

AVL: 엄격한 균형 유지, 검색 최적화
- BF가 항상 -1, 0, 1
- 높이가 가장 낮음
- 검색이 많을 때 사용

Red-Black: 느슨한 균형, 삽입/삭제 최적화
- 빨강/검정 노드로 균형 유지
- 회전 빈도 낮음
- 실무에서 가장 많이 사용 (Java TreeMap 등)
```

### 상세 답변

```
1. BST (Binary Search Tree):
   - 왼쪽 < 루트 < 오른쪽 규칙만 유지
   - 균형 보장 없어서 편향 트리 가능
   - 최악의 경우 O(N)
   - 구현은 간단하지만 실무에선 잘 안 씀

2. AVL Tree:
   - 모든 노드의 Balance Factor가 -1, 0, 1
   - 가장 엄격한 균형 조건
   - 높이가 최대 1.44 log N (가장 낮음)
   - 검색 성능이 최고
   - 하지만 삽입/삭제 시 회전이 빈번
   - 사용 사례: 데이터베이스 인덱스 (검색 중심)

3. Red-Black Tree:
   - 빨강/검정 노드로 균형 유지
   - 5가지 규칙 (루트는 검정, 빨강-빨강 연속 불가 등)
   - 높이가 최대 2 log N (AVL보다 높음)
   - 하지만 회전 빈도가 낮아 삽입/삭제가 빠름
   - 실무에서 가장 많이 사용
   - 사용 사례: Java TreeMap, C++ map, Linux 커널

선택 기준:
- 검색이 99% → AVL Tree
- 삽입/삭제가 빈번 → Red-Black Tree
- 단순 구현 → BST (실무에선 거의 안 씀)
```

---

# 4. Array vs ArrayList vs LinkedList

---

## 📊 비교 표

| 구분 | Array | ArrayList | LinkedList |
|------|-------|-----------|------------|
| **타입** | 기본 자료구조 | 동적 배열 | 이중 연결 리스트 |
| **크기** | 고정 ✘ | 동적 ✔ | 동적 ✔ |
| **메모리** | 연속적 | 연속적 | 비연속적 |
| **인덱스 접근** | O(1) ✔ | O(1) ✔ | O(N) ✘ |
| **검색** | O(N) | O(N) | O(N) |
| **맨앞 삽입** | - | O(N) ✘ | O(1) ✔ |
| **맨뒤 삽입** | - | O(1) (분할상환) | O(1) ✔ |
| **중간 삽입** | - | O(N) | O(N) |
| **맨앞 삭제** | - | O(N) ✘ | O(1) ✔ |
| **맨뒤 삭제** | - | O(1) ✔ | O(1) ✔ |
| **중간 삭제** | - | O(N) | O(N) |
| **메모리 효율** | 높음 ✔ | 중간 | 낮음 (포인터) ✘ |
| **캐시 효율** | 높음 ✔ | 높음 ✔ | 낮음 ✘ |
| **Null 허용** | 타입에 따라 | ✔ | ✔ |
| **초기 용량** | 필수 | 선택 (기본 10) | 불필요 |
| **Thread-Safe** | - | ✘ | ✘ |

---

## 1️⃣ Array (배열)

### 특징

```java
// 고정 크기
int[] arr = new int[5];
String[] names = new String[10];

// 크기 변경 불가
arr[5] = 10;  // ✘ ArrayIndexOutOfBoundsException
```

### 메모리 구조

```
int[] arr = {10, 20, 30, 40, 50};

메모리:
주소   | 1000 | 1004 | 1008 | 1012 | 1016 |
-------|------|------|------|------|------|
인덱스 |  0   |  1   |  2   |  3   |  4   |
값     |  10  |  20  |  30  |  40  |  50  |

연속된 메모리 공간 ✔
```

### 장단점

```
장점:
✔ 인덱스로 O(1) 접근
✔ 메모리 효율적 (오버헤드 없음)
✔ 캐시 친화적
✔ 원시 타입 저장 가능
✔ 성능 최적화

단점:
✘ 크기 고정 (변경 불가)
✘ 삽입/삭제 시 수동 관리 필요
✘ 크기 초과 시 새 배열 생성 필요
```

### 사용 사례

```
✔ 크기가 고정된 경우
✔ 메모리가 제한적일 때
✔ 고성능이 중요한 경우
✔ 원시 타입 저장 (int, double 등)

예시:
- 고정된 학생 수 (30명)
- 요일 배열 (7개)
- RGB 색상 (3개 값)
```

---

## 2️⃣ ArrayList

### 특징

```java
// 동적 크기
ArrayList<Integer> list = new ArrayList<>();

// 초기 용량 지정 가능
ArrayList<String> names = new ArrayList<>(100);

// 크기 자동 조절
list.add(10);  // size: 1
list.add(20);  // size: 2
// 계속 추가 가능... ✔
```

### 내부 구조

```java
public class ArrayList<E> {
    private Object[] elementData;  // 내부 배열
    private int size;              // 현재 원소 수
    
    private static final int DEFAULT_CAPACITY = 10;
}
```

### 동적 확장 (Resizing)

```
초기: 용량 10
[0][1][2][3][4][5][6][7][8][9]

10개 채움:
[10][20][30][40][50][60][70][80][90][100]

11번째 추가 시:
1. 새 배열 생성 (용량 15 = 10 * 1.5)
2. 기존 원소 복사
3. 새 원소 추가

[10][20][30][40][50][60][70][80][90][100][110][_][_][_][_]

시간복잡도:
- 일반 add: O(1)
- resizing 발생: O(N)
- 분할 상환: O(1) ✔
```

### 주요 메서드

```java
ArrayList<Integer> list = new ArrayList<>();

// 삽입
list.add(10);           // 맨 뒤: O(1)
list.add(0, 5);         // 맨 앞: O(N)
list.add(2, 15);        // 중간: O(N)

// 접근
int value = list.get(2);  // O(1) ✔

// 수정
list.set(2, 20);        // O(1)

// 삭제
list.remove(0);         // 맨 앞: O(N)
list.remove(list.size()-1);  // 맨 뒤: O(1)
list.remove(Integer.valueOf(20));  // 값으로: O(N)

// 검색
int index = list.indexOf(20);  // O(N)
boolean exists = list.contains(20);  // O(N)

// 크기
int size = list.size();
boolean empty = list.isEmpty();

// 용량
list.ensureCapacity(100);  // 미리 용량 확보
list.trimToSize();         // 불필요한 용량 제거
```

### 중간 삽입/삭제 과정

```java
// 중간 삽입
list = [10, 20, 30, 40, 50]
list.add(2, 25);

1. 인덱스 2부터 뒤로 이동:
[10, 20, 30, 40, 50, _]
[10, 20, 30, 30, 40, 50]

2. 인덱스 2에 삽입:
[10, 20, 25, 30, 40, 50]

// 중간 삭제
list = [10, 20, 30, 40, 50]
list.remove(2);

1. 인덱스 2 삭제
2. 뒤의 원소들 앞으로 이동:
[10, 20, 40, 50, _]

이동 횟수: N - index
시간복잡도: O(N)
```

### 장단점

```
장점:
✔ 동적 크기 조절
✔ 인덱스로 O(1) 접근
✔ 사용하기 편리 (API 풍부)
✔ 순차 접근 시 빠름 (캐시 효율)
✔ 메모리 연속 배치

단점:
✘ 중간 삽입/삭제 느림 O(N)
✘ Resizing 오버헤드
✘ 초기 용량 낭비 가능
✘ 원시 타입 저장 시 Boxing 필요
```

### 사용 사례

```
✔ 인덱스 접근이 빈번할 때
✔ 순차 접근이 많을 때
✔ 맨 뒤 삽입/삭제가 주된 작업
✔ 크기 예측 가능할 때

예시:
- 검색 결과 리스트
- 로그 저장
- 데이터 수집 후 분석
```

---

## 3️⃣ LinkedList

### 특징

```java
// 이중 연결 리스트
LinkedList<Integer> list = new LinkedList<>();

// 양방향 접근 가능
list.addFirst(10);   // 맨 앞 추가
list.addLast(20);    // 맨 뒤 추가
list.getFirst();     // 맨 앞 조회
list.getLast();      // 맨 뒤 조회
```

### 내부 구조

```java
public class LinkedList<E> {
    private static class Node<E> {
        E item;
        Node<E> next;    // 다음 노드
        Node<E> prev;    // 이전 노드
        
        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
    
    private Node<E> first;  // 첫 노드
    private Node<E> last;   // 마지막 노드
    private int size;
}
```

### 메모리 구조

```
LinkedList: [10, 20, 30, 40]

NULL ← [10|●] ⇄ [20|●] ⇄ [30|●] ⇄ [40|●] → NULL
       ↑                              ↑
     first                          last

각 노드:
- item: 데이터 (8바이트, 참조)
- next: 다음 노드 포인터 (8바이트)
- prev: 이전 노드 포인터 (8바이트)

총 24바이트/노드 (ArrayList는 8바이트)
```

### 주요 메서드

```java
LinkedList<Integer> list = new LinkedList<>();

// 삽입
list.add(10);           // 맨 뒤: O(1)
list.addFirst(5);       // 맨 앞: O(1) ✔
list.addLast(15);       // 맨 뒤: O(1)
list.add(2, 12);        // 중간: O(N)

// 접근
int first = list.getFirst();   // O(1)
int last = list.getLast();     // O(1)
int value = list.get(2);       // O(N) ✘

// 삭제
list.removeFirst();     // 맨 앞: O(1) ✔
list.removeLast();      // 맨 뒤: O(1) ✔
list.remove(2);         // 중간: O(N)

// 큐/스택 연산
list.offer(10);        // 큐: enqueue
list.poll();           // 큐: dequeue
list.push(10);         // 스택: push
list.pop();            // 스택: pop
```

### 중간 접근 최적화

```java
// LinkedList의 get(index) 구현
public E get(int index) {
    // 절반 기준으로 앞/뒤에서 탐색
    if (index < size / 2) {
        // 앞에서부터 탐색
        Node<E> x = first;
        for (int i = 0; i < index; i++)
            x = x.next;
        return x.item;
    } else {
        // 뒤에서부터 탐색
        Node<E> x = last;
        for (int i = size - 1; i > index; i--)
            x = x.prev;
        return x.item;
    }
}

평균 이동 횟수: N/4
여전히 O(N)이지만 실제로는 2배 빠름
```

### 장단점

```
장점:
✔ 맨 앞/뒤 삽입/삭제 O(1)
✔ 크기 제한 없음
✔ Resizing 오버헤드 없음
✔ 메모리 단편화 방지

단점:
✘ 인덱스 접근 O(N)
✘ 메모리 오버헤드 (포인터)
✘ 캐시 비효율적
✘ 순차 접근도 느림
```

### 사용 사례

```
✔ 맨 앞/뒤 삽입/삭제가 빈번할 때
✔ 큐(Queue) 구현
✔ 스택(Stack) 구현
✔ 덱(Deque) 구현
✔ 인덱스 접근이 없을 때

예시:
- 브라우저 방문 기록 (앞/뒤 이동)
- 음악 재생 목록
- Undo/Redo 기능
- 작업 큐
```

---

## 🎯 상세 비교

### 1. 메모리 사용량

```java
// 1000개 Integer 저장 기준

Array (int[]):
4바이트 × 1000 = 4KB ✔

ArrayList<Integer>:
- 내부 배열: 8바이트 × 1000 = 8KB (참조)
- Integer 객체: 16바이트 × 1000 = 16KB
- 총: 24KB

LinkedList<Integer>:
- 노드: 24바이트 × 1000 = 24KB
- Integer 객체: 16바이트 × 1000 = 16KB
- 총: 40KB ✘

LinkedList가 ArrayList보다 1.7배 많은 메모리 사용
```

### 2. 성능 비교 (실측)

```
10,000개 원소 기준:

1. 순차 접근 (0부터 9999까지):
   Array:      0.1ms ✔
   ArrayList:  0.2ms
   LinkedList: 1500ms ✘ (15,000배 느림!)

2. 랜덤 접근 (무작위 인덱스):
   Array:      0.5ms ✔
   ArrayList:  0.6ms
   LinkedList: 750ms ✘

3. 맨 앞 삽입 1000번:
   ArrayList:  150ms (매번 이동)
   LinkedList: 0.1ms ✔

4. 맨 뒤 삽입 10,000번:
   ArrayList:  1ms ✔
   LinkedList: 2ms

5. 중간 삽입 1000번:
   ArrayList:  80ms
   LinkedList: 90ms
   (거의 비슷, 둘 다 O(N))
```

### 3. 반복 성능

```java
List<Integer> list = ... (10,000개)

// 1. for-each (Iterator 사용)
for (Integer value : list) {
    // ...
}
// ArrayList: 1ms ✔
// LinkedList: 2ms (노드 탐색)

// 2. 인덱스 접근
for (int i = 0; i < list.size(); i++) {
    int value = list.get(i);
}
// ArrayList: 1ms ✔
// LinkedList: 1500ms ✘ (절대 사용하지 말 것!)

// 3. Iterator 직접 사용
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    int value = it.next();
}
// ArrayList: 1ms ✔
// LinkedList: 2ms
```

**결론: LinkedList는 반드시 Iterator나 for-each 사용!**

---

## 💬 면접 답변 예시

### 짧은 답변

```
Array:
- 고정 크기, 연속 메모리
- 인덱스 접근 O(1)
- 원시 타입 저장 가능

ArrayList:
- 동적 배열 (내부는 배열)
- 인덱스 접근 O(1)
- 맨 뒤 삽입/삭제 빠름

LinkedList:
- 이중 연결 리스트
- 맨 앞/뒤 삽입/삭제 O(1)
- 인덱스 접근 O(N)

선택 기준:
- 인덱스 접근 많음 → ArrayList
- 맨 앞 삽입/삭제 많음 → LinkedList
- 고정 크기 + 원시 타입 → Array
```

### 상세 답변

```
1. Array (배열):
   
   특징:
   - 고정 크기, 연속된 메모리 공간
   - 컴파일 타임에 크기 결정
   - 원시 타입(int, double) 직접 저장 가능
   
   성능:
   - 접근: O(1) ✔
   - 메모리: 가장 효율적 ✔
   - 캐시: 가장 효율적 ✔
   
   사용:
   - 크기 고정 (요일, RGB 값 등)
   - 고성능 필요 시
   - 메모리 제한적일 때

2. ArrayList:
   
   특징:
   - 내부적으로 배열 사용
   - 동적 크기 조절 (자동 확장)
   - 기본 용량 10, 1.5배씩 증가
   
   성능:
   - 접근: O(1) ✔
   - 맨 뒤 삽입: O(1) 분할상환
   - 중간 삽입/삭제: O(N) (원소 이동)
   - 메모리: 연속 배치로 캐시 효율 높음
   
   내부 동작:
   - 용량 초과 시 새 배열 생성 및 복사
   - 메모리 재할당 오버헤드
   
   사용:
   - 인덱스 접근이 주된 작업
   - 맨 뒤 삽입이 대부분
   - 크기 예측 가능 (초기 용량 지정)

3. LinkedList:
   
   특징:
   - 이중 연결 리스트 (prev, next 포인터)
   - 비연속적 메모리
   - first, last 포인터로 양 끝 관리
   
   성능:
   - 접근: O(N) ✘ (순차 탐색)
   - 맨 앞/뒤 삽입/삭제: O(1) ✔
   - 중간 삽입/삭제: O(N) (위치 찾기)
   - 메모리: 포인터 오버헤드 (노드당 24바이트)
   
   주의사항:
   - get(index) 절대 사용 금지!
   - Iterator나 for-each만 사용
   
   사용:
   - 큐/스택/덱 구현
   - 맨 앞 삽입/삭제가 빈번
   - 인덱스 접근이 없는 경우

성능 비교 (10,000개 기준):
                  | ArrayList | LinkedList
------------------|-----------|------------
순차 접근         | 0.2ms ✔  | 1500ms ✘
맨 앞 삽입 1000번 | 150ms     | 0.1ms ✔
메모리 (Integer)  | 24KB      | 40KB

선택 기준:
- 읽기가 99% → ArrayList
- 맨 앞 작업이 많음 → LinkedList
- 원시 타입 + 고정 크기 → Array
- 실무에서는 대부분 ArrayList 사용
```

---

## 🎓 추가 팁

### ArrayList 최적화

```java
// ✘ 비효율적
ArrayList<Integer> list = new ArrayList<>();
for (int i = 0; i < 10000; i++) {
    list.add(i);  // 여러 번 resizing
}

// ✔ 효율적
ArrayList<Integer> list = new ArrayList<>(10000);
for (int i = 0; i < 10000; i++) {
    list.add(i);  // resizing 없음
}
```

### LinkedList 주의사항

```java
LinkedList<Integer> list = ...;

// ✘ 절대 금지! O(N²)
for (int i = 0; i < list.size(); i++) {
    int value = list.get(i);  // 매번 O(N)
}

// ✔ 올바른 방법 O(N)
for (Integer value : list) {
    // ...
}

// ✔ Iterator 사용
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    int value = it.next();
}
```

### Thread-Safe 버전

```java
// ArrayList
List<Integer> syncList = Collections.synchronizedList(new ArrayList<>());

// CopyOnWriteArrayList (읽기가 많을 때)
List<Integer> cowList = new CopyOnWriteArrayList<>();

// LinkedList
List<Integer> syncLinked = Collections.synchronizedList(new LinkedList<>());
```

---

**핵심 정리:**
1. **인덱스 접근이 많으면 ArrayList**
2. **맨 앞/뒤 작업이 많으면 LinkedList**
3. **고정 크기 + 원시 타입이면 Array**
4. **실무에서는 대부분 ArrayList 사용**
5. **LinkedList는 get(index) 절대 사용 금지!**
