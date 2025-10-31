
# 그리디 & 구현

그리디(Greedy)는 매 순간 최선의 선택을 하는 알고리즘이고,   
구현(Implementation)은 문제에서 요구하는 대로 정확히 코드로 옮기는 능력이다.   
두 유형 모두 코딩테스트에서 자주 출제된다.

---

## 그리디 알고리즘

### 그리디란?

**Greedy = 탐욕적 선택**

```

핵심 아이디어:  

- 현재 상황에서 가장 좋은 선택  
- 선택을 번복하지 않음  
- 지역 최적해 → 전역 최적해  

```

**특징:**
- 빠름: O(n), O(n log n)
- 간단한 구현
- 증명이 어려움

---

### 그리디 vs DP

| 특성 | 그리디 | DP |
|------|--------|-----|
| **선택** | 현재 최선 | 모든 경우 |
| **되돌림** | 불가능 | 가능 |
| **최적해** | 조건부 보장 | 항상 보장 |
| **속도** | 빠름 | 느림 |
| **예시** | 거스름돈 | 배낭 문제 |

---

### 그리디가 가능한 조건

**1. 탐욕적 선택 속성 (Greedy Choice Property)**
```

현재 최선의 선택이 전체 최적해를 이룸

예: 동전 거스름돈 큰 단위부터 선택 → 최소 개수 보장 (특정 조건)

```

