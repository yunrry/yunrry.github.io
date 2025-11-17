
# 📌 배열 Array

**같은 타입의 데이터를 연속된 메모리 공간에 저장하는 자료구조**
- 인덱스로 빠른 접근 가능
- 고정된 크기

```
배열: int arr[5] = {10, 20, 30, 40, 50};

메모리:
주소    | 1000 | 1004 | 1008 | 1012 | 1016 |
--------|------|------|------|------|------|
인덱스  |  0   |  1   |  2   |  3   |  4   |
값      |  10  |  20  |  30  |  40  |  50  |

연속된 메모리 공간에 저장 ✔
```

---

## 🔧 배열의 기본 연산

### 1. 선언 및 초기화

```c
// 선언
int arr[5];

// 선언과 동시에 초기화
int arr[5] = {10, 20, 30, 40, 50};

// 부분 초기화 (나머지는 0)
int arr[5] = {10, 20};  // {10, 20, 0, 0, 0}

// 모두 0으로 초기화
int arr[5] = {0};

// 크기 생략 (컴파일러가 자동 계산)
int arr[] = {10, 20, 30};  // 크기: 3
```

### 2. 접근 (Access)

```c
int arr[5] = {10, 20, 30, 40, 50};

// 읽기
int value = arr[2];  // 30

// 쓰기
arr[2] = 100;  // {10, 20, 100, 40, 50}

// 시간복잡도: O(1) ✔ (인덱스로 직접 접근)
```

**인덱스 계산 공식:**
```
주소 = 시작주소 + (인덱스 × 데이터크기)

arr[2]의 주소 = 1000 + (2 × 4) = 1008
(int는 4바이트)
```

### 3. 탐색 (Search)

```c
// 선형 탐색 (Linear Search)
int search(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            return i;  // 찾은 인덱스 반환
        }
    }
    return -1;  // 못 찾음
}

// 시간복잡도: O(N)
```

**예시:**
```
arr[] = {10, 20, 30, 40, 50}
key = 30 찾기

비교 1: arr[0] = 10 ≠ 30
비교 2: arr[1] = 20 ≠ 30
비교 3: arr[2] = 30 = 30 ✔ 찾음!

최악의 경우: N번 비교 (맨 끝 또는 없음)
```

### 4. 삽입 (Insert)

#### 맨 뒤 삽입 (가장 빠름)
```c
int arr[10] = {10, 20, 30, 40, 50};
int size = 5;

// 맨 뒤에 60 삽입
arr[size] = 60;
size++;

// 결과: {10, 20, 30, 40, 50, 60}
// 시간복잡도: O(1) ✔
```

#### 중간 삽입 (느림)
```c
void insertAt(int arr[], int *size, int index, int value) {
    // 뒤에서부터 한 칸씩 이동
    for (int i = *size; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    
    arr[index] = value;
    (*size)++;
}

// 시간복잡도: O(N) ✘
```

**예시: 인덱스 2에 25 삽입**
```
초기: {10, 20, 30, 40, 50}
       0   1   2   3   4

1단계: 뒤에서부터 이동
{10, 20, 30, 40, 50, 50}  // 50 복사
{10, 20, 30, 40, 40, 50}  // 40 복사
{10, 20, 30, 30, 40, 50}  // 30 복사

2단계: 해당 위치에 삽입
{10, 20, 25, 30, 40, 50}
       0   1   2   3   4   5

이동 횟수: 3번 (size - index)
```

### 5. 삭제 (Delete)

#### 맨 뒤 삭제 (가장 빠름)
```c
int arr[10] = {10, 20, 30, 40, 50};
int size = 5;

// 맨 뒤 삭제
size--;

// 결과: {10, 20, 30, 40} (50은 무시됨)
// 시간복잡도: O(1) ✔
```

#### 중간 삭제 (느림)
```c
void deleteAt(int arr[], int *size, int index) {
    // 앞으로 한 칸씩 이동
    for (int i = index; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    
    (*size)--;
}

// 시간복잡도: O(N) ✘
```

**예시: 인덱스 2 삭제**
```
초기: {10, 20, 30, 40, 50}
       0   1   2   3   4

1단계: 앞으로 이동
{10, 20, 40, 40, 50}  // arr[2] = arr[3]
{10, 20, 40, 50, 50}  // arr[3] = arr[4]

2단계: 크기 감소
{10, 20, 40, 50}
 0   1   2   3

이동 횟수: 2번 (size - index - 1)
```

