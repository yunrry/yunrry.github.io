
# 그래프 탐색

그래프는 정점(Vertex)과 간선(Edge)으로 이루어진 자료구조로, 네트워크, 지도, 소셜 관계 등 다양한 문제를 표현할 수 있습니다. BFS와 DFS는 그래프 탐색의 핵심 알고리즘입니다.

---

## 📊 그래프 기초

### 그래프 용어

```

정점(Vertex/Node): 그래프의 노드 간선(Edge): 정점을 연결하는 선 차수(Degree): 정점에 연결된 간선의 수 경로(Path): 정점들을 잇는 간선들의 순서 사이클(Cycle): 시작과 끝이 같은 경로

```

### 그래프 종류

```

무향 그래프(Undirected): A-B = B-A 유향 그래프(Directed): A→B ≠ B→A 가중치 그래프(Weighted): 간선에 비용/거리 비가중치 그래프(Unweighted): 모든 간선 동일

````

---

## 🗂️ 그래프 표현 방법

### 1. 인접 행렬 (Adjacency Matrix)

{% raw %}
```java
public class AdjacencyMatrix {
    private int[][] matrix;
    private int vertices;
    
    public AdjacencyMatrix(int n) {
        this.vertices = n;
        this.matrix = new int[n][n];
    }
    
    // 무향 그래프 간선 추가
    public void addEdge(int from, int to) {
        matrix[from][to] = 1;
        matrix[to][from] = 1;
    }
    
    // 가중치 그래프 간선 추가
    public void addEdgeWeighted(int from, int to, int weight) {
        matrix[from][to] = weight;
        matrix[to][from] = weight;
    }
    
    // 유향 그래프 간선 추가
    public void addDirectedEdge(int from, int to) {
        matrix[from][to] = 1;
    }
    
    // 간선 존재 확인
    public boolean hasEdge(int from, int to) {
        return matrix[from][to] != 0;
    }
    