**2. 최적 부분 구조 (Optimal Substructure)**
```

부분 문제의 최적해가 전체 최적해에 포함

예: 활동 선택 문제 가장 빨리 끝나는 활동 선택 → 최대 개수

````

---

## 그리디 기본 예제

### 예제 1: 거스름돈

{% raw %}
```java
public class ChangeMaking {
    // 큰 단위부터 거슬러주기
    public int minCoins(int money) {
        int[] coins = {500, 100, 50, 10};
        int count = 0;
        
        for (int coin : coins) {
            count += money / coin;
            money %= coin;
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        ChangeMaking cm = new ChangeMaking();
        System.out.println(cm.minCoins(1260));  // 6
        // 500×2 + 100×2 + 50×1 + 10×1 = 6개
    }
}
````

{% endraw %}

**! 주의**: 동전 단위가 배수 관계가 아니면 그리디 실패!

```
예: 동전 [1, 4, 6], 목표 8
그리디: 6 + 1 + 1 = 3개 ✘
최적: 4 + 4 = 2개 ✔
```

---

### 예제 2: 회의실 배정

{% raw %}

```java
import java.util.*;

public class MeetingRoom {
    static class Meeting {
        int start, end;
        
        public Meeting(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    
    // 최대한 많은 회의 배정
    public int maxMeetings(int[][] meetings) {
        Meeting[] m = new Meeting[meetings.length];
        for (int i = 0; i < meetings.length; i++) {
            m[i] = new Meeting(meetings[i][0], meetings[i][1]);
        }
        
        // 끝나는 시간 기준 정렬 (핵심!)
        Arrays.sort(m, (a, b) -> a.end - b.end);
        
        int count = 0;
        int lastEnd = 0;
        
        for (Meeting meeting : m) {
            // 이전 회의가 끝난 후 시작 가능하면 선택
            if (meeting.start >= lastEnd) {
                count++;
                lastEnd = meeting.end;
            }
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        MeetingRoom mr = new MeetingRoom();
        int[][] meetings = {
            {1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9},
            {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}
        };
        System.out.println(mr.maxMeetings(meetings));  // 4
        // [1,4], [5,7], [8,11], [12,14]
    }
}
```

{% endraw %}

**핵심**: 빨리 끝나는 회의부터 선택 → 최대 개수

---

### 예제 3: 큰 수 만들기

{% raw %}

```java
public class CreateLargestNumber {
    // 프로그래머스: 큰 수 만들기
    // k개 숫자를 제거하여 가장 큰 수 만들기
    
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int length = number.length() - k;  // 최종 길이
        
        int start = 0;
        for (int i = 0; i < length; i++) {
            char max = '0';
            int maxIdx = start;
            
            // 현재 위치에서 선택 가능한 범위 내 최대값
            for (int j = start; j <= k + i; j++) {
                if (number.charAt(j) > max) {
                    max = number.charAt(j);
                    maxIdx = j;
                }
            }
            
            sb.append(max);
            start = maxIdx + 1;
        }
        
        return sb.toString();
    }
    
    // 스택 활용 (더 효율적)
    public String solutionOptimized(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        int toRemove = k;
        
        for (char digit : number.toCharArray()) {
            // 현재 숫자보다 작은 숫자들 제거
            while (toRemove > 0 && !stack.isEmpty() && 
                   stack.peekLast() < digit) {
                stack.pollLast();
                toRemove--;
            }
            stack.offerLast(digit);
        }
        
        // 아직 제거할 개수가 남았으면 뒤에서 제거
        while (toRemove > 0) {
            stack.pollLast();
            toRemove--;
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollFirst());
        }
        
        return sb.toString();
    }
    
    public static void main(String[] args) {
        CreateLargestNumber cln = new CreateLargestNumber();
        System.out.println(cln.solution("1924", 2));      // "94"
        System.out.println(cln.solution("1231234", 3));   // "3234"
        System.out.println(cln.solution("4177252841", 4)); // "775841"
    }
}
```

{% endraw %}

---

### 예제 4: 배 배치

{% raw %}

```java
public class BoatAssignment {
    // 프로그래머스: 구명보트
    // 최대 2명, 무게 제한 있을 때 최소 배 개수
    
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        
        int left = 0;
        int right = people.length - 1;
        int boats = 0;
        
        while (left <= right) {
            // 가장 가벼운 사람 + 가장 무거운 사람
            if (people[left] + people[right] <= limit) {
                left++;   // 둘 다 태움
            }
            right--;  // 무거운 사람은 무조건 태움
            boats++;
        }
        
        return boats;
    }
    
    public static void main(String[] args) {
        BoatAssignment ba = new BoatAssignment();
        System.out.println(ba.solution(new int[]{70, 50, 80, 50}, 100));  // 3
        System.out.println(ba.solution(new int[]{70, 80, 50}, 100));       // 3
    }
}
```

{% endraw %}

---

### 예제 5: 섬 연결하기 (크루스칼)

{% raw %}

```java
import java.util.*;

public class ConnectIslands {
    // 프로그래머스: 섬 연결하기
    // 최소 비용으로 모든 섬 연결 (MST)
    
    static class Edge implements Comparable<Edge> {
        int from, to, cost;
        
        public Edge(int from, int to, int cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Edge other) {
            return this.cost - other.cost;
        }
    }
    
    int[] parent;
    
    public int solution(int n, int[][] costs) {
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // 간선을 비용 기준 정렬
        Edge[] edges = new Edge[costs.length];
        for (int i = 0; i < costs.length; i++) {
            edges[i] = new Edge(costs[i][0], costs[i][1], costs[i][2]);
        }
        Arrays.sort(edges);
        
        int totalCost = 0;
        int edgeCount = 0;
        
        for (Edge edge : edges) {
            // 사이클이 생기지 않으면 선택
            if (union(edge.from, edge.to)) {
                totalCost += edge.cost;
                edgeCount++;
                
                if (edgeCount == n - 1) break;  // MST 완성
            }
        }
        
        return totalCost;
    }
    
    private int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    
    private boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        
        if (x == y) return false;  // 사이클
        
        parent[y] = x;
        return true;
    }
    
    public static void main(String[] args) {
        ConnectIslands ci = new ConnectIslands();
        int[][] costs = {{0,1,1}, {0,2,2}, {1,2,5}, {1,3,1}, {2,3,8}};
        System.out.println(ci.solution(4, costs));  // 4
    }
}
```

{% endraw %}

---

## 그리디 문제 패턴

### 패턴 1: 정렬 후 선택

{% raw %}

```java
// 가장 작은/큰 것부터 선택
Arrays.sort(arr);

for (int item : arr) {
    if (조건) {
        선택();
    }
}
```

{% endraw %}

**예시**: 거스름돈, 회의실 배정

---

### 패턴 2: 두 포인터

{% raw %}

```java
// 양쪽 끝에서 접근
Arrays.sort(arr);
int left = 0, right = arr.length - 1;

while (left < right) {
    if (조건) {
        // 선택
    }
    // 포인터 이동
}
```

{% endraw %}

**예시**: 구명보트, 용액

---

### 패턴 3: 우선순위 큐

{% raw %}

```java
// 항상 최선의 선택
PriorityQueue<Integer> pq = new PriorityQueue<>();

while (!pq.isEmpty()) {
    int best = pq.poll();
    // 처리
}
```

{% endraw %}

**예시**: 디스크 컨트롤러, 이중우선순위큐

---

### 패턴 4: 카운팅

{% raw %}

```java
// 빈도수 계산 후 선택
Map<Character, Integer> count = new HashMap<>();

for (char c : s.toCharArray()) {
    count.put(c, count.getOrDefault(c, 0) + 1);
}

// 빈도 기준 처리
```

{% endraw %}

**예시**: 문자열 압축, 단어 변환

---

## 🔧 구현 (Implementation)

### 구현이란?

**문제에서 요구하는 대로 정확히 구현**

```
특징:
- 알고리즘은 간단
- 코드가 길어짐
- 실수하기 쉬움
- 디버깅 중요
```

---

### 구현 문제 유형

**1. 시뮬레이션**

```
주어진 규칙대로 시뮬레이션

예: 로봇 이동, 게임 구현
```

**2. 완전 탐색**

```
모든 경우의 수 확인

예: 순열, 조합
```

**3. 문자열 처리**

```
복잡한 문자열 조작

예: 압축, 파싱
```

**4. 그리드/격자**

```
2D 배열에서 작업

예: 지도, 보드 게임
```

---

## 구현 예제

### 예제 1: 상하좌우 이동

{% raw %}

```java
public class RobotMovement {
    // 프로그래머스 유형
    // N×N 격자, 명령에 따라 이동
    
    public int[] solution(int n, String[] commands) {
        int x = 1, y = 1;  // 시작 (1, 1)
        
        // 방향: 상하좌우
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        Map<Character, Integer> dir = new HashMap<>();
        dir.put('U', 0);
        dir.put('D', 1);
        dir.put('L', 2);
        dir.put('R', 3);
        
        for (String command : commands) {
            char d = command.charAt(0);
            int nx = x + dx[dir.get(d)];
            int ny = y + dy[dir.get(d)];
            
            // 범위 체크
            if (nx >= 1 && nx <= n && ny >= 1 && ny <= n) {
                x = nx;
                y = ny;
            }
        }
        
        return new int[]{x, y};
    }
    
    public static void main(String[] args) {
        RobotMovement rm = new RobotMovement();
        String[] commands = {"R", "R", "R", "U", "D", "D"};
        System.out.println(Arrays.toString(rm.solution(5, commands)));
        // [3, 4]
    }
}
```

{% endraw %}

---

### 예제 2: 시계 방향 회전

{% raw %}

```java
public class RotateMatrix {
    // 2D 배열 90도 회전
    
    public int[][] rotate90(int[][] matrix) {
        int n = matrix.length;
        int[][] result = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[j][n - 1 - i] = matrix[i][j];
            }
        }
        
        return result;
    }
    
    // 제자리 회전 (공간 O(1))
    public void rotateInPlace(int[][] matrix) {
        int n = matrix.length;
        
        // 전치 (transpose)
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // 좌우 반전
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
    
    public static void main(String[] args) {
        RotateMatrix rm = new RotateMatrix();
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        int[][] rotated = rm.rotate90(matrix);
        for (int[] row : rotated) {
            System.out.println(Arrays.toString(row));
        }
        // [7, 4, 1]
        // [8, 5, 2]
        // [9, 6, 3]
    }
}
```

{% endraw %}

---

### 예제 3: 나선형 순회

{% raw %}

```java
public class SpiralMatrix {
    // 달팽이 배열
    
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int num = 1;
        
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        
        while (top <= bottom && left <= right) {
            // 오른쪽
            for (int j = left; j <= right; j++) {
                matrix[top][j] = num++;
            }
            top++;
            
            // 아래
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--;
            
            // 왼쪽
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    matrix[bottom][j] = num++;
                }
                bottom--;
            }
            
            // 위
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++;
            }
        }
        
        return matrix;
    }
    
    public static void main(String[] args) {
        SpiralMatrix sm = new SpiralMatrix();
        int[][] matrix = sm.generateMatrix(3);
        
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
        // [1, 2, 3]
        // [8, 9, 4]
        // [7, 6, 5]
    }
}
```

{% endraw %}

---

### 예제 4: 문자열 압축

{% raw %}

```java
public class StringCompression {
    // 프로그래머스: 문자열 압축
    
    public int solution(String s) {
        int minLength = s.length();
        
        // 1개부터 s.length()/2개까지 자르기 시도
        for (int size = 1; size <= s.length() / 2; size++) {
            String compressed = compress(s, size);
            minLength = Math.min(minLength, compressed.length());
        }
        
        return minLength;
    }
    
    private String compress(String s, int size) {
        StringBuilder sb = new StringBuilder();
        String prev = "";
        int count = 0;
        
        for (int i = 0; i < s.length(); i += size) {
            String current = s.substring(i, Math.min(i + size, s.length()));
            
            if (current.equals(prev)) {
                count++;
            } else {
                if (count > 1) {
                    sb.append(count);
                }
                sb.append(prev);
                prev = current;
                count = 1;
            }
        }
        
        if (count > 1) {
            sb.append(count);
        }
        sb.append(prev);
        
        return sb.toString();
    }
    
    public static void main(String[] args) {
        StringCompression sc = new StringCompression();
        System.out.println(sc.solution("aabbaccc"));       // 7 (2a2ba3c)
        System.out.println(sc.solution("ababcdcdababcdcd")); // 9 (2ababcdcd)
        System.out.println(sc.solution("abcabcdede"));     // 8 (2abcdede)
    }
}
```

{% endraw %}

---

### 예제 5: 뱀 게임

{% raw %}

```java
public class SnakeGame {
    // 백준 3190: 뱀
    
    static class Point {
        int x, y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Point)) return false;
            Point p = (Point) o;
            return x == p.x && y == p.y;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    
    public int solution(int n, int[][] apples, String[] commands) {
        Set<Point> appleSet = new HashSet<>();
        for (int[] apple : apples) {
            appleSet.add(new Point(apple[0], apple[1]));
        }
        
        // 방향: 우하좌상
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int dir = 0;  // 초기 방향: 오른쪽
        
        Deque<Point> snake = new LinkedList<>();
        snake.offer(new Point(1, 1));
        
        int time = 0;
        int commandIdx = 0;
        
        while (true) {
            time++;
            
            // 머리 이동
            Point head = snake.peekFirst();
            int nx = head.x + dx[dir];
            int ny = head.y + dy[dir];
            
            // 벽 또는 자기 몸 충돌
            if (nx < 1 || nx > n || ny < 1 || ny > n ||
                snake.contains(new Point(nx, ny))) {
                break;
            }
            
            Point newHead = new Point(nx, ny);
            snake.offerFirst(newHead);
            
            // 사과 있으면 꼬리 유지, 없으면 꼬리 제거
            if (appleSet.contains(newHead)) {
                appleSet.remove(newHead);
            } else {
                snake.pollLast();
            }
            
            // 방향 전환
            if (commandIdx < commands.length) {
                String[] cmd = commands[commandIdx].split(" ");
                if (Integer.parseInt(cmd[0]) == time) {
                    if (cmd[1].equals("D")) {
                        dir = (dir + 1) % 4;  // 오른쪽
                    } else {
                        dir = (dir + 3) % 4;  // 왼쪽
                    }
                    commandIdx++;
                }
            }
        }
        
        return time;
    }
}
```

{% endraw %}

---

## 실전 팁

### 그리디 문제 풀이

```
Step 1: 정렬할 기준 찾기
Step 2: 선택 규칙 정하기
Step 3: 반례 생각하기
Step 4: 증명 시도
Step 5: 구현

⚠️ 주의: 그리디가 항상 맞는지 확인!
```

---

### 구현 문제 풀이

```
Step 1: 문제 이해 (조건, 규칙)
Step 2: 입출력 예시 확인
Step 3: 단계별로 나누기
Step 4: 작은 함수로 분리
Step 5: 디버깅

⚠️ 주의: 경계 조건, 인덱스!
```

---

### 디버깅 팁

{% raw %}

```java
// 1. 중간 상태 출력
System.out.println("현재 상태: " + state);
System.out.println("배열: " + Arrays.toString(arr));

// 2. 격자 출력
for (int[] row : grid) {
    for (int cell : row) {
        System.out.print(cell + " ");
    }
    System.out.println();
}

// 3. 조건 확인
System.out.println("조건 만족: " + (condition));
```

{% endraw %}

---

## 추천 문제

### 그리디 (⭐)

1. **[백준 11399] ATM**
    - 정렬 그리디
2. **[백준 11047] 동전 0**
    - 거스름돈
3. **[백준 1931] 회의실 배정**
    - 활동 선택
4. **[백준 2839] 설탕 배달**
    - 그리디 or DP
5. **[프로그래머스] 체육복**
    - 간단한 그리디
6. **[프로그래머스] 큰 수 만들기**
    - 스택 그리디
7. **[프로그래머스] 구명보트**
    - 투 포인터

---

### 그리디 응용 (⭐⭐)

1. **[백준 1541] 잃어버린 괄호**
    - 수식 최소화
2. **[백준 1026] 보물**
    - 정렬
3. **[백준 13305] 주유소**
    - 누적 최소
4. **[백준 1715] 카드 정렬하기**
    - 우선순위 큐
5. **[프로그래머스] 섬 연결하기**
    - MST (크루스칼)
6. **[프로그래머스] 단속카메라**
    - 구간 선택

---

### 구현 - 시뮬레이션 (⭐)

1. **[백준 14503] 로봇 청소기**
    - 구현 + 시뮬레이션
2. **[백준 14891] 톱니바퀴**
    - 시뮬레이션
3. **[백준 15686] 치킨 배달**
    - 완전 탐색
4. **[백준 3190] 뱀**
    - 큐 시뮬레이션
5. **[프로그래머스] 문자열 압축**
    - 문자열 처리

---

### 구현 - 격자 (⭐⭐)

1. **[백준 14500] 테트로미노**
    - 완전 탐색
2. **[백준 16234] 인구 이동**
    - BFS + 시뮬레이션
3. **[백준 17144] 미세먼지 안녕!**
    - 시뮬레이션
4. **[백준 15683] 감시**
    - 백트래킹
5. **[프로그래머스] 자물쇠와 열쇠**
    - 2D 배열

---

### 심화 (⭐⭐⭐)

1. **[백준 17822] 원판 돌리기**
    - 복잡한 시뮬레이션
2. **[백준 19237] 어른 상어**
    - 시뮬레이션 + 구현
3. **[백준 20055] 컨베이어 벨트 위의 로봇**
    - 시뮬레이션
4. **[백준 23288] 주사위 굴리기 2**
    - 시뮬레이션
5. **[프로그래머스] 블록 이동하기**
    - BFS + 회전

---

## 학습 로드맵

### 1주차: 그리디 기초

- [ ] 거스름돈 문제
- [ ] 회의실 배정
- [ ] 체육복
- [ ] ATM

### 2주차: 그리디 응용

- [ ] 큰 수 만들기
- [ ] 구명보트
- [ ] 섬 연결하기 (MST)
- [ ] 주유소

### 3주차: 구현 기초
- [ ] 상하좌우 이동
- [ ] 시각 (완전탐색)
- [ ] 문자열 압축
- [ ] 왕실의 나이트

### 4주차: 구현 심화

- [ ] 로봇 청소기
- [ ] 뱀 게임
- [ ] 톱니바퀴
- [ ] 테트로미노

---

## 패턴별 템플릿

### 1. 정렬 그리디

{% raw %}

```java
// 배열 정렬 후 순차 처리
Arrays.sort(arr);

int result = 0;
for (int item : arr) {
    if (조건_만족) {
        선택();
        result += item;
    }
}
```

{% endraw %}

---

### 2. 우선순위 큐 그리디

{% raw %}

```java
// 항상 최선 선택
PriorityQueue<Integer> pq = new PriorityQueue<>();

for (int item : items) {
    pq.offer(item);
}

while (!pq.isEmpty()) {
    int best = pq.poll();
    처리(best);
}
```

{% endraw %}

---

### 3. 4방향 이동

{% raw %}

```java
// 상하좌우 이동 템플릿
int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};

for (int dir = 0; dir < 4; dir++) {
    int nx = x + dx[dir];
    int ny = y + dy[dir];
    
    if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
        // 유효한 이동
    }
}
```

{% endraw %}

---

### 4. 8방향 이동

{% raw %}

```java
// 8방향 (상하좌우 + 대각선)
int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

for (int dir = 0; dir < 8; dir++) {
    int nx = x + dx[dir];
    int ny = y + dy[dir];
    
    if (범위_체크(nx, ny)) {
        // 처리
    }
}
```

{% endraw %}

---

### 5. 회전 구현

{% raw %}

```java
// 시계방향 90도 회전
public void rotate90(int[][] matrix) {
    int n = matrix.length;
    
    // 전치
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    
    // 좌우 반전
    for (int i = 0; i < n; i++) {
        reverse(matrix[i]);
    }
}
```

{% endraw %}

---

## 고급 예제

### 예제 1: 뱀과 사다리 게임

{% raw %}

```java
public class SnakeAndLadder {
    // LeetCode 909
    // 최소 주사위 굴림 횟수
    
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        int target = n * n;
        
        // 보드를 1차원으로 변환
        int[] cells = new int[target + 1];
        boolean leftToRight = true;
        int idx = 1;
        
        for (int i = n - 1; i >= 0; i--) {
            if (leftToRight) {
                for (int j = 0; j < n; j++) {
                    cells[idx++] = board[i][j];
                }
            } else {
                for (int j = n - 1; j >= 0; j--) {
                    cells[idx++] = board[i][j];
                }
            }
            leftToRight = !leftToRight;
        }
        
        // BFS
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[target + 1];
        
        queue.offer(1);
        visited[1] = true;
        int moves = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                int curr = queue.poll();
                
                if (curr == target) return moves;
                
                // 주사위 1~6
                for (int dice = 1; dice <= 6; dice++) {
                    int next = curr + dice;
                    if (next > target) break;
                    
                    // 뱀 또는 사다리
                    if (cells[next] != -1) {
                        next = cells[next];
                    }
                    
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }
            moves++;
        }
        
        return -1;
    }
}
```

{% endraw %}

---

### 예제 2: 캐슬 디펜스

{% raw %}

```java
public class CastleDefense {
    // 백준 17135: 캐슬 디펜스
    
    static class Enemy {
        int x, y;
        
        public Enemy(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    int N, M, D;
    int[][] grid;
    int maxKill = 0;
    
    public int solution(int n, int m, int d, int[][] map) {
        this.N = n;
        this.M = m;
        this.D = d;
        this.grid = map;
        
        // 궁수 3명 배치 (조합)
        placeArchers(0, 0, new ArrayList<>());
        
        return maxKill;
    }
    
    // 궁수 배치 (조합)
    private void placeArchers(int start, int count, List<Integer> archers) {
        if (count == 3) {
            // 게임 시뮬레이션
            int kills = simulate(archers);
            maxKill = Math.max(maxKill, kills);
            return;
        }
        
        for (int i = start; i < M; i++) {
            archers.add(i);
            placeArchers(i + 1, count + 1, archers);
            archers.remove(archers.size() - 1);
        }
    }
    
    // 게임 시뮬레이션
    private int simulate(List<Integer> archers) {
        // 적 복사
        List<Enemy> enemies = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    enemies.add(new Enemy(i, j));
                }
            }
        }
        
        int kills = 0;
        
        // 적이 모두 사라질 때까지
        while (!enemies.isEmpty()) {
            Set<Enemy> toRemove = new HashSet<>();
            
            // 각 궁수가 공격
            for (int archer : archers) {
                Enemy target = findTarget(enemies, N, archer);
                if (target != null) {
                    toRemove.add(target);
                }
            }
            
            kills += toRemove.size();
            enemies.removeAll(toRemove);
            
            // 적 이동
            List<Enemy> remaining = new ArrayList<>();
            for (Enemy enemy : enemies) {
                enemy.x++;
                if (enemy.x < N) {
                    remaining.add(enemy);
                }
            }
            enemies = remaining;
        }
        
        return kills;
    }
    
    // 가장 가까운 적 찾기
    private Enemy findTarget(List<Enemy> enemies, int archerRow, int archerCol) {
        Enemy target = null;
        int minDist = Integer.MAX_VALUE;
        
        for (Enemy enemy : enemies) {
            int dist = Math.abs(archerRow - enemy.x) + Math.abs(archerCol - enemy.y);
            
            if (dist <= D) {
                if (dist < minDist || 
                    (dist == minDist && enemy.y < target.y)) {
                    minDist = dist;
                    target = enemy;
                }
            }
        }
        
        return target;
    }
}
```

{% endraw %}

---

### 예제 3: 컨베이어 벨트

{% raw %}

```java
public class ConveyorBelt {
    // 백준 20055: 컨베이어 벨트 위의 로봇
    
    public int solution(int n, int k, int[] durability) {
        boolean[] robot = new boolean[n];  // 로봇 위치
        int step = 0;
        
        while (true) {
            step++;
            
            // 1. 벨트 회전
            int temp = durability[2 * n - 1];
            for (int i = 2 * n - 1; i > 0; i--) {
                durability[i] = durability[i - 1];
            }
            durability[0] = temp;
            
            // 로봇도 회전
            for (int i = n - 1; i > 0; i--) {
                robot[i] = robot[i - 1];
            }
            robot[0] = false;
            robot[n - 1] = false;  // 내리는 위치
            
            // 2. 로봇 이동
            for (int i = n - 2; i >= 0; i--) {
                if (robot[i] && !robot[i + 1] && durability[i + 1] > 0) {
                    robot[i] = false;
                    robot[i + 1] = true;
                    durability[i + 1]--;
                }
            }
            robot[n - 1] = false;
            
            // 3. 로봇 올리기
            if (durability[0] > 0) {
                robot[0] = true;
                durability[0]--;
            }
            
            // 4. 종료 조건
            int count = 0;
            for (int d : durability) {
                if (d == 0) count++;
            }
            
            if (count >= k) break;
        }
        
        return step;
    }
}
```

{% endraw %}

---

## 💡 자주하는 실수

### 1. 인덱스 오류

{% raw %}

```java
// ✘ 잘못된 코드
for (int i = 0; i <= n; i++) {  // n 포함 X
    arr[i] = ...;  // ArrayIndexOutOfBoundsException
}

// ✔ 올바른 코드
for (int i = 0; i < n; i++) {
    arr[i] = ...;
}
```

{% endraw %}

---

### 2. 얕은 복사

{% raw %}

```java
// ✘ 잘못된 복사
int[][] copy = original;  // 같은 참조!

// ✔ 깊은 복사
int[][] copy = new int[n][m];
for (int i = 0; i < n; i++) {
    copy[i] = original[i].clone();
}
```

{% endraw %}

---

### 3. 경계 조건

{% raw %}

```java
// ✘ 경계 체크 누락
int nx = x + dx;
grid[nx][ny] = 1;  // 범위 밖일 수 있음!

// ✔ 경계 체크
if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
    grid[nx][ny] = 1;
}
```

{% endraw %}

---

### 4. 정렬 실수

{% raw %}

```java
// ✘ 기본형 배열은 내림차순 불가
int[] arr = {3, 1, 2};
Arrays.sort(arr, Collections.reverseOrder());  // 컴파일 에러!

// ✔ Integer 배열 사용
Integer[] arr = {3, 1, 2};
Arrays.sort(arr, Collections.reverseOrder());
```

{% endraw %}

---

## 핵심 체크리스트

### 그리디

- [ ] 정렬 기준 명확한가?
- [ ] 반례 확인했는가?
- [ ] 지역 최적 = 전역 최적?
- [ ] DP가 필요한 건 아닌가?

### 구현

- [ ] 입출력 형식 확인
- [ ] 경계 조건 체크
- [ ] 인덱스 범위 확인
- [ ] 변수 초기화 확인
- [ ] 작은 예시로 테스트

---

## 빠른 입출력 템플릿

{% raw %}

```java
import java.io.*;
import java.util.*;

public class FastIO {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        // 한 줄 읽기
        String line = br.readLine();
        
        // 정수 읽기
        int n = Integer.parseInt(br.readLine());
        
        // 여러 정수 읽기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        // 배열 입력
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        // 출력
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
```

{% endraw %}

---

## 🔧 유틸리티 함수

{% raw %}

```java
public class Utils {
    // 2D 배열 출력
    public static void print2D(int[][] arr) {
        for (int[] row : arr) {
            System.out.println(Arrays.toString(row));
        }
    }
    
    // 범위 체크
    public static boolean inRange(int x, int y, int n, int m) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
    
    // 배열 복사
    public static int[][] copy2D(int[][] original) {
        int[][] copy = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            copy[i] = original[i].clone();
        }
        return copy;
    }
    
    // 최대공약수
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    
    // 최소공배수
    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
    
    // 소수 판별
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

{% endraw %}

---

## 📚 추가 학습 자료

### 그리디 심화 주제

- 최소 신장 트리 (MST)
    - 크루스칼 알고리즘
    - 프림 알고리즘
- 허프만 코딩
- 작업 스케줄링
- 분할 가능 배낭 문제

### 구현 심화 주제

- 시뮬레이션
- 백트래킹
- 비트마스킹
- 좌표 압축

---

## 마무리

### 그리디 핵심

```
1. 정렬이 핵심
2. 반례 찾기 중요
3. 증명은 어려움
4. 빠른 실행 시간
```

### 구현 핵심

```
1. 정확한 이해
2. 단계별 구현
3. 꼼꼼한 디버깅
4. 경계 조건 확인
```

### 연습 방법

```
1. 쉬운 문제부터
2. 손으로 시뮬레이션
3. 작은 입력으로 테스트
4. 다양한 예제 확인
5. 반복 연습
```

---
## 🏷️ Keywords
`#Java` `#그리디` `#Greedy` `#구현` `#Implementation` `#시뮬레이션` `#Simulation`   
`#알고리즘` `#코딩테스트``#정렬` `#문자열` `#격자` `#2D배열`  