# 플로이드-워셜 (Floyd-Warshall) 알고리즘

## 핵심 개념

**모든 정점 쌍 사이의 최단 경로**를 구하는 알고리즘입니다. 동적 계획법(DP)을 사용.

## 기본 아이디어

"A에서 B로 가는 경로에 K를 거쳐가면 더 짧아질까?"를 모든 정점에 대해 확인.

```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**핵심: k를 거쳐가는 것이 더 나은지 비교**

## 알고리즘 구조

```java
// 1. 초기화: 인접 행렬로 그래프 표현
int[][] dist = new int[n][n];
for (int i = 0; i < n; i++) {
    Arrays.fill(dist[i], INF);
    dist[i][i] = 0;  // 자기 자신은 0
}

// 간선 정보 입력
for (int[] edge : edges) {
    dist[edge[0]][edge[1]] = edge[2];  // 가중치
}

// 2. 플로이드-워셜 핵심 로직
for (int k = 0; k < n; k++) {           // 경유지
    for (int i = 0; i < n; i++) {       // 출발지
        for (int j = 0; j < n; j++) {   // 도착지
            if (dist[i][k] + dist[k][j] < dist[i][j]) {
                dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
}
```

## 3중 루프의 의미

```java
for (int k = 0; k < n; k++)      // "k번 정점을 거쳐갈까?"
    for (int i = 0; i < n; i++)  // "i에서 출발해서"
        for (int j = 0; j < n; j++)  // "j로 가는데"
```

**중요: k가 가장 바깥 루프여야 합니다!** 이것이 DP의 핵심이다.

## 시각적 예제

```
그래프:
1 → 2 (3)
2 → 3 (4)
1 → 3 (10)

초기 dist:
    1   2   3
1   0   3  10
2  INF  0   4
3  INF INF  0

k=1 (1번 정점 경유):
    1   2   3
1   0   3  10
2  INF  0   4
3  INF INF  0
(변화 없음)

k=2 (2번 정점 경유):
    1   2   3
1   0   3   7  ← dist[1][3] = min(10, 3+4) = 7
2  INF  0   4
3  INF INF  0

k=3 (3번 정점 경유):
    1   2   3
1   0   3   7
2  INF  0   4
3  INF INF  0
(변화 없음)

최종 결과: 1→3 최단거리 = 7
```

## 실전 활용 패턴

### 1. 최단 거리 구하기
```java
public int[][] floydWarshall(int n, int[][] edges) {
    int[][] dist = new int[n + 1][n + 1];
    
    for (int i = 1; i <= n; i++) {
        Arrays.fill(dist[i], INF);
        dist[i][i] = 0;
    }
    
    for (int[] edge : edges) {
        dist[edge[0]][edge[1]] = edge[2];
    }
    
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = Math.min(dist[i][j], 
                                          dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    return dist;
}
```

### 2. 경로 존재 여부 (boolean 버전)
```java
public boolean[][] findReachability(int n, int[][] edges) {
    boolean[][] reach = new boolean[n + 1][n + 1];
    
    // 자기 자신은 도달 가능
    for (int i = 1; i <= n; i++) {
        reach[i][i] = true;
    }
    
    // 직접 연결된 간선
    for (int[] edge : edges) {
        reach[edge[0]][edge[1]] = true;
    }
    
    // 전이적 폐포 (Transitive Closure)
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (reach[i][k] && reach[k][j]) {
                    reach[i][j] = true;
                }
            }
        }
    }
    
    return reach;
}
```

### 3. 음수 사이클 탐지
```java
// 플로이드-워셜 실행 후
for (int i = 1; i <= n; i++) {
    if (dist[i][i] < 0) {
        System.out.println("음수 사이클 존재!");
        break;
    }
}
```

## 시간 복잡도

- **시간: O(n³)** - 3중 반복문
- **공간: O(n²)** - 인접 행렬

## 다른 최단 경로 알고리즘과 비교

| 알고리즘 | 시간 복잡도 | 용도 | 음수 간선 |
|---------|-----------|------|----------|
| **플로이드-워셜** | O(n³) | 모든 쌍 최단 경로 | ✓ (사이클 X) |
| **다익스트라** | O((V+E)logV) | 단일 출발점 | ✗ |
| **벨만-포드** | O(VE) | 단일 출발점 | ✓ |

## 실전 문제 유형

### 1. 순위 결정 문제 (당신의 권투 문제)
- A→B, B→C이면 A→C 추론
- 전이적 관계 찾기

### 2. 최단 거리 문제
- 모든 도시 쌍의 최단 거리
- 중간 경유지를 거쳐가는 경로

### 3. 연결성 문제
- 두 노드가 연결되어 있는가?
- 몇 단계 거쳐서 도달 가능한가?

## 주의사항

1. **k루프가 가장 바깥쪽이어야 함** (DP 순서 중요!)
2. **INF 처리 주의** (오버플로우 방지)
3. **자기 자신은 거리 0으로 초기화**
4. **양방향 그래프면 양쪽 다 추가**

## 권투 문제에 적용

```java
// Win 관계를 boolean으로 표현
boolean[][] win = new boolean[n + 1][n + 1];

// 직접 경기 결과
for (int[] result : results) {
    win[result[0]][result[1]] = true;
}

// 전이적 관계 추론
for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            // i→k이고 k→j이면, i→j도 성립
            if (win[i][k] && win[k][j]) {
                win[i][j] = true;
            }
        }
    }
}
```

