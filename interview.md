
### 1. 다익스트라 알고리즘이란 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 여러개의 노드가 있을때 특정한 노드에서 다른 노드로 가는 최단 경로를 계산하는데 현재 노드에서 갈 수 있는 노드중 최단 거리가 짧은 노드를 방문해가며 최단 거리 테이블을 갱신한다.
</div>
</details>

<br/><br/>
___


### 2. 재귀를 활용하여 주어진 문자열이 회문(palindrome)인지 판단할 경우, 참(true)으로 판단할 조건은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 문자열의 길이가 2 이하인 경우, 2. 주어진 문자열의 첫 문자와 끝 문자가 동일하고 나머지 문자열의 길이가 1 이하인 경우
</div>
</details>

<br/><br/>
___


### 3. 시간복잡도가 O(nlogn)보다 빠른 비교 정렬(Comparison Sort)은 존재하는가? 존재/존재하지 않다면, 그 이유는?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 불가능하다. 최소 비교 횟수를 디시전트리를 이용해 증명가능하다.  
(정렬의 하한(Lower Bound)을 묻는 문제. 참고 링크 : https://twinparadox.tistory.com/196)
</div>
</details>

<br/><br/>
___


### 4. 정렬 알고리즘의 stable 과 unstable 속성은 무엇인가요?,  어떤 정렬방법이 여기에 속하나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 값이 동일한 케이스에 대해서 정렬 전의 순서가 보장되면 stable, 그렇지 않고 순서가 달라질 수 있으면 unstable 
stable : merge sort
unstable : quick sort, heap sort
</div>
</details>

<br/><br/>
___


### 5. 패스워드와 같이 사용자 본인만 알아야할 정보를 저장한다고 했을때 보안적 안전하게 사용할수 있는 암호 알고리즘 종류는 무엇인가요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 복호화가 불가능한 단방향(hash) 암호화 알고리즘인 SHA-2이상을 사용하여야 하며, 추가적으로 salt를 적용하면 좀 더 안전합니다
</div>
</details>

<br/><br/>
___


### 6. 허프만코딩이란? 동작 방식은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 개념: 데이터를 압축하는데 사용하는 방법
자주 등장하는 문자는 짧은 비트로 표현하고, 그렇지 않은 문자는 긴 비트로 표현하여,
전체 데이터를 표현하는데 필요한 비트수를 줄임.

방식: 문자의 출현빈도를 계산하고, 각 문자의 출현 빈도수를 비교하면서 허프만 트리를 구성한다.
이 후 루트로부터 문자까지의 이진문자를 읽어 해당 문자의 이진코드를 얻고 이를 사용한다.
</div>
</details>

<br/><br/>
___


### 7. 암호화 알고리즘의 종류에 대해 알고 계시면 간략하게 분류하고 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 대칭형 암호화(ex AES) 2. 비대칭형 암호화(ex RSA) 3. 단방향 암호화(ex MD5, SHA-1, SHA-2) 알고리즘 방식으로 분류

대칭형 암호의 경우 암호화, 복호화 키가 같고 AES가 널리사용된다. 
비대칭형 암호의 경우 Public/Private 키가 존재하며 Public 키는 복호화시, Private는 암호화시 사용된다.
단방향 알고리즘은 해싱을 사용해 암호화하는 것으로 해싱을 이용해서 암호화는 가능하지만 복호화가 불가능하다. MD5, SHA 같은 방식이 있다.
</div>
</details>

<br/><br/>
___


### 8. 피보나치 수열을 구현하는 방법과 각 방법의 시간 복잡도는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀 O(2^N), 동적 O(n^2), 반복 O(n)
</div>
</details>

<br/><br/>
___


### 9. 이진 검색 트리의 탐색, 삽입, 삭제 연산의 평균적인 시간 복잡도는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> O(h), h는 트리의 높이
</div>
</details>

<br/><br/>
___


### 10. DFS와 BFS를 설명하고 수도코드로 작성해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS(스택/재귀 이용), BFS(큐 이용) 수도코드 작성
</div>
</details>

<br/><br/>
___


### 11. N개의 공 중에 하나만 무게가 무거울 경우 무거운 공을 어떤 방식을 찾을수 있는지, 그때의 시간복잡도는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형탐색 O(N) 또는 이진 탐색 O(logN) 사용
</div>
</details>

<br/><br/>
___


### 12. N 개의 공 모두가 무게가 다를 경우 중간 무게 구슬을 찾는 방식?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> BFS,DFS 사용 목적
</div>
</details>

<br/><br/>
___


### 13. 재귀 알고리즘이란 무엇이며 시간복잡도는 어떻게 되는지?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 함수가 자기 자신을 호출하여 문제를 해결하는 기법이며 시간복잡도는 O(n) 이다.
</div>
</details>

<br/><br/>
___


### 14. MergeSort의 시간복잡도를 구하는 방법과 재귀호출을 통한 분할정복(divide and conquer) 알고리즘의 시간복잡도 도출방법에는 무엇이 있는지 설명하시오

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> MergeSort와 같이 재귀호출을 하는 알고리즘의 시간복잡도는 점화식(recurrence relation)을 통해 정의할 수 있다. 
n개의 요소를 merge sort한다고 하고, merge sort가 절반으로 나눠 문제를 해결한다고 할 때, n/2크기로 나눠 각각 2번 재귀호출하고, 중간 index를 찾아 자르는 것이므로 상수시간에 절반으로 분할 가능하고, n개의 원소를 머지하는데 n이 걸린다. 
따라서 점화식으로 

T(n) = 2T(n/2) + n 으로 나타낼 수 있다.

점화식으로부터 시간복잡도를 구하기 위한 방법으로는 

1. 치환법 (substitution)
2. 재귀트리 (recursion tree)
3. 마스터 정리(master theorem) 

가 있다.

1. 치환법은 시간복잡도 (upper bound든 lower bound 든)를 추측해서 치환후 증명하는 방법이라 치환하는 것은 어렵지 않지만, 추측하는 것이 어렵다.

2. 재귀트리는 점화식에 n부터 분할될 때마다 도출되는 값들을 종료조건에 해당하는 leaf node까지 트리로 그려 나타내고, 각 트리의 레벨의 합을 구함으로써 시간복잡도를 계산할 수 있다.

3. 마지막은 마스터정리인데, 머지소트의 경우 마스터정리로 구할 수 있지만, 마스터정리가 모든 점화식의 시간복잡도를 계산할 수 있는 것은 아니다.
      특정조건에 해당된다면 마스터정리로 시간복잡도를 구할 수 있다.

인터뷰 자체가 암기력을 테스트하는 것이 아니므로, 마스터정리의 특정조건 같은거 까지 설명하는지 볼 필요는 없다고 생각합니다. 
재귀호출을 통한 분할정복 알고리즘을 구현할 때 구현자체 뿐 아니라, 구현된 내용의 시간복잡도를 공식으로 정의하고 분석하는 방법에 대한 이해가 있는지 확인하는 목적이라 생각했습니다.
</div>
</details>

<br/><br/>
___


### 15. 길이가 N 인 두개의 리스트에서 공통된 요소를 구하는 알고리즘과 시간복잡도는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 첫 번째 리스트의 요소마다 두 번째 리스트에 대해서 선형 탐색: O(n^2)
두 번째 리스트를 HashMap 이나 TreeMap 에 저장 후 첫 번 째 리스트 요소마다 Map 에서 탐색
 > HashMap: 평균 O(n), 최악 O(n^2)
 > TreeMap: 평균 O(n*logn), 최악 O(n*logn)
</div>
</details>

<br/><br/>
___


### 16. N 의 값이 너무 커 메모리에 다 올려 놓을 수 없을 경우 해결 방법

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 각각의 리스트를 디스크를 이용한 머지소트로 정렬. 각각의 정렬된 리스트를 머지소트를 이용하여 공통 요소 추출
</div>
</details>

<br/><br/>
___


### 17. - 퀵소트의 단점 (O(N^2) 시간복잡도)을 어떻게 개선할 수 있을지. 피봇을 잘 고르는 법 말고, 다른 알고리즘의 장점을 가져올 수 있을지 
- 힙소트로 전환하는 타이밍은 언제가 좋을지. 
- 왜 힙소트인지. 대신 머지소트는 어떨지

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 퀵소트에서 일정 recursion depth 이후 힙소트로 전환 (Intro sort에서 사용됨)
- 퀵소트의 recursion depth가 O(N)이 될 수 있는 게 문제이므로, C*logN정도에서 전환
- O(N)의 공간복잡도가 추가됨. 힙소트의 O(nlgn) 시간복잡도에 가려졌던 자잘한 연산들이 
  없어져 속도는 조금 빨라질 수 있지만 더 이상 inplace sort가 아니게 됨
</div>
</details>

<br/><br/>
___


### 18. 탐욕 알고리즘 (greedy algorithm) 이란? 어떤 경우에 사용하는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 순간마다 최적의 답을 선택하여 결정하면서 진행하는 최적화 알고리즘
탐욕스러운 선택 조건(Greedy choice property), 최적 부분 구조 조건(Optimal Substructure) 특성을 가진 문제 해결
(선택한 결정이 다른 결정에 영향을 주지 않고, 부분의 최적의 문제의 최적인 경우에 사용)
활동선택 문제, 거스름돈 문제 (동전들이 배수로 이루어져야 함) 등을 답변도 포함
</div>
</details>

<br/><br/>
___


### 19. 페이징 알고리즘 또는 기법에 대해 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> os관점에서 메모리를 블록(페이지) 단위로 나누어서 운용하는 기법.
또는 실제 구현 관점에서 게시판 같은 앱에서 데이터를 한번에 가져오지 않고, 일덩한 덩어리(페이지)로 
나누어서 가져오는 방법
</div>
</details>

<br/><br/>
___


### 20. 페이지 교체 알고리즘의 일종인 LRU, LFU 알고리즘의 개념과
각각의 장단점을 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> LRU : Least Recently Used. 가장 오래 사용되지 않은 페이지를 교체하는 알고리즘
LFU : Least Frequently Used. 참조된 횟수를 카운팅하여 참조횟수가 가장 적은 페이지를 
교체하는 알고리즘
</div>
</details>

<br/><br/>
___


### 21. 정렬된 두 리스트를 병합하여 정렬된 리스트를 반환하는 방법을 설명하고 시간 복잡도를 말하라.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 두 리스트의 front 값을 비교해 작은 값을 선택. 이를 반복한다.
시간 복잡도: (O(n + m))
</div>
</details>

<br/><br/>
___


### 22. 분할정복법(divide & conquer)과 동적계획법(Dynamic programming)의 공통점과 차이점을 설명하세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 공통점 : 풀어야 할 문제를 작은 문제들로 나누고 그 문제를 푼 뒤 다시 합쳐나가는 방식의 접근방식
차이점 : 동적계획법은 나뉘어진 문제가 중복될수있다. 쪼개진 문제에서 풀었던 계산했던 것을 재활용할수있다. 더 복잡한 문제를 빠르게 풀수 있다.
</div>
</details>

<br/><br/>
___


### 23. Counting Sort는 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 각 입력이 특정 집합 S에 속하는 경우에 사용하며, 집합 S의 크기 만큼의 정렬된 배열을 생성하고, 
각 입력은 배열의 값을 1씩 증가시키며 정렬을 수행합니다.
</div>
</details>

<br/><br/>
___


### 24. Counting Sort의 시간 복잡도

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 평균 O(|S| + n), worst case도 O(|S| + n)
</div>
</details>

<br/><br/>
___


### 25. Counting Sort의 시간 복잡도가 매우 빠름에도 불구하고, 사용 빈도가 낮은 이유에 대해 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 집합을 구성하는 원소의 범위에 비례해 공간 복잡도가 증가합니다. 따라서 '범위 조건'이 있는 
제한적인 상황에서 사용해야하기 때문입니다.
</div>
</details>

<br/><br/>
___


### 26. 문자열 뒤집기

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀함수 이용. 배열 루프로 처리했다면 다른 방식에 대해 질의
input.charAt(input.length() - 1) + rev(input.substring(0, input.length() - 1));
함수 앞에 종료조건 (input.length() == 0) 처리
</div>
</details>

<br/><br/>
___


### 27. 페이지랭크 알고리즘을 설명하세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1.구글의 설립자로 널리 알려진 래리 페이지와 세르게이 브린이 개발한 알고리즘으로, 웹 문서의 중요도를 구할 때 사용.
2.페이지 랭크는 더 중요한 페이지는 더 많은 다른 사이트로부터 링크를 받는다는 관찰에 기초하여 인터넷상의 인용되어 지는 링크들을 기반으로 각 사이트들의 중요도를 측정하는 알고리즘.
</div>
</details>

<br/><br/>
___


### 28. CPU가 프로세스를 처리하는 방법에는 여러가지가 고안되었습니다. 그중 대표적으로 FIFO, SJF, PRIORITY, RR이 있는데 각 스케쥴링의 특징을 설명해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> FIFO - 시간순서대로 처리/장시간 점유 문제발생
SJF - 수행시간이 짧은 프로세스 먼저 처리 / 상대적으로 긴 프로세스는 순서가 밀리고 지연 될 수 있음 
PRIORITY - 미리 정해둔 우선순위에 의해 처리 / 우선순위가 적절하게 배분되지 못하면 우선순위가 낮은 프로세스는 지연 될 수 있음
RR - 특정 작은 시간단위로 프로세스를 처리, 평균대기시간이 짧음 / context switch 비용이 큼
</div>
</details>

<br/><br/>
___


### 29. n개의 서로 다른 문자열로 구성된 A Set 와
m개의 서로 다른 문자열로 구성된 B Set 가 존재할때
A와B 에 중복되는 문자열을 가장 빠르게 구하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> intersection set을 구하는 원리
Loop를 돌리면 n*m 번의 루프를 돌아야한다.
갯수가 많아질수록 많아짐.
Hash set을 사용하면 효율적으로 구할수 있음.
</div>
</details>

<br/><br/>
___


### 30. 미로생성 Backtracking, binary-tree, sidewinder 
알고리즘의 특징, 장단점을 설명해주세요.

**난이도:** <span style="color:#000000; font-weight:bold;"></span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> recursive Backtracking - 이웃된 셀중 랜덤으로 하나씩 진행, 더이상 갈 방향이 없는 경우 한 방향씩 되돌아오면서 반복
  장 : 일반적인 복잡한 미로 생성, 단 : 생성이 오래걸린다. 메모리를 많이 사용
binary tree - 랜덤하게 오른쪽으로 진행, 종료시 하단으로 1회, 다음행에서 반복, 최종 행은 다 연결한다.
  장 : 빠르다, 단 : 편향적이고 단순한 모양이 만들어진다. 2개 방향의 곧은 직선이 생김
sidewinder - 첫 행은 다 연결, 이후 랜덤하게 오른쪽으로 진행, 진행블럭중 하나를 상단으로 뚫는다.
  장 : 바이너리트리의 단순함 보완, 단 : 여전히 1개방향의 곧은 직선이 생김.
</div>
</details>

<br/><br/>
___


### 31. O(1), O(logn), O(nlogn), O(n^2) 시간 복잡도를 가지는 알고리즘을 말하고 왜 그런지 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 기본적인 알고리즘들을 알고 있는지, 시간복잡도에 대한 이해가 있는지 확인하는 질문입니다.
O(1): 해시, 한 번의 연산으로 원하는 값을 찾음
O(logn): 바이너리 서치, 원하는 값을 찾기 위해 검색 범위를 절반씩 줄여나감
O(nlogn): 머지 소트, 전체 데이터를 원소 하나의 리스트 n개로 만들고 리스트 두 개씩 합치는 과정을 반복하여 정렬
O(n^2): 버블 소트, 전체 데이터 n개에서 하나를 선택하고 나머지와 비교하는 형태를 반복하여 정렬
</div>
</details>

<br/><br/>
___


### 32. N개 데이터가 존재하는 배열에서 길이가 M인 서브 배열의 합계가 가장 큰 서브 배열을 찾기 위한 방법은 무엇인가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 답변은 크게 두 가지가 있습니다.
첫번째는 단순하게 이중 반복문을 사용하여 최대 값을 구하는 방법 
두번째는 슬라이딩 윈도우란 알고리즘 기법을 이용하여 중복되는 요소를 재사용하는 방법으로 반복문을 줄이는 방법이 있습니다.
이 중에서 두번째 방법을 언급하거나 중복되는 요소를 재사용하는 방법으로 반복문을 줄인다는 말을 언급하면 알고 있다고 판단 할 수 있습니다
</div>
</details>

<br/><br/>
___


### 33. 슬라이딩 윈도우에 대한 알고리즘을 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 기존의 서브 배열의 합이 S 이고 새로운 서브 배열에서 빠지는 맨 앞 원소가 A 고 그 새로운 서브 배열에 들어오게 된 원소를 B 라고 하면 새로운 배열의 합은 S - A + B 가 된다.
위와 같은 내용을 설명하면 맞았다고 판단할 수 있습니다. 또한 시간 복잡도를 O(N)이라고 말한다면 정확히 알고 있다고 판단됩니다.
</div>
</details>

<br/><br/>
___


### 34. 다음 코드가 무엇을 의미하는지 설명해주세요: 
((n & (n-1)) == 0)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 2진수 기준으로 스스로와 -1 한 값과의 AND 연산 결과가 0이 나오는 케이스는 N이

1. 0000 & 1111 == 0 (N=0, 언더플로우 케이스) 
2. 0001 & 0000 == 0 
    0010 & 0001 == 0
    0100 & 0011 == 0
    1000 & 0111 == 0 (N=2^x, 2의 지수인 케이스)

두 가지 경우입니다. 코드를 기준으로 데이터타입 형태와 맞추어 동작을 예측할 수 있는지 확인합니다.
</div>
</details>

<br/><br/>
___


### 35. 내림차순 정렬을 위해 구성한 최대 힙 트리에서 최댓값을 제거했을 때, 나머지 요소들로 다시 최대 힙 조건을 만족하는 트리를 재구성하는 절차에 대해 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1. 트리의 마지막 노드를 가져와 제거된 루트 노드(최대 힙의 최댓값) 위치에 삽입 (완전 이진 트리 속성 유지)
2. 삽입된 노드를 부모로 놓고 자식 노드들과 값을 비교해 자식의 값이 더 큰 경우 서로 위치를 교환한다. (자식 노드가 모두 큰 경우 더 큰 값과 교환)
3. 2번 과정을 반복
</div>
</details>

<br/><br/>
___


### 36. linked list를 역순으로 출력하는 방법

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> recursion으로 다음 link를 주고 호출한 다음 현재 link를 출력하는 식으로 구현
</div>
</details>

<br/><br/>
___


### 37. 공개키 암호화 알고리즘에 대해 설명하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 동작과정을 설명한다면 개념을 알고있음. 문제점과 해결방안을 알고있다면 이해가 깊음. 각 암호화 알고리즘의 구현을 설명한다면 저희팀에
* 동작과정 : 양쪽에 각각 공개키/비밀키를 생성하고 각자의 공개키를 공유. A는 B의 공개키로 암호화한 정보를 B에게 전달. B는 자신의 개인키로 복호화
* 문제점과 해결방안 : 대칭키 대비 느린 암복호화 속도 -> 데이터는 대칭키로, 대칭키는 공개키로 암호화 하는 방식 사용 / MITM -> pki 시스템 이용
</div>
</details>

<br/><br/>
___


### 38. 선형 / 이진 / 해시 탐색 법의 탐색 방법과 특징에 대하여 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형 탐색은 앞에서 부터 순서대로 데이터가 있는지 확인하는 방법. 최악의 경우 모든 데이터를 탐색 해야 함.
이진 탐색은 가운데  데이터를 먼저 탐색 한 후 요소의 크기를 비교하여 탐색 범위를 좁혀 나감. 데이터가 이미 정렬해야 사용 가능함.
해시 탐색은 데이터와 저장한 위치와 미리 연결하여 빠른 시간에 데이터를 탐색할 수 있도록 함. 해시 충돌이 빈번할 경우 탐색 속도가 증가함
</div>
</details>

<br/><br/>
___


### 39. 최단거리 알고리즘에 대해서 알고있는 종류에 대해서 간단하게 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 다익스트라, 벨만-포드, 플로이드 등의 알고있는 알고리즘에 대해서 설명
각 알고리즘들의 간략한 특징 (single-source, all pairs)
어떤 경우에 어떤 알고리즘을 선택해야 하는지까지
</div>
</details>

<br/><br/>
___


### 40. BFS로도 최단거리를 계산할 수 있는데 최단거리알고리즘을 어떨 때 사용하는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 간선 가중치 있는 경우 알고리즘 사용
가중치가 음수도 존재하는 경우 구분 사용 설명
음수도 해결가능한 알고리즘을 사용하는게 무조건 좋지 않은가? 라는 추가 질문을 통해 알고리즘의 시간복잡도 차이와 성능에 대한 인지 확인
</div>
</details>

<br/><br/>
___


### 41. 알고리즘의 복잡도를 대체로 Big-o 표기법으로 비교하는 이유를 설명해주세요
(이어서)
중첩 반복문이 있고 두 반복문 다 인풋 크기에 비례하는 경우 big-o표기법의 시간 복잡도는? 
ex) def print_pairs(list):
    for i in range(len(list)):
        for x in range(len(list)):
            print(list[i], list[x])

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 최선의 경우는 어떤 알고리즘을 돌려도 만족할만한 결과를 얻을 수 있어서 비교 할수가 없고,
평균적인 값의 비교는 평균값을 도출하기가 힘들기때문에 최악의 경우를 비교 기준으로 삼아 판단하면 
평균과 가까운 성능으로 예측이 가능하여 Big-o를 대체로 사용함. 최악이란 아무리 오래걸려도가 이시간안에는 끝남을 같이 설명 해주면 좋음.
- O(n^2)
</div>
</details>

