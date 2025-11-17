# Structure Interview

### 1. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> ArrayList가 유리하고 ArrayList는 특정 인덱스에 바로 접근 가능한데 LinkedList는 처음부터 순차 탐색하면서 찾아가야 하기때문
</div>
</details>

<br/><br/>
___


### 2. 입력 순서에 상관 없이 큰 숫자를 꺼낼 수 있는 우선순위 큐를 만들고 싶습니다. 어떤 자료구조을 이용해서 만드시겠습니까? 시간 복잡도는 어떻게 될까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 배열, 링크드 리스트 (정렬) : 삽입 O(N), 삭제 O(1)
- 배열, 링크드 리스트 (비정렬) : 삽입 O(1), 삭제 O(N)
- Heap : 삽입 및 삭제 O(logN)
</div>
</details>

<br/><br/>
___


### 3. 힙(Heap) 구현은 배열 혹은 링크드 리스트로 할 수 있는데 보통 배열로 많이 합니다. 그 이유는 무엇일까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - Heap의 경우 "완전 이진 트리"이므로 배열로 구현할 경우 각 노드에 대응되는 배열의 인덱스는 고정되어 있다.
- 링크드 리스트의 경우 특정 노드의 검색, 이동 과정이 배열에 비해서 더 번거롭다.
</div>
</details>

<br/><br/>
___


### 4. 배열을 이용한 힙(Heap)으로 우선순위 큐를 구현하였고 데이터를 하나 꺼내면 루트가 삭제됩니다. 그 이후에 힙의 모양 규칙를 유지하기 위해서 어떻게 처리해야 될까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 루트를 삭제 후 힙의 가장 마지막 노드를 루트 자리로 위치시키고 (배열로 만들었다면 어차피 지워질 부분이니) 루트로 옮기면 힙의 모양 규칙은 만족하며 각 원소간 대소 관계를 맞추기 위해서 정렬을 진행합니다.
</div>
</details>

<br/><br/>
___


### 5. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 6. 해시 테이블이란?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠른 데이터 검색이 필요할 때 유용하다. 해시 테이블은 각각의 키값에 해시함수를 적용해 배열의 고유한 인덱스를 생성하고, 인덱스를 활용해 값을 저장, 검색, 삭제 한다.
</div>
</details>

<br/><br/>
___


### 7. 해시테이블의 시간 복잡도는 어떻게 되는지?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시충돌이 발생할 수 있으며, 최악의 경우 O(N), 일반적으로 잘 구현된 경우는 O(1)의 시간 복잡도를 가지게 된다.
</div>
</details>

<br/><br/>
___


### 8. 해시함수란 무엇이며, 해시충돌이 발생할 수 밖에 없는 이유와 해결하는 방안은 어떻게 될까?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시함수: 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수로 출력으로 입력을 찾는 것이 불가능하고 주어진 입력은 같은 출력을 보장하는 함수. 충돌이유: 해시함수가 반환하는 값이 자료형의 한계(int 32bit)로 String이나 Object을 완벽한 해시함수로 만들 수 없고 메모리 절약을 위해 더 적은 배열만 사용하기 때문. Separate Chaining, Open Addressing 등을 이용해서 해결
</div>
</details>

<br/><br/>
___


### 9. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 스택은 후입 선출 (LIFO) / 큐는 선입 선출 (FIFO)
- 스택은 입출력이 한곳 (top) 에서만 발생 / 큐는 입력 (rear)과 출력(front)이 각각 다른 곳에서 발생
</div>
</details>

<br/><br/>
___


### 10. 그래프와 트리의 차이

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 그래프는 노드 사이에 단방향 및 양방향 경로 가능. 트리는 단방향만 가능.
- 트리는 부모-자식 관계 성립. 그래프는 부모-자식 관계 없음.
</div>
</details>

<br/><br/>
___


### 11. 두개 이상의 스레드가 해시맵에 접근할 경우 어떤 문제가 생기나?
이를 방지하려면 어떻게 해야하나?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 두 스레드가 하나의 해시키에 접근하면 문제가 된다
해시맵 사용 전에 락을 걸거나 해시 테이블을 쓴다(70점)
concorrenthashmap을 사용하거나 키별로 다른 락을 건다(100점)
</div>
</details>

<br/><br/>
___


### 12. 컴퓨터에서 float이나 double을 메모리에 어떻게 저장하는지 설명하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 부동소수점 표현 설명
부호(+-), 자릿수, 유효수 등으로 나누어 저장된다
</div>
</details>

<br/><br/>
___


### 13. float 자료형에서 숫자 0.1을 10번더하면 정확하게 1이 나오나?
아니라며 이유는 무엇인가?
정확한 결과를 얻기 위해 어떻게 해야하나?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1보다 약간 큰 값
컴퓨터는 10진수를 2진수로 변환해서 저장하는데 0.1의 경우 2의 거듭제곱형태로는 완벽하게 표현할 수 없기 때문
double같은 더 큰 자료구조를 사용한다 등
</div>
</details>

<br/><br/>
___


### 14. 그래프를 구현하는 대표적인 2가지 방법과 특징

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 인접 리스트: 노드에 연결된 간선 정보를 리스트로 관리한다.
   - 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph)일 때 유리.
   - 노드에서 인접한 노드를 찾을 수 있다.

 - 인접 행렬: 간선 정보를 행렬로 관리.
   - 많은 노드가 연결된 밀집 그래프 형태일 때 유리
   - 간선 여부를 바로 O(1)으로 알 수 있다. (M[u][v])
</div>
</details>

<br/><br/>
___


### 15. 그래프 노드를 순회하는 두가지 방법

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 너비 우선 탐색: 시작 노드에서 모든 인접 노드를 탐색 후 인접 노드의 간선을 사용해서 순회.
 - 깊이 우선 탐색: 연결된 노드를 끝까지 탐색하면서 인접 노드에 간선이 없으면 다음 인접 노드를 탐색.
</div>
</details>

<br/><br/>
___


### 16. 그래프를 사용한 최단 비용 알고리즘

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 벨먼-포드 알고리즘, 다익스트라 알고리즘, A* 알고리즘 등
</div>
</details>

<br/><br/>
___


### 17. 

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 18. 서비스에 검색 기능이 있다.
사용자의 검색 키워드를 저장해 놓고 이 키워드들을 이용해 자동완성 기능을 구현하려고 하는데
검색했던 키워드들을 어떤 자료 구조에 어떤 방식으로 저장해서 구현해보면 좋을까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 다양한 자료구조로도 구현이 가능하겠지만 
원하는 답은 tree 구조. 
입력된 키워드에 해당하는 노드의 하위 노드들을 이용해 추천해줄 수 있음.
k - ka - kak - kaka - kakao
   - ko - kor - kore - korea
tree가 아닌 다른 자료구조를 선택해서 구현한다면 그 이유.
</div>
</details>

<br/><br/>
___


### 19. 대부분의 DBMS 인덱스에서 B-tree 계열을 사용하는 이유

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> B-Tree의 장점 
- 부등호 처리 가능
- 자식노드의 순차 저장으로 인해 참조 포인터 접근 횟수가 적음
- 노드들은 정렬상태
- 탐색, 탐색, 수정, 추가, 삭제 시간 복잡도 O(log N)

