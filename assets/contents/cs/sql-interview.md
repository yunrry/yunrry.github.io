## 면접 필수 개념

### 1. 인덱스 내부 구조 (B-Tree)

- 균형 이진 트리 구조
- 루트 → 브랜치 → 리프 노드로 구성
- 리프 노드에 실제 데이터 포인터 저장
- 시간복잡도 O(logN)

### 2. 클러스터링 vs 리플리케이션

**클러스터링 (Clustering)**

- 여러 DB 서버가 하나의 DB처럼 동작
- Active-Active 구성 (모두 쓰기 가능)
- 고가용성(HA) 제공
- 장애 발생 시 자동 전환

**리플리케이션 (Replication)**

- Master(쓰기) - Slave(읽기) 구조
- 데이터 복제로 부하 분산
- 읽기 성능 향상
- Master 장애 시 수동 전환 필요

### 3. DB Lock의 종류

**Shared Lock (공유 락, S Lock)**

- 읽기 작업에 사용
- 여러 트랜잭션이 동시에 읽기 가능
- 쓰기는 불가

**Exclusive Lock (배타 락, X Lock)**

- 쓰기 작업에 사용
- 다른 트랜잭션의 읽기/쓰기 모두 차단

**Optimistic Lock (낙관적 락)**

- 충돌이 드물다고 가정
- 버전 컬럼으로 충돌 감지
- UPDATE 시점에 검증

**Pessimistic Lock (비관적 락)**

- 충돌이 빈번하다고 가정
- 데이터 조회 시점에 락 획득
- `SELECT ... FOR UPDATE`

### 4. 트랜잭션 격리 수준 문제

**Dirty Read**

- 커밋되지 않은 데이터 읽기
- READ UNCOMMITTED에서 발생

**Non-Repeatable Read**

- 같은 데이터를 두 번 읽었을 때 값이 다름
- READ COMMITTED에서 발생

**Phantom Read**

- 같은 조건으로 조회했을 때 행 개수가 다름
- REPEATABLE READ에서 발생

### 5. 정규화 vs 역정규화

**정규화 (Normalization)**

- 중복 제거, 무결성 향상
- 읽기가 적고 쓰기가 많은 경우 유리

**역정규화 (Denormalization)**

- 의도적으로 중복 허용
- JOIN 감소로 읽기 성능 향상
- 읽기가 많고 쓰기가 적은 경우 유리

### 6. NoSQL vs RDBMS

**RDBMS**

- 정형 데이터, 강한 일관성
- ACID 보장
- 복잡한 쿼리 지원
- 수직 확장 (Scale-Up)

**NoSQL**

- 비정형 데이터, 유연한 스키마
- BASE (Basically Available, Soft state, Eventually consistent)
- 단순한 쿼리
- 수평 확장 (Scale-Out)

### 7. 실행 계획 (Execution Plan)

```sql
EXPLAIN SELECT * FROM employees WHERE department = 'IT';
```

- type: ALL(풀스캔), index, range, ref, eq_ref
- key: 사용된 인덱스
- rows: 예상 행 수
- Extra: Using where, Using index, Using filesort
