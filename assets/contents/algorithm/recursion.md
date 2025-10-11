
# 재귀와 완전탐색

재귀는 자기 자신을 호출하는 함수로, 복잡한 문제를 작은 문제로 나누어 해결하는 강력한 기법입니다. 완전탐색과 백트래킹의 기초가 됩니다.

---

## 🔄 재귀 (Recursion)

### 재귀의 원리

**재귀 = 자기 자신을 호출하는 함수**

```

재귀 함수의 구조:

1. Base Case (종료 조건)
2. Recursive Case (재귀 호출)

````

**실생활 예시:**
- 러시아 인형 (마트료시카)
- 거울 속의 거울
- "재귀를 이해하려면 먼저 재귀를 이해해야 한다"

---

### 재귀의 기본 구조

{% raw %}
```java
public class RecursionBasic {
    // 기본 템플릿
    public ReturnType recursiveFunction(Parameters params) {
        // 1. Base Case (종료 조건) - 필수!
        if (종료조건) {
            return 기본값;
        }
        
        // 2. Recursive Case (재귀 호출)
        // - 문제를 작게 만들기
        // - 자기 자신 호출
        return recursiveFunction(더_작은_문제);
    }
}
````

{% endraw %}

---

### 기초 예제

#### 1. 팩토리얼 (Factorial)

{% raw %}

```java
public class Factorial {
    // n! = n × (n-1) × (n-2) × ... × 1
    public int factorial(int n) {
        // Base Case
        if (n <= 1) {
            return 1;
        }
        
        // Recursive Case
        return n * factorial(n - 1);
    }
    
    public static void main(String[] args) {
        Factorial f = new Factorial();
        System.out.println(f.factorial(5));  // 120
        
        // 호출 과정:
        // factorial(5) = 5 × factorial(4)
        // factorial(4) = 4 × factorial(3)
        // factorial(3) = 3 × factorial(2)
        // factorial(2) = 2 × factorial(1)
        // factorial(1) = 1 ← Base Case
        // 역순으로 계산: 1 → 2 → 6 → 24 → 120
    }
}
```

{% endraw %}

---

#### 2. 피보나치 수열 (Fibonacci)

{% raw %}

```java
public class Fibonacci {
    // F(n) = F(n-1) + F(n-2)
    public int fib(int n) {
        // Base Case
        if (n <= 1) {
            return n;
        }
        
        // Recursive Case
        return fib(n - 1) + fib(n - 2);
    }
    
    // 메모이제이션 (최적화)
    public int fibMemo(int n, int[] memo) {
        if (n <= 1) return n;
        
        // 이미 계산한 값이 있으면 재사용
        if (memo[n] != 0) return memo[n];
        
        memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
        return memo[n];
    }
    
    public static void main(String[] args) {
        Fibonacci f = new Fibonacci();
        
        // 기본 재귀: O(2^n) - 매우 느림!
        System.out.println(f.fib(10));  // 55
        
        // 메모이제이션: O(n) - 빠름!
        int[] memo = new int[50];
        System.out.println(f.fibMemo(10, memo));  // 55
    }
}
```

{% endraw %}

**시각화:**

```
fib(5) 호출 트리:
                    fib(5)
                   /      \
              fib(4)        fib(3)
             /     \        /     \
        fib(3)   fib(2)  fib(2)  fib(1)
        /   \     /   \   /   \
    fib(2) fib(1) f(1) f(0) f(1) f(0)
    /   \
  f(1) f(0)

많은 중복 계산 발생! → 메모이제이션 필요
```

---

#### 3. 배열 합 구하기

{% raw %}

```java
public class ArraySum {
    // 배열의 합을 재귀로 구하기
    public int sum(int[] arr, int index) {
        // Base Case: 끝에 도달
        if (index >= arr.length) {
            return 0;
        }
        
        // Recursive Case
        return arr[index] + sum(arr, index + 1);
    }
    
    public static void main(String[] args) {
        ArraySum as = new ArraySum();
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(as.sum(arr, 0));  // 15
    }
}
```

{% endraw %}

---

#### 4. 문자열 뒤집기

{% raw %}