B-Tree외의 다른 자료 구조는 어떤 단점이 있는지.
해시는 == 연산에만 특화되어 있어 부등호가 필요한 경우의 데이터베이스 검색에 적합하지 않음
배열은 탐색은 더 빠르지만 값의 추가와 수정, 삭제가 느림
RedBlack-Tree는 자식노드가 하나 뿐이라 순차적인 검색이 느림
linked list의 경우 정렬이나 특정 순서의 요소에 대한 접근이 배열보다 느림
</div>
</details>

<br/><br/>
___


### 20. hash table에 대한 설명과 DBMS 인덱스로 사용하기에 부적합한 이유

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - Key-Value 형태로 데이터를 저장하는 구조 
- 탐색시간이 제일 빠름
- 범위 조회에는 모든 값이 정렬되어있지 않아 O(1)의 시간 복잡도를 보장할 수 없고 매우 비효율적
</div>
</details>

<br/><br/>
___


### 21. 그래프나 트리를 탐색하는 기본적인 방법에는 Depth-First (DFS), Breadth-First (BFS) 방법이 있는데, 트리를 기준으로 각 방법의 탐색과정을 설명하고, 각 방법을 구현할 때 적합하다고 생각하는 자료구조는 무엇인가?

**난이도:** <span style="color:#000000; font-weight:bold;">초금</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - DFS: root를 기준으로 가장 멀리 방문 할 수 있는 곳 까지 방문하는 방식.
보퉁 stack을 이용, 방문하는 node를 stack에 push하며, 더 이상 갈곳이 없는 경우, stack에서 pop하여 다른 경로로 탐색을 계속 함. 
- BFS: root를 기준으로 현재 depth(=level, layer)에 있는 모든 노드를 방문한 뒤 다음 노드를 방문.
보통 queue를 이용, 방문하는 node의 모든 자식들을 queue에 넣으면서, queue에 있는 node를 방문하는 방식
- stack과 queue를 어떠한 문제에 적용해야 하는지 이해하고 있는지를 확인하는 질문, FILO인 stack은 직전의 상태로 돌아가야하는 경우에 사용. FIFO인 QUEUE는 순차적으로 처리해야하는 경우에 사용.
- BFS/DFS를 알지 못한다면 함수호출 과정/process scheduling하고 엮어서 질문해 볼 수 있음.
</div>
</details>

<br/><br/>
___


### 22. Priority Queue에 대해 설명하고, Priority Queue를 구현할때 
Array와 Heap중 어떤걸로 구현 하는것이 더 좋다고 생각하나, 
그 이유는 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 먼저 들어오는 데이터가 아니라, 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조
- 모든 항목에 우선순위가 존재하며, 우선순위 높은 데이터가 먼저 deque 
- Heap방식이 Array방식보다 시간복잡도로 따지면 worst도 O(logN)을 보장하므로 더 나음.
- Array는 선형 자료구조라 삽입 또는 삭제 연산을 위한 시간복잡도가 O(n)
</div>
</details>

<br/><br/>
___


### 23. linked list와 array list의 중간 삽입 과정과 성능 비교

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - linked list는 추가/삭제가 많거나 순환과 같은 전체 순차적 참조가 많을때 유리, array list는 추가/삭제가 적고 인덱스로 참조할때가 많을때 유리.
</div>
</details>

<br/><br/>
___


### 24. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - linked list는 추가/삭제자체는 빠르지만(O(1)) 삽입할 곳을 탐색하는 데에 오래걸림(O(n)). array list는 삽입할 곳의 탐색은 빠르지만(O(1)), 삽입시 뒤의 원소들을 모두 다시 복사해야해서 오래걸림(O(n))
- 추가로, array list는 삽입으로 인해 미리 지정해둔 capacity를 초과하는 경우, 새로 메모리를 할당해야하기 때문에 훨씬 오랜 시간이 걸림
</div>
</details>

<br/><br/>
___


### 25. Collection에 어떤 값이 들어있는지(contrains) 검사하는 코드를 작성해야할 때,
ArrayList 와 HashSet의 시간 복잡도를 설명하라.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - ArrayList에서 contains를 구현하려면, 전체를 순회하며 찾을때까지 비교를 해야하므로, 원소의 갯수가 n개 일때 O(n)이 걸림
- HashSet에서 contains를 구현하려면, 값에 대한 Hash값으로 랜덤엑세스를 하므로, O(1)이 걸림
</div>
</details>

<br/><br/>
___


### 26. ArrayList 와 HashSet 중에 어떤 것을 선택해서 사용할 것인지? 시간복잡도 또는 메모리 효율등의 관점에서 선택의 이유에 대해서 설명하라.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 목록의 크기나 처리 시간등 다각적으로 검토하는 지를 확인하는 것이 목적
예시) 허용되는 처리시간이 T라고 할때,
- ArrayList는 T를 넘지않는 선에서는, 메모리와 연산시간을 아낄수 있음
- HashSet은 ArrayList로 처리시 T를 넘길 정도로 원소가 많은 경우에 적합
</div>
</details>

<br/><br/>
___


### 27. 이진트리의 탐색(순회)의 의미와 종류에 대해서 설명해보세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 모든 노드를 한번씩 방문하기위해 순회를 하며, 순회 순서에 따라 트리 데이터를 선형으로 만드는게 가능합니다. 보편적인 방법으로는 전위 순회(preorder), 중위 순회(inorder), 후위 순회(postorder), 레벨 순회(levelorder)가 있습니다.
</div>
</details>

<br/><br/>
___


### 28. 똑같은 데이터를 LinkedList와 Array에 넣고 FullScan했을때, 어떤 자료구조가 더 빠르며, 왜 그런 것인지 설명하라

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - Random access로 cache효과를 받지 못하는 linked list에 비해 array가 fullscan 성능이 빠르다
- 다음 키를 찾는 process가 link를 쫓아가는 linked list대비 바로 다음 slot을 찾는 array가 부담이 적다
</div>
</details>

<br/><br/>
___


### 29. QuickSort시 o(n^2)가 나오는 상황은? 개선할 수 있는 방법은?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> pivot 설정이 잘못되어 분할이 1:n으로 되어 step 마다 모든 entry를 모두 비교한다는 것을 설명할 수 있어야 한다. 

개선방향
pivot 설정시, 여러 키를 선정하고 그중 중간값을 잡는다던가 pivot을 random하게 설정하여 1:n 으로 분할되지 않도록 하는 것을 설명할 수 있어야 한다.
</div>
</details>

<br/><br/>
___


### 30. HashMap의 자료구조를 설명하고 random access 시간 복잡도 설명. Hash 충돌 해결 방법은 무엇이 있는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> HashMap은 key를 hash 함수에 넣어 나온 value를 bucket의 특정 인덱스에 저장한다. H(k) = k mod M 의 계산식을 통해서 버킷의 크기보다 작은 인덱스에 저장을 하도록 한다
일반적인 경우, O(1). 최악의 경우, hash 충돌로 인해 bucket 에 value가 몰려 있을 경우, O(n). 

충돌 방지 방법  
- Separate chaning : 버켓에 리스트를 두어서, 순서대로 저장한다
- Open addressing : 버켓의 시작점을 찾은 후 비어있는 공간이 나올때까지 확인 후 저장
</div>
</details>

<br/><br/>
___


### 31. Hash 테이블에서 연산에 키값 충돌과 같은 오류가 없다는 전제하에 
삽입, 검색, 삭제의 시간 복잡도를 Big-O 표기법으로 설명해 주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 연산에 오류가 없다는 전제하에 hash 테이블에 대한 삽입, 검색, 삭제의 시간 복잡도는 O(1)
</div>
</details>