---

## 📊 배열의 장단점

### 장점 ✔

1. **빠른 접근 (Random Access)**
```c
arr[100] = 10;  // O(1) - 인덱스로 바로 접근
```

2. **구현이 간단**
```c
int arr[100];  // 선언만 하면 됨
```

3. **메모리 효율적**
```
데이터만 저장 (포인터 불필요)
int 배열: 4바이트 × N개 = 4N 바이트
```

4. **캐시 친화적 (Cache-Friendly)**
```
연속된 메모리 → CPU 캐시 효율 높음
→ 성능 향상
```

### 단점 ✘

1. **고정 크기**
```c
int arr[5];  // 크기 5로 고정
// 6개를 저장하고 싶으면? → 새 배열 생성 필요
```

2. **삽입/삭제가 느림**
```c
// 중간에 삽입/삭제 시 O(N)
// 모든 원소를 이동해야 함
```

3. **메모리 낭비**
```c
int arr[1000];  // 1000개 선언
// 실제 10개만 사용 → 990개 낭비
```

4. **크기 변경 불가**
```c
int arr[5];
// 런타임에 크기 변경 불가능
// (동적 배열 제외)
```

---

## 💻 배열 활용 예제

### 1. 최댓값/최솟값 찾기

```c
int findMax(int arr[], int size) {
    int max = arr[0];
    
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    return max;
}

int findMin(int arr[], int size) {
    int min = arr[0];
    
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    
    return min;
}

// 시간복잡도: O(N)
```

### 2. 배열 역순 정렬

```c
void reverse(int arr[], int size) {
    int temp;
    
    for (int i = 0; i < size / 2; i++) {
        // 양 끝을 교환
        temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}

// 시간복잡도: O(N)
```

**예시:**
```
초기: {10, 20, 30, 40, 50}
       0   1   2   3   4

교환 1: arr[0] ↔ arr[4]
{50, 20, 30, 40, 10}

교환 2: arr[1] ↔ arr[3]
{50, 40, 30, 20, 10}

중간(arr[2])은 그대로
```

### 3. 중복 제거

```c
int removeDuplicates(int arr[], int size) {
    if (size == 0) return 0;
    
    int newSize = 1;  // 첫 원소는 항상 포함
    
    for (int i = 1; i < size; i++) {
        int isDuplicate = 0;
        
        // 이전 원소들과 비교
        for (int j = 0; j < newSize; j++) {
            if (arr[i] == arr[j]) {
                isDuplicate = 1;
                break;
            }
        }
        
        // 중복이 아니면 추가
        if (!isDuplicate) {
            arr[newSize] = arr[i];
            newSize++;
        }
    }
    
    return newSize;
}

// 시간복잡도: O(N²)
```

**예시:**
```
초기: {10, 20, 10, 30, 20, 40}

처리:
10 → 추가 (첫 원소)
20 → 추가 (중복 아님)
10 → 제외 (중복)
30 → 추가 (중복 아님)
20 → 제외 (중복)
40 → 추가 (중복 아님)

결과: {10, 20, 30, 40}
```

---

## 🎯 2차원 배열

### 선언 및 초기화

```c
// 선언
int arr[3][4];  // 3행 4열

// 초기화
int arr[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// 일괄 초기화
int arr[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
```

### 메모리 배치 (행 우선 순서)

```
arr[3][4]:

논리적 구조:
     col0  col1  col2  col3
row0 [1]   [2]   [3]   [4]
row1 [5]   [6]   [7]   [8]
row2 [9]   [10]  [11]  [12]

실제 메모리 (연속 배치):
[1][2][3][4][5][6][7][8][9][10][11][12]
```

### 2차원 배열 순회

```c
int arr[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// 행 우선 순회
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        printf("%d ", arr[i][j]);
    }
    printf("\n");
}

// 출력:
// 1 2 3 4
// 5 6 7 8
// 9 10 11 12
```

### 주소 계산

```
arr[i][j]의 주소 = 시작주소 + ((i × 열개수) + j) × 데이터크기

예: arr[1][2]의 주소
= 1000 + ((1 × 4) + 2) × 4
= 1000 + 6 × 4
= 1000 + 24
= 1024
```

---


# 📌 링크드 리스트 LinkedList