    // 출력
    public void print() {
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

// 사용 예시
public static void main(String[] args) {
    AdjacencyMatrix graph = new AdjacencyMatrix(5);
    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(1, 3);
    graph.addEdge(2, 4);
    graph.print();
    
    // 출력:
    // 0 1 1 0 0
    // 1 0 0 1 0
    // 1 0 0 0 1
    // 0 1 0 0 0
    // 0 0 1 0 0
}
````

{% endraw %}

**장점:**

- 간선 존재 여부 O(1)에 확인
- 구현 간단

**단점:**

- 공간복잡도 O(V²)
- 희소 그래프에 비효율적

---

### 2. 인접 리스트 (Adjacency List) ⭐ 추천

{% raw %}

```java
import java.util.*;

public class AdjacencyList {
    private List<List<Integer>> adjList;
    private int vertices;
    
    public AdjacencyList(int n) {
        this.vertices = n;
        this.adjList = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
    }
    
    // 무향 그래프 간선 추가
    public void addEdge(int from, int to) {
        adjList.get(from).add(to);
        adjList.get(to).add(from);
    }
    
    // 유향 그래프 간선 추가
    public void addDirectedEdge(int from, int to) {
        adjList.get(from).add(to);
    }
    
    // 인접 노드 가져오기
    public List<Integer> getNeighbors(int node) {
        return adjList.get(node);
    }
    
    // 출력
    public void print() {
        for (int i = 0; i < vertices; i++) {
            System.out.print(i + " → ");
            for (int neighbor : adjList.get(i)) {
                System.out.print(neighbor + " ");
            }
            System.out.println();
        }
    }
}

// 사용 예시
public static void main(String[] args) {
    AdjacencyList graph = new AdjacencyList(5);
    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(1, 3);
    graph.addEdge(2, 4);
    graph.print();
    
    // 출력:
    // 0 → 1 2
    // 1 → 0 3
    // 2 → 0 4
    // 3 → 1
    // 4 → 2
}
```

{% endraw %}

**장점:**

- 공간복잡도 O(V+E) - 효율적
- 희소 그래프에 적합
- 인접 노드 순회 빠름

**단점:**

- 간선 존재 확인 O(V) (worst case)

---

### 3. 간선 리스트 (Edge List)

{% raw %}

```java
public class EdgeList {
    static class Edge {
        int from, to, weight;
        
        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }
    
    private List<Edge> edges;
    
    public EdgeList() {
        edges = new ArrayList<>();
    }
    
    public void addEdge(int from, int to, int weight) {
        edges.add(new Edge(from, to, weight));
    }
    
    public List<Edge> getEdges() {
        return edges;
    }
}

// 크루스칼 알고리즘 등에서 사용
```

{% endraw %}

---

## 🔍 BFS (Breadth-First Search)

### 원리

**너비 우선 탐색 = 레벨별로 탐색**

```
BFS 특징:
- Queue 사용
- 가까운 노드부터 탐색
- 최단 경로 보장 (비가중치)
- 메모리 사용량 많음
```

**시각화:**

```
       1
      / \
     2   3
    / \   \
   4   5   6

BFS 순서: 1 → 2 → 3 → 4 → 5 → 6
(레벨별로 탐색)
```

---

### 기본 구현

{% raw %}

```java
import java.util.*;

public class BFS {
    // 기본 BFS
    public void bfs(List<List<Integer>> graph, int start) {
        int n = graph.size();
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        
        // 시작 노드
        queue.offer(start);
        visited[start] = true;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            
            // 인접 노드 탐색
            for (int next : graph.get(node)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }
    }
    
    public static void main(String[] args) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            graph.add(new ArrayList<>());
        }
        
        // 간선 추가
        graph.get(1).addAll(Arrays.asList(2, 3));
        graph.get(2).addAll(Arrays.asList(1, 4, 5));
        graph.get(3).addAll(Arrays.asList(1, 6));
        graph.get(4).add(2);
        graph.get(5).add(2);
        graph.get(6).add(3);
        
        BFS bfs = new BFS();
        bfs.bfs(graph, 1);  // 1 2 3 4 5 6
    }
}
```

{% endraw %}

---

### 레벨별 BFS

{% raw %}

```java
public class LevelBFS {
    // 각 레벨을 구분하여 탐색
    public void bfsByLevel(List<List<Integer>> graph, int start) {
        boolean[] visited = new boolean[graph.size()];
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(start);
        visited[start] = true;
        int level = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();  // 현재 레벨의 노드 수
            System.out.print("Level " + level + ": ");
            
            // 현재 레벨의 모든 노드 처리
            for (int i = 0; i < size; i++) {
                int node = queue.poll();
                System.out.print(node + " ");
                
                for (int next : graph.get(node)) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }
            System.out.println();
            level++;
        }
    }
}

// 출력:
// Level 0: 1
// Level 1: 2 3
// Level 2: 4 5 6
```

{% endraw %}

---

### 최단 거리 구하기

{% raw %}

```java
public class ShortestPath {
    // 시작점부터 모든 노드까지의 최단 거리
    public int[] bfsDistance(List<List<Integer>> graph, int start) {
        int n = graph.size();
        int[] distance = new int[n];
        Arrays.fill(distance, -1);  // -1 = 방문 안 함
        
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        distance[start] = 0;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int next : graph.get(node)) {
                if (distance[next] == -1) {
                    distance[next] = distance[node] + 1;
                    queue.offer(next);
                }
            }
        }
        
        return distance;
    }
    
    public static void main(String[] args) {
        // 그래프 생성
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            graph.add(new ArrayList<>());
        }
        
        graph.get(1).addAll(Arrays.asList(2, 3));
        graph.get(2).addAll(Arrays.asList(1, 4, 5));
        graph.get(3).addAll(Arrays.asList(1, 6));
        graph.get(4).add(2);
        graph.get(5).add(2);
        graph.get(6).add(3);
        
        ShortestPath sp = new ShortestPath();
        int[] dist = sp.bfsDistance(graph, 1);
        
        for (int i = 1; i < dist.length; i++) {
            System.out.println("1 → " + i + ": " + dist[i]);
        }
        
        // 출력:
        // 1 → 1: 0
        // 1 → 2: 1
        // 1 → 3: 1
        // 1 → 4: 2
        // 1 → 5: 2
        // 1 → 6: 2
    }
}
```

{% endraw %}

---

### 경로 역추적

{% raw %}

```java
public class PathTracking {
    public List<Integer> bfsPath(List<List<Integer>> graph, int start, int end) {
        int n = graph.size();
        int[] parent = new int[n];  // 부모 노드 기록
        Arrays.fill(parent, -1);
        
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        
        queue.offer(start);
        visited[start] = true;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            if (node == end) break;  // 목표 도달
            
            for (int next : graph.get(node)) {
                if (!visited[next]) {
                    visited[next] = true;
                    parent[next] = node;  // 부모 기록
                    queue.offer(next);
                }
            }
        }
        
        // 경로 역추적
        List<Integer> path = new ArrayList<>();
        if (parent[end] == -1 && start != end) {
            return path;  // 경로 없음
        }
        
        for (int at = end; at != -1; at = parent[at]) {
            path.add(at);
        }
        
        Collections.reverse(path);
        return path;
    }
    
    public static void main(String[] args) {
        // 그래프 생성
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            graph.add(new ArrayList<>());
        }
        
        graph.get(1).addAll(Arrays.asList(2, 3));
        graph.get(2).addAll(Arrays.asList(1, 4));
        graph.get(3).addAll(Arrays.asList(1, 6));
        graph.get(4).add(2);
        graph.get(6).add(3);
        
        PathTracking pt = new PathTracking();
        List<Integer> path = pt.bfsPath(graph, 1, 4);
        System.out.println("경로: " + path);  // [1, 2, 4]
    }
}
```

{% endraw %}

---

## 🔄 DFS vs BFS 비교

### 차이점

|특성|DFS|BFS|
|---|---|---|
|**자료구조**|Stack (재귀)|Queue|
|**탐색 방향**|깊이 우선|너비 우선|
|**메모리**|O(H) - 높이|O(W) - 너비|
|**최단 경로**|보장 안 함|보장함 (비가중치)|
|**구현**|재귀가 간단|반복문 사용|
|**활용**|백트래킹, 사이클, 위상정렬|최단거리, 레벨|

---

### 시각적 비교

```
그래프:
       1
      /|\
     2 3 4
    /|   |
   5 6   7

DFS: 1 → 2 → 5 → 6 → 3 → 4 → 7 (깊이)
BFS: 1 → 2 → 3 → 4 → 5 → 6 → 7 (레벨)
```

---

### DFS 구현 (복습)

{% raw %}

```java
public class DFS {
    // 재귀 버전
    public void dfsRecursive(List<List<Integer>> graph, int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " ");
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                dfsRecursive(graph, next, visited);
            }
        }
    }
    
    // 스택 버전
    public void dfsIterative(List<List<Integer>> graph, int start) {
        boolean[] visited = new boolean[graph.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        
        stack.push(start);
        
        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            if (visited[node]) continue;
            
            visited[node] = true;
            System.out.print(node + " ");
            
            // 역순으로 추가 (작은 번호부터 방문)
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

### 언제 무엇을 사용할까?

**DFS 사용:**

- ✅ 모든 경로 탐색
- ✅ 백트래킹
- ✅ 사이클 감지
- ✅ 위상 정렬
- ✅ 연결 요소

**BFS 사용:**

- ✅ 최단 거리 (비가중치)
- ✅ 레벨별 처리
- ✅ 가장 가까운 노드 찾기
- ✅ 미로 탈출

---

## 🎯 BFS 실전 예제

### 예제 1: 미로 탈출

{% raw %}

```java
public class MazeEscape {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    static class Point {
        int x, y, dist;
        
        public Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
    
    public int shortestPath(int[][] maze) {
        int n = maze.length;
        int m = maze[0].length;
        boolean[][] visited = new boolean[n][m];
        Queue<Point> queue = new LinkedList<>();
        
        // 시작점 (0, 0)
        queue.offer(new Point(0, 0, 1));
        visited[0][0] = true;
        
        while (!queue.isEmpty()) {
            Point p = queue.poll();
            
            // 도착점 (n-1, m-1)
            if (p.x == n - 1 && p.y == m - 1) {
                return p.dist;
            }
            
            // 4방향 탐색
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                    maze[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new Point(nx, ny, p.dist + 1));
                }
            }
        }
        
        return -1;  // 도달 불가
    }
    
    public static void main(String[] args) {
        int[][] maze = {
            {1, 0, 1, 1, 1},
            {1, 0, 1, 0, 1},
            {1, 0, 1, 0, 1},
            {1, 1, 1, 0, 1}
        };
        
        MazeEscape me = new MazeEscape();
        System.out.println(me.shortestPath(maze));  // 9
    }
}
```

{% endraw %}

---

### 예제 2: 단어 변환

{% raw %}

```java
public class WordLadder {
    public int ladderLength(String begin, String end, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(end)) return 0;
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(begin);
        int level = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                
                if (word.equals(end)) return level;
                