<br/><br/>
___


### 32. arraylist와 linkedlist중 댓글 서비스를 구현한다면 더 적합한 것은? 그 이유는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> arraylist 와 linkedlist의 특징에 따라 댓글 서비스의 성격에 따라 골라서 설명할 수 있는지 확인한다.
</div>
</details>

<br/><br/>
___


### 33. 해시테이블에서 해시 함수를 통해 주어진 키 x 를 일정 범위 내의 integer값으로 변환해서 저장하는데, 이때 사용하는 hash code 및 compression function 을 설명해 주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. hash code : key 값을 일정 범위 내의 integer 값으로 변환 (방법: integer cast, component sum, polynomial accumulation)
	2. compression function : hash code를 통해 integer 형태로 변환된 key 값은 정해진 범위 내로 축소 (방법: division, multiply add and divide )
</div>
</details>

<br/><br/>
___


### 34. 배열(Array)과 ArrayList의 차이

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 배열은 크기가 고정되어있지만 arrayList는 사이즈가 동적인 배열이다.
- 배열은 primitive type(int, byte, char 등)과 object 모두를 담을 수 있지만, arrayList는 object element만 담을 수 있다.
- 배열은 제네릭을 사용할 수 없지만, arrayList는 사용할 수 있다.
- 길이에 대해 배열은 length 변수를 쓰고, arrayList는 size() 메서드를 써야한다.
- 배열은 element들을 할당하기 위해 assignment(할당) 연산자를 써야하고, arrayList는 add() 메서드를 통해 element를 삽입한다.
</div>
</details>

<br/><br/>
___


### 35. 단일 연결리스트에서 역순으로 출력하는 방법

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 재귀를 이용하여 역순 출력 
- 리스트의 포인터를 역방향으로 재 순환시켜 새로운 리스트를 만들어서 출력
- 스택을 이용하여 push/pop을 통해 데이터 출력
</div>
</details>

<br/><br/>
___


### 36. 

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 37. singly linked list (단방향 연결 리스트) 와 doubly linked list (양방향 연결 리스트) 의 차이

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - singly linked list는 다음 노드에 대한 포인터만 존재하여 한방향으로만 순회할 수 있다.
- doubly linked list는 이전 노드, 다음 노드에 대한 양방향 포인터가 존재하여 앞, 뒤 양방향으로 순회할 수 있다.
- 리스트 내에서 노드를 삭제할 경우 삭제할 노드를 알고 있다면 삭제를 위한 Time Complexity는 singly linked list의 경우 O(n), doubly linked list는 O(1)이다.
</div>
</details>

<br/><br/>
___


### 38. Multi Process 와 Multi Thread 의 차이점

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - multi thread 의 경우 thread 간에 메모리 공유가 가능하지만 multi process 의 경우에는 메모리 공유가 불가능하다. 따라서 multi process 에서 프로세스 간의 데이터 공유를 위해서는 프로세스 간에 통신 채널이 반드시 필요하다. 
- process 간 통신 방법 예시 : IPC(socket, pipe, memory map, signal)
</div>
</details>

<br/><br/>
___


### 39. 

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 40. Binary Seach Tree 에서 노드를 삭제할 때 일어나는 과정을 설명해 주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 자식노드가 0개, 1개, 2개일 경우를 구분하여 설명
- 0개일 경우, 해당 노드만 삭제
- 1개일 경우, 해당 노드를 삭제하고 자식 노드를 해당 노드의 위치로 변경
- 2개일 경우, 해당 노드를 삭제하고 왼쪽 서브 트리의 가장 큰 노드(혹은 오른쪽 서브 트리의 가장 작은 노드)를 삭제할 노드의 위치로 변경한다.
</div>
</details>

<br/><br/>
___


### 41. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 42. 우선순위 큐란 무엇인가 ?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 큐에 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 반환되는 큐
</div>
</details>

<br/><br/>
___


### 43. 우선순위 큐를 구현하는 방안은 무엇이며 각 방안의 장/단점은 ?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 배열 : 구현이 간단하다 / 데이터 삽입을 위해 배열에 저장된 모든 데이터와 비교해야 하며, 삽입/삭제 시 데이터 이동이 필요하다.
- 연결리스트 : 구현이 간단하다 / 데이터가 많아질수록 삽입 위치를 찾기 위한 비교대상이 증가하여 성능이 떨어진다.
- 힙 : top의 데이터에 따라 최소힙/최대힙으로 구현이 가능하며, 완전이진트리를 이용하기 때문에 삽입/삭제 모두 o(logN)으로 수행이 가능 / 구현이 위 두 방법보다 어렵다.
</div>
</details>

<br/><br/>
___


### 44. LRU란, 이것을 자료 구조를 사용해서 구현을 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 가장 최근에 사용된 데이터는 다음에도 사용될 가능성이 높기 때문에 데이터를 삭제할 때 가장 오래 전에 참조된 것부터 삭제하는 알고리즘
- 데이터가 들어온 순서대로 정렬하기 위해 double linked list 를 사용
-- head에 가까운 데이터 일수록 최신 데이터 tail 에 가까울수록 가장 오랫동안 사용하지 않은 데이터로 간주하여 새로운 데이터를 삽입할때 가장 먼저 삭제 되도록 함 
-- 새로 삽입한 데이터/ 최근에 찾은(get)한 데이터는 head로 옮겨주어, 우선순위를 높여줌
- 탐색 효율을 높이기 위해 hashMap 을 사용 
-- 이론적으로 hashMap 의 탐색 속도는 O(1) 이고 linked list 는 O(N)
-- 아이템 넣기 / 아이템 얻기 / 아이템 삭제 O(1)
</div>
</details>

<br/><br/>
___


### 45. Java에서 HashTable과 HashMap의 차이점에 대해서 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - HashMap은 동기화를 지원하지 않는다. 단일스레드 환경에서 사용하기 좋음
- HashTable은 동기화를 지원하여, thread-safe하다. 멀티스레드 환경에서 사용하기 좋지만 HashMap에 비해 느림, key/value 에 null 사용 불가
</div>
</details>

<br/><br/>
___


### 46. 뮤텍스와 세마포어에 대한 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 세마포어(Semaphore)
공유 자원의 상태를 나타낼 수 있는 카운터로 표현하여 최대 허용치만큼 동시에 사용자가 접근할 수 있다.
- 뮤텍스
한 프로세스에 의해 소유될 수 있는 Key를 기반으로 한 상호배제 기법
</div>
</details>

<br/><br/>
___


### 47. 배열의 Access(Read), Search, Add, Delete 연산을 
속도 관점에서 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Access(Read): 배열 크기와 상관없이 인덱스에서 요소를 읽는 속도는 동일하다.
Search: 찾는 값이 나올 때까지 하나하나 확인하므로, 찾는 값이 어디에 위치하느냐에 따라
 속도가 달라진다.  최악의 경우, 배열의 모든 요소를 찾아야 한다.
Add: 맨 끝에 추가하는 것은 속도가 빠르다. 하지만, 배열 중간에 추가하려면 기
존 항목을 밀어내고 해당 공간을 비워야 하므로, 맨 끝 추가보다 느리다.
Delete: 맨 끝 요소 삭제는 속도가 빠르다.  하지만, 배열 중간 요소를 삭제하는 경우, 
삭제된 요소로 부터 뒤에 있는 모든 항목을 앞으로 이동시켜야 하므로, 맨 끝 요소 삭제보다 느리다.
</div>
</details>