<br/><br/>
___


### 42. 해시 테이블에 데이터를 저장하는 방식과 검색 방식 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 해시 충돌 시 저장 방식 2가지 (Open Addressing, Separate Chaining) 설명 확인
</div>
</details>

<br/><br/>
___


### 43. 일련의 문자열이 주어질 때, 한번만 사용한 첫번째 문자는 어떻게 찾을 수 있을까?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 문자를 순차적으로 선택하고 해당 문자가 문자열에서 중복되는지 일일히 검사
- 문자열을 순회하면서 키에 대해 순서를 가진 맵에 (문자, 빈도수) 형태로 저장 후 조회
- 각 문자에 대해 counting sort 방식으로 빈도수 저장, 문자열을 distinct하여 각 문자의 빈도수를 빈도수 배열에서 차례로 검사 등등
</div>
</details>

<br/><br/>
___


### 44. 어떤 데이터 파일에 100만개의 정렬되지 않은 데이터가 있을 때, 상위 1000개의 아이템을 찾는 방법은?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 100만개의 데이터를 정렬 후, 상위 1000개를 찾는다.
ㄴ 이 방식의 단점 : in-memory sort 어려움, 정렬을 위한 추가 디스크 공간 필요, 대부분의 데이터는 정렬될 필요 없음 등
- 크기가 1000이고, heap tree 구조를 가진 자료구조에 데이터를 순차적으로 넣는데, 자료구조의 크기가 1000 이하라면 무조건 넣고, 1000이라면 root node와 비교하여 작은 경우에만 넣고, root node는 삭제한다.
ㄴ in-memory sort의 개념, heap tree 자료구조의 개념, 제시한 방식의 시간/공간복잡도 등 설명 확인, quick selection 이야기도 하면 가점
</div>
</details>