                // 한 글자씩 바꿔보기
                char[] chars = word.toCharArray();
                for (int j = 0; j < chars.length; j++) {
                    char original = chars[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        
                        chars[j] = c;
                        String next = new String(chars);
                        
                        if (wordSet.contains(next)) {
                            queue.offer(next);
                            wordSet.remove(next);  // 방문 처리
                        }
                    }
                    
                    chars[j] = original;
                }
            }
            
            level++;
        }
        
        return 0;
    }
    
    public static void main(String[] args) {
        WordLadder wl = new WordLadder();
        List<String> wordList = Arrays.asList("hot","dot","dog","lot","log","cog");
        System.out.println(wl.ladderLength("hit", "cog", wordList));  // 5
        // hit → hot → dot → dog → cog
    }
}
```

{% endraw %}

---

### 예제 3: 벽 부수고 이동하기

{% raw %}

```java
public class BreakWall {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    static class State {
        int x, y, dist, walls;
        
        public State(int x, int y, int dist, int walls) {
            this.x = x;
            this.y = y;
            this.dist = dist;
            this.walls = walls;
        }
    }
    
    public int shortestPath(int[][] map) {
        int n = map.length;
        int m = map[0].length;
        
        // visited[x][y][walls] = (x,y)에 벽을 walls개 부수고 도달 가능
        boolean[][][] visited = new boolean[n][m][2];
        Queue<State> queue = new LinkedList<>();
        
        queue.offer(new State(0, 0, 1, 0));
        visited[0][0][0] = true;
        
        while (!queue.isEmpty()) {
            State s = queue.poll();
            
            if (s.x == n - 1 && s.y == m - 1) {
                return s.dist;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = s.x + dx[i];
                int ny = s.y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                
                // 빈 칸
                if (map[nx][ny] == 0 && !visited[nx][ny][s.walls]) {
                    visited[nx][ny][s.walls] = true;
                    queue.offer(new State(nx, ny, s.dist + 1, s.walls));
                }
                
                // 벽 (아직 안 부쉈으면)
                if (map[nx][ny] == 1 && s.walls == 0 && !visited[nx][ny][1]) {
                    visited[nx][ny][1] = true;
                    queue.offer(new State(nx, ny, s.dist + 1, 1));
                }
            }
        }
        
        return -1;
    }
}
```

{% endraw %}

---

## 🛣️ 최단 경로 알고리즘

### 다익스트라 (Dijkstra)

**원리: 가중치가 있는 그래프에서 최단 경로**

```
특징:
- 음수 가중치 불가
- 우선순위 큐 사용
- 시간복잡도: O((V+E) log V)
```

---

### 기본 구현

{% raw %}

```java
import java.util.*;