**노드들이 포인터로 연결된 자료구조**
- 동적 크기 조절 가능
- 비연속적 메모리 사용

```
노드 구조:
┌──────┬──────┐
│ data │ next │  → next: 다음 노드의 주소
└──────┴──────┘

링크드 리스트:
Head → [10|●] → [20|●] → [30|●] → [40|NULL]
       1000     2000     3000     4000

메모리는 비연속적! ✔
```

---

## 💻 링크드 리스트 구현

### 노드 구조체

```c
typedef struct Node {
    int data;           // 데이터
    struct Node* next;  // 다음 노드 포인터
} Node;
```

### 1. 노드 생성

```c
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    
    newNode->data = data;
    newNode->next = NULL;
    
    return newNode;
}
```

### 2. 삽입 (Insert)

#### 맨 앞 삽입 (Head에 삽입)

```c
void insertFront(Node** head, int data) {
    Node* newNode = createNode(data);
    
    newNode->next = *head;  // 새 노드가 현재 head를 가리킴
    *head = newNode;         // head를 새 노드로 변경
}

// 시간복잡도: O(1) ✔
```

**예시:**
```
초기: Head → [20|●] → [30|NULL]

10 삽입:

1단계: 새 노드 생성
[10|NULL]

2단계: newNode->next = head
[10|●] → [20|●] → [30|NULL]

3단계: head = newNode
Head → [10|●] → [20|●] → [30|NULL]
```

#### 맨 뒤 삽입 (Tail에 삽입)

```c
void insertBack(Node** head, int data) {
    Node* newNode = createNode(data);
    
    // 리스트가 비어있으면
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    // 마지막 노드 찾기
    Node* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = newNode;
}

// 시간복잡도: O(N) ✘ (마지막까지 순회)
```

**예시:**
```
초기: Head → [10|●] → [20|NULL]

30 삽입:

1단계: 마지막 노드 찾기
Head → [10|●] → [20|NULL]
                  ↑
              current

2단계: current->next = newNode
Head → [10|●] → [20|●] → [30|NULL]
```

#### 중간 삽입 (특정 위치)

```c
void insertAt(Node** head, int position, int data) {
    Node* newNode = createNode(data);
    
    // 맨 앞 삽입
    if (position == 0) {
        newNode->next = *head;
        *head = newNode;
        return;
    }
    
    // 이전 노드 찾기
    Node* current = *head;
    for (int i = 0; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Invalid position\n");
        free(newNode);
        return;
    }
    
    newNode->next = current->next;
    current->next = newNode;
}

// 시간복잡도: O(N)
```

**예시: 인덱스 2에 25 삽입**
```
초기: Head → [10|●] → [20|●] → [30|NULL]
              0         1         2

1단계: position-1 (1번) 노드 찾기
Head → [10|●] → [20|●] → [30|NULL]
                  ↑
              current

2단계: newNode->next = current->next
       current->next = newNode

결과: Head → [10|●] → [20|●] → [25|●] → [30|NULL]
              0         1         2         3
```

### 3. 삭제 (Delete)

#### 맨 앞 삭제

```c
void deleteFront(Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
}

// 시간복잡도: O(1) ✔
```

**예시:**
```
초기: Head → [10|●] → [20|●] → [30|NULL]

1단계: temp = head
temp → [10|●] → [20|●] → [30|NULL]
  ↓
Head

2단계: head = head->next
Head → [20|●] → [30|NULL]
temp → [10|●]

3단계: free(temp)
Head → [20|●] → [30|NULL]
```

#### 맨 뒤 삭제

```c
void deleteBack(Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    // 노드가 1개만 있을 때
    if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }
    
    // 마지막 이전 노드 찾기
    Node* current = *head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    
    free(current->next);
    current->next = NULL;
}

// 시간복잡도: O(N) ✘
```

#### 특정 값 삭제

```c
void deleteValue(Node** head, int value) {
    if (*head == NULL) {
        return;
    }
    
    // 첫 노드가 삭제 대상
    if ((*head)->data == value) {
        Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    
    // 삭제할 노드의 이전 노드 찾기
    Node* current = *head;
    while (current->next != NULL && current->next->data != value) {
        current = current->next;
    }
    
    // 못 찾음
    if (current->next == NULL) {
        printf("Value not found\n");
        return;
    }
    
    // 삭제
    Node* temp = current->next;
    current->next = current->next->next;
    free(temp);
}
```

