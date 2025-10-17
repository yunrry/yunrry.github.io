# 플로이드-워셜 유사 문제 모음

## 🔴 프로그래머스

### 1. **순위** (Level 3) ⭐
- 문제: 권투 선수 순위 결정
- 유형: 전이적 관계 (Transitive Closure)
- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49191

### 2. **가장 먼 노드** (Level 3)
- 문제: 1번 노드로부터 가장 먼 노드들의 개수
- 유형: 최단 거리 (BFS도 가능하지만 플로이드-워셜로도 풀 수 있음)
- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49189

### 3. **합승 택시 요금** (Level 3) ⭐ 추천
- 문제: A, B가 중간까지 합승 후 각자 목적지로
- 유형: 모든 쌍 최단 경로
- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/72413

### 4. **배달** (Level 2)
- 문제: K 이하의 시간에 배달 가능한 마을
- 유형: 최단 경로 (다익스트라/플로이드-워셜)
- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12978


## 🟠 LeetCode

### 1. **Floyd Warshall 직접 구현**

#### **1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance** (Medium) ⭐ 추천
```java
// 거리 임계값 이내에 도달 가능한 도시가 가장 적은 도시 찾기
// 전형적인 플로이드-워셜 문제
```
- 링크: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

#### **399. Evaluate Division** (Medium) ⭐ 추천
```java
// a/b = 2.0, b/c = 3.0이면 a/c = 6.0 추론
// 전이적 관계를 곱셈으로 계산
```
- 링크: https://leetcode.com/problems/evaluate-division/

#### **1462. Course Schedule IV** (Medium)
```java
// 선수과목 관계에서 A를 들으면 B도 들을 수 있는지 판단
// 전이적 폐포 문제
```
- 링크: https://leetcode.com/problems/course-schedule-iv/

### 2. **최단 경로 관련**

#### **743. Network Delay Time** (Medium)
```java
// 모든 노드에 신호가 도달하는 최소 시간
// 다익스트라 또는 플로이드-워셜
```
- 링크: https://leetcode.com/problems/network-delay-time/

#### **1976. Number of Ways to Arrive at Destination** (Medium)
```java
// 최단 경로의 개수 구하기
```
- 링크: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

### 3. **전이적 관계**

#### **1615. Maximal Network Rank** (Medium)
```java
// 두 도시를 연결하는 네트워크 랭크의 최댓값
```
- 링크: https://leetcode.com/problems/maximal-network-rank/

#### **1391. Check if There is a Valid Path in a Grid** (Medium)
```java
// 격자에서 경로 존재 여부
```
- 링크: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/



## 🟢 백준

### 1. **플로이드-워셜 기본**

#### **11404. 플로이드** (Gold 4) ⭐ 기본 중의 기본
```
모든 도시 쌍의 최단 경로 구하기
전형적인 플로이드-워셜 템플릿 문제
```
- 링크: https://www.acmicpc.net/problem/11404

#### **11403. 경로 찾기** (Silver 1) ⭐ 입문용
```
i에서 j로 가는 경로가 있는지 판단
boolean 배열로 전이적 폐포
```
- 링크: https://www.acmicpc.net/problem/11403

#### **1389. 케빈 베이컨의 6단계 법칙** (Silver 1)
```
모든 사람 쌍의 단계 수 합이 가장 작은 사람
```
- 링크: https://www.acmicpc.net/problem/1389

### 2. **응용 문제**

#### **1956. 운동** (Gold 4) ⭐ 추천
```
최소 사이클 길이 찾기
플로이드-워셜 + dist[i][i] 확인
```
- 링크: https://www.acmicpc.net/problem/1956

#### **2458. 키 순서** (Gold 4) ⭐⭐ 권투 문제와 거의 동일!
```
학생들의 키 순서가 확정되는 학생 수
당신이 푼 순위 문제와 완전히 동일한 로직!
```
- 링크: https://www.acmicpc.net/problem/2458

#### **1613. 역사** (Gold 3)
```
사건의 전후 관계 판단
전이적 관계
```
- 링크: https://www.acmicpc.net/problem/1613

#### **1738. 골목길** (Gold 2)
```
최단 경로에서 양수 사이클 찾기
플로이드-워셜 응용
```
- 링크: https://www.acmicpc.net/problem/1738

### 3. **어려운 응용**

#### **1507. 궁금한 민호** (Gold 2) ⭐ 흥미로운 문제
```
주어진 최단 거리 행렬에서 불필요한 간선 제거
역발상 문제
```
- 링크: https://www.acmicpc.net/problem/1507

#### **13168. 내일로 여행** (Gold 2)
```
티켓을 샀을 때와 안 샀을 때 비교
플로이드-워셜 두 번
```
- 링크: https://www.acmicpc.net/problem/13168

#### **2660. 회장뽑기** (Gold 5)
```
회원 간 관계에서 회장 후보 찾기
```
- 링크: https://www.acmicpc.net/problem/2660

---

## 📚 난이도별 추천 학습 순서

### **입문 (플로이드-워셜 이해하기)**
1. 백준 11403 - 경로 찾기
2. 백준 1389 - 케빈 베이컨
3. 백준 11404 - 플로이드

### **기본 (전이적 관계)**
4. 백준 2458 - 키 순서 ⭐ 권투 문제와 동일!
5. 백준 1613 - 역사
6. LeetCode 1462 - Course Schedule IV

### **응용 (실전 문제)**
7. 프로그래머스 - 합승 택시 요금
8. LeetCode 1334 - Find the City
9. 백준 1956 - 운동

### **심화**
10. LeetCode 399 - Evaluate Division (곱셈 전이)
11. 백준 1507 - 궁금한 민호 (역발상)

---

## 💡 유형별 분류

### **전이적 폐포 (Transitive Closure)**
- 프로그래머스: 순위
- 백준: 2458 (키 순서), 1613 (역사), 11403 (경로 찾기)
- LeetCode: 1462 (Course Schedule IV)

### **모든 쌍 최단 경로**
- 프로그래머스: 합승 택시 요금
- 백준: 11404 (플로이드), 1389 (케빈 베이컨)
- LeetCode: 1334 (Find the City)

### **사이클 탐지**
- 백준: 1956 (운동), 1738 (골목길)

### **특수 응용**
- LeetCode: 399 (나눗셈 전이)
- 백준: 1507 (불필요한 간선 제거)