public class Dijkstra {
    static class Edge {
        int to, weight;
        
        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
    
    static class Node implements Comparable<Node> {
        int vertex, distance;
        
        public Node(int vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }
    
    public int[] dijkstra(List<List<Edge>> graph, int start) {
        int n = graph.size();
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int u = current.vertex;
            int d = current.distance;
            
            // 이미 처리한 노드
            if (d > dist[u]) continue;
            
            // 인접 노드 확인
            for (Edge edge : graph.get(u)) {
                int v = edge.to;
                int newDist = dist[u] + edge.weight;
                
                // 더 짧은 경로 발견
                if (newDist < dist[v]) {
                    dist[v] = newDist;
                    pq.offer(new Node(v, newDist));
                }
            }
        }
        
        return dist;
    }
    
    public static void main(String[] args) {
        int n = 6;
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        // 간선 추가 (양방향)
        graph.get(0).add(new Edge(1, 2));
        graph.get(0).add(new Edge(2, 5));
        graph.get(1).add(new Edge(0, 2));
        graph.get(1).add(new Edge(2, 3));
        graph.get(1).add(new Edge(3, 6));
        graph.get(2).add(new Edge(0, 5));
        graph.get(2).add(new Edge(1, 3));
        graph.get(2).add(new Edge(3, 1));
        graph.get(2).add(new Edge(4, 5));
        graph.get(3).add(new Edge(1, 6));
        graph.get(3).add(new Edge(2, 1));
        graph.get(3).add(new Edge(4, 2));
        graph.get(3).add(new Edge(5, 3));
        graph.get(4).add(new Edge(2, 5));
        graph.get(4).add(new Edge(3, 2));
        graph.get(4).add(new Edge(5, 6));
        graph.get(5).add(new Edge(3, 3));
        graph.get(5).add(new Edge(4, 6));
        
        Dijkstra dij = new Dijkstra();
        int[] dist = dij.dijkstra(graph, 0);
        
        for (int i = 0; i < n; i++) {
            System.out.println("0 → " + i + ": " + dist[i]);
        }
        
        // 출력:
        // 0 → 0: 0
        // 0 → 1: 2
        // 0 → 2: 5
        // 0 → 3: 6
        // 0 → 4: 8
        // 0 → 5: 9
    }
}
```

{% endraw %}

---

### 경로 역추적 포함

{% raw %}

```java
public class DijkstraWithPath {
    static class Edge {
        int to, weight;
        
        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
    