```java
public class StringReverse {
    public String reverse(String str) {
        // Base Case: 빈 문자열 또는 길이 1
        if (str.length() <= 1) {
            return str;
        }
        
        // Recursive Case
        // "hello" → reverse("ello") + "h"
        return reverse(str.substring(1)) + str.charAt(0);
    }
    
    public static void main(String[] args) {
        StringReverse sr = new StringReverse();
        System.out.println(sr.reverse("hello"));  // "olleh"
        
        // 호출 과정:
        // reverse("hello") = reverse("ello") + "h"
        // reverse("ello") = reverse("llo") + "e"
        // reverse("llo") = reverse("lo") + "l"
        // reverse("lo") = reverse("o") + "l"
        // reverse("o") = "o" ← Base Case
        // 결과: "o" + "l" + "l" + "e" + "h" = "olleh"
    }
}
```

{% endraw %}

---

## 🎯 완전탐색 (Brute Force)

### 원리

**모든 경우의 수를 다 확인하는 방법**

```
완전탐색 = 무식하지만 확실한 방법
- 작은 입력 크기에서 유용
- 최적화의 시작점
```

---

### 패턴 1: 중첩 반복문

{% raw %}

```java
public class BruteForce1 {
    // 두 수의 합이 target인 쌍 찾기
    public int[] twoSum(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] + arr[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }
    
    // 시간복잡도: O(n²)
}
```

{% endraw %}

---

### 패턴 2: 재귀로 완전탐색

{% raw %}

```java
public class BruteForce2 {
    // 부분집합의 합이 target인지 확인
    public boolean subsetSum(int[] arr, int index, int sum, int target) {
        // Base Case
        if (sum == target) return true;
        if (index >= arr.length) return false;
        
        // Recursive Case: 포함 or 불포함
        // 1. 현재 원소 포함
        if (subsetSum(arr, index + 1, sum + arr[index], target)) {
            return true;
        }
        
        // 2. 현재 원소 불포함
        return subsetSum(arr, index + 1, sum, target);
    }
    
    public static void main(String[] args) {
        BruteForce2 bf = new BruteForce2();
        int[] arr = {3, 34, 4, 12, 5, 2};
        System.out.println(bf.subsetSum(arr, 0, 0, 9));  // true (4+5)
    }
}
```

{% endraw %}

---

## 🔙 백트래킹 (Backtracking)

### 원리

**완전탐색 + 가지치기(Pruning)**

```
백트래킹 = DFS + 조건 검사
1. 선택 (Choose)
2. 탐색 (Explore)
3. 취소 (Unchoose)
```

**핵심 아이디어:**

- 답이 될 수 없는 경로는 조기에 포기
- 메모리와 시간 절약

---

### 백트래킹 기본 템플릿

{% raw %}

```java
public void backtrack(상태, 선택들) {
    // Base Case: 답 찾음
    if (목표_달성) {
        결과_저장();
        return;
    }
    
    // Recursive Case
    for (각_선택지 : 가능한_선택들) {
        // 1. 가지치기 (Pruning)
        if (!유효한_선택(선택지)) continue;
        
        // 2. 선택 (Choose)
        상태_변경(선택지);
        
        // 3. 탐색 (Explore)
        backtrack(새로운_상태, 선택들);
        
        // 4. 취소 (Unchoose) - 중요!
        상태_복원();
    }
}
```

{% endraw %}

---

### 예제 1: 순열 (Permutation)

{% raw %}

```java
import java.util.*;

public class Permutation {
    List<List<Integer>> result = new ArrayList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        backtrack(new ArrayList<>(), nums, new boolean[nums.length]);
        return result;
    }
    
    private void backtrack(List<Integer> current, int[] nums, boolean[] used) {
        // Base Case: 모든 원소 사용
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        // Recursive Case
        for (int i = 0; i < nums.length; i++) {
            // 가지치기: 이미 사용한 숫자
            if (used[i]) continue;
            
            // 선택
            current.add(nums[i]);
            used[i] = true;
            
            // 탐색
            backtrack(current, nums, used);
            
            // 취소 (Backtrack)
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
    
    public static void main(String[] args) {
        Permutation p = new Permutation();
        int[] nums = {1, 2, 3};
        System.out.println(p.permute(nums));
        // [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    }
}
```

{% endraw %}

**시각화:**

```
                     []
          /          |          \
        [1]         [2]         [3]
       /   \       /   \       /   \
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
      |     |     |     |     |     |
  [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

---

### 예제 2: 조합 (Combination)

{% raw %}

```java
import java.util.*;