<br/><br/>
___


### 45. 비번을 안전하게 저장하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 비번을 salt 와 함께 SHA-{256,512} 를 사용하여 저장한다.
</div>
</details>

<br/><br/>
___


### 46. 최대공약수와 최소공배수를 구하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 최대공약수 : 유클리드 호제법을 사용하며 %를 사용하여 구한다. 뺄셈(-) 을 사용할수도 있음
최소공배수 : 두개의 숫자를 곱하고 최대 공약수로 나눈다.
</div>
</details>

<br/><br/>
___


### 47. 힙 정렬에 대해서 설명하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 부모 노드가 자식 노드보다 크거나(최대 힙) 작은(최소 힙) 완전 이진 트리인 힙의 특성을 이용한 정렬로서, 
힙의 구축 과정 이후 루트 원소를 힙의 마지막 원소와 교체, 힙의 크기 감소, 힙의 특성 유지 과정을 반복함으로써 정렬한다.
오름 차순 정렬인 경우엔 최대 힙을 사용하고, 내림 차순 정렬인 경우엔 최소 힙을 사용한다.
어떠한 입력에도 NlogN의 성능이 보장되지만, 일반적으로 잘 구현된 퀵 정렬보다 느리다.
</div>
</details>

<br/><br/>
___


### 48. 길이가 N인 문자열이 주어졌을 때 문자열 안에서 반복되어서 등장하는 substring 중 가장 긴 문자열의 길이를 구하는 방법은? (반복부분문자열) 
ex) aabaaba -> aab가 2번 반복적으로 등장하면서 가장 긴 substring이므로 답은 3

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> brute-force : 모든 substring에 대해서 반복되는 문자열이 있는지 모두 탐색 O(N^4)
kmp : O(N^3) : 모든 substring에 대해서 kmp를 사용하여 전체 문자열 내에서 반복적으로 등장하는지 검색 O(N^3)
kmp + binary-search : 최대 길이 L을 고정하여 길이가 L인 substring 중 반복적으로 등장하는 문자열 존재 여부를 kmp로 확인하고 최대 길이 L을 binary-search로 탐색하여 찾음 O(N^2 logN)
hash : 해시를 이용하여 kmp의 검색 기능을 대체하여 kmp와 동일한 방식으로 해결  O(N^2)
hash + binary-search : 해시를 이용하여 kmp 검색 기능을 대체하여 kmp와 동일한 방식으로 해결 O(NlogN)
</div>
</details>