    static class Node implements Comparable<Node> {
        int vertex, distance;
        
        public Node(int vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }
    
    public List<Integer> dijkstraPath(List<List<Edge>> graph, int start, int end) {
        int n = graph.size();
        int[] dist = new int[n];
        int[] parent = new int[n];  // 경로 추적
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int u = current.vertex;
            
            if (u == end) break;  // 목표 도달
            if (current.distance > dist[u]) continue;
            
            for (Edge edge : graph.get(u)) {
                int v = edge.to; 
                int newDist = dist[u] + edge.weight;
                
            if (newDist < dist[v]) {
                dist[v] = newDist;
                parent[v] = u;  // 부모 기록
                pq.offer(new Node(v, newDist));
            }
        }
    }
    
    // 경로 역추적
    List<Integer> path = new ArrayList<>();
    if (dist[end] == Integer.MAX_VALUE) {
        return path;  // 경로 없음
    }
    
    for (int at = end; at != -1; at = parent[at]) {
        path.add(at);
    }
    Collections.reverse(path);
    
    return path;
}

	public static void main(String[] args) {
    // 그래프 생성 (위와 동일)
    // ...
	    DijkstraWithPath dwp = new DijkstraWithPath();
	    List<Integer> path = dwp.dijkstraPath(graph, 0, 5);
	    System.out.println("최단 경로: " + path);
	    // [0, 1, 2, 3, 5]
		}
}

````
{% endraw %}

---

### 벨만-포드 (Bellman-Ford)

**음수 가중치 허용**

{% raw %}
```java
public class BellmanFord {
    static class Edge {
        int from, to, weight;
        
        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }
    
    public int[] bellmanFord(int n, List<Edge> edges, int start) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        
        // V-1번 반복
        for (int i = 0; i < n - 1; i++) {
            for (Edge edge : edges) {
                if (dist[edge.from] != Integer.MAX_VALUE &&
                    dist[edge.from] + edge.weight < dist[edge.to]) {
                    dist[edge.to] = dist[edge.from] + edge.weight;
                }
            }
        }
        
        // 음수 사이클 검사
        for (Edge edge : edges) {
            if (dist[edge.from] != Integer.MAX_VALUE &&
                dist[edge.from] + edge.weight < dist[edge.to]) {
                System.out.println("음수 사이클 존재!");
                return null;
            }
        }
        
        return dist;
    }
}
````

{% endraw %}

**시간복잡도**: O(VE)  
**사용 시기**: 음수 가중치가 있을 때

---

## 📊 알고리즘 선택 가이드

### 최단 경로 문제

|상황|알고리즘|시간복잡도|
|---|---|---|
|**비가중치 그래프**|BFS|O(V+E)|
|**양수 가중치**|다익스트라|O((V+E) log V)|
|**음수 가중치**|벨만-포드|O(VE)|
|**모든 쌍 최단 경로**|플로이드-워셜|O(V³)|

---

## 🎯 실전 문제 패턴

### 패턴 1: 기본 BFS

{% raw %}

```java
// 템플릿
public void bfs(int start) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[n];
    