<br/><br/>
___


### 48. 일반적인 리스트로 구현되는 선형 큐의 한계를 설명하고 
이를 극복하기 위한 대안을 제시해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 한계 (일반적인 답변) : 허용된 공간 만큼의 삽입/삭제가 발생한 경우 큐가 포화 상태라고 판단한다. 
한계 (구체적인 답변) : rear = size-1 경우 enqueue 수행 불가, 
front ≠ 0 인 경우 앞의 공간을 활용할 수 있음에도 불구하고 더이상 동작할 수 없는 문제점이 있다.

대안 (일반적인 답변) : 원형큐 자료구조를 채택하는 것이다.
대안 (구체적인 답변) : enqueue 시도시 rear + 1 이 존재하지 않다면 rear는 인덱스 0 을 선택한다.

옵션문제 (보너스 점수) : enqueue 시도시, 큐 사이즈를 고려한 rear 인덱스의 결정 공식을 세울수 있겠는가?
옵션문제 (답변) : rear = (rear+1) % MAX_QUEUE_SIZE
</div>
</details>

<br/><br/>
___


### 49. 룰렛으로 10개의 아이템을 선택하는데,
선택될 확률이 각각 다른 경우,
이를 구현한다면 어떤 자료 구조가 좋을까요? 그 이유는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 50. 2차원 행렬(n x m)을 저장하려고 한다. 
이 행렬은 다음과 같은 특징이 있다.
1. 실수를 저장하고 있는데, 0이 90% 이상 차지하고 있다
2. n, m은 가변적이며, 최대값은 100만
이런 데이터를 효율적으로 저장할 수 있는 방법은 무엇일까?

**난이도:** <span style="color:#000000; font-weight:bold;">초급, 중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 2-dim array가 가장 간단한 방법이지만, n, m의 최대값을 고려하면 메모리 낭비가 심하다. 
- 이런 답변의 경우 1Mx1M  matrix의 메모리 사용량을 계산하도록 하고 다른 방법을 고민하도록 진행
2. sparse matrix 를 표현하는 대표적인 방식 중 하나를 설명하면 된다. 
   (1) col, row, value representation
   (2) linked list representation 
3. 메모리 효율을 극대화하기 위한 CSR(compressed sparse row)까지 등장하면 +알파
</div>
</details>

<br/><br/>
___


### 51. array list와 linked list의 장단점은 무엇일까?

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - array list
(장점) 데이터에 빠르게 접근 가능
(단점) 메모리 사용 비효율적, 배열내 데이터 이동 및 재구성이 어려움

- linked list
(장점) 동적으로 메모리 사용 가능, 데이터 재구성 용이
(단점) 특정 위치 데이터 검색이 느림
</div>
</details>

<br/><br/>
___


### 52. 검색어 자동완성 기능을 구현하고자 한다. 입력에 맞추어 자동완성 목록을 빠르게 추천해주기 위해서 사용할 수 있는 자료구조와 자료구조를 선택한 이유를 소개해달라.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - trie, prefix tree 등. 사용자의 입력이 검색할 단어의 앞에서부터 뒤로 쓴다는 가정을 했을 때 prefix를 기준으로 검색이 쉬운 자료구조를 설명해주면 일차적인 답변
- 검색어 ranking에 대한 idea, 검색어의 중간 내용을 입력했을 때도 추천할 수 있는 idea를 제안하면 가점 ("뉴스" 입력 -> "다음 뉴스" 추천)
</div>
</details>

<br/><br/>
___


### 53. 그래프 순회 방법인 DFS, BFS 구현 시, 
적합한 자료구조와 그 이유에 대해서 이야기해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. DFS : 스택을 활용
    - DFS 기법은 하나의 노드로부터 최대한 깊이 탐색을 한 뒤에 더이상 내려갈 곳이 없을 경우에 
      (되돌아가서) 탐지되지 않은 옆의 노드로 이동하여 탐색하는 방법
    - 스택을 활용하여 인접 노드를 쌓는 경우, 마지막에 출력된 인접 노드부터 탐색하면서 
      하나의 분기(혹은 경로)를 끝까지 깊이 탐지가 가능

2. BFS : 큐를 활용
    - BFS 기법은 하나의 노드로부터 옆에 인접한 노드 위주로 최대한 넓게 탐색하는 방법
    - 큐를 활용하여 인접 노드를 넣는 경우, 넣은 순서대로 출력된 인접 노드를 탐색하면서 
      여러 분기의 넓은 탐지가 가능
</div>
</details>

<br/><br/>
___


### 54. DFS, BFS를 활용하여 길찾기 알고리즘을 만들 때, 
추가적으로 고려되야 될 자료나 자료구조는 무엇이 있고 
왜 그렇게 생각하는지?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 입력 데이터 관점 : 출발지와 목적지의 거리에 따라서 탐색 방법의 시간 효율이 다를 수 있음
    - 거리 기준 =  노드 차이 수량(=간선의 weight이 모두 동일하다는 가정)
        - 보통 거리가 가까운 경우에는 넓게 탐지되는 BFS가 
          다양한 옆 분기의 노드를 search하면서 최단 경로를 찾는데 유리함
        - 거리가 먼 경우에도 대체적으로 BFS가 유리한 편이나 
          edge case로 경로의 다양성이 적은 경우에는 
          깊게 탐지되는 DFS가 최단 경로를 찾는데 좀 더 유리할 수 있음

2 .출력 데이터 관점 : 경로(path) 정보에 대해서 저장이 필요하고 
                               크기는 경로 거리에 따라서 동적인 특성을 지님
   1) 경로 정보에 대해서 저장하는 방안은 2가지 정도
       (1) 그래프 내부 관점: 노드 객체 내에 최단 경로에 대한 간선 정보 속성등을 따로 추가하여 저장
       (2) 그래프 외부 관점: list등을 별도로 생성하여 최단 경로에 속하는 노드 정보를 누적하여 저장
    2) 동적 크기로 생성되는 부분을 고려하면 array보다 linked list의 특성을 지닌 자료구조가 더 적합
        - 공간 복잡도의 경우, 저장방식과 상관없이 경로(분기 별)로 생겨날 수 있고 
          알고리즘(BFS, DFS)에 따라 공간 복잡도에 대한 차이가 생겨날 수 있음
          -> BFS 공간 복잡도 : O(node+edge) 
              #최악의 경우, 목적지에 도달하기 까지 경로 계산에 대한 중간 결과를 유지하고 있어야 함
          -> DFS 공간 복잡도: O(depth) 
              #가장 긴 depth 길이 만큼 데이터 공간이 있으면 가능
</div>
</details>

<br/><br/>
___


### 55. DFS, BFS 를 활용한 길찾기 알고리즘 외에 
다른 길찾기 알고리즘(다이스트라, A*등)을 활용할때, 
추가적으로 고려되야 될 자료나 
자료구조는 무엇이 있고 왜 그렇게 생각하는지?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. priority queue : 간선의 weight 혹은 휴리스틱과 같은 경로 선택에 대한 가중치 
    계산이 들어가면서 가중치에 따른 우선 순위를 고려해야 함

2.  추가 연계 질문 : priority qeueue 구현 방식에는 어떤 자료 구조가 적합한지 등(heap)
</div>
</details>

<br/><br/>
___