**예시: 20 삭제**
```
초기: Head → [10|●] → [20|●] → [30|NULL]

1단계: 20의 이전 노드(10) 찾기
Head → [10|●] → [20|●] → [30|NULL]
        ↑        ↑
    current    temp

2단계: current->next = temp->next
Head → [10|●] ─────┐
                    ↓
       [20|●]   [30|NULL]
        temp

3단계: free(temp)
Head → [10|●] → [30|NULL]
```

### 4. 탐색 (Search)

```c
Node* search(Node* head, int key) {
    Node* current = head;
    
    while (current != NULL) {
        if (current->data == key) {
            return current;  // 찾음
        }
        current = current->next;
    }
    
    return NULL;  // 못 찾음
}

// 시간복잡도: O(N)
```

### 5. 출력 (Display)

```c
void display(Node* head) {
    Node* current = head;
    
    printf("List: ");
    while (current != NULL) {
        printf("%d → ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

### 6. 전체 삭제 (메모리 해제)

```c
void deleteAll(Node** head) {
    Node* current = *head;
    Node* next;
    
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    
    *head = NULL;
}
```

---

## 🔗 링크드 리스트의 종류

### 1. 단일 링크드 리스트 (Singly Linked List)

위에서 설명한 기본 형태

```
Head → [10|●] → [20|●] → [30|NULL]

특징:
- 한 방향으로만 이동 가능
- 이전 노드로 돌아갈 수 없음
```

### 2. 이중 링크드 리스트 (Doubly Linked List)

양방향 포인터

```c
typedef struct DNode {
    int data;
    struct DNode* prev;  // 이전 노드
    struct DNode* next;  // 다음 노드
} DNode;
```

```
NULL ← [10|●] ⇄ [20|●] ⇄ [30|●] → NULL
       prev  next
```

**장점:**
- 양방향 탐색 가능
- 이전 노드 삭제 쉬움

**단점:**
- 메모리 사용량 증가 (포인터 2개)
- 구현 복잡

### 3. 원형 링크드 리스트 (Circular Linked List)

마지막 노드가 첫 노드를 가리킴

```
     ┌─────────────────┐
     ↓                 │
Head → [10|●] → [20|●] → [30|●]
```

**장점:**
- 모든 노드 접근 가능 (시작점 무관)
- 큐 구현에 유용

**활용:**
- 라운드 로빈 스케줄링
- 멀티플레이어 게임 (턴제)

---

## 📊 배열 vs 링크드 리스트

### 비교표

| 구분 | 배열 | 링크드 리스트 |
|------|------|--------------|
| **메모리** | 연속적 | 비연속적 |
| **크기** | 고정 | 동적 |
| **접근** | O(1) ✔ | O(N) ✘ |
| **탐색** | O(N) | O(N) |
| **맨앞 삽입** | O(N) ✘ | O(1) ✔ |
| **맨뒤 삽입** | O(1) ✔ | O(N) ✘ |
| **중간 삽입** | O(N) | O(N) |
| **맨앞 삭제** | O(N) ✘ | O(1) ✔ |
| **맨뒤 삭제** | O(1) ✔ | O(N) ✘ |
| **중간 삭제** | O(N) | O(N) |
| **메모리 효율** | 높음 ✔ | 낮음 (포인터) ✘ |
| **캐시 효율** | 높음 ✔ | 낮음 ✘ |

---

### 상세 비교

#### 1. 접근 속도

```c
// 배열: O(1)
int value = arr[100];  // 바로 접근

// 링크드 리스트: O(N)
Node* current = head;
for (int i = 0; i < 100; i++) {
    current = current->next;  // 100번 이동
}
int value = current->data;
```

#### 2. 메모리 사용

```
배열 (10개 int):
[10][20][30][40][50]...[100]
메모리: 4바이트 × 10 = 40바이트

링크드 리스트 (10개 int):
[10|●] → [20|●] → ... → [100|NULL]
메모리: (4바이트 + 8바이트) × 10 = 120바이트
(64비트 시스템에서 포인터 8바이트)

배열이 3배 효율적! ✔
```

#### 3. 삽입/삭제 비교

**배열의 중간 삽입:**
```
{10, 20, 30, 40, 50}에 25 삽입 (인덱스 2)