public class Combination {
    List<List<Integer>> result = new ArrayList<>();
    
    // n개 중 k개 선택
    public List<List<Integer>> combine(int n, int k) {
        backtrack(new ArrayList<>(), 1, n, k);
        return result;
    }
    
    private void backtrack(List<Integer> current, int start, int n, int k) {
        // Base Case: k개 선택 완료
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        // Recursive Case
        for (int i = start; i <= n; i++) {
            // 선택
            current.add(i);
            
            // 탐색 (i+1부터 시작 → 중복 방지)
            backtrack(current, i + 1, n, k);
            
            // 취소
            current.remove(current.size() - 1);
        }
    }
    
    public static void main(String[] args) {
        Combination c = new Combination();
        System.out.println(c.combine(4, 2));
        // [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
    }
}
```

{% endraw %}

---

### 예제 3: 부분집합 (Subset)

{% raw %}

```java
import java.util.*;

public class Subset {
    List<List<Integer>> result = new ArrayList<>();
    
    public List<List<Integer>> subsets(int[] nums) {
        backtrack(new ArrayList<>(), nums, 0);
        return result;
    }
    
    private void backtrack(List<Integer> current, int[] nums, int start) {
        // 모든 상태를 결과에 추가
        result.add(new ArrayList<>(current));
        
        // Recursive Case
        for (int i = start; i < nums.length; i++) {
            // 선택
            current.add(nums[i]);
            
            // 탐색
            backtrack(current, nums, i + 1);
            
            // 취소
            current.remove(current.size() - 1);
        }
    }
    
    public static void main(String[] args) {
        Subset s = new Subset();
        int[] nums = {1, 2, 3};
        System.out.println(s.subsets(nums));
        // [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    }
}
```

{% endraw %}

---

### 예제 4: N-Queen 문제

{% raw %}

```java
import java.util.*;

public class NQueen {
    List<List<String>> result = new ArrayList<>();
    
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        backtrack(board, 0);
        return result;
    }
    
    private void backtrack(char[][] board, int row) {
        // Base Case: 모든 행에 퀸 배치 완료
        if (row == board.length) {
            result.add(construct(board));
            return;
        }
        
        // Recursive Case: 현재 행의 각 열 시도
        for (int col = 0; col < board.length; col++) {
            // 가지치기: 유효하지 않은 위치
            if (!isValid(board, row, col)) continue;
            
            // 선택
            board[row][col] = 'Q';
            
            // 탐색
            backtrack(board, row + 1);
            
            // 취소
            board[row][col] = '.';
        }
    }
    
    private boolean isValid(char[][] board, int row, int col) {
        int n = board.length;
        
        // 같은 열 체크
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }
        
        // 왼쪽 대각선 체크
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        
        // 오른쪽 대각선 체크
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        
        return true;
    }
    
    private List<String> construct(char[][] board) {
        List<String> res = new ArrayList<>();
        for (char[] row : board) {
            res.add(new String(row));
        }
        return res;
    }
    
    public static void main(String[] args) {
        NQueen nq = new NQueen();
        List<List<String>> solutions = nq.solveNQueens(4);
        
        for (List<String> solution : solutions) {
            for (String row : solution) {
                System.out.println(row);
            }
            System.out.println();
        }
        
        // 출력:
        // .Q..
        // ...Q
        // Q...
        // ..Q.
        //
        // ..Q.
        // Q...
        // ...Q
        // .Q..
    }
}
```

{% endraw %}

---

## 🌳 DFS (Depth-First Search)

### 원리

**깊이 우선 탐색 = 한 방향으로 끝까지 탐색**

```
DFS 특징:
- 스택 또는 재귀 사용
- 메모리 효율적
- 백트래킹의 기초
```

---

### DFS 구현 방법

#### 1. 재귀 버전 (추천)

{% raw %}

```java
import java.util.*;

public class DFSRecursive {
    // 그래프: 인접 리스트
    List<List<Integer>> graph;
    boolean[] visited;
    
    public void dfs(int node) {
        // 방문 처리
        visited[node] = true;
        System.out.print(node + " ");
        
        // 인접 노드 탐색
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }
    
    public static void main(String[] args) {
        DFSRecursive dfs = new DFSRecursive();
        
        // 그래프 초기화
        dfs.graph = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            dfs.graph.add(new ArrayList<>());
        }
        