### 56. 다익스트라, 벨만-포드 알고리즘을 설명하고 
어떨때 어떤 알고리즘을 써야하는가?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 다익스트라 알고리즘, 벨만-포드 알고리즘은 최단 경로 탐색 알고리즘
가중 그래프에서 최단 거리를 계산하는데 사용되며 모든 가중치가 양수일 때만 정상적으로 동작하며
가중치가 음수이면 벨만-포드 알고리즘을 사용
</div>
</details>

<br/><br/>
___


### 57. 128개의 이름이 정렬되어있는 리스트가 있을때,
이진 탐색으로 이름을 찾을 때 필요한 최대의 추측 횟수는 얼마인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 7번
이진 탐색은 빅오표기법으로 O(logN) 이기 때문에 O(log128) 으로 최대 추측 횟수는 7번
</div>
</details>

<br/><br/>
___


### 58. 만약 리스트의 크기가 두배가 된다면 최대 추측 횟수는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 8번
리스트 크기가 두배가 늘어나도 O(log256) 이기 때문에 추측횟수가 2배로 늘어나지 않고 8번
</div>
</details>

<br/><br/>
___


### 59. 순환 연결 리스트 (circular linked list)의 순환되는 첫 노드를 어떻게 찾을 수 있을까?
예) A > B > C > D > E > C 라면 E의 next가 C이므로 순환되는 첫 노드는 C

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - slow와 fast 두 포인터를 만들어 slow는 한 번에 한 노드, fast는 한 번에 두 노드를 이동
- (slow와 fast가 충돌하지 않으면 순환되지 않는 것)
- slow와 fast가 충돌하면 slow 또는 fast를 head로 이동시키고 slow, fast 둘 다 한 노드씩 이동
- slow와 fast가 충돌하는 위치가 순환되는 첫 노드
</div>
</details>

<br/><br/>
___


### 60. 다음 조건을 만족하는 리스트 자료 구조를 제안하시오.
* 한쪽 끝에서만 추가, 제거가 일어난다.
* 변경이 일어나기 전 리스트와 후의 리스트를 모두 사용할 수 있어야 한다.
* 메모리 복사를 적게 해야한다.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Singly linked list
</div>
</details>

<br/><br/>
___


### 61. 해시 테이블은 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시 테이블은 연관배열 구조를 이용하여 키(key)에 결과 값(value)을 저장하는 자료구조이다.
</div>
</details>

<br/><br/>
___


### 62. Hash Collision(해시 충돌) 해결 방법

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Separate Chaining, Open Addressing 등등
</div>
</details>

<br/><br/>
___


### 63. Separate Chaining, Open Addressing 에 대해 설명?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Separate Chaining 방식은 색인을 Linked List로 구현하여 같은 해시값을 가질 경우에도 원하는 데이터의 접근이 가능해짐. Open Addressing 방식은 같은 해시값을 이미 사용하고 있을 경우 색인 중에 비어있는 곳에 넣어서 해결.
</div>
</details>

<br/><br/>
___


### 64. 세마포어(Semaphore) 와 뮤텍스 (Mutex) 비교

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 세마포어(Semaphore) 
  : 커널모드 동기화 객체.
  : 공유된 자원의 데이터를 여러 프로세스가 접근하는 것을 막는 것.
  : 운영체제 또는 커널의 한 지정된 저장장치 내 값. 각 프로세스는 이를 확인하고 변경할 수 있음.

- 뮤텍스(Mutex, 상호배제) 
  : 커널모드 동기화 객체
  : 공유된 자원의 데이터를 여러 쓰레드가 접근하는 것을 막는 것.
  : 다중 프로세스들의 공유 리소스에 대한 접근을 조율하기 위해 locking과 unlocking을 사용.

- 세마포어와 뮤텍스 비교
  : 세마포어는 뮤텍스가 될수 있지만, 뮤텍스는 세마포어가 될 수 없음. (Mutex 는 상태가 0, 1 두 개 뿐인 binary Semaphore)
  : 뮤텍스의 경우, 뮤텍스를 소유하고 있는 쓰레드가 이 뮤텍스를 해제할 수 있음.
  반면, 세마포어의 경우, 세마포어를 소유하고 있지 않은 쓰레드도 이 세마포어를 해제할 수 있음.
  : Mutex는 동기화 대상이 오직 하나뿐일 때, Semaphore는 동기화 대상이 하나 이상일 때 사용.
</div>
</details>

<br/><br/>
___


### 65. 자료구조를 선택할때 고려할 사항은 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 효율성, 크기, 활용빈도, 갱신빈도, 용이성
</div>
</details>

<br/><br/>
___


### 66. 자료구조 효율성을 감안했을때 검색 알고리즘 선택 예시는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 순차검색 vs 이분검색 등으로 설명
</div>
</details>

<br/><br/>
___


### 67. 자료구조의 종류는 분류한다면 어떤 방식?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형구조, 비선형 구조
</div>
</details>

<br/><br/>
___


### 68. 자료구조 선형구조와 비선형 구조에 해당하는 것들을 나열?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형(배열, 연결리스트, 스택, 큐), 비선형(트리, 그래프)
</div>
</details>

<br/><br/>
___


### 69. List 와 Hash의 탐색 속도를 빅오표기법(Big-O Notation) 비교 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> List 선형 자료구조 O(N), Hash는 알고리즘에 의해 O(1) 으로 상수 시간 보장
</div>
</details>

<br/><br/>
___


### 70. Array와 Linked List의 차이점

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Array는 element가 메모리에 연속적으로 저장된다. 탐색이 빠르다. 시간복잡도 O(1)
Linked List는 element가 다음 element의 메모리 위치를 저장한다. 탐색이 느리다. 시간복잡도 O(n)
</div>
</details>

<br/><br/>
___


### 71. Queue에 대해서 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Queue의 종류, FIFO 등 특성
</div>
</details>

<br/><br/>
___


### 72. Queue를 직접 만든다면 어떻게 만들건지 간단히 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 자유롭게(Stack, Array 등 활용) Queue의 기능(add, peak) 구현
</div>
</details>

<br/><br/>
___


### 73. Tree 와 Hash로 인덱스를 만들 때 어떤 차이가 있는가?
어떤 조건일 때 각각을 사용하는가?
어떤 조건일 때 각각을 사용할 수 없는가?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Tree: 순서가 있다. 순서가 인접한 여러 키를 효율적으로 쿼리할 수 있다.
Hash: 순서가 없다. 임의의 키를 효율적으로 쿼리할 수 있다. 키보다 큰 키들, 작은 키들 등 범위를 쿼리할 수 없다.
</div>
</details>

<br/><br/>
___


### 74. B-Tree는 어떻게 균형을 유지하는가?
대략적인 전략을 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀적 자료구조. 노드 분할, 병합. 노드 분할과 병합으로 트리 깊이의 변경.
</div>
</details>

<br/><br/>
___


### 75. B-Tree의 branching factor는 어떻게 결정하는게 효율적인가?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 키의 크기와 IO 단위를 고려하여 한 번의 IO에 최대한 많은 키에 접근할 수 있게 정한다.
</div>
</details>

<br/><br/>
___


### 76. 최근 n 초간 어떤 이벤트가 몇 번 발생했는지 알고 싶다.
어떤 자료 구조를 쓰겠는가? 이유는?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> circular/ring buffer 같은 자료구조를 쓸 수 있다.
공간을 재사용하기 때문에 효율적이다.
n초가 지난 데이터를 따로 지울 필요가 없다.
</div>
</details>