이동 필요: 30, 40, 50 → 3개
시간: O(N)
```

**링크드 리스트의 중간 삽입:**
```
[10] → [20] → [30] → [40] → [50]에 25 삽입

찾기: 20까지 이동 → O(N)
삽입: 포인터 2개 변경 → O(1)
전체: O(N)
```

**결론: 삽입/삭제도 비슷하지만, 맨 앞 작업은 링크드 리스트가 유리**

#### 4. 캐시 효율

```
배열:
[10][20][30][40][50]  ← 연속 메모리
캐시에 한 번에 로드 → 빠름 ✔

링크드 리스트:
[10] → [20] → [30] → [40] → [50]
각 노드가 다른 위치 → 캐시 미스 → 느림 ✘
```

---

## 🎯 언제 무엇을 사용할까?

### 배열을 사용해야 할 때 ✔

```
1. 인덱스 접근이 빈번할 때
   예: arr[i], 랜덤 액세스

2. 크기가 고정되어 있을 때
   예: 학생 100명의 성적

3. 메모리가 제한적일 때
   예: 임베디드 시스템

4. 순차 접근이 많을 때
   예: for문으로 전체 순회
```

### 링크드 리스트를 사용해야 할 때 ✔

```
1. 크기가 동적으로 변할 때
   예: 사용자 입력에 따라 크기 변화

2. 맨 앞 삽입/삭제가 빈번할 때
   예: 스택, 큐 구현

3. 중간 삽입/삭제가 빈번하고
   해당 위치를 이미 알고 있을 때
   예: 포인터로 위치를 저장해둔 경우

4. 메모리 단편화를 피하고 싶을 때
   예: 큰 연속 메모리 확보 어려움
```

---

# 실기 기출 유형

## 🎯 유형 1: 코드 결과 예측

### 배열 문제

```c
int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int i;
    
    for (i = 0; i < 5; i++) {
        arr[i] = arr[i] + 5;
    }
    
    printf("%d %d", arr[2], arr[4]);
    
    return 0;
}
```

**풀이:**
```
초기: arr[] = {10, 20, 30, 40, 50}

반복문 실행:
i=0: arr[0] = 10 + 5 = 15
i=1: arr[1] = 20 + 5 = 25
i=2: arr[2] = 30 + 5 = 35
i=3: arr[3] = 40 + 5 = 45
i=4: arr[4] = 50 + 5 = 55

최종: arr[] = {15, 25, 35, 45, 55}

출력: arr[2]=35, arr[4]=55
답: 35 55
```

---

### 링크드 리스트 문제

```c
typedef struct Node {
    int data;
    struct Node* next;
} Node;

int main() {
    Node* head = NULL;
    
    // 노드 생성 및 연결
    Node* n1 = createNode(10);
    Node* n2 = createNode(20);
    Node* n3 = createNode(30);
    
    head = n1;
    n1->next = n2;
    n2->next = n3;
    n3->next = NULL;
    
    // 맨 앞에 5 삽입
    Node* newNode = createNode(5);
    newNode->next = head;
    head = newNode;
    
    // 출력
    printf("%d %d", head->data, head->next->next->data);
    
    return 0;
}
```

**풀이:**
```
1. 초기 리스트 생성:
Head → [10] → [20] → [30] → NULL

2. 맨 앞에 5 삽입:
newNode = [5]
newNode->next = head  → [5] → [10] → [20] → [30] → NULL
head = newNode

최종: Head → [5] → [10] → [20] → [30] → NULL

출력:
head->data = 5
head->next = [10]
head->next->next = [20]
head->next->next->data = 20

답: 5 20
```

---

## 🎯 유형 2: 빈칸 채우기

### 배열 문제

```c
// 배열에서 최댓값 찾기
int findMax(int arr[], int size) {
    int max = arr[0];
    
    for (int i = 1; i < size; i++) {
        if (arr[i] ______ max) {  // 빈칸 1
            max = ______;          // 빈칸 2
        }
    }
    
    return max;
}
```

**정답:**
```c
if (arr[i] > max) {      // 빈칸 1: >
    max = arr[i];         // 빈칸 2: arr[i]
}
```

---

### 링크드 리스트 문제

```c
// 맨 뒤에 노드 삽입
void insertBack(Node** head, int data) {
    Node* newNode = createNode(data);
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node* current = *head;
    while (current->______ != NULL) {  // 빈칸 1
        current = current->next;
    }
    
    current->next = ______;             // 빈칸 2
}
```

**정답:**
```c
while (current->next != NULL) {  // 빈칸 1: next
    current = current->next;
}