        // 간선 추가
        dfs.graph.get(0).addAll(Arrays.asList(1, 2));
        dfs.graph.get(1).addAll(Arrays.asList(0, 3, 4));
        dfs.graph.get(2).addAll(Arrays.asList(0, 5, 6));
        dfs.graph.get(3).add(1);
        dfs.graph.get(4).add(1);
        dfs.graph.get(5).add(2);
        dfs.graph.get(6).add(2);
        
        dfs.visited = new boolean[7];
        dfs.dfs(0);  // 0 1 3 4 2 5 6
    }
}
```

{% endraw %}

---

#### 2. 스택 버전

{% raw %}

```java
import java.util.*;

public class DFSStack {
    public void dfs(List<List<Integer>> graph, int start) {
        boolean[] visited = new boolean[graph.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        
        stack.push(start);
        
        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            if (visited[node]) continue;
            
            // 방문 처리
            visited[node] = true;
            System.out.print(node + " ");
            
            // 인접 노드를 스택에 추가 (역순으로)
            List<Integer> neighbors = graph.get(node);
            for (int i = neighbors.size() - 1; i >= 0; i--) {
                if (!visited[neighbors.get(i)]) {
                    stack.push(neighbors.get(i));
                }
            }
        }
    }
}
```

{% endraw %}

---

### DFS 응용

#### 1. 경로 찾기

{% raw %}

```java
import java.util.*;

public class PathFinding {
    List<List<Integer>> graph;
    boolean[] visited;
    
    // start에서 end까지 경로 존재 여부
    public boolean hasPath(int start, int end) {
        visited = new boolean[graph.size()];
        return dfs(start, end);
    }
    
    private boolean dfs(int node, int target) {
        if (node == target) return true;
        
        visited[node] = true;
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                if (dfs(next, target)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // 모든 경로 찾기
    public List<List<Integer>> allPaths(int start, int end) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        visited = new boolean[graph.size()];
        
        path.add(start);
        dfsAllPaths(start, end, path, result);
        
        return result;
    }
    
    private void dfsAllPaths(int node, int target, 
                             List<Integer> path, 
                             List<List<Integer>> result) {
        if (node == target) {
            result.add(new ArrayList<>(path));
            return;
        }
        
        visited[node] = true;
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                path.add(next);
                dfsAllPaths(next, target, path, result);
                path.remove(path.size() - 1);  // Backtrack
            }
        }
        
        visited[node] = false;  // Backtrack
    }
}
```

{% endraw %}

---

#### 2. 연결 요소 개수

{% raw %}

```java
public class ConnectedComponents {
    public int countComponents(int n, int[][] edges) {
        // 그래프 구성
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        // DFS로 연결 요소 카운트
        boolean[] visited = new boolean[n];
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(graph, i, visited);
                count++;
            }
        }
        
        return count;
    }
    
    private void dfs(List<List<Integer>> graph, int node, boolean[] visited) {
        visited[node] = true;
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                dfs(graph, next, visited);
            }
        }
    }
    
    public static void main(String[] args) {
        ConnectedComponents cc = new ConnectedComponents();
        int[][] edges = {{0,1}, {1,2}, {3,4}};
        System.out.println(cc.countComponents(5, edges));  // 2
    }
}
```

{% endraw %}

---

#### 3. 섬의 개수 (2D 그리드)

{% raw %}

```java
public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int count = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private void dfs(char[][] grid, int i, int j) {
        // 경계 체크
        if (i < 0 || i >= grid.length || 
            j < 0 || j >= grid[0].length || 
            grid[i][j] != '1') {
            return;
        }
        
        // 방문 처리
        grid[i][j] = '0';
        
        // 4방향 탐색
        dfs(grid, i + 1, j);  // 아래
        dfs(grid, i - 1, j);  // 위
        dfs(grid, i, j + 1);  // 오른쪽
        dfs(grid, i, j - 1);  // 왼쪽
    }
    
    public static void main(String[] args) {
        NumberOfIslands sol = new NumberOfIslands();
        char[][] grid = {
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
        };
        System.out.println(sol.numIslands(grid));  // 3
    }
}
```

{% endraw %}

---

## 🎨 실전 패턴

### 패턴 1: 선택/비선택 (Include/Exclude)

{% raw %}

```java
// 부분집합, 조합 문제
public void backtrack(int index) {
    if (index == n) {
        // 결과 처리
        return;
    }
    
    // 선택 O
    선택(index);
    backtrack(index + 1);
    취소(index);
    
    // 선택 X
    backtrack(index + 1);
}
```

{% endraw %}

---

### 패턴 2: 가능한 모든 선택 시도

{% raw %}

```java
// 순열, N-Queen 문제
public void backtrack(상태) {
    if (목표_달성) {
        결과_저장();
        return;
    }
    
    for (각_선택지 : 가능한_선택들) {
        if (!유효(선택지)) continue;
        
        선택(선택지);
        backtrack(새로운_상태);
        취소(선택지);
    }
}
```

{% endraw %}

---

### 패턴 3: 격자 탐색 (Grid DFS)

{% raw %}

```java
// 섬, 영역 문제
int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};