<br/><br/>
___


### 77. 캐시가 효과적으로 동작하려면 어떤 조건이 만족되어야 하는가?

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 캐시에 저장한 값을 다시 쓸 확률이 높아야 한다. Time locality, Space locality 등 locality가 있어야 한다.
</div>
</details>

<br/><br/>
___


### 78. Stack 2개로 Queue를 구현한다면?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> inBox, outBox 두개의 Stack을 만들고,
enquene 는 inBox에 넣고,
dequeue는 outBox가 빈 경우 inBox를 모두 팝하여 순서대로 outBox에 넣은 후 pop을 하여 리턴한다.
outBox가 비어있지 않다면 outBox에서 pop을 하여 리턴한다.
</div>
</details>

<br/><br/>
___


### 79. 배열로 구현한 우선순위 큐가 있을 때 성능상 어떤 문제가 있는가?
해당 문제를 개선한다면 어떻게 하겠는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 삭제시 전체 탐색을 해야하기 때문에 O(n)의 시간이 걸린다.
삭제연산을 줄이기 위해서 힙으로 우선순위 큐를 구현하면 O(log n)의 시간으로 개선할 수 있다.
</div>
</details>

<br/><br/>
___


### 80. 3가지 상태(default, enabled, disabled)를 가지는 값이 n개 있다.
어떻게 저장하겠는가?
가능한 다양한 방법을 제시하라. 그 방식의 장단점은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 프리미티브 타입에 3가지 상태를 부여.
열거형 정의.
비트 필드.
</div>
</details>

<br/><br/>
___


### 81. List A 와 List B 에서 중복되는 값을 찾아보세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 단순히 2중 루프를 돌리는지, 아니면 다른 자료구조를 활용해 찾는지 등 어떻게 문제를 해결하는지 본다.
</div>
</details>

<br/><br/>
___


### 82. LRU Cache 를 직접 구현한다면 어떤 자료구조로 어떻게 구현할것인가

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 순서를 표현하는 자료구조 1개, 캐싱을 위한 자료구조 1개 둘의 연결을 잘 설명하는지 확인한다.
</div>
</details>

<br/><br/>
___


### 83. 두 사람의 가위바위보 결과를 데이터로 표현한다면? 계산식으로 표현한다면?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> (가위,바위,보)를 키로하는 2차원 자료구조의 값에 승,패,무승부로 표현.
가위,바위,보 각각에 값을 부여하고 승,패,무승부에도 값을 부여하고 계산식 수립.
예. A승: 2, 무승부: 1, A패: 0
가위: 1, 바위: 2, 보: 3
(A - B + 1) % 3 = R
</div>
</details>

<br/><br/>
___


### 84. tree 와 Hash로 인덱스를 만들 때 어떤 차이가 있는가?
어떤 조건일 때 각각을 사용하는가?
어떤 조건일 때 각각을 사용할 수 없는가?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 쓰레드 사이에 동기화가 되지 않으면 자료구조가 깨질 수 있다.
그 자료구조가 만족시켜야 하는 조건을 만족하지 못하는 상태가 된다.
자료 구조 전체 접근에 락을 사용한다. 간단. 블럭되는 쓰레드가 많아진다.
상호배제가 필요한 부분들의 접근에만 락을 사용한다. 복잡. 블럭되는 쓰레드가 적지만 구현 오류 발생 가능성이 높다.
lock-free data structure, persistent data structure 등등
</div>
</details>

<br/><br/>
___


### 85. 연결리스트(LinkedList)란?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 엘리먼트간(혹은 노드)의 연결(link)을 이용해서 리스트를 구현한 것
</div>
</details>

<br/><br/>
___


### 86. 연결리스트를 배열과 비교하여 장단점을 서술하세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 탐색: 배열 O(1), 연결리스트 O(n), 삽입(삭제): 배열 데이터를 앞뒤에 추가하는게 아니라면 O(n), 연결리스트 O(1)
</div>
</details>

<br/><br/>
___


### 87. String 2개의 단어가 주어졌다. 두개의 단어가 얼마나 유사한지 판단할 수 있는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 자소, 음절, 발음, 로마자 등 어떤 단위로 비교할 것인지/ 유사도 계산을 어떻게 할 것인지 나누어 접근이 필요하다.
일반적으로 각각의 키워드를 집합(Set)으로 바라보고 공통 원소수의 비율/패턴을 비교하는 방식으로 진행 
- Jaccard :두 문자열 간의 교집합/합집합을 계산 
- Sorensen-Dice : 두 문자열 간의 공통 원소 개수를 계산
그밖에 Jaro, Overlap, Hamming 과 같은 계산 방식이 있다. 이 같은 방식을 선택하지 않더라도 적당한 방법을 생각해내고 그 안에서 사용하는 자료구조의 이유를 설명할 수 있다.
</div>
</details>

<br/><br/>
___


### 88. 단어가 아니라, 1000자 이상의 text간 유사도를 어떻게 비교할 수 있는가? 
텍스트에서 키워드는 어떻게 추출해야 할까? 미리 정의된 사전을 이용한다면 이때 사전은 메모리에 어떤 형태여야 효율적일까? 사전에 등록된 키워드가 10만개라면?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> #미리 단어가 정의된 사전이 있다고 가정하고 사전과 매칭하여 text에서 키워드를 추출하는 경우
텍스트에서 품사에 기반한 주요 키워드를 미리 정의한 사전을 만들어 해당 text에서 등장하는 키워드를 추출, 주요순위로 N개를 뽑아 위와 비슷한 방식으로 유사함을 비교한다. 
사전에 등록된 키워드 여부파악을 위해 트리구조를 떠올릴 수 있다. 한번 확인한 문자는 다시 확인하지 않는, 텍스트의 글자와 키워드 트리의 간선의 글자와 비교하면서 정점으로 내려가며 탐색하는 방식을 설명한다. 예) 아호 코라식 알고리즘
주요 키워드를 선정하는 방식에 대해서도 설명할 수 있으면 베스트 예) TextRank, TF-IDF
#임베딩을 활용하는 방식
배열(벡터)을 떠올릴 수 있다. 텍스트를 숫자로 임베딩하여 cosine 유사도를 이용할 수 있다.
임베딩 방식으로는 음절 단위 로마나이즈, Word2Vec, GloVe, fastText, sent2vec, Bert 등 ML,DL 모델을 활용한 미리 학습된 말뭉치가 필요하다.
</div>
</details>

<br/><br/>
___


### 89. 

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 
</div>
</details>

<br/><br/>
___


### 90. List 와 Set 의 주요 차이점은 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> * 중복 요소 허용 여부: List 는 중복 허용하지만 Set 은 중복 허용하지 않는다.
* 요소들의 순서 보장: List 는 순서가 보장되지만 Set 은 보장되지 않는다.
</div>
</details>

<br/><br/>
___


### 91. 해쉬테이블과 해쉬함수에 대해 설명하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시테이블: 원소가 저장될 자리가 원소의 값에 의해 결정되는 자료구조
해시함수: 키값을 입력으로 받아 해시 테이블 상의 주소를 리턴하는 함수
</div>
</details>

<br/><br/>
___