    queue.offer(start);
    visited[start] = true;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                visited[next] = true;
                queue.offer(next);
            }
        }
    }
}
```

{% endraw %}

---

### 패턴 2: 레벨별 BFS

{% raw %}

```java
// 레벨(거리) 추적
public void bfsByLevel(int start) {
    Queue<Integer> queue = new LinkedList<>();
    int[] distance = new int[n];
    Arrays.fill(distance, -1);
    
    queue.offer(start);
    distance[start] = 0;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        
        for (int next : graph.get(node)) {
            if (distance[next] == -1) {
                distance[next] = distance[node] + 1;
                queue.offer(next);
            }
        }
    }
}
```

{% endraw %}

---

### 패턴 3: 다중 시작점 BFS

{% raw %}

```java
// 여러 시작점 동시 탐색
public void multiSourceBFS(List<Integer> sources) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[n];
    
    // 모든 시작점 큐에 추가
    for (int source : sources) {
        queue.offer(source);
        visited[source] = true;
    }
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                visited[next] = true;
                queue.offer(next);
            }
        }
    }
}
```

{% endraw %}

---

### 패턴 4: 양방향 BFS

{% raw %}

```java
// 시작점과 끝점에서 동시에 BFS
public int bidirectionalBFS(int start, int end) {
    Set<Integer> visited1 = new HashSet<>();
    Set<Integer> visited2 = new HashSet<>();
    Queue<Integer> queue1 = new LinkedList<>();
    Queue<Integer> queue2 = new LinkedList<>();
    
    queue1.offer(start);
    queue2.offer(end);
    visited1.add(start);
    visited2.add(end);
    
    int level = 0;
    
    while (!queue1.isEmpty() && !queue2.isEmpty()) {
        // 작은 큐부터 확장 (최적화)
        if (queue1.size() > queue2.size()) {
            Queue<Integer> temp = queue1;
            queue1 = queue2;
            queue2 = temp;
            
            Set<Integer> tempSet = visited1;
            visited1 = visited2;
            visited2 = tempSet;
        }
        
        int size = queue1.size();
        level++;
        
        for (int i = 0; i < size; i++) {
            int node = queue1.poll();
            
            for (int next : graph.get(node)) {
                // 만남!
                if (visited2.contains(next)) {
                    return level;
                }
                
                if (!visited1.contains(next)) {
                    visited1.add(next);
                    queue1.offer(next);
                }
            }
        }
    }
    
    return -1;
}
```

{% endraw %}

---

## 💡 최적화 기법

### 1. 조기 종료

{% raw %}

```java
// 목표 찾으면 즉시 종료
while (!queue.isEmpty()) {
    int node = queue.poll();
    
    if (node == target) {
        return distance[node];  // 조기 종료
    }
    
    // ...
}
```

{% endraw %}

---

### 2. 방문 체크 최적화

{% raw %}

```java
// ❌ 느림: poll 후 체크
while (!queue.isEmpty()) {
    int node = queue.poll();
    if (visited[node]) continue;
    visited[node] = true;
    // ...
}