public void dfs(int[][] grid, int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != target) {
        return;
    }
    
    grid[x][y] = visited_mark;
    
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        dfs(grid, nx, ny);
    }
}
```

{% endraw %}

---

## 📊 복잡도 분석

### 재귀 시간복잡도

|문제|시간복잡도|공간복잡도|
|---|---|---|
|팩토리얼|O(n)|O(n) 스택|
|피보나치 (기본)|O(2^n)|O(n) 스택|
|피보나치 (메모)|O(n)|O(n)|
|순열|O(n!)|O(n)|
|조합|O(2^n)|O(n)|
|부분집합|O(2^n)|O(n)|
|N-Queen|O(n!)|O(n²)|
|DFS (그래프)|O(V+E)|O(V)|

---

## ⚠️ 주의사항

### 1. Base Case 필수!

{% raw %}

```java
// ❌ 무한 재귀 - Base Case 없음
public int wrong(int n) {
    return n + wrong(n - 1);  // 멈추지 않음!
}

// ✅ 올바른 재귀
public int correct(int n) {
    if (n <= 0) return 0;  // Base Case
    return n + correct(n - 1);
}
```

{% endraw %}

---

### 2. Stack Overflow 주의

{% raw %}

```java
// 재귀 깊이가 너무 깊으면 Stack Overflow
// Java 기본 스택 크기: 약 1MB (약 5000~10000 재귀)

// 해결 방법:
// 1. 메모이제이션
// 2. 반복문으로 변환
// 3. 꼬리 재귀 최적화 (Java는 지원 안 함)
```

{% endraw %}

---

### 3. 상태 복원 (Backtrack) 필수!

{% raw %}

```java
// ❌ 잘못된 백트래킹 - 상태 복원 안 함
public void wrong(List<Integer> path) {
    if (조건) {
        result.add(path);  // 위험! 같은 객체 참조
        return;
    }
    
    for (int i : choices) {
        path.add(i);
        wrong(path);
        // path.remove(path.size() - 1);  // 복원 안 함!
    }
}

// ✅ 올바른 백트래킹
public void correct(List<Integer> path) {
    if (조건) {
        result.add(new ArrayList<>(path));  // 복사!
        return;
    }
    
    for (int i : choices) {
        path.add(i);
        correct(path);
        path.remove(path.size() - 1);  // 상태 복원!
    }
}
```

{% endraw %}

---

### 4. 방문 체크 주의

{% raw %}

```java
// DFS에서 방문 체크 타이밍

// 패턴 1: 방문 전에 체크 (일반적)
public void dfs1(int node) {
    visited[node] = true;
    
    for (int next : graph.get(node)) {
        if (!visited[next]) {
            dfs1(next);
        }
    }
}

// 패턴 2: 모든 경로 찾기 (백트래킹)
public void dfs2(int node) {
    visited[node] = true;
    
    if (node == target) {
        // 경로 저장
    }
    
    for (int next : graph.get(node)) {
        if (!visited[next]) {
            dfs2(next);
        }
    }
    
    visited[node] = false;  // 백트래킹!
}
```

{% endraw %}

---

## 💡 최적화 기법

### 1. 메모이제이션 (Memoization)

{% raw %}

```java
public class Memoization {
    // 피보나치 최적화
    private Map<Integer, Integer> memo = new HashMap<>();
    
    public int fib(int n) {
        if (n <= 1) return n;
        
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        
        int result = fib(n - 1) + fib(n - 2);
        memo.put(n, result);
        return result;
    }
    