### 92. 해쉬 충돌이란? 그리고 이를 해결하는 방법을 아는대로 설명하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시충돌: 두개 이상의 키값이 동일한 주소를 가르키는 경우. 
1. 체이닝 - 같은 주소로 해싱되는 원소를 모두 하나의 연결리스트로 관리. 
2. 개방주소 방법 - 원래의 주소가 아닌 다른 주소를 계산하여 넣는 방식. 선형조사, 이차원조사등이 있음. 
3. 더블해싱 - 두개의 해시함수를 사용하여 첫번째 함수의 주소에서 충돌이 생긴경우, 두번째 함수의 값만큼 점프하는 방법.
</div>
</details>

<br/><br/>
___


### 93. 개방주소 방법에서 중간의 원소를 삭제했을때 어떤 문제가 발생하는가? 해결방법은?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 중간 충돌지점이 삭제되는 경우, 원소가 저장된 위치를 찾을수 없다. 따라서 삭제시 원래 원소가 있던 곳임을 표시하여야 함.
</div>
</details>

<br/><br/>
___


### 94. linked list와 vector(혹은 ArrayList)를 자료의 추가/삭제/탐색 연산 기준으로 동작 방식을 설명하면?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> linked list: 각 노드를 자료와 다음 노드를 가리키는 포인터로 구성, 추가/삭제는 다음 노드에 대한 포인터만 변경하는 작업이기 때문에 빠르게 처리, 하지만 탐색은 처음부터 순차적으로 해야 함
vector: 힐당된 메모리에 순차적으로 데이트를 저장, 데이터 추가/삭제 시 메모리 청크를 할당하고 이동하는 작업이 필요하므로 상대적으로 느림, 하지만 탐색은 인덱스 기반으로 빠르게 처리
</div>
</details>

<br/><br/>
___


### 95. 위의 설명을 기준으로 일반적으로 어떤 경우에 linked list와 vector를 사용하는 것이 좋을까?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> linked list: 자료의 추가/삭제가 빈번한 경우, 순차 접근이 자연스러운 경우(DB에서 조회된 레코드 처리 등)
vector: 자료의 탐색이 빈번한 경우
예외: 메모리가 부족하여 캐시 히트율이 낮은 경우에는 linked list도 빈번한 추가/삭제 시 느릴 수 있음을 언급할 수 있으면 보너스
</div>
</details>

<br/><br/>
___


### 96. 그래프(Graph)란?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 노드(node)와 노드를 연결하는 간선(edge)를 모아 놓은 자료 구조
</div>
</details>

<br/><br/>
___


### 97. 그래프와 트리의 차이

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 트리는 그래프의 한 종류
그래프는 사이클이 가능하나 트리는 불가능
그래프는 부모자식 관계가 없어 루트 노드가 없으나, 트리는 루트노드가 존재하고 하나의 부모만 가짐
</div>
</details>

<br/><br/>
___


### 98. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS: Depth-First Search. 깊이우선 탐색
- 넓게(wide) 탐색하기 전에 깊게(deep) 탐색
- 특정 노드에서 시작해서 다음 분기(branch)로 넘어가기전 해당 분기를 완벽하게 탐색
- 모든 노드를 방문할 때 사용. BFS 보다 간단
BFS: Breadth-First Search. 너비 우선 탐색
- 깊게(deep) 탐색하기 전에 넓게(wide) 탐색
- 특정 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법
- 두 노드 사이의 최단 경로를 찾거나 임의의 경로를 찾고 싶을 때 사용
</div>
</details>

<br/><br/>
___


### 99. 수 억건의 2차원 좌표 집합이 있다.
입출력 성능 만을 고려했을 때 어떠한 자료구조를 선택하는것이 좋을까?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 다차원 트리 (Quad Tree, R Tree, K-d Tree...) 를 이용한다.
</div>
</details>

<br/><br/>
___


### 100. (K-d Tree 와 R Tree를 모두 안다면) 두 자료구조의 공통점과 차이점은?
각각 어떠한 상황에 사용하는지 알고있는지?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> K-d Tree 는 단일 지점 (point) 정보를 저장하는데 적합.
R Tree 는 면적 혹은 부피를 갖는 입체 정보를 관리하는데 적합
</div>
</details>

<br/><br/>
___


### 101. 재귀함수에 대해 간략한 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 하나의 함수에서 자기 자신을 재참조하여 작업 수행
재귀함수 종료에 대해 같이 설명 필요
</div>
</details>

<br/><br/>
___


### 102. 재귀함수 구현에 가장 적합한 자료구조는 무엇일까

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 주요 자료구조(스택/큐/배열)등에 대한 이해 
stack(LIFO)를 활용하면 쉽게 구현 가능
</div>
</details>

<br/><br/>
___


### 103. 연결 리스트의 헤드 노드를 설명 하고, 헤드 노드를 사용하는 이유를 설명 하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 헤드 노드 : 값을 가지지 않는 첫번째 노드
단일 연결 리스트 : 삽입/삭제 맨앞 O(1), 나머지는 O(n)
-> 헤드노드를 사용하지 않은 원형 단일 연결 리스트 : 맨앞,맨뒤 O(n)
-> 헤드노드를 사용한 원형 단일 연결 리스트 : 맨앞 O(1), 나머지 O(n)
</div>
</details>

<br/><br/>
___


### 104. 이중 연결 리스트를 설명 하고 원형 이중 연결 리스트를 설명 하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 이중 연결 리스트 : 노드가 앞, 뒤의 주소를 가지고 있는 리스트
원형 이중 연결 리스트 : 맨앞, 맨뒤 O(1)
</div>
</details>

<br/><br/>
___


### 105. 연결리스트로 스택과 큐를 구현 시 적합한 연결 리스트는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 스택 : 단일 연결 리스트, 원형 단일 연결 리스트
큐 : 원형 이중 연결 리스트
</div>
</details>

<br/><br/>
___


### 106. 그래프(Graph) 구현의 대표적인 방식 두가지는 ?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 인접리스트(Adjacency List) : 각 정점으로부터 연결되는 정점 및 가중치(cost)를 리스트로 관리
2. 인접행렬(Adjacency Matrix) : 모든 정점을 행과 열로 만들어 간선이 존재하면 true 또는 가중치(cost) 로 생성
</div>
</details>

<br/><br/>
___


### 107. 그래프 탐색 알고리즘 중 Shortest Path 를 찾기 위한 대표적인 알고리즘은 ?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 다익스트라(Dijkstra) 알고리즘, A* 알고리즘 등
</div>
</details>

<br/><br/>
___


### 108. 피보나치 수열을 재귀함수를 이용하여 구현

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 기초적인 재귀함수를 구현할 수 있는지 검증
</div>
</details>

<br/><br/>
___


### 109. 스택, 큐, 트리, 힙 구조를 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 스택: First-In Last-Out(FILO) 구조
큐: First-In First-Out(FIFO) 구조
트리: 노드와 엣지를 이용해 사이클을 이루지 않도록 구성한 Graph로, 계층이 있는 데이터를 표현
힙: 노드의 키값이 자식의 키값 보다 작지 않거나(최대힙) 크지 않은(최소힙) 완전 이진트리
</div>
</details>

<br/><br/>
___


### 110. 우선순위 큐의 내부 구조 및 시간복잡도는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 우선순위 큐를 구현하기 위해서 일반적으로 힙을 사용하며,
힙은 완전이진트리를 통해 구현되었기 때문에 우선순위 큐의 시간복잡도는 O(logn)임.
</div>
</details>

<br/><br/>
___


