# 스택, 큐, 트리

## 📌 스택 (Stack)

**LIFO (Last In First Out)** 구조
- 마지막에 들어간 데이터가 가장 먼저 나옴
- "접시 쌓기"와 같은 구조

```
┌─────┐
│  3  │ ← Top (가장 최근에 삽입)
├─────┤
│  2  │
├─────┤
│  1  │
└─────┘
```

---

### 🔧 스택의 주요 연산

**1. push (삽입)**
```
스택에 데이터 추가

초기: [1, 2]
push(3) → [1, 2, 3]
push(4) → [1, 2, 3, 4]
```

**2. pop (삭제)**
```
스택의 Top 데이터 제거 및 반환

초기: [1, 2, 3, 4]
pop() → 4 반환, 스택: [1, 2, 3]
pop() → 3 반환, 스택: [1, 2]
```

**3. peek / top (조회)**
```
스택의 Top 데이터 조회 (제거하지 않음)

초기: [1, 2, 3]
peek() → 3 반환, 스택: [1, 2, 3] (그대로)
```

**4. isEmpty (공백 검사)**
```
스택이 비어있는지 확인

[1, 2, 3] → isEmpty() → False
[] → isEmpty() → True
```

**5. isFull (포화 검사)**
```
스택이 가득 찼는지 확인 (배열 기반 스택)

최대 크기 5, 현재 [1, 2, 3] → isFull() → False
최대 크기 5, 현재 [1, 2, 3, 4, 5] → isFull() → True
```

---

### 💻 스택 구현 (C언어)

**배열 기반 스택**

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

// 초기화
void init(Stack *s) {
    s->top = -1;
}

// 공백 검사
int isEmpty(Stack *s) {
    return s->top == -1;
}

// 포화 검사
int isFull(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

// push
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack Overflow\n");
        return;
    }
    s->data[++(s->top)] = value;
}

// pop
int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow\n");
        return -1;
    }
    return s->data[(s->top)--];
}

// peek
int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    return s->data[s->top];
}
```

---

### 🎯 스택의 활용

**1. 함수 호출 (Call Stack)**
```
main() {
    funcA();      // Call Stack: [main]
}

funcA() {
    funcB();      // Call Stack: [main, funcA]
}

funcB() {
    return;       // Call Stack: [main, funcA, funcB]
}                 // funcB 종료 → [main, funcA]
                  // funcA 종료 → [main]
```

**2. 괄호 검사**
```c
// 올바른 괄호: (), (()), (())(), {[()]}
// 잘못된 괄호: ((), ))(, ([)]

bool isValid(char* str) {
    Stack s;
    init(&s);
    
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '(' || str[i] == '{' || str[i] == '[') {
            push(&s, str[i]);  // 여는 괄호 push
        }
        else if (str[i] == ')' || str[i] == '}' || str[i] == ']') {
            if (isEmpty(&s)) return false;  // 닫는 괄호인데 스택이 비어있음
            
            char top = pop(&s);
            // 괄호 짝 확인
            if ((str[i] == ')' && top != '(') ||
                (str[i] == '}' && top != '{') ||
                (str[i] == ']' && top != '[')) {
                return false;
            }
        }
    }
    
    return isEmpty(&s);  // 모든 괄호가 닫혔는지 확인
}
```

**3. 수식 계산 (후위 표기법)**

중위 표기법 → 후위 표기법
```
중위: A + B * C
후위: A B C * +

중위: (A + B) * C
후위: A B + C *
```

후위 표기법 계산
```
예: 5 3 + 2 *

1. 5 push → Stack: [5]
2. 3 push → Stack: [5, 3]
3. + 연산 → pop 3, pop 5, 5+3=8, push 8 → Stack: [8]
4. 2 push → Stack: [8, 2]
5. * 연산 → pop 2, pop 8, 8*2=16, push 16 → Stack: [16]

결과: 16
```

**4. DFS (깊이 우선 탐색)**
```
그래프 탐색에서 스택 사용
- 한 경로를 끝까지 탐색
- 막히면 되돌아가서 다른 경로 탐색
```

---

### 📊 스택 시간복잡도

| 연산 | 시간복잡도 |
|------|-----------|
| push | O(1) |
| pop | O(1) |
| peek | O(1) |
| isEmpty | O(1) |

---

## 📌 큐 (Queue)

**FIFO (First In First Out)** 구조
- 먼저 들어간 데이터가 먼저 나옴
- "줄서기"와 같은 구조

```
Front                    Rear
  ↓                        ↓
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  ↑                   ↑
 삭제(Dequeue)      삽입(Enqueue)
```

---

## 🔧 큐의 주요 연산

**1. enqueue (삽입)**
```
큐의 rear에 데이터 추가