    // 배열로 메모이제이션 (더 빠름)
    public int fibArray(int n, int[] memo) {
        if (n <= 1) return n;
        if (memo[n] != 0) return memo[n];
        
        memo[n] = fibArray(n - 1, memo) + fibArray(n - 2, memo);
        return memo[n];
    }
}
```

{% endraw %}

---

### 2. 가지치기 (Pruning)

{% raw %}

```java
public class Pruning {
    // 조합의 합 최적화
    public void combinationSum(int[] nums, int target, int start, 
                              List<Integer> current, int sum) {
        if (sum == target) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        // 가지치기: 이미 target 초과
        if (sum > target) return;
        
        for (int i = start; i < nums.length; i++) {
            // 가지치기: 정렬되어 있다면 이후는 볼 필요 없음
            if (sum + nums[i] > target) break;
            
            current.add(nums[i]);
            combinationSum(nums, target, i, current, sum + nums[i]);
            current.remove(current.size() - 1);
        }
    }
}
```

{% endraw %}

---

### 3. 중복 제거

{% raw %}

```java
public class DuplicateRemoval {
    // 중복 있는 배열에서 순열
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);  // 정렬 필수!
        backtrack(result, new ArrayList<>(), nums, new boolean[nums.length]);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> temp,
                          int[] nums, boolean[] used) {
        if (temp.size() == nums.length) {
            result.add(new ArrayList<>(temp));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            // 중복 제거: 같은 숫자가 연속되고 이전 것을 안 썼으면 스킵
            if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) {
                continue;
            }
            
            used[i] = true;
            temp.add(nums[i]);
            backtrack(result, temp, nums, used);
            temp.remove(temp.size() - 1);
            used[i] = false;
        }
    }
}
```

{% endraw %}

---

## 🎯 실전 문제 풀이

### 문제 1: 전화번호 문자 조합 (LeetCode 17)

{% raw %}

```java
public class LetterCombinations {
    private static final String[] KEYS = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };
    
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) return result;
        
        backtrack(result, new StringBuilder(), digits, 0);
        return result;
    }
    
    private void backtrack(List<String> result, StringBuilder current, 
                          String digits, int index) {
        // Base Case
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }
        
        // 현재 숫자에 대응하는 문자들
        String letters = KEYS[digits.charAt(index) - '0'];
        
        for (char c : letters.toCharArray()) {
            current.append(c);
            backtrack(result, current, digits, index + 1);
            current.deleteCharAt(current.length() - 1);
        }
    }
    
    public static void main(String[] args) {
        LetterCombinations lc = new LetterCombinations();
        System.out.println(lc.letterCombinations("23"));
        // [ad, ae, af, bd, be, bf, cd, ce, cf]
    }
}
```

{% endraw %}

---

### 문제 2: 단어 검색 (LeetCode 79)

{% raw %}

```java
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        
        // 모든 위치에서 시작 시도
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    private boolean dfs(char[][] board, String word, int i, int j, int index) {
        // Base Case: 단어 완성
        if (index == word.length()) return true;
        
        // 경계 체크
        if (i < 0 || i >= board.length || 
            j < 0 || j >= board[0].length || 
            board[i][j] != word.charAt(index)) {
            return false;
        }
        
        // 방문 표시
        char temp = board[i][j];
        board[i][j] = '#';
        
        // 4방향 탐색
        boolean found = dfs(board, word, i+1, j, index+1) ||
                       dfs(board, word, i-1, j, index+1) ||
                       dfs(board, word, i, j+1, index+1) ||
                       dfs(board, word, i, j-1, index+1);
        
        // 복원
        board[i][j] = temp;
        
        return found;
    }
    
    public static void main(String[] args) {
        WordSearch ws = new WordSearch();
        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        System.out.println(ws.exist(board, "ABCCED"));  // true
        System.out.println(ws.exist(board, "SEE"));     // true
        System.out.println(ws.exist(board, "ABCB"));    // false
    }
}
```

{% endraw %}

---

### 문제 3: 팰린드롬 분할 (LeetCode 131)

{% raw %}

```java
public class PalindromePartitioning {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), s, 0);
        return result;
    }
    
    private void backtrack(List<List<String>> result, List<String> current,
                          String s, int start) {
        // Base Case: 문자열 끝
        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        // 모든 가능한 분할 시도
        for (int end = start; end < s.length(); end++) {
            // 팰린드롬인 경우만 선택
            if (isPalindrome(s, start, end)) {
                current.add(s.substring(start, end + 1));
                backtrack(result, current, s, end + 1);
                current.remove(current.size() - 1);
            }
        }
    }
    
    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        PalindromePartitioning pp = new PalindromePartitioning();
        System.out.println(pp.partition("aab"));
        // [[a, a, b], [aa, b]]
    }
}
```

{% endraw %}

---

### 문제 4: 스도쿠 풀기 (LeetCode 37)

{% raw %}

```java
public class SudokuSolver {
    public void solveSudoku(char[][] board) {
        solve(board);
    }
    