// ✅ 빠름: offer 전 체크
while (!queue.isEmpty()) {
    int node = queue.poll();
    
    for (int next : graph.get(node)) {
        if (!visited[next]) {
            visited[next] = true;  // 큐에 넣을 때 체크
            queue.offer(next);
        }
    }
}
```

{% endraw %}

---

### 3. 다익스트라 최적화

{% raw %}

```java
// 이미 처리한 노드 스킵
while (!pq.isEmpty()) {
    Node current = pq.poll();
    
    // 이미 더 짧은 경로 발견됨
    if (current.distance > dist[current.vertex]) {
        continue;  // 처리 안 함
    }
    
    // ...
}
```

{% endraw %}

---

## 🏆 추천 문제

### BFS 기초 (⭐)

1. **[백준 1260] DFS와 BFS**
    - BFS 기본 구현
2. **[백준 2178] 미로 탐색**
    - 2D BFS, 최단 거리
3. **[백준 7576] 토마토**
    - 다중 시작점 BFS
4. **[LeetCode 102] Binary Tree Level Order Traversal**
    - 레벨별 순회
5. **[LeetCode 111] Minimum Depth of Binary Tree**
    - 트리 BFS

---

### BFS 응용 (⭐⭐)

1. **[백준 7569] 토마토 (3D)**
    - 3차원 BFS
2. **[백준 1697] 숨바꼭질**
    - 1차원 BFS
3. **[백준 2206] 벽 부수고 이동하기**
    - 상태 추가 BFS
4. **[백준 16236] 아기 상어**
    - 우선순위 BFS
5. **[LeetCode 127] Word Ladder**
    - 단어 변환
6. **[LeetCode 207] Course Schedule**
    - 위상 정렬 (BFS)
7. **[LeetCode 994] Rotting Oranges**
    - 다중 시작점

---

### DFS vs BFS (⭐⭐)

1. **[백준 2667] 단지번호붙이기**
    - 연결 요소 (둘 다 가능)
2. **[백준 11724] 연결 요소의 개수**
    - 연결 요소
3. **[백준 1012] 유기농 배추**
    - 영역 찾기
4. **[LeetCode 200] Number of Islands**
    - 섬 개수
5. **[LeetCode 695] Max Area of Island**
    - 최대 영역

---

### 다익스트라 (⭐⭐⭐)

1. **[백준 1753] 최단경로**
    - 다익스트라 기본
2. **[백준 1916] 최소비용 구하기**
    - 최단 경로
3. **[백준 1238] 파티**
    - 왕복 최단 경로
4. **[백준 4485] 녹색 옷 입은 애가 젤다지?**
    - 2D 다익스트라
5. **[LeetCode 743] Network Delay Time**
    - 기본 다익스트라
6. **[LeetCode 787] Cheapest Flights Within K Stops**
    - 제약 조건 추가

---

### 심화 (⭐⭐⭐⭐)

1. **[백준 1167] 트리의 지름**
    - BFS 2번
2. **[백준 2250] 트리의 높이와 너비**
    - 레벨별 처리
3. **[백준 13549] 숨바꼭질 3**
    - 0-1 BFS
4. **[백준 1865] 웜홀**
    - 벨만-포드 (음수 사이클)
5. **[LeetCode 847] Shortest Path Visiting All Nodes**
    - 비트마스킹 BFS

---

## 📚 학습 로드맵

### 1주차: BFS 기초

- [ ] BFS 기본 구현 (그래프)
- [ ] 2D 그리드 BFS
- [ ] 최단 거리 구하기
- [ ] 경로 역추적

### 2주차: BFS 응용

- [ ] 레벨별 BFS
- [ ] 다중 시작점 BFS
- [ ] 상태 확장 BFS
- [ ] 양방향 BFS

### 3주차: DFS vs BFS

- [ ] DFS 재귀/스택 구현
- [ ] BFS와 DFS 차이 이해
- [ ] 문제별 적합한 방법 선택
- [ ] 연결 요소, 사이클 감지

### 4주차: 최단 경로

- [ ] 다익스트라 구현
- [ ] 우선순위 큐 활용
- [ ] 경로 역추적
- [ ] 벨만-포드 이해

---

## 💡 디버깅 팁

### 1. BFS 시각화

{% raw %}

```java
public void bfsDebug(int start) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[n];
    
    queue.offer(start);
    visited[start] = true;
    
    int level = 0;
    while (!queue.isEmpty()) {
        int size = queue.size();
        System.out.println("=== Level " + level + " ===");
        System.out.println("Queue: " + queue);
        
        for (int i = 0; i < size; i++) {
            int node = queue.poll();
            System.out.println("Processing: " + node);
            
            for (int next : graph.get(node)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                    System.out.println("  Added: " + next);
                }
            }
        }
        level++;
    }
}
```

{% endraw %}

---

### 2. 다익스트라 디버깅

{% raw %}

```java
while (!pq.isEmpty()) {
    Node current = pq.poll();
    System.out.printf("처리: node=%d, dist=%d%n", 
        current.vertex, current.distance);
    
    if (current.distance > dist[current.vertex]) {
        System.out.println("  → 스킵 (이미 처리됨)");
        continue;
    }
    
    for (Edge edge : graph.get(current.vertex)) {
        int newDist = dist[current.vertex] + edge.weight;
        System.out.printf("  검사: %d → %d, 기존=%d, 새=%d%n",
            current.vertex, edge.to, dist[edge.to], newDist);
        
        if (newDist < dist[edge.to]) {
            System.out.println("    → 갱신!");
            dist[edge.to] = newDist;
            pq.offer(new Node(edge.to, newDist));
        }
    }
}
```

{% endraw %}

---

## 🎯 핵심 정리

### BFS 체크리스트

- [ ] Queue 사용
- [ ] 방문 체크 (offer 시)
- [ ] 레벨 구분 필요한지 확인
- [ ] 최단 거리 = 비가중치만!

### 다익스트라 체크리스트

- [ ] 우선순위 큐 사용
- [ ] 음수 가중치 없는지 확인
- [ ] 이미 처리한 노드 스킵
- [ ] 경로 역추적 필요한지

### DFS vs BFS 선택

- [ ] 최단 거리? → BFS
- [ ] 모든 경로? → DFS
- [ ] 백트래킹? → DFS
- [ ] 레벨 구분? → BFS

---

## 📝 암기 필수 템플릿

### 1. BFS 기본

{% raw %}

```java
public void bfs(int start) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] visited = new boolean[n];
    
    queue.offer(start);
    visited[start] = true;
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                visited[next] = true;
                queue.offer(next);
            }
        }
    }
}
```

{% endraw %}

---

### 2. 2D BFS

{% raw %}

```java
int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};

