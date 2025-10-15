## 트랜잭션

### 트랜잭션이란?

하나의 논리적 작업 단위, 전부 성공 또는 전부 실패 (All or Nothing)

```sql
-- 트랜잭션 시작
START TRANSACTION;

-- 작업 수행
UPDATE accounts SET balance = balance - 10000 WHERE id = 1;
UPDATE accounts SET balance = balance + 10000 WHERE id = 2;

-- 성공 시 확정
COMMIT;

-- 실패 시 취소
ROLLBACK;
```

### ACID 속성

**Atomicity (원자성)**

- 트랜잭션의 모든 연산이 완전히 수행되거나 전혀 수행되지 않아야 함
- 예: 계좌이체 시 출금과 입금이 모두 성공하거나 모두 실패

**Consistency (일관성)**

- 트랜잭션 실행 전후 데이터베이스가 일관된 상태 유지
- 예: 총 잔액의 합은 항상 동일해야 함

**Isolation (격리성)**

- 동시에 실행되는 트랜잭션들이 서로 영향을 주지 않음
- 격리 수준: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE

**Durability (지속성)**

- 커밋된 트랜잭션은 시스템 장애가 발생해도 영구 반영
- 예: COMMIT 후에는 데이터베이스에 영구 저장

### 격리 수준 (Isolation Level)

**READ UNCOMMITTED (레벨 0)**

- 커밋되지 않은 데이터 읽기 가능
- 문제: Dirty Read

**READ COMMITTED (레벨 1)**

- 커밋된 데이터만 읽기 가능
- 문제: Non-Repeatable Read

**REPEATABLE READ (레벨 2)**

- 트랜잭션 내에서 같은 데이터는 항상 동일
- 문제: Phantom Read

**SERIALIZABLE (레벨 3)**

- 가장 엄격한 격리 수준
- 완전한 격리 보장, 성능 저하