    private boolean solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    // 1~9 시도
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c;
                            
                            if (solve(board)) {
                                return true;
                            }
                            
                            board[i][j] = '.';  // Backtrack
                        }
                    }
                    return false;  // 모든 숫자 실패
                }
            }
        }
        return true;  // 모든 칸 채움
    }
    
    private boolean isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            // 행 체크
            if (board[row][i] == c) return false;
            
            // 열 체크
            if (board[i][col] == c) return false;
            
            // 3×3 박스 체크
            int boxRow = 3 * (row / 3) + i / 3;
            int boxCol = 3 * (col / 3) + i % 3;
            if (board[boxRow][boxCol] == c) return false;
        }
        return true;
    }
}
```

{% endraw %}

---

## 🏆 추천 문제

### 재귀 기초 (⭐)

1. **[LeetCode 344] Reverse String**
    
    - 재귀로 문자열 뒤집기
2. **[LeetCode 509] Fibonacci Number**
    
    - 피보나치 수열
3. **[LeetCode 206] Reverse Linked List**
    
    - 재귀로 연결 리스트 뒤집기
4. **[백준 10872] 팩토리얼**
    
    - 기본 재귀
5. **[백준 2447] 별 찍기 - 10**
    
    - 분할 정복

---

### 백트래킹 (⭐⭐)

1. **[LeetCode 46] Permutations**
    
    - 순열
2. **[LeetCode 77] Combinations**
    
    - 조합
3. **[LeetCode 78] Subsets**
    
    - 부분집합
4. **[LeetCode 39] Combination Sum**
    
    - 조합의 합
5. **[LeetCode 51] N-Queens**
    
    - N-Queen 문제
6. **[LeetCode 22] Generate Parentheses**
    
    - 유효한 괄호 생성
7. **[프로그래머스] 피로도**
    
    - 순열 응용
8. **[백준 15649] N과 M (1)**
    
    - 순열 기초
9. **[백준 9663] N-Queen**
    
    - 백트래킹 대표 문제
10. **[백준 1987] 알파벳**
    
    - 격자 백트래킹

---

### DFS (⭐⭐)

1. **[LeetCode 200] Number of Islands**
    
    - 섬의 개수
2. **[LeetCode 695] Max Area of Island**
    
    - 최대 섬 크기
3. **[LeetCode 133] Clone Graph**
    
    - 그래프 복제
4. **[LeetCode 547] Number of Provinces**
    
    - 연결 요소 개수
5. **[LeetCode 79] Word Search**
    
    - 단어 검색
6. **[백준 2606] 바이러스**
    
    - DFS 기초
7. **[백준 1260] DFS와 BFS**
    
    - DFS 구현
8. **[백준 2667] 단지번호붙이기**
    
    - 영역 찾기
9. **[백준 11724] 연결 요소의 개수**
    
    - 연결 요소
10. **[백준 1012] 유기농 배추**
    
    - 2D DFS

---

### 심화 (⭐⭐⭐)

1. **[LeetCode 37] Sudoku Solver**
    - 스도쿠
2. **[LeetCode 131] Palindrome Partitioning**
    - 팰린드롬 분할
3. **[LeetCode 212] Word Search II**
    - Trie + DFS
4. **[LeetCode 301] Remove Invalid Parentheses**
    - BFS/DFS 응용
5. **[백준 14888] 연산자 끼워넣기**
    - 백트래킹 응용

---

## 📚 학습 로드맵

### 1주차: 재귀 기초

- [ ] 팩토리얼, 피보나치 구현
- [ ] 배열 합, 문자열 뒤집기
- [ ] 재귀 → 반복문 변환 연습
- [ ] 메모이제이션 이해

### 2주차: 백트래킹 기초

- [ ] 순열 구현 (중복 X)
- [ ] 조합 구현 (중복 X)
- [ ] 부분집합 구현
- [ ] 순열 (중복 O) 구현

### 3주차: DFS 기초

- [ ] 그래프 DFS 구현 (재귀)
- [ ] 그래프 DFS 구현 (스택)
- [ ] 2D 그리드 DFS
- [ ] 연결 요소 찾기

### 4주차: 종합 응용

- [ ] N-Queen 문제
- [ ] 단어 검색 문제
- [ ] 조합의 합 문제
- [ ] 섬의 개수 문제

---

## 💡 디버깅 팁

### 1. 재귀 호출 추적

{% raw %}

```java
public class DebugRecursion {
    private int depth = 0;
    