<br/><br/>
___


### 49. 크기를 알 수 없는 리스트의 모든 요소의 합을 구하시오. 리스트의 크기가 아주 크다면?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> sum(xs, acc = 0) = if (empty?(xs)) acc else sum(tail(xs), acc + head(xs))
</div>
</details>

<br/><br/>
___


### 50. 중첩된 리스트의 모든 요소의 합을 재귀호출을 이용해서 작성하시오

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> sum(xs, acc = 0) = if (empty?(xs)) acc else sum(tail(xs), acc + if (list?(head(xs)) sum(head(xs)) else head(cs))
</div>
</details>

<br/><br/>
___


### 51. 크기를 알 수 없는 리스트에서 처음 최대 N개의 합을 구하는 알고리즘을 작성하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> sumn(xs, n, acc = 0) = if (empty?(xs)) acc elseif (n == 0) acc else sumn(tail(xs), n - 1, acc + head(xs))
</div>
</details>

<br/><br/>
___


### 52. depth-first vs breadth-first 탐색이란? 차이점?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> depth-first는 자식과 그 아래를 먼저 다 탐색, breadth-first는 sibling 먼저 다 탐색
</div>
</details>

<br/><br/>
___


### 53. 각각의 장단점?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> depth-first는 구현 쉬움 (recursive), breadth-first는 탐색속도가 상대적으로 빠름
</div>
</details>

<br/><br/>
___


### 54. 그리디 알고리즘의 결과는 항상 최적해 인가? 그럼에도 사용하는 이유는? 최적해를 구해야 할 때는 어떤 알고리즘을 사용해야 하나

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 최적해는 아님,  최적해를 구하는 시간보다 빠른 시간내에 적절한 수준의 답을 구할 수 있음
</div>
</details>

<br/><br/>
___


### 55. 그리디 알고리즘을 사용하기에 적당한 상황과 그렇지 않은 상황, 이유

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 초급
</div>
</details>

<br/><br/>
___


### 56. 정렬 알고리즘의 안정적 특성과 불안정적 특성에 대해서 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> sort 이전의 동일 key를 가진 element의 순서가 sort 후와 동일하면 안정적(stable), 그렇지 않으면 unstable이다.
</div>
</details>

<br/><br/>
___


### 57. 불안정적 특성의 정렬 알고리즘 종류

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> selection sort, heap sort, quick sort 등
</div>
</details>

<br/><br/>
___


### 58. 어떤 경우에 불안정적 특성의 정렬알고리즘을 사용하면 안되는지?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 동일 key의 순서를 보장해야 하는 구조에서는 불안정적 특성의 정렬알고리즘을 사용하면 안된다
</div>
</details>

<br/><br/>
___


### 59. O(1) 시간 복잡도를 가질 수 있는 데이터 저장 방법은 무엇인가

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Direct-Address 해시 테이블(알고리즘) 사용
</div>
</details>

<br/><br/>
___


### 60. Direct-Address 의 단점으로 과도한 공간 사용을 꼽을 수 있는데 해결 할 수 있는 방법은 무엇인가? 그 방법의 문제점은 없는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 저장하고자 하는 키의 수보다 적은 해시 테이블의 사이즈를 적용함, 충돌 문제가 발생할 수 있고, 해시된키에 리스트를 붙이거나 해시의 사이즈를 점진적으로 늘려서 해결 할 수 있다.
</div>
</details>

<br/><br/>
___


### 61. 피보나치 수열을 수도코드로 구현해보시요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 피보나치 수열을 코드로 구현
</div>
</details>

<br/><br/>
___


### 62. 재귀로 구현했다면 루프 방식으로 변경해보세요. 루프 방식이면 재귀로 변경해보세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀와 루프의 변환
</div>
</details>

<br/><br/>
___


### 63. 카카오에서 전체 사용자 중 10% 에게만 다른 디자인의 UI를 적용하는 A/B 테스트를 진행해보기로 했다.
사용자 아이디가 UUID와 유사하게 '0'부터 '9'까지의 캐릭터로 랜덤하게 발급된 32자 형식으로 주어진다 가정하고 매 요청마다 랜덤하게 실험군인지 여부를 판단하는 방법을 말씀해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - '0'부터 '9' 중에 임의의 캐릭터 하나를 정해 아이디의 첫번째(or 임의의 자리) 캐릭터 값과 비교해서 같다면 실험군이다.
- 아이디를 hashCode 또는 정수로 변환 후 10으로 mod 연산 후 0(or 0-9 중에 임의의 수)이면 실험군이다. 
- (오답) 아이디와 상관없이 0~9 사이에 난수(random)를 발생시켜 특정값(예를들어, 0)만 비교해서 실험군으로 판단도 가능 하지만 사용자 중 10% 란 요구사항에 부합하지 않음.
- 기타 답변의 경우에도 매 요청마다 사용 할 수 있는 수준의 성능이고 실험군이 사용자 기준으로 고정된다면 OK
</div>
</details>

<br/><br/>
___


### 64. 해당 실험군이 하루마다 자동으로 바로 이전 실험군과는 겹치지 않도록 변경할 수 있는 방법을 추가적으로 말씀해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

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


### 65. pow(x,n) 함수를 작성하세요(x^n)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> divide and conquer 알고리즘으로 time complexity: O(n), space complexity: O(1)
</div>
</details>

<br/><br/>
___


### 66. 위 함수를 time complexity: O(Log y) 가 되도록 iterative하게 변경

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> pow(x, y/2)를 한번 계산한 값을 활용
</div>
</details>

<br/><br/>
___


### 67. 방향 그래프에 사이클이 존재하는지 알아내시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS를 사용하여 back edge가 존재하는지 확인
</div>
</details>

<br/><br/>
___


### 68. 버블 정렬이란?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서로 인접한 두 원소를 비교하여 정렬하는 알고리즘. 시간복잡도가 O(n2) 느리지만,코드가 단순.
</div>
</details>

<br/><br/>
___


### 69. 버블 정렬에서 시간복잡도를 최적화하기 위한 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서로 교환이 일어나지 않으면 정렬를 중지하도록 함.
</div>
</details>

<br/><br/>
___


### 70. 문자열을 루프(반복)없이 뒤집는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀 이용: input.charAt(input.length() - 1) + rev(input.substring(0, input.length() - 1));
함수 앞에 종료조건 (input.length() == 0) 처리
</div>
</details>

<br/><br/>
___


### 71. 선형 / 이진 / 해시 탐색 법의 탐색 방법과 특징에 대하여 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형 탐색은 앞에서 부터 순서대로 데이터가 있는지 확인하는 방법. 최악의 경우 모든 데이터를 탐색 해야 함.
이진 탐색은 가운데  데이터를 먼저 탐색 한 후 요소의 크기를 비교하여 탐색 범위를 좁혀 나감. 데이터가 이미 정렬해야 사용 가능함.
해시 탐색은 데이터와 저장한 위치와 미리 연결하여 빠른 시간에 데이터를 탐색할 수 있도록 함. 해시 충돌이 빈번할 경우 탐색 속도가 증가함
</div>
</details>

<br/><br/>
___


### 72. 모든 재귀함수는 동적프로그래밍이 가능한가 ? 그 이유는 ?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 정답: 동적 프로그래밍은 피보나치 함수처럼 재귀적 중복이 일어나는 경우를 해결하는데 사용한다. 따라서 정렬 알고리즘 같이 중간 결과에 중복이 없는 경우엔 사용할 수 없다. 
가능하다고 대답한 경우: 혹시 놓친 케이스는 없는지 ?를 다시 물어본후 대답을 수정하고 위의 이유를 말하면 OK
</div>
</details>

<br/><br/>
___


### 73. 주로 사용하는 언어로 피보나치 함수를 동적프로그래밍 기법으로 작성해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 작은수의 결과를 캐시해서 재사용하도록 구현하면 인정
</div>
</details>

<br/><br/>
___


### 74. 전체 n 개의 데이터에서 top k 개를 고르려면 어떤 방법들이 있을까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 정렬 후 앞(또는 뒤)에서 k 개 선택
- 크기 k 인 priority queue 사용
- quick select 사용해서 k 개 선택
- 등등 이외 가능한 다른 방법들
</div>
</details>

<br/><br/>
___


### 75. - 앞에서 고른 방법의 시간복잡도와 공간복잡도는 어떻게 되나요? 이에 근거해서 어떤 경우에 어떤 방법을 쓰는게 효율적일까요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - k 가 n 에 비해 상당히 작을 경우 전체 정렬은 비효율적임. n 을 메모리에 올릴 수 있다면 quick select 후 고른 것만 필요에 따라 정렬해서 반환. n 이 크다면 priority queue 사용 등등..
- 각 방법의 트레이드 오프에 대한 언급과 이에 따른 결정이 합리적인지를 중점적으로 판단.
</div>
</details>

<br/><br/>
___


### 76. 한번에 계단을 1개 혹은 2개를 올라갈 수 있다고 할 때, 100개의 계단을 올라갈 수 있는 경우의 수는 어떻게 구할 수 있을까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 각 1 step, 2 step을 올라가는 경우에 대한 tree 를 구성하여 경우의 수 합산. time complexity O(2^n)
- f(N) = f(N-1) + f(N-2) 로 착안하여 결과값을 저장하며 계산하도록 구현(DP). time complexity O(n), space complexity O(n)
</div>
</details>

<br/><br/>
___


### 77. 좀 더 최적화할 방법이 있을까요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - f(N) = f(N-1) + f(N-2) 공식이 피보나치 수 공식과 동일함에 착안하여 루프로 N번째 피보나치 수 출력으로 구현 time complexity O(n), space complexity O(1)
</div>
</details>

<br/><br/>
___


### 78. 피보나치 수열의 항 구하는 문제를 분할정복법을 사용해 풀 경우 어떤 문제점이 발생하나요?
그 문제점을 해결하기 위해 사용할 수 있는 방법은 무엇이 있나요?
해당 방법으로 이항계수 (5 3)을 구하는 과정을 설명해보세요. ((n k) = (n-1 k-1) + (n-1 k) 임은 제시해줌)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재계산.
동적계획법(=다이나믹 프로그래밍).
bottom-up으로 필요한 것만 계산해나가는 과정을 제대로 설명하면 OK.
</div>
</details>

<br/><br/>
___


### 79. 힙정렬 이란? (힙정렬로 만들어진 binary heap 자료구조의 특징).
힙정렬의 Time Complexity

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> binary heap 자료구조를 이용한 sorting 방법 (binary heap은 부모 노드의 우선순위가 자식노드보다 높은 완전이진트리. 높은 값이 우선순위가 높은 경우 max heap, 낮은 값이 우선순위가 높은 경우 min heap)
주어진 배열을 binary heap으로 만든 후 삭제 연산을 이용하여 정렬 리스트를 만듬. 복잡도는 O(nlogn). - 구체적으로 힙을 만드는데 O(N), 삭제연산을 이용하여 정렬하는데 (N-1)*O(logN) 이므로 총 O(NlogN)
삭제연산은 root와 가장 마지막 노드를 교차한 후 다운힙
</div>
</details>

<br/><br/>
___


### 80. n개의 배열이 주어졌을 때, 가장 큰 값과 가장 작은 값을 한꺼번에 찾는 방법은?
비교 횟수를 줄이려면 어떻게 하면 될까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형 탐색을 각각 하면 2n번.
우선 큰값고 비교해서 더 크면 큰값만 업데이트, 더 작으면 작은값과 비교. 평군 1.5n, 최악 2n
둘씩 짝을 지어 큰값과 작은 값 집합으로 나누고, 큰갑끼리, 작은값끼리 비교. 최악 2n번
</div>
</details>

<br/><br/>
___


### 81. 가장 큰 k개를 찾으려면?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> k값이 크다면 정렬 후 큰 k개를 반환 O(n log n)
퀵정렬을 변형한 퀵 selection 으로 하면 O(n)
</div>
</details>

<br/><br/>
___


### 82. 루프 없이, 자연수 1부터 n까지 합을 구하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> n*(n+1)/2 수식사용
</div>
</details>

<br/><br/>
___


### 83. 루프를 사용하는 경우와 시간 복잡도가 어떻게 달라지나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 수식사용은 상수 O(1), 루프는 선형 O(n)
</div>
</details>

<br/><br/>
___


### 84. 공 8개가 있는데 7개는 무게가 동일하고 하나만 약간 무거울 때 무거운 공을 어떻게 찾을 수 있을까? (비교 횟수도 같이 물어봄)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형탐색 O(N), 이진탐색 O(logN)
이진탐색으로 접근하면 3번에 가능
</div>
</details>

<br/><br/>
___


### 85. 위 문제에서 최소 비교로 무거운 공을 찾아낼 수 있는 방법과 비교 횟수는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 2번 (이진탐색 응용)
먼저 6개를 선택해서 양쪽에 3개씩 올림 (1번 비교)
  - 서로 같을 경우 -> 선택하지 않은 2개를 서로 비교
  - 서로 다른 경우 -> 무거운 쪽 3개 중 2개를 뽑아 다시 비교 후 같으면 안 뽑힌 공, 다르면 기우는 공
</div>
</details>

<br/><br/>
___


### 86. 길이가 n인 숫자 배열이 주어졌을때, merge sort 하는 방법과 시간복잡도 공간복잡도를 Big-O 표기법으로 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 알고리즘설명 : 분할정복방식으로 배열을 나눠가며 작은 단위로 만들어 정렬 후 합치는 과정을 설명, 시간복잡도 : O(nlog), 공간복잡도 : O(nlogn) 이라고 설명하면 개선할 수 없는지 재질문 O(n) 이라고 대답한 경우 ok
</div>
</details>

<br/><br/>
___


### 87. 머지소트의 경우 퀵소트와 같은 시간복잡도를 가지는데 머지소트의 장점은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 메모리에 다 올리기 힘든 큰 사이즈이 데이터도 디스크를 활용해 정렬하시 수월, 기본구현 방법에 있어 stable sort 이다.
</div>
</details>

<br/><br/>
___


### 88. DFS와 BFS 대해 이야기 해보고, 간단하게 수도코드를 작성해 보자

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS 는 stack 재귀호출 , BFS는 queue 를 이용하여 코딩
</div>
</details>

<br/><br/>
___


### 89. 정렬 알고리즘 중 가장 빠른 방식은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 퀵 정렬 (Quick Sort)
퀵정렬은 분할 정복 (Divide and conquer)을 이용하여 정렬을 수행하는 알고리즘이다. 
퀵정렬은 평균적으로 nlogn의 시간복잡도를 가지지만, 최악의 경우 n^2의 시간복잡도를 가진다. 
빅오표기법으로 표현한다면 시간복잡도는 O(n2)입니다.

특징
1. 랜덤배열에서 빠른 정렬 속도를 보인다.
2. 피벗(pivot)을 선정하는 방법에 따라 속도가 달라진다.
3. 순열이나 역순의 경우 매우 느린 속도를 보인다.
4. 재귀함수 기반으로 구현시 복잡하게 생각될 수 있다.
</div>
</details>

<br/><br/>
___


### 90. 길이가 N인 숫자 배열이 주어졌을때, 증가하는 형태의 가장 긴 부분 수열의 길이를 구하는 방법을 설명하시오

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> LIS(Longest Increasing Sequence) 문제로, 
- 부분 수열을 구성해 나갈 때, 증가하는 순서대로 숫자를 고르면서, 고른 수열의  길이가 최대 길이가 되도록 숫자를 선택하는 문제입니다.
- LIS[i] =  i 번째 수 까지의 LIS 형태의 숫자 배열이라고 정의하고, 이때, LIS 배열의 길이는 가장 긴 부분수열의 길이가 됩니다.
</div>
</details>

<br/><br/>
___


### 91. (O(N^2)로 설명한 경우) O(N log N)으로 처리할 수 없는지?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 숫자를 처음부터 하나씩 살펴보는건 동일하다. i번째 수 까지 LIS를 구성했다면, j 번쨰 수에 대해 기존에 구성했던 숫자 배열에서 j번째 수보다 작거나 같은 수를 찾아야 하는데, 이는 오름차순으로 된 숫자 배열에서 j번째 수가 들어갈 곳을 찾아야 하고, 이때 Binary Search 하면 된다.
</div>
</details>

<br/><br/>
___


### 92. 2020년 중 두 날짜가 주어질 때 같은 요일인지 확인하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 두 날짜의 차를 구하는 방법을 설명한다
</div>
</details>

<br/><br/>
___


### 93. 위를 구할 때 루프를 사용하지 않는 방법은?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 각 달까지의 총 날짜 수를 미리 계산해두고 사용한다
</div>
</details>

<br/><br/>
___


### 94. 그레고리력에서 1년 1월 1일 이후 임의의 두 날짜가 주어질 때 같은 요일인지 확인하는 방법은?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1년, 4년, 100년, 400년 단위의 날짜 수를 미리 계산해두고 사용한다
</div>
</details>

<br/><br/>
___


### 95. Hash에 대해서 설명할 수 있나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> O(1)로 자주 쓰이는 대표적인 자료구조. 효율적인 탐색을 위한 자료구조로서 key를 value에 대응
</div>
</details>

<br/><br/>
___


### 96. Hash collision이 발생했을때 해결방법을 말씀해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Chaining(해시 충돌이 발생하면 연결리스트로 데이터들을 연결)이나 Open Addressing(다른 버켓에 데이터를 삽입하는 방식)을 이용할수 있다.
</div>
</details>

<br/><br/>
___


### 97. N * N 행렬을 부가적인 행렬없이 90도 회전시키는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> N * N 행렬의 바깥쪽(또는 안쪽) 레이어부터 회전(위쪽 > 오른쪽, 오른쪽 > 아래쪽, 아래쪽 > 왼쪽, 왼쪽 > 위쪽) 이동한다.
</div>
</details>

<br/><br/>
___


### 98. o(nlogn)의 시간복잡도를 가지는 결정론적 알고리즘은 어떤게 있나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 병합정렬과 힙정렬이 o(nlogn)의 시간복잡도를 가지는 전형적인 결정론적 정렬알고리즘. 퀵정렬은 대개의 경우 O(nlogn)의 시간복잡도를 가지나 최악의 경우 O(n^2)이 될수있다.
</div>
</details>

<br/><br/>
___


### 99. (퀵정렬을 얘기했다면) 퀵소트의 경우 랜덤피벗을 사용해도 결정론적 알고리즘이라고 볼 수 있는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 퀵소트는 좀 더 나은 성능을 보여줄것으로 예상되는 랜덤피벗을 사용하는 경우가 있기때문에 항상 결정론적인 것은 아니다.
</div>
</details>

<br/><br/>
___


### 100. depth-first vs breadth-first 탐색이란? 차이점?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> depth-first는 자식과 그 아래를 먼저 다 탐색, breadth-first는 sibling 먼저 다 탐색
</div>
</details>

<br/><br/>
___


### 101. 각각의 장단점?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> depth-first는 구현 쉬움 (recursive), breadth-first는 탐색속도가 상대적으로 빠름
</div>
</details>

<br/><br/>
___


### 102. 그리디 알고리즘의 결과는 항상 최적해 인가? 그럼에도 사용하는 이유는? 최적해를 구해야 할 때는 어떤 알고리즘을 사용해야 하나

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 최적해는 아님,  최적해를 구하는 시간보다 빠른 시간내에 적절한 수준의 답을 구할 수 있음
</div>
</details>

<br/><br/>
___


### 103. 그리디 알고리즘을 사용하기에 적당한 상황과 그렇지 않은 상황, 이유

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 초급
</div>
</details>

<br/><br/>
___


### 104. 정렬 알고리즘의 안정적 특성과 불안정적 특성에 대해서 설명

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> sort 이전의 동일 key를 가진 element의 순서가 sort 후와 동일하면 안정적(stable), 그렇지 않으면 unstable이다.
</div>
</details>

<br/><br/>
___


### 105. 불안정적 특성의 정렬 알고리즘 종류

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> selection sort, heap sort, quick sort 등
</div>
</details>

<br/><br/>
___


### 106. 어떤 경우에 불안정적 특성의 정렬알고리즘을 사용하면 안되는지?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 동일 key의 순서를 보장해야 하는 구조에서는 불안정적 특성의 정렬알고리즘을 사용하면 안된다
</div>
</details>

<br/><br/>
___


### 107. O(1) 시간 복잡도를 가질 수 있는 데이터 저장 방법은 무엇인가

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Direct-Address 해시 테이블(알고리즘) 사용
</div>
</details>

<br/><br/>
___


### 108. Direct-Address 의 단점으로 과도한 공간 사용을 꼽을 수 있는데 해결 할 수 있는 방법은 무엇인가? 그 방법의 문제점은 없는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 저장하고자 하는 키의 수보다 적은 해시 테이블의 사이즈를 적용함, 충돌 문제가 발생할 수 있고, 해시된키에 리스트를 붙이거나 해시의 사이즈를 점진적으로 늘려서 해결 할 수 있다.
</div>
</details>

<br/><br/>
___


### 109. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 피보나치 수열을 코드로 구현
</div>
</details>

<br/><br/>
___


### 110. 재귀로 구현했다면 루프 방식으로 변경해보세요. 루프 방식이면 재귀로 변경해보세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀와 루프의 변환
</div>
</details>

<br/><br/>
___


### 111. 카카오에서 전체 사용자 중 10% 에게만 다른 디자인의 UI를 적용하는 A/B 테스트를 진행해보기로 했다.
사용자 아이디가 UUID와 유사하게 '0'부터 '9'까지의 캐릭터로 랜덤하게 발급된 32자 형식으로 주어진다 가정하고 매 요청마다 랜덤하게 실험군인지 여부를 판단하는 방법을 말씀해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - '0'부터 '9' 중에 임의의 캐릭터 하나를 정해 아이디의 첫번째(or 임의의 자리) 캐릭터 값과 비교해서 같다면 실험군이다.
- 아이디를 hashCode 또는 정수로 변환 후 10으로 mod 연산 후 0(or 0-9 중에 임의의 수)이면 실험군이다. 
- (오답) 아이디와 상관없이 0~9 사이에 난수(random)를 발생시켜 특정값(예를들어, 0)만 비교해서 실험군으로 판단도 가능 하지만 사용자 중 10% 란 요구사항에 부합하지 않음.
- 기타 답변의 경우에도 매 요청마다 사용 할 수 있는 수준의 성능이고 실험군이 사용자 기준으로 고정된다면 OK
</div>
</details>

<br/><br/>
___


### 112. 해당 실험군이 하루마다 자동으로 바로 이전 실험군과는 겹치지 않도록 변경할 수 있는 방법을 추가적으로 말씀해주세요.

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

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


### 113. pow(x,n) 함수를 작성하세요(x^n)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> divide and conquer 알고리즘으로 time complexity: O(n), space complexity: O(1)
</div>
</details>

<br/><br/>
___


### 114. 위 함수를 time complexity: O(Log y) 가 되도록 iterative하게 변경

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> pow(x, y/2)를 한번 계산한 값을 활용
</div>
</details>

<br/><br/>
___


### 115. 방향 그래프에 사이클이 존재하는지 알아내시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS를 사용하여 back edge가 존재하는지 확인
</div>
</details>

<br/><br/>
___


### 116. 버블 정렬에서 시간복잡도를 최적화하기 위한 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서로 인접한 두 원소를 비교하여 정렬하는 알고리즘. 시간복잡도가 O(n2) 느리지만,코드가 단순.
</div>
</details>

<br/><br/>
___


### 117. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 서로 교환이 일어나지 않으면 정렬를 중지하도록 함.
</div>
</details>

<br/><br/>
___


### 118. 문자열을 루프(반복)없이 뒤집는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재귀 이용: input.charAt(input.length() - 1) + rev(input.substring(0, input.length() - 1));
함수 앞에 종료조건 (input.length() == 0) 처리
</div>
</details>

<br/><br/>
___


### 119. 선형 / 이진 / 해시 탐색 법의 탐색 방법과 특징에 대하여 설명하시오.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형 탐색은 앞에서 부터 순서대로 데이터가 있는지 확인하는 방법. 최악의 경우 모든 데이터를 탐색 해야 함.
이진 탐색은 가운데  데이터를 먼저 탐색 한 후 요소의 크기를 비교하여 탐색 범위를 좁혀 나감. 데이터가 이미 정렬해야 사용 가능함.
해시 탐색은 데이터와 저장한 위치와 미리 연결하여 빠른 시간에 데이터를 탐색할 수 있도록 함. 해시 충돌이 빈번할 경우 탐색 속도가 증가함
</div>
</details>

<br/><br/>
___


### 120. 모든 재귀함수는 동적프로그래밍이 가능한가 ? 그 이유는 ?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 정답: 동적 프로그래밍은 피보나치 함수처럼 재귀적 중복이 일어나는 경우를 해결하는데 사용한다. 따라서 정렬 알고리즘 같이 중간 결과에 중복이 없는 경우엔 사용할 수 없다. 
가능하다고 대답한 경우: 혹시 놓친 케이스는 없는지 ?를 다시 물어본후 대답을 수정하고 위의 이유를 말하면 OK
</div>
</details>

<br/><br/>
___


### 121. 주로 사용하는 언어로 피보나치 함수를 동적프로그래밍 기법으로 작성해주세요

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 작은수의 결과를 캐시해서 재사용하도록 구현하면 인정
</div>
</details>

<br/><br/>
___


### 122. 전체 n 개의 데이터에서 top k 개를 고르려면 어떤 방법들이 있을까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 정렬 후 앞(또는 뒤)에서 k 개 선택
- 크기 k 인 priority queue 사용
- quick select 사용해서 k 개 선택
- 등등 이외 가능한 다른 방법들
</div>
</details>

<br/><br/>
___


### 123. - 앞에서 고른 방법의 시간복잡도와 공간복잡도는 어떻게 되나요? 이에 근거해서 어떤 경우에 어떤 방법을 쓰는게 효율적일까요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - k 가 n 에 비해 상당히 작을 경우 전체 정렬은 비효율적임. n 을 메모리에 올릴 수 있다면 quick select 후 고른 것만 필요에 따라 정렬해서 반환. n 이 크다면 priority queue 사용 등등..
- 각 방법의 트레이드 오프에 대한 언급과 이에 따른 결정이 합리적인지를 중점적으로 판단.
</div>
</details>

<br/><br/>
___


### 124. 한번에 계단을 1개 혹은 2개를 올라갈 수 있다고 할 때, 100개의 계단을 올라갈 수 있는 경우의 수는 어떻게 구할 수 있을까요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - 각 1 step, 2 step을 올라가는 경우에 대한 tree 를 구성하여 경우의 수 합산. time complexity O(2^n)
- f(N) = f(N-1) + f(N-2) 로 착안하여 결과값을 저장하며 계산하도록 구현(DP). time complexity O(n), space complexity O(n)
</div>
</details>

<br/><br/>
___


### 125. 좀 더 최적화할 방법이 있을까요?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> - f(N) = f(N-1) + f(N-2) 공식이 피보나치 수 공식과 동일함에 착안하여 루프로 N번째 피보나치 수 출력으로 구현 time complexity O(n), space complexity O(1)
</div>
</details>

<br/><br/>
___


### 126. 피보나치 수열의 항 구하는 문제를 분할정복법을 사용해 풀 경우 어떤 문제점이 발생하나요?
그 문제점을 해결하기 위해 사용할 수 있는 방법은 무엇이 있나요?
해당 방법으로 이항계수 (5 3)을 구하는 과정을 설명해보세요. ((n k) = (n-1 k-1) + (n-1 k) 임은 제시해줌)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 재계산.
동적계획법(=다이나믹 프로그래밍).
bottom-up으로 필요한 것만 계산해나가는 과정을 제대로 설명하면 OK.
</div>
</details>

<br/><br/>
___


### 127. 힙정렬 이란? (힙정렬로 만들어진 binary heap 자료구조의 특징).
힙정렬의 Time Complexity

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> binary heap 자료구조를 이용한 sorting 방법 (binary heap은 부모 노드의 우선순위가 자식노드보다 높은 완전이진트리. 높은 값이 우선순위가 높은 경우 max heap, 낮은 값이 우선순위가 높은 경우 min heap)
주어진 배열을 binary heap으로 만든 후 삭제 연산을 이용하여 정렬 리스트를 만듬. 복잡도는 O(nlogn). - 구체적으로 힙을 만드는데 O(N), 삭제연산을 이용하여 정렬하는데 (N-1)*O(logN) 이므로 총 O(NlogN)
삭제연산은 root와 가장 마지막 노드를 교차한 후 다운힙
</div>
</details>

<br/><br/>
___


### 128. n개의 배열이 주어졌을 때, 가장 큰 값과 가장 작은 값을 한꺼번에 찾는 방법은?
비교 횟수를 줄이려면 어떻게 하면 될까?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형 탐색을 각각 하면 2n번.
우선 큰값고 비교해서 더 크면 큰값만 업데이트, 더 작으면 작은값과 비교. 평군 1.5n, 최악 2n
둘씩 짝을 지어 큰값과 작은 값 집합으로 나누고, 큰갑끼리, 작은값끼리 비교. 최악 2n번
</div>
</details>

<br/><br/>
___


### 129. 가장 큰 k개를 찾으려면?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> k값이 크다면 정렬 후 큰 k개를 반환 O(n log n)
퀵정렬을 변형한 퀵 selection 으로 하면 O(n)
</div>
</details>

<br/><br/>
___


### 130. 루프 없이, 자연수 1부터 n까지 합을 구하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> n*(n+1)/2 수식사용
</div>
</details>

<br/><br/>
___


### 131. 루프를 사용하는 경우와 시간 복잡도가 어떻게 달라지나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 수식사용은 상수 O(1), 루프는 선형 O(n)
</div>
</details>

<br/><br/>
___


### 132. 공 8개가 있는데 7개는 무게가 동일하고 하나만 약간 무거울 때 무거운 공을 어떻게 찾을 수 있을까? (비교 횟수도 같이 물어봄)

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 선형탐색 O(N), 이진탐색 O(logN)
이진탐색으로 접근하면 3번에 가능
</div>
</details>

<br/><br/>
___


### 133. 위 문제에서 최소 비교로 무거운 공을 찾아낼 수 있는 방법과 비교 횟수는?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 2번 (이진탐색 응용)
먼저 6개를 선택해서 양쪽에 3개씩 올림 (1번 비교)
  - 서로 같을 경우 -> 선택하지 않은 2개를 서로 비교
  - 서로 다른 경우 -> 무거운 쪽 3개 중 2개를 뽑아 다시 비교 후 같으면 안 뽑힌 공, 다르면 기우는 공
</div>
</details>

<br/><br/>
___


### 134. 길이가 n인 숫자 배열이 주어졌을때, merge sort 하는 방법과 시간복잡도 공간복잡도를 Big-O 표기법으로 설명해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 알고리즘설명 : 분할정복방식으로 배열을 나눠가며 작은 단위로 만들어 정렬 후 합치는 과정을 설명, 시간복잡도 : O(nlog), 공간복잡도 : O(nlogn) 이라고 설명하면 개선할 수 없는지 재질문 O(n) 이라고 대답한 경우 ok
</div>
</details>

<br/><br/>
___


### 135. 머지소트의 경우 퀵소트와 같은 시간복잡도를 가지는데 머지소트의 장점은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 메모리에 다 올리기 힘든 큰 사이즈이 데이터도 디스크를 활용해 정렬하시 수월, 기본구현 방법에 있어 stable sort 이다.
</div>
</details>

<br/><br/>
___


### 136. DFS와 BFS 대해 이야기 해보고, 간단하게 수도코드를 작성해 보자

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> DFS 는 stack 재귀호출 , BFS는 queue 를 이용하여 코딩
</div>
</details>

<br/><br/>
___


### 137. 정렬 알고리즘 중 가장 빠른 방식은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 퀵 정렬 (Quick Sort)
퀵정렬은 분할 정복 (Divide and conquer)을 이용하여 정렬을 수행하는 알고리즘이다. 
퀵정렬은 평균적으로 nlogn의 시간복잡도를 가지지만, 최악의 경우 n^2의 시간복잡도를 가진다. 
빅오표기법으로 표현한다면 시간복잡도는 O(n2)입니다.

특징
1. 랜덤배열에서 빠른 정렬 속도를 보인다.
2. 피벗(pivot)을 선정하는 방법에 따라 속도가 달라진다.
3. 순열이나 역순의 경우 매우 느린 속도를 보인다.
4. 재귀함수 기반으로 구현시 복잡하게 생각될 수 있다.
</div>
</details>

<br/><br/>
___


### 138. 길이가 N인 숫자 배열이 주어졌을때, 증가하는 형태의 가장 긴 부분 수열의 길이를 구하는 방법을 설명하시오

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

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


### 139. (O(N^2)로 설명한 경우) O(N log N)으로 처리할 수 없는지?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 숫자를 처음부터 하나씩 살펴보는건 동일하다. i번째 수 까지 LIS를 구성했다면, j 번쨰 수에 대해 기존에 구성했던 숫자 배열에서 j번째 수보다 작거나 같은 수를 찾아야 하는데, 이는 오름차순으로 된 숫자 배열에서 j번째 수가 들어갈 곳을 찾아야 하고, 이때 Binary Search 하면 된다.
</div>
</details>

<br/><br/>
___


### 140. 2020년 중 두 날짜가 주어질 때 같은 요일인지 확인하는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 두 날짜의 차를 구하는 방법을 설명한다
</div>
</details>

<br/><br/>
___


### 141. 위를 구할 때 루프를 사용하지 않는 방법은?

**난이도:** <span style="color:#e67e22; font-weight:bold;">중급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 각 달까지의 총 날짜 수를 미리 계산해두고 사용한다
</div>
</details>

<br/><br/>
___


### 142. 그레고리력에서 1년 1월 1일 이후 임의의 두 날짜가 주어질 때 같은 요일인지 확인하는 방법은?

**난이도:** <span style="color:#e74c3c; font-weight:bold;">고급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 1년, 4년, 100년, 400년 단위의 날짜 수를 미리 계산해두고 사용한다
</div>
</details>

<br/><br/>
___


### 143. Hash에 대해서 설명할 수 있나요?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> O(1)로 자주 쓰이는 대표적인 자료구조. 효율적인 탐색을 위한 자료구조로서 key를 value에 대응
</div>
</details>

<br/><br/>
___


### 144. Hash collision이 발생했을때 해결방법을 말씀해주세요.

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> Chaining(해시 충돌이 발생하면 연결리스트로 데이터들을 연결)이나 Open Addressing(다른 버켓에 데이터를 삽입하는 방식)을 이용할수 있다.
</div>
</details>

<br/><br/>
___


### 145. N * N 행렬을 부가적인 행렬없이 90도 회전시키는 방법은?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> N * N 행렬의 바깥쪽(또는 안쪽) 레이어부터 회전(위쪽 > 오른쪽, 오른쪽 > 아래쪽, 아래쪽 > 왼쪽, 왼쪽 > 위쪽) 이동한다.
</div>
</details>

<br/><br/>
___


### 146. 

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 병합정렬과 힙정렬이 o(nlogn)의 시간복잡도를 가지는 전형적인 결정론적 정렬알고리즘. 퀵정렬은 대개의 경우 O(nlogn)의 시간복잡도를 가지나 최악의 경우 O(n^2)이 될수있다.
</div>
</details>

<br/><br/>
___


### 147. (퀵정렬을 얘기했다면) 퀵소트의 경우 랜덤피벗을 사용해도 결정론적 알고리즘이라고 볼 수 있는가?

**난이도:** <span style="color:#2ecc71; font-weight:bold;">초급</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> 퀵소트는 좀 더 나은 성능을 보여줄것으로 예상되는 랜덤피벗을 사용하는 경우가 있기때문에 항상 결정론적인 것은 아니다.
</div>
</details>

<br/><br/>
___