초기: [1, 2, 3]
enqueue(4) → [1, 2, 3, 4]
enqueue(5) → [1, 2, 3, 4, 5]
```

**2. dequeue (삭제)**
```
큐의 front 데이터 제거 및 반환

초기: [1, 2, 3, 4]
dequeue() → 1 반환, 큐: [2, 3, 4]
dequeue() → 2 반환, 큐: [3, 4]
```

**3. peek / front (조회)**
```
큐의 front 데이터 조회 (제거하지 않음)

초기: [1, 2, 3]
peek() → 1 반환, 큐: [1, 2, 3] (그대로)
```

---

### 💻 큐 구현

**1. 선형 큐 (Linear Queue)**

```c
#define MAX_SIZE 5

typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} Queue;

// 초기화
void init(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// 공백 검사
int isEmpty(Queue *q) {
    return q->front == q->rear;
}

// 포화 검사
int isFull(Queue *q) {
    return q->rear == MAX_SIZE - 1;
}

// enqueue
void enqueue(Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue Overflow\n");
        return;
    }
    q->data[++(q->rear)] = value;
}

// dequeue
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue Underflow\n");
        return -1;
    }
    return q->data[++(q->front)];
}
```

**선형 큐의 문제점:**
```
초기: front=-1, rear=-1
       [ ][ ][ ][ ][ ]

enqueue(1,2,3): front=-1, rear=2
       [1][2][3][ ][ ]

dequeue 2번: front=1, rear=2
       [ ][ ][3][ ][ ]
              ↑
            front+1부터 데이터

enqueue(4,5): front=1, rear=4
       [ ][ ][3][4][5]

enqueue(6)? → Overflow! (rear가 끝에 도달)
하지만 앞쪽에 공간이 있음 → 공간 낭비!
```

---

**2. 원형 큐 (Circular Queue) ⭐**

선형 큐의 공간 낭비 문제 해결

```c
#define MAX_SIZE 5

typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} CircularQueue;

// 초기화
void init(CircularQueue *q) {
    q->front = 0;
    q->rear = 0;
}

// 공백 검사
int isEmpty(CircularQueue *q) {
    return q->front == q->rear;
}

// 포화 검사
int isFull(CircularQueue *q) {
    return (q->rear + 1) % MAX_SIZE == q->front;
}