### 111. 1초마다 발생하는 랜덤 숫자를 저장하고, 
중간 중간 가장 큰 숫자를 뽑아야 하는 경우가 발생했다. 
어떤 자료구조에 저장하고 어떻게 가장 큰 숫자를 선택하겠는가

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> selection tree, heap 등의 자료구조를 설명. 
만약 정렬을 사용한다면 더 좋은 방법이 없을지 추가 질문
</div>
</details>

<br/><br/>
___


### 112. 10000개의 숫자를 배열/정렬된배열/이진트리에 
각각 저장했을 때 특정 숫자를 찾는 탐색시간은?(평균, 최악), 
더 개선할 방법은 없을까?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 정렬된 배열에서 binary search 사용 여부, 이진트리의 최악의 경우 N 확인
</div>
</details>

<br/><br/>
___


### 113. LRU캐시를 직접 구현한다면 어떻게 구현할것인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> HashMap 개념 LinkedHashMap이나 두가지 자료를 가지고 상황별로 어떻게 처리 할지
</div>
</details>

<br/><br/>
___


### 114. 해시충돌이 발생하기 전에 이를 완화하는 방법은 무엇이 있을까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 해시버킷을 특정 임계점이상에서 동적으로 확장 시키거나,  보조적인 해싱 알고리즘을 사용하여 충돌이 날 확률을 줄일수 있다. 이 방식들의 위험성에 대해서도 논할수 있다.
</div>
</details>

<br/><br/>
___


### 115. LRU캐시를 구현한다고 하면 어떤 방식들이 있을까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 53번 문항에 더해 double linked list와 map을 사용하는 방법이나, min heap을 이용하는 방법들을 얘기하고 어떻게 데이터 노드를 구성할지 얘기할수 있다.
</div>
</details>

<br/><br/>
___


### 116. 자바.python, node, c, go등으로 어플리케이션을 작성했다. 
본인이 자신있는 언어/환경에 대해서,
 이 어플리케이션이 실행된 후의
시스템의 전체 메모리 layout 요소에 대해서 애기하시오.

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> code영역, heap영역, stack영역, 초기화 변수 영역등

어플리케이션 run time 상태에 대한 인식 수준을 다양하게 파악하기 위한 문제.
</div>
</details>

<br/><br/>
___


### 117. 덱 - deque(double ended queue)에 대해 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 양방향으로 데이터 삽입 , 삭제가 가능한 자료구조
- 사용법에 따라 stack, queue로 사용가능
- Scroll - 입력은 한쪽으로 가능하고 출력은 양쪽에서 모두 가능
- Shelf - 출력이 한쪽에서만 가능하고 입력이 양쪽에서 모두 가능
- ArrayDeque, LinkedList, ConcurrentLinkedDeque, LinkedBlockingDeque 등..
</div>
</details>

<br/><br/>
___


### 118. Sort의 종류 아는대로 설명하고 각각의 time complexity 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Selection/Bubble/Insertion/Heap/Quick/Merge/Bucket/Radix
</div>
</details>

<br/><br/>
___


### 119. 하나의 array(list)를 두개의 쓰레드에서
 동시에 접근해서 element를 추가하려고 한다. 
이때 생길수 있는 문제와 가능한 해결방안들

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 병렬성 이슈에 대해 다양한 수준에서 판단할수 있다.
왜 동시에 접근하면 문제가 생기는지 물어볼수 있다. 메모리와 캐시 레이어 기준으로 설명해주면 더욱 좋다.
해결방법으로복제방식인 copyOnWriteArrayList 를 지원하는 컬렉션을 사용할수 있다. 
혹은 시스템 수준에서 syncronize 키워드로 os의 지원을 받거나 할수도 있다.
</div>
</details>

<br/><br/>
___


### 120. String 클래스를 설계한다면 내부적으로 
어떤 데이터 구조를 갖도록 설계하는 것이 좋을까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 일반적으로 동적 메모리(heap)를 내부에 가지며 문자열을 보관하겠지만, 
동적 메모리는 할당과 해제에 많은 시간이 들기 때문에 문자열의 크기가 작다면 
로컬 메모리(stack)를 사용하는 것과 같은 SSO(Small string optimization) 트릭을 
사용하는 것이 좋다
</div>
</details>

<br/><br/>
___


### 121. 그래프의 탐색순서에 따른 2가지 방법

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 너비 우선 탐색 (Breadth-First Search) : 노드를 탐색할때 시작점에 가까운 모든 노드를 탐색 
- 깊이 우선 탐색 (Depth-First Search) : 노드를 탐색할때 하나의 패스를 끝까지 따라가며 진행할 수 없는 곳에 다다르면 다음 브랜치를 탐색
</div>
</details>

<br/><br/>
___


### 122. 네비게이션, 지하철 길찾기에서와 같이 시작 노드와 목적지 노드가 명확한 그래프의 최단 경로 탐색 (Shortest Path) 에 쓰이는 알고리즘에는 어떤 것이 있는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 벨먼-포드 알고리즘, 다익스트라 알고리즘, A* 알고리즘
</div>
</details>

<br/><br/>
___


### 123. 그래프 최단 경로 탐색 알고리즘의 특징을 설명할 수 있는가?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 벨먼-포드 : 음의 가중치 계산 가능
- 다익스트라 : 벨먼-포드보다 성능이 좋으나 양의 가중치만 가능
- A Star 알고리즘 : 다익스트라를 발전시킨것으로 휴리스틱 추정값을 통해 불필요한 탐색을 방지하도록 개선
</div>
</details>

<br/><br/>
___


### 124. 게시물을 위해 id, title, content를 요소로한 post 자료구조가 있습니다. 게시물에 여러가지 해시태그를 등록할 수 있고 해시태그로 게시물을 검색할 수 있는 기능을 추가하려고 합니다. 자료구조를 개선하고 해시태그 등록 및 검색 과정을 설명해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 자료구조 설계에 대한 실습 경험과 역량을 확인하는데 출제의도가 있습니다.
먼저 post 자료구조에 복수개의 해시태그 정보를 연결할 수 있도록 적합하게 개선했는지 확인합니다.
추가적으로 여러 게시물에 등록되어 있는 특정 해시태그로 검색 시 성능을 고려한 자료구조인지 확인합니다.
자료구조상 정답은 없으니 아래와 같이 예상된 답변을 참고해서 설계 경험과 역량을 평가합니다.

답변 유형1)  post 자료구조에 단순 tags(해시태그 문자열의 배열) 요소를 추가한 개선안 
   >> 해시태그 검색 시 성능에 대해 의견을 추가로 확인합니다.

답변 유형2) 해시태그 검색 시 성능을 고려해 id, tag_name을 요소로한 tag 자료구조를 추가하고, post에는 tag 배열을, tag에는 post배열로, post와 tag의 다중연결을 고려한 개선안
   >> 해시태그 등록 및 검색과정, 게시물 삭제 시 관련 해시태그 정보를 정리하는 과정을 올바르게 설명하는지 추가로 확인합니다.

답변 유형3) 추가적으로 데이터베이스 기반의 최적화를 고려해 post와 tag간의 직접적인 연결을 분리하고 post_id와 tag_id를 요소로한 별도의 연결 자료구조 tag_map을 추가한 개선안
   >> 자료구조관련 기초지식 수준을 넘어선 답변으로 출제의도를 충분히 만족하는 답변입니다.
</div>
</details>

<br/><br/>
___