public void bfs2D(int[][] grid, int x, int y) {
    Queue<int[]> queue = new LinkedList<>();
    boolean[][] visited = new boolean[n][m];
    
    queue.offer(new int[]{x, y});
    visited[x][y] = true;
    
    while (!queue.isEmpty()) {
        int[] pos = queue.poll();
        int cx = pos[0], cy = pos[1];
        
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                !visited[nx][ny] && grid[nx][ny] == 1) {
                visited[nx][ny] = true;
                queue.offer(new int[]{nx, ny});
            }
        }
    }
}
```

{% endraw %}

---

### 3. 다익스트라

{% raw %}

```java
public int[] dijkstra(int start) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;
    
    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.offer(new Node(start, 0));
    
    while (!pq.isEmpty()) {
        Node cur = pq.poll();
        
        if (cur.distance > dist[cur.vertex]) continue;
        
        for (Edge edge : graph.get(cur.vertex)) {
            int newDist = dist[cur.vertex] + edge.weight;
            
            if (newDist < dist[edge.to]) {
                dist[edge.to] = newDist;
                pq.offer(new Node(edge.to, newDist));
            }
        }
    }
    
    return dist;
}
```

{% endraw %}

---

#Java #그래프 #Graph #BFS #DFS #다익스트라 #Dijkstra #최단경로 #ShortestPath #큐 #Queue #우선순위큐 #PriorityQueue #알고리즘 #코딩테스트