current->next = newNode;          // 빈칸 2: newNode
```

---

## 🎯 유형 3: 알고리즘 작성

### 배열 문제: 배열 회전 (왼쪽으로 1칸)

```c
// 배열을 왼쪽으로 1칸 회전
// {10, 20, 30, 40} → {20, 30, 40, 10}

void rotateLeft(int arr[], int size) {
    int temp = arr[0];  // 첫 원소 저장
    
    // 왼쪽으로 이동
    for (int i = 0; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    
    arr[size - 1] = temp;  // 마지막에 저장
}

// 시간복잡도: O(N)
```

**동작 과정:**
```
초기: {10, 20, 30, 40}

temp = 10

이동:
arr[0] = arr[1] → {20, 20, 30, 40}
arr[1] = arr[2] → {20, 30, 30, 40}
arr[2] = arr[3] → {20, 30, 40, 40}

마지막에 temp 배치:
arr[3] = temp → {20, 30, 40, 10}
```

---

### 배열 문제: 두 배열 합치기

```c
// arr1과 arr2를 result에 합치기
void mergeArrays(int arr1[], int size1, 
                 int arr2[], int size2, 
                 int result[]) {
    int i, j;
    
    // arr1 복사
    for (i = 0; i < size1; i++) {
        result[i] = arr1[i];
    }
    
    // arr2 복사
    for (j = 0; j < size2; j++) {
        result[i + j] = arr2[j];
    }
}

// 시간복잡도: O(N + M)
```

**예시:**
```
arr1[] = {10, 20, 30}  (size1 = 3)
arr2[] = {40, 50}      (size2 = 2)

결과: result[] = {10, 20, 30, 40, 50}
```

---

### 링크드 리스트 문제: 리스트 역순

```c
// 링크드 리스트를 역순으로 변경
Node* reverse(Node* head) {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;    // 다음 노드 저장
        current->next = prev;     // 방향 전환
        prev = current;           // prev 이동
        current = next;           // current 이동
    }
    
    return prev;  // 새로운 head
}

// 시간복잡도: O(N)
```

**동작 과정:**
```
초기: [10] → [20] → [30] → NULL

1단계: current = [10]
next = [20]
[10] → NULL (방향 전환)
prev = [10], current = [20]

2단계: current = [20]
next = [30]
[20] → [10] → NULL
prev = [20], current = [30]

3단계: current = [30]
next = NULL
[30] → [20] → [10] → NULL
prev = [30], current = NULL

최종: [30] → [20] → [10] → NULL
```

---

### 링크드 리스트 문제: 중간 노드 찾기

```c
// 리스트의 중간 노드 찾기 (Fast & Slow Pointer)
Node* findMiddle(Node* head) {
    if (head == NULL) return NULL;
    
    Node* slow = head;
    Node* fast = head;
    
    // fast는 2칸, slow는 1칸씩 이동
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow;  // slow가 중간 지점
}

// 시간복잡도: O(N)
```

**동작 과정:**
```
리스트: [10] → [20] → [30] → [40] → [50] → NULL

초기:
slow = [10], fast = [10]

1단계:
slow = [20], fast = [30]

2단계:
slow = [30], fast = [50]

3단계:
fast->next = NULL → 종료
slow = [30] ✔ (중간 노드)
```

---

### 링크드 리스트 문제: 순환 감지

```c
// 리스트에 순환(Cycle)이 있는지 확인
bool hasCycle(Node* head) {
    if (head == NULL) return false;
    
    Node* slow = head;
    Node* fast = head;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        
        // 만나면 순환 있음
        if (slow == fast) {
            return true;
        }
    }
    
    return false;  // 순환 없음
}

// 시간복잡도: O(N)
```

**동작 원리:**
```
순환이 있는 경우:
[10] → [20] → [30] → [40]
              ↑       ↓
              └───────┘

slow와 fast가 언젠가 만남 ✔

순환이 없는 경우:
[10] → [20] → [30] → [40] → NULL