// enqueue
void enqueue(CircularQueue *q, int value) {
    if (isFull(q)) {
        printf("Queue Overflow\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = value;
}

// dequeue
int dequeue(CircularQueue *q) {
    if (isEmpty(q)) {
        printf("Queue Underflow\n");
        return -1;
    }
    q->front = (q->front + 1) % MAX_SIZE;
    return q->data[q->front];
}
```

**원형 큐 동작 원리:**
```
배열 크기: 5 (인덱스 0~4)

초기: front=0, rear=0
  0   1   2   3   4
[ ] [ ] [ ] [ ] [ ]
 ↑
F/R

enqueue(1): front=0, rear=1
  0   1   2   3   4
[ ] [1] [ ] [ ] [ ]
 ↑   ↑
 F   R

enqueue(2,3,4): front=0, rear=4
  0   1   2   3   4
[ ] [1] [2] [3] [4]
 ↑               ↑
 F               R

dequeue 2번: front=2, rear=4
  0   1   2   3   4
[ ] [ ] [ ] [3] [4]
         ↑       ↑
         F       R

enqueue(5): rear가 4 → (4+1)%5=0
  0   1   2   3   4
[5] [ ] [ ] [3] [4]
 ↑       ↑       ↑
 R       F      

공간 재사용 가능! ✅
```

---

### 🎯 큐의 활용

**1. 프로세스 스케줄링**
```
CPU 작업 대기 큐
- 먼저 요청한 프로세스가 먼저 실행
- Round Robin 스케줄링
```

**2. BFS (너비 우선 탐색)**
```
그래프 탐색에서 큐 사용
- 같은 레벨의 노드를 먼저 탐색
- 최단 경로 찾기에 유용
```

**3. 프린터 대기열**
```
출력 요청이 들어온 순서대로 인쇄
```

**4. 버퍼 (Buffer)**
```
데이터 전송 시 임시 저장
- 키보드 입력 버퍼
- 네트워크 패킷 버퍼
```

---

### 📊 큐 시간복잡도

| 연산 | 시간복잡도 |
|------|-----------|
| enqueue | O(1) |
| dequeue | O(1) |
| peek | O(1) |
| isEmpty | O(1) |

---

## 🆚 스택 vs 큐 비교

| 구분 | 스택 (Stack) | 큐 (Queue) |
|------|-------------|-----------|
| 구조 | LIFO | FIFO |
| 삽입 | push (top) | enqueue (rear) |
| 삭제 | pop (top) | dequeue (front) |
| 조회 | peek/top | peek/front |
| 활용 | 함수 호출, 괄호 검사, DFS | 프로세스 스케줄링, BFS, 버퍼 |

---



## 📌 트리 (Tree)

**계층적 구조를 표현하는 비선형 자료구조**
- 하나의 루트(Root) 노드
- 부모-자식 관계
- 사이클(Cycle) 없음

```
         1          ← Root (루트)
        / \
       2   3        ← Level 1
      / \   \
     4   5   6      ← Level 2 (Leaf 노드들)
```

---

### 🔑 트리 용어

**1. 노드 (Node)**
```
트리의 각 요소

위 예시: 1, 2, 3, 4, 5, 6 모두 노드
```

**2. 루트 (Root)**
```
트리의 최상위 노드

위 예시: 1
```

**3. 부모 (Parent), 자식 (Child)**
```
         1          
        / \
       2   3        
      / \   
     4   5   

1의 자식: 2, 3
2의 부모: 1
2의 자식: 4, 5
```

**4. 형제 (Sibling)**
```
같은 부모를 가진 노드

2와 3은 형제 (부모가 1로 같음)
4와 5는 형제 (부모가 2로 같음)
```

**5. 리프 (Leaf) / 단말 노드**
```
자식이 없는 노드

위 예시: 4, 5, 6
```

**6. 내부 노드 (Internal Node)**
```
자식이 있는 노드 (루트와 리프 제외)

위 예시: 2, 3
```

**7. 간선 (Edge)**
```
노드와 노드를 연결하는 선

위 예시: 총 5개 간선
(1-2, 1-3, 2-4, 2-5, 3-6)
```

**8. 레벨 (Level)**
```
루트로부터의 깊이 (0부터 시작)

         1          ← Level 0
        / \
       2   3        ← Level 1
      / \   \
     4   5   6      ← Level 2
```

**9. 높이 (Height)**
```
트리의 최대 레벨 + 1

위 예시: 높이 = 3
```

**10. 차수 (Degree)**
```
노드의 자식 수

1의 차수: 2 (자식 2, 3)
2의 차수: 2 (자식 4, 5)
3의 차수: 1 (자식 6)
4의 차수: 0 (리프 노드)

트리의 차수: 노드 차수의 최댓값 = 2
```

---

### 🌲 이진 트리 (Binary Tree)

### 정의
**모든 노드의 차수가 2 이하인 트리**
- 각 노드는 최대 2개의 자식 (왼쪽, 오른쪽)

```
         1
        / \
       2   3
      /   / \
     4   5   6
```

---

### 🎨 이진 트리의 종류

**1. 포화 이진 트리 (Full Binary Tree)**
**모든 레벨이 꽉 찬 트리**

```
         1
        / \
       2   3
      / \ / \
     4  5 6  7

높이 h일 때 노드 개수: 2^h - 1
높이 3 → 2^3 - 1 = 7개
```

**2. 완전 이진 트리 (Complete Binary Tree) ⭐**
**마지막 레벨을 제외하고 모두 채워져 있고, 마지막 레벨은 왼쪽부터 채워진 트리**

```
✅ 완전 이진 트리
         1
        / \
       2   3
      / \  /
     4  5 6

❌ 완전 이진 트리 아님 (왼쪽부터 채워지지 않음)
         1
        / \
       2   3
      /     \
     4       6
```

**완전 이진 트리의 특징:**
- 배열로 구현 가능
- 힙(Heap) 자료구조의 기본 구조

**3. 편향 이진 트리 (Skewed Binary Tree)**
**한쪽으로만 치우친 트리**

```
왼쪽 편향:           오른쪽 편향:
    1                    1
   /                      \
  2                        2
 /                          \
3                            3

사실상 연결 리스트와 동일
```

---

### 💻 이진 트리 구현

**노드 구조**

```c
typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

// 노드 생성
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
```

---

### 🚶 트리 순회 (Tree Traversal)

트리의 모든 노드를 한 번씩 방문하는 방법

```
예시 트리:
         1
        / \
       2   3
      / \
     4   5
```

**1. 전위 순회 (Preorder) ⭐**
**Root → Left → Right**

```c
void preorder(Node* root) {
    if (root == NULL) return;
    
    printf("%d ", root->data);    // Root 방문
    preorder(root->left);          // Left 순회
    preorder(root->right);         // Right 순회
}
```

**순회 순서:**
```
1. Root(1) 방문 → 출력: 1
2. Left(2) 방문 → 출력: 1, 2
3. Left의 Left(4) 방문 → 출력: 1, 2, 4
4. Left의 Right(5) 방문 → 출력: 1, 2, 4, 5
5. Right(3) 방문 → 출력: 1, 2, 4, 5, 3

결과: 1 → 2 → 4 → 5 → 3
```

**2. 중위 순회 (Inorder) ⭐**
**Left → Root → Right**

```c
void inorder(Node* root) {
    if (root == NULL) return;
    
    inorder(root->left);           // Left 순회
    printf("%d ", root->data);     // Root 방문
    inorder(root->right);          // Right 순회
}
```

**순회 순서:**
```
1. Left의 Left(4) 방문 → 출력: 4
2. Left(2) 방문 → 출력: 4, 2
3. Left의 Right(5) 방문 → 출력: 4, 2, 5
4. Root(1) 방문 → 출력: 4, 2, 5, 1
5. Right(3) 방문 → 출력: 4, 2, 5, 1, 3

결과: 4 → 2 → 5 → 1 → 3
```

**중위 순회의 특징:**
- 이진 탐색 트리(BST)에서 **오름차순 정렬** 결과

**3. 후위 순회 (Postorder) ⭐**
**Left → Right → Root**

```c
void postorder(Node* root) {
    if (root == NULL) return;
    
    postorder(root->left);         // Left 순회
    postorder(root->right);        // Right 순회
    printf("%d ", root->data);     // Root 방문
}
```

**순회 순서:**
```
1. Left의 Left(4) 방문 → 출력: 4
2. Left의 Right(5) 방문 → 출력: 4, 5
3. Left(2) 방문 → 출력: 4, 5, 2
4. Right(3) 방문 → 출력: 4, 5, 2, 3
5. Root(1) 방문 → 출력: 4, 5, 2, 3, 1

결과: 4 → 5 → 2 → 3 → 1
```

**후위 순회의 특징:**
- 자식 노드를 먼저 처리
- 디렉토리 용량 계산, 수식 트리 계산에 사용

---

### 🔍 이진 탐색 트리 (BST: Binary Search Tree) ⭐⭐⭐

### 정의
**정렬된 이진 트리**

**규칙:**
- 왼쪽 서브트리의 모든 값 < 루트 값
- 오른쪽 서브트리의 모든 값 > 루트 값

```
         50
        /  \
      30    70
     / \    / \
   20  40 60  80

왼쪽(30, 20, 40) < 50 < 오른쪽(70, 60, 80) ✅
```

**BST 탐색 (Search)**

```c
Node* search(Node* root, int key) {
    // 기저 조건: 노드가 없거나 찾음
    if (root == NULL || root->data == key) {
        return root;
    }
    
    // key가 작으면 왼쪽, 크면 오른쪽
    if (key < root->data) {
        return search(root->left, key);
    } else {
        return search(root->right, key);
    }
}
```

**탐색 예시: 60 찾기**
```
         50          50과 비교 → 60 > 50 → 오른쪽
        /  \
      30    70       70과 비교 → 60 < 70 → 왼쪽
     / \    / \
   20  40 60  80     60과 비교 → 60 = 60 → 찾음!

비교 횟수: 3회
시간복잡도: O(log N) (균형 잡힌 경우)
```

**BST 삽입 (Insert)**

```c
Node* insert(Node* root, int data) {
    // 빈 자리에 새 노드 삽입
    if (root == NULL) {
        return createNode(data);
    }
    
    // 값 비교하여 위치 결정
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}
```

**삽입 예시: 65 삽입**
```
초기:
         50
        /  \
      30    70
     / \    / \
   20  40 60  80

1. 50과 비교 → 65 > 50 → 오른쪽
2. 70과 비교 → 65 < 70 → 왼쪽
3. 60과 비교 → 65 > 60 → 오른쪽 (NULL)
4. 60의 오른쪽에 삽입

결과:
         50
        /  \
      30    70
     / \    / \
   20  40 60  80
           \
           65
```

**BST 삭제 (Delete)**

**경우의 수 3가지:**

**1. 리프 노드 삭제**
```
         50
        /  \
      30    70
     / \    / \
   20  40 60  80

20 삭제 → 그냥 제거

         50
        /  \
      30    70
       \    / \
       40 60  80
```

**2. 자식이 1개인 노드 삭제**
```
         50
        /  \
      30    70
       \    / \
       40 60  80

30 삭제 → 40을 30 자리로 이동

         50
        /  \
      40    70
           / \
         60  80
```

**3. 자식이 2개인 노드 삭제 (복잡) ⭐**
```
         50
        /  \
      30    70
     / \    / \
   20  40 60  80

50 삭제 → ?

방법 1: 왼쪽 서브트리의 최댓값(40)으로 대체
방법 2: 오른쪽 서브트리의 최솟값(60)으로 대체 (주로 사용)

결과 (방법 2):
         60
        /  \
      30    70
     / \      \
   20  40     80
```

```c
Node* deleteNode(Node* root, int key) {
    if (root == NULL) return root;
    
    // 삭제할 노드 찾기
    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        // 경우 1, 2: 자식이 0개 또는 1개
        if (root->left == NULL) {
            Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            Node* temp = root->left;
            free(root);
            return temp;
        }
        
        // 경우 3: 자식이 2개
        // 오른쪽 서브트리의 최솟값 찾기
        Node* temp = findMin(root->right);
        root->data = temp->data;  // 값 복사
        root->right = deleteNode(root->right, temp->data);  // 최솟값 노드 삭제
    }
    
    return root;
}

Node* findMin(Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}
```

---

### 📊 BST 시간복잡도

| 연산 | 평균 | 최악 |
|------|------|------|
| 탐색 | O(log N) | O(N) |
| 삽입 | O(log N) | O(N) |
| 삭제 | O(log N) | O(N) |

**최악의 경우: 편향 트리**
```
    1
     \
      2
       \
        3
         \
          4

탐색 시 4번 비교 → O(N)
```

**해결책: 균형 이진 탐색 트리**
- AVL Tree
- Red-Black Tree

---


## 🎯 AVL 트리 (균형 이진 탐색 트리)

### 정의
**스스로 균형을 잡는 이진 탐색 트리**
- 모든 노드의 왼쪽/오른쪽 서브트리 높이 차이가 최대 1

### 균형 인수 (Balance Factor)
```
BF = (왼쪽 서브트리 높이) - (오른쪽 서브트리 높이)

균형 조건: -1 ≤ BF ≤ 1
```

**예시:**
```
✅ 균형 잡힌 트리 (AVL)
         50 (BF=0)
        /  \
      30    70 (BF=0)
     / \      \
   20  40     80

❌ 불균형 트리 (AVL 아님)
         50 (BF=2)
        /
      30 (BF=1)
     /
   20

좌측으로 치우침 → 회전 필요!
```

### AVL 트리 회전

#### 1. LL 회전 (Left-Left)
```
불균형:              회전 후:
    30 (BF=2)           20
   /                   /  \
  20 (BF=1)          10    30
 /
10

오른쪽으로 회전 →
```

#### 2. RR 회전 (Right-Right)
```
불균형:              회전 후:
10 (BF=-2)              20
  \                    /  \
   20 (BF=-1)         10   30
     \
      30

왼쪽으로 회전 →
```

#### 3. LR 회전 (Left-Right)
```
불균형:              왼쪽회전:         오른쪽회전:
    30                30                20
   /                 /                 /  \
  10               20                10   30
    \             /
     20         10
```

#### 4. RL 회전 (Right-Left)
```
불균형:              오른쪽회전:       왼쪽회전:
10                    10                20
  \                     \              /  \
   30                   20           10   30
  /                       \
20                        30
```

---

## 🌳 힙 (Heap) ⭐⭐⭐

### 정의
**완전 이진 트리 + 부모와 자식 간의 대소 관계**

### 종류

#### 1. 최대 힙 (Max Heap)
**부모 노드 ≥ 자식 노드**

```
         100          ← 최댓값이 루트
        /   \
      90     80
     / \    /
   70  60  50

루트: 항상 최댓값
```

#### 2. 최소 힙 (Min Heap)
**부모 노드 ≤ 자식 노드**

```
         10           ← 최솟값이 루트
        /  \
      20    30
     / \   /
   40  50 60

루트: 항상 최솟값
```

---

## 💻 힙 구현 (배열 기반)

### 배열 인덱스 관계

```
배열: [_, 100, 90, 80, 70, 60, 50]
인덱스: 0   1   2   3   4   5   6

트리:
         100(1)
        /      \
     90(2)    80(3)
     / \      /
  70(4) 60(5) 50(6)

규칙:
- 부모 인덱스 = i / 2
- 왼쪽 자식 = i * 2
- 오른쪽 자식 = i * 2 + 1
```

**예시:**
```
노드 90 (인덱스 2):
- 부모: 2 / 2 = 1 (100)
- 왼쪽 자식: 2 * 2 = 4 (70)
- 오른쪽 자식: 2 * 2 + 1 = 5 (60)
```

---

### 최대 힙 구현 (C언어)

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int size;  // 현재 힙의 크기
} MaxHeap;

// 초기화
void init(MaxHeap* h) {
    h->size = 0;
}

// 삽입
void insert(MaxHeap* h, int value) {
    if (h->size >= MAX_SIZE - 1) {
        printf("Heap is full\n");
        return;
    }
    
    // 1. 마지막 위치에 삽입
    h->size++;
    int i = h->size;
    
    // 2. 부모와 비교하며 위로 이동 (상향식)
    while (i != 1 && value > h->data[i / 2]) {
        h->data[i] = h->data[i / 2];  // 부모를 아래로
        i = i / 2;  // 인덱스를 부모로 이동
    }
    
    h->data[i] = value;  // 최종 위치에 삽입
}

// 삭제 (루트 제거)
int delete(MaxHeap* h) {
    if (h->size == 0) {
        printf("Heap is empty\n");
        return -1;
    }
    
    int root = h->data[1];  // 최댓값 (루트)
    int last = h->data[h->size];  // 마지막 노드
    h->size--;
    
    int parent = 1;
    int child = 2;
    
    // 하향식으로 재구성
    while (child <= h->size) {
        // 더 큰 자식 선택
        if (child < h->size && h->data[child] < h->data[child + 1]) {
            child++;
        }
        
        // 마지막 노드가 자식보다 크면 종료
        if (last >= h->data[child]) {
            break;
        }
        
        // 자식을 위로 이동
        h->data[parent] = h->data[child];
        parent = child;
        child = child * 2;
    }
    
    h->data[parent] = last;  // 최종 위치에 배치
    return root;
}
```

---

### 힙 삽입 과정 예시

**90 삽입:**
```
초기:
         100
        /   \
      80     70
     / 
   60  

배열: [_, 100, 80, 70, 60]

1. 마지막에 삽입:
         100
        /   \
      80     70
     / \
   60  90

배열: [_, 100, 80, 70, 60, 90]
인덱스 5에 삽입

2. 부모(80)와 비교: 90 > 80 → 교환
         100
        /   \
      90     70
     / \
   60  80

배열: [_, 100, 90, 70, 60, 80]

3. 부모(100)와 비교: 90 < 100 → 종료

최종:
         100
        /   \
      90     70
     / \
   60  80
```

---

### 힙 삭제 과정 예시

**루트 삭제 (최댓값 제거):**
```
초기:
         100          ← 삭제
        /   \
      90     80
     / \    /
   70  60  50

배열: [_, 100, 90, 80, 70, 60, 50]

1. 루트 삭제, 마지막(50) 임시 저장:
         ?
        /  \
      90    80
     / \
   70  60

2. 자식 중 큰 값(90)과 비교: 50 < 90 → 90을 위로
         90
        /  \
      ?     80
     / \
   70  60

3. 자식 중 큰 값(70)과 비교: 50 < 70 → 70을 위로
         90
        /  \
      70    80
     / \
   ?  60

4. 50을 최종 위치에 배치:
         90
        /  \
      70    80
     / \
   50  60

배열: [_, 90, 70, 80, 50, 60]
```

---

### 📊 힙의 시간복잡도

| 연산 | 시간복잡도 | 이유 |
|------|-----------|------|
| 삽입 | O(log N) | 트리 높이만큼 이동 |
| 삭제 | O(log N) | 트리 높이만큼 이동 |
| 최댓값/최솟값 조회 | O(1) | 루트만 확인 |

---

### 🎯 힙의 활용

#### 1. 우선순위 큐 (Priority Queue)
```
일반 큐: FIFO
우선순위 큐: 우선순위가 높은 것부터 처리

예: 병원 응급실
- 위급 환자(우선순위 높음)
- 일반 환자(우선순위 낮음)

최대 힙 사용 → 우선순위가 높은 것이 루트
```

#### 2. 힙 정렬 (Heap Sort)
```
1. 배열을 힙으로 구성
2. 루트(최댓값)를 제거하며 정렬

시간복잡도: O(N log N)
```

```c
void heapSort(int arr[], int n) {
    MaxHeap h;
    init(&h);
    
    // 1. 모든 원소를 힙에 삽입
    for (int i = 0; i < n; i++) {
        insert(&h, arr[i]);
    }
    
    // 2. 힙에서 하나씩 제거 (큰 순서대로)
    for (int i = n - 1; i >= 0; i--) {
        arr[i] = delete(&h);
    }
}
```

#### 3. 최단 경로 알고리즘 (Dijkstra)
```
최소 힙을 사용하여 최단 거리 노드 선택
```

---

## 🌲 기타 트리

### 1. B-Tree
```
- 데이터베이스 인덱스에 사용
- 한 노드에 여러 키 저장
- 균형 잡힌 다진 트리
- 디스크 I/O 최소화

예: MySQL 인덱스
```

### 2. Red-Black Tree
```
- 자가 균형 이진 탐색 트리
- AVL보다 균형 조건 완화
- 삽입/삭제가 AVL보다 빠름

규칙:
1. 노드는 빨강 또는 검정
2. 루트는 검정
3. 모든 리프(NULL)는 검정
4. 빨강 노드의 자식은 검정
5. 모든 경로의 검정 노드 수 동일
```

### 3. Trie (접두사 트리)
```
- 문자열 검색에 특화
- 자동완성, 사전 검색에 사용

예: "app", "apple", "application" 저장

       root
        |
        a
        |
        p
        |
        p (end)
        |
        l
        |
        e (end)
        |
    ...ication (end)
```

---

# 실기 기출 유형

## 🎯 유형 1: 코드 결과 예측

### 스택 문제
```c
int main() {
    Stack s;
    init(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    printf("%d ", pop(&s));
    push(&s, 40);
    printf("%d ", pop(&s));
    printf("%d ", pop(&s));
    
    return 0;
}
```

**풀이:**
```
1. push(10) → [10]
2. push(20) → [10, 20]
3. push(30) → [10, 20, 30]
4. pop() → 30 출력, [10, 20]
5. push(40) → [10, 20, 40]
6. pop() → 40 출력, [10, 20]
7. pop() → 20 출력, [10]

출력: 30 40 20
```

---

### 큐 문제 (원형 큐)
```c
int main() {
    CircularQueue q;
    init(&q);  // front = 0, rear = 0
    
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    printf("%d ", dequeue(&q));
    enqueue(&q, 40);
    printf("%d ", dequeue(&q));
    
    return 0;
}
```

**풀이:**
```
초기: front=0, rear=0

1. enqueue(10): rear=1, [_, 10, _, _, _]
2. enqueue(20): rear=2, [_, 10, 20, _, _]
3. enqueue(30): rear=3, [_, 10, 20, 30, _]
4. dequeue(): front=1, 10 출력, [_, _, 20, 30, _]
5. enqueue(40): rear=4, [_, _, 20, 30, 40]
6. dequeue(): front=2, 20 출력

출력: 10 20
```

---

### 트리 순회 문제
```
트리:
         1
        / \
       2   3
      / \
     4   5

Q: 전위, 중위, 후위 순회 결과는?
```

**풀이:**
```
전위 (Root→Left→Right):
1 → 2 → 4 → 5 → 3

중위 (Left→Root→Right):
4 → 2 → 5 → 1 → 3

후위 (Left→Right→Root):
4 → 5 → 2 → 3 → 1
```

---

## 🎯 유형 2: 빈칸 채우기

### 스택 push 함수
```c
void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Overflow\n");
        return;
    }
    s->data[______(s->top)] = value;  // 빈칸
}
```

**정답:** `++`
```c
s->data[++(s->top)] = value;
```

---

### BST 탐색 함수
```c
Node* search(Node* root, int key) {
    if (root == NULL || root->data == key) {
        return root;
    }
    
    if (key < root->data) {
        return search(______, key);  // 빈칸
    } else {
        return search(root->right, key);
    }
}
```

**정답:** `root->left`

---

## 🎯 유형 3: 알고리즘 작성

### 스택으로 괄호 검사
```c
// 올바른 괄호 쌍 판단
// 입력: "((()))" → 올바름
// 입력: "(()" → 잘못됨

bool isValid(char* str) {
    Stack s;
    init(&s);
    
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '(') {
            // 여는 괄호는 push
            push(&s, str[i]);
        }
        else if (str[i] == ')') {
            // 닫는 괄호 처리
            if (isEmpty(&s)) {
                return false;  // 짝이 안 맞음
            }
            pop(&s);
        }
    }
    
    // 스택이 비어있어야 올바름
    return isEmpty(&s);
}
```

---

### BST 삽입 함수
```c
Node* insert(Node* root, int data) {
    // 1. 빈 자리 찾음 → 새 노드 생성
    if (root == NULL) {
        return createNode(data);
    }
    
    // 2. 값 비교
    if (data < root->data) {
        // 왼쪽 서브트리에 삽입
        root->left = insert(root->left, data);
    }
    else if (data > root->data) {
        // 오른쪽 서브트리에 삽입
        root->right = insert(root->right, data);
    }
    // data == root->data인 경우 중복이므로 삽입 안 함
    
    return root;
}
```

---

### 힙 삽입 함수
```c
void insert(MaxHeap* h, int value) {
    if (h->size >= MAX_SIZE - 1) {
        return;
    }
    
    h->size++;
    int i = h->size;
    
    // 상향식 재구성
    while (i != 1 && value > h->data[i / 2]) {
        h->data[i] = h->data[i / 2];  // 부모를 아래로
        i = i / 2;  // 위로 이동
    }
    
    h->data[i] = value;
}
```

---

## 🎯 유형 4: 개념 서술

### Q1: 스택과 큐의 차이점을 설명하시오.
```
답:
- 스택은 LIFO(Last In First Out) 구조로, 
  마지막에 삽입된 데이터가 가장 먼저 삭제됩니다.
  
- 큐는 FIFO(First In First Out) 구조로,
  먼저 삽입된 데이터가 먼저 삭제됩니다.

예시:
- 스택: 함수 호출, 괄호 검사, DFS
- 큐: 프로세스 스케줄링, BFS, 버퍼
```

### Q2: 이진 탐색 트리의 중위 순회 특징은?
```
답:
이진 탐색 트리를 중위 순회하면
오름차순으로 정렬된 결과를 얻을 수 있습니다.

이유:
중위 순회는 Left → Root → Right 순서이고,
BST는 왼쪽 < 루트 < 오른쪽이므로
작은 값부터 큰 값 순서로 방문하게 됩니다.
```

### Q3: 완전 이진 트리란?
```
답:
마지막 레벨을 제외한 모든 레벨이 완전히 채워져 있고,
마지막 레벨은 왼쪽부터 차례대로 채워진 이진 트리입니다.

특징:
- 배열로 효율적으로 구현 가능
- 힙 자료구조의 기본 형태
- 부모-자식 인덱스 관계가 명확함
  (부모: i/2, 왼쪽자식: 2i, 오른쪽자식: 2i+1)
```

### Q4: 힙의 시간복잡도와 그 이유는?
```
답:
삽입: O(log N)
삭제: O(log N)
최댓값 조회: O(1)

이유:
- 삽입/삭제 시 트리의 높이만큼만 이동하므로 O(log N)
  (완전 이진 트리이므로 높이는 log N)
- 최댓값은 항상 루트에 있으므로 O(1)
```

---

## 📝 핵심 암기 사항

### 스택
```
✅ LIFO 구조
✅ push, pop, peek 연산
✅ 시간복잡도: O(1)
✅ 활용: 함수 호출, 괄호 검사, DFS, 후위 표기법
✅ Overflow: 스택이 가득 참
✅ Underflow: 스택이 비어있는데 pop
```

### 큐
```
✅ FIFO 구조
✅ enqueue, dequeue, peek 연산
✅ 원형 큐: 공간 재사용 가능, (rear+1) % MAX_SIZE
✅ 시간복잡도: O(1)
✅ 활용: 프로세스 스케줄링, BFS, 버퍼
```

### 이진 트리
```
✅ 최대 자식 수: 2개
✅ 전위: Root → Left → Right
✅ 중위: Left → Root → Right (BST에서 오름차순)
✅ 후위: Left → Right → Root
✅ 포화: 모든 레벨이 꽉 참
✅ 완전: 마지막 레벨 제외 모두 채워짐, 왼쪽부터
```

### BST (이진 탐색 트리)
```
✅ 왼쪽 < 루트 < 오른쪽
✅ 중위 순회 → 오름차순 정렬
✅ 탐색/삽입/삭제: O(log N) 평균, O(N) 최악
✅ 최악의 경우: 편향 트리 (한쪽으로 치우침)
```

### 힙
```
✅ 완전 이진 트리
✅ 최대 힙: 부모 ≥ 자식
✅ 최소 힙: 부모 ≤ 자식
✅ 배열 구현: 부모 i/2, 자식 2i, 2i+1
✅ 삽입/삭제: O(log N)
✅ 활용: 우선순위 큐, 힙 정렬
```

---

## 🎓 실기 시험 팁

### 1. 코드 추적
```
스택/큐 문제는 손으로 그림 그리면서 추적!

예:
push(10) → [10]
push(20) → [10, 20]
pop() → [10], 반환값: 20
```

### 2. 트리 그리기
```
순회 문제는 트리를 직접 그려서 확인!

전위: 1 2 4 5 3
→ 1부터 시작, 왼쪽 끝까지, 오른쪽
```

### 3. 인덱스 계산
```
배열 기반 힙 문제:
- 부모: i / 2
- 왼쪽 자식: i * 2
- 오른쪽 자식: i * 2 + 1

인덱스 1부터 시작!
```

### 4. 시간복잡도 암기
```
배열/링크드리스트: O(N)
스택/큐: O(1)
BST/힙: O(log N) 평균
정렬: O(N log N) 평균
```

---

**chek list:** 
- [ ] 각 자료구조를 직접 손으로 그려보기
- [ ] 코드를 보면서 동작 과정을 추적하기
- [ ] 기출문제를 반복해서 풀어보기
- [ ] 용어와 시간복잡도를 정확히 암기하기