    public int factorial(int n) {
        // 들여쓰기로 깊이 표시
        String indent = "  ".repeat(depth);
        System.out.println(indent + "→ factorial(" + n + ")");
        depth++;
        
        if (n <= 1) {
            depth--;
            System.out.println(indent + "← return 1");
            return 1;
        }
        
        int result = n * factorial(n - 1);
        
        depth--;
        System.out.println(indent + "← return " + result);
        return result;
    }
    
    public static void main(String[] args) {
        DebugRecursion dr = new DebugRecursion();
        dr.factorial(5);
        
        // 출력:
        // → factorial(5)
        //   → factorial(4)
        //     → factorial(3)
        //       → factorial(2)
        //         → factorial(1)
        //         ← return 1
        //       ← return 2
        //     ← return 6
        //   ← return 24
        // ← return 120
    }
}
```

{% endraw %}

---

### 2. 백트래킹 상태 출력

{% raw %}

```java
public void backtrackDebug(List<Integer> current, int start) {
    System.out.println("현재 경로: " + current + ", start: " + start);
    
    if (current.size() == target) {
        System.out.println("  → 답 발견: " + current);
        return;
    }
    
    for (int i = start; i < n; i++) {
        System.out.println("  선택: " + i);
        current.add(i);
        backtrackDebug(current, i + 1);
        current.remove(current.size() - 1);
        System.out.println("  취소: " + i);
    }
}
```

{% endraw %}

---

## 🎯 핵심 정리

### 재귀 체크리스트

- [ ] Base Case 확인
- [ ] 재귀 호출이 더 작은 문제로 수렴하는가?
- [ ] Stack Overflow 가능성은?
- [ ] 메모이제이션 필요한가?

### 백트래킹 체크리스트

- [ ] 선택 → 탐색 → 취소 패턴
- [ ] 상태 복원 (Backtrack) 했는가?
- [ ] 가지치기 최적화 가능한가?
- [ ] 중복 제거 필요한가?

### DFS 체크리스트

- [ ] 방문 체크 위치 정확한가?
- [ ] 경계 조건 확인했는가?
- [ ] 모든 경로 vs 하나의 경로?
- [ ] 재귀 vs 스택 선택 기준은?

---

## 📝 암기 필수 템플릿

### 1. 백트래킹 기본

{% raw %}

```java
public void backtrack(List<Integer> current, ...) {
    if (목표_달성) {
        result.add(new ArrayList<>(current));
        return;
    }
    
    for (선택지 : 선택들) {
        if (!유효(선택지)) continue;
        
        current.add(선택지);
        backtrack(current, ...);
        current.remove(current.size() - 1);
    }
}
```

{% endraw %}

---

### 2. DFS (재귀)

{% raw %}

```java
public void dfs(int node) {
    visited[node] = true;
    
    for (int next : graph.get(node)) {
        if (!visited[next]) {
            dfs(next);
        }
    }
}
```

{% endraw %}

---

### 3. 2D 그리드 DFS

{% raw %}

```java
int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};

public void dfs(int[][] grid, int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != target) {
        return;
    }
    
    grid[x][y] = visited;
    
    for (int i = 0; i < 4; i++) {
        dfs(grid, x + dx[i], y + dy[i]);
    }
}
```

{% endraw %}

---

#Java #재귀 #Recursion #백트래킹 #Backtracking #DFS #완전탐색 #BruteForce #순열 #조합 #NQueen #알고리즘 #코딩테스트