fast가 NULL에 도달 → 순환 없음 ✔
```

---

## 🎯 유형 4: 개념 서술

### Q1: 배열과 링크드 리스트의 차이점을 3가지 서술하시오.

**답:**
```
1. 메모리 구조:
   - 배열: 연속된 메모리 공간에 저장
   - 링크드 리스트: 비연속적 메모리, 포인터로 연결

2. 접근 속도:
   - 배열: 인덱스로 직접 접근 O(1)
   - 링크드 리스트: 순차 접근 O(N)

3. 크기 변경:
   - 배열: 고정 크기, 변경 불가
   - 링크드 리스트: 동적 크기, 자유롭게 변경 가능
```

---

### Q2: 배열에서 중간 삽입의 시간복잡도가 O(N)인 이유를 설명하시오.

**답:**
```
중간에 데이터를 삽입하려면 해당 위치 이후의
모든 원소를 한 칸씩 뒤로 이동해야 합니다.

예: {10, 20, 30, 40, 50}의 인덱스 2에 25 삽입

1. 50을 인덱스 5로 이동
2. 40을 인덱스 4로 이동
3. 30을 인덱스 3으로 이동
4. 인덱스 2에 25 삽입

이동 횟수는 (배열 크기 - 삽입 위치)이므로
최악의 경우(맨 앞 삽입) N번 이동 → O(N)
```

---

### Q3: 링크드 리스트에서 맨 뒤 삽입이 O(N)인데, 이를 O(1)로 개선하는 방법은?

**답:**
```
Tail 포인터를 추가로 유지합니다.

구조:
typedef struct List {
    Node* head;
    Node* tail;  // 마지막 노드를 가리킴
} List;

삽입 시:
1. newNode 생성
2. tail->next = newNode
3. tail = newNode

Tail 포인터로 마지막 노드를 바로 접근하므로
순회 없이 O(1)에 삽입 가능합니다.
```

---

### Q4: 이중 링크드 리스트의 장점과 단점을 설명하시오.

**답:**
```
장점:
1. 양방향 탐색 가능 (prev 포인터)
2. 특정 노드 삭제 시 이전 노드 찾기 쉬움
3. 역순 순회 가능

단점:
1. 메모리 사용량 증가 (포인터 2개)
2. 삽입/삭제 시 포인터 관리 복잡 (prev, next 모두 처리)
3. 구현 난이도 증가

활용:
- 브라우저의 앞/뒤 이동
- 텍스트 에디터의 Undo/Redo
- LRU 캐시 구현
```

---

## 💡 실전 응용 문제

### 문제 1: 배열에서 두 수의 합

```c
// 배열에서 합이 target인 두 수의 인덱스 찾기
// arr[] = {2, 7, 11, 15}, target = 9
// 답: [0, 1] (2 + 7 = 9)

void twoSum(int arr[], int size, int target) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[i] + arr[j] == target) {
                printf("[%d, %d]\n", i, j);
                return;
            }
        }
    }
    printf("Not found\n");
}

// 시간복잡도: O(N²)
```

---

### 문제 2: 배열 회전 (오른쪽으로 k칸)

```c
// 배열을 오른쪽으로 k칸 회전
// arr[] = {1, 2, 3, 4, 5}, k = 2
// 결과: {4, 5, 1, 2, 3}

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotateRight(int arr[], int size, int k) {
    k = k % size;  // k가 size보다 클 경우 대비
    
    // 1. 전체 역순
    reverse(arr, 0, size - 1);
    
    // 2. 앞 k개 역순
    reverse(arr, 0, k - 1);
    
    // 3. 나머지 역순
    reverse(arr, k, size - 1);
}

// 시간복잡도: O(N)
```

**동작 과정:**
```
초기: {1, 2, 3, 4, 5}, k = 2

1. 전체 역순:
{5, 4, 3, 2, 1}

2. 앞 2개 역순:
{4, 5, 3, 2, 1}

3. 나머지 역순:
{4, 5, 1, 2, 3} ✔
```

---

### 문제 3: 링크드 리스트 병합 (정렬된 두 리스트)

```c
// 정렬된 두 리스트를 병합하여 정렬된 하나의 리스트로
// list1: [1] → [3] → [5]
// list2: [2] → [4] → [6]
// 결과: [1] → [2] → [3] → [4] → [5] → [6]

Node* mergeSortedLists(Node* l1, Node* l2) {
    // 더미 노드 생성
    Node dummy;
    Node* tail = &dummy;
    dummy.next = NULL;
    
    while (l1 != NULL && l2 != NULL) {
        if (l1->data <= l2->data) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    
    // 남은 노드 연결
    if (l1 != NULL) {
        tail->next = l1;
    } else {
        tail->next = l2;
    }
    
    return dummy.next;
}

// 시간복잡도: O(N + M)
```

---

### 문제 4: 링크드 리스트에서 N번째 뒤 노드 삭제

```c
// 뒤에서 N번째 노드 삭제
// 리스트: [1] → [2] → [3] → [4] → [5], N = 2
// 결과: [1] → [2] → [3] → [5] (4 삭제)

Node* removeNthFromEnd(Node* head, int n) {
    Node dummy;
    dummy.next = head;
    
    Node* first = &dummy;
    Node* second = &dummy;
    
    // first를 n+1칸 앞서게 이동
    for (int i = 0; i <= n; i++) {
        if (first == NULL) return head;
        first = first->next;
    }
    
    // 둘 다 이동 (간격 유지)
    while (first != NULL) {
        first = first->next;
        second = second->next;
    }
    
    // 삭제
    Node* temp = second->next;
    second->next = second->next->next;
    free(temp);
    
    return dummy.next;
}

// 시간복잡도: O(N)
```

**동작 과정:**
```
리스트: [1] → [2] → [3] → [4] → [5], N = 2

1. first를 n+1=3칸 이동:
first → [4], second → [dummy]

2. 둘 다 끝까지 이동 (간격 유지):
first → NULL, second → [3]

3. second->next (4) 삭제:
[1] → [2] → [3] → [5]
```

---

## 📝 핵심 암기 사항

### 배열 (Array)

```
✔ 연속된 메모리
✔ 고정 크기
✔ 인덱스 접근: O(1)
✔ 탐색: O(N)
✔ 맨뒤 삽입/삭제: O(1)
✔ 중간 삽입/삭제: O(N)
✔ 메모리 효율적
✔ 캐시 친화적

주소 계산: 시작주소 + (인덱스 × 데이터크기)
```

### 링크드 리스트 (Linked List)

```
✔ 비연속적 메모리
✔ 동적 크기
✔ 인덱스 접근: O(N)
✔ 탐색: O(N)
✔ 맨앞 삽입/삭제: O(1)
✔ 맨뒤 삽입/삭제: O(N) (Tail 없을 때)
✔ 중간 삽입/삭제: O(N)
✔ 포인터 메모리 오버헤드

노드 구조: data + next 포인터
```

### 시간복잡도 비교

| 연산 | 배열 | 링크드 리스트 |
|------|------|--------------|
| 접근 | **O(1)** | O(N) |
| 탐색 | O(N) | O(N) |
| 맨앞 삽입 | O(N) | **O(1)** |
| 맨뒤 삽입 | **O(1)** | O(N) |
| 중간 삽입 | O(N) | O(N) |
| 맨앞 삭제 | O(N) | **O(1)** |
| 맨뒤 삭제 | **O(1)** | O(N) |

---

## 🎓 실기 시험 팁

### 1. 배열 인덱스 주의
```c
int arr[5];  // 인덱스: 0, 1, 2, 3, 4

arr[5] = 10;  // ✘ 범위 초과 (Undefined Behavior)
arr[4] = 10;  // ✔ 올바름
```

### 2. 포인터 초기화
```c
Node* head = NULL;  // ✔ 반드시 초기화

if (head == NULL) {  // NULL 체크 습관화
    // 처리
}
```

### 3. 메모리 해제
```c
Node* temp = head;
head = head->next;
free(temp);  // ✔ 반드시 해제
```

### 4. 이중 포인터 이해
```c
void insertFront(Node** head, int data) {
    // *head를 수정하려면 **head 필요
    *head = newNode;
}
```

### 5. 경계 조건 체크
```c
// 빈 리스트
if (head == NULL) { ... }

// 노드 1개
if (head->next == NULL) { ... }

// 배열 범위
if (index < 0 || index >= size) { ... }
```

---

**check list:**
- [ ] 배열과 링크드 리스트를 직접 그려가며 이해하기
- [ ] 포인터 동작을 단계별로 추적하기
- [ ] 시간복잡도를 항상 함께 생각하기
- [ ] 기출문제를 반복해서 풀어보기
- [ ] 코드를 손으로 직접 작성해보기
