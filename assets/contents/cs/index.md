## 인덱스

### 인덱스란?

데이터 검색 속도를 향상시키는 자료구조 (보통 B-Tree 사용)

### 인덱스 생성

```sql
-- 단일 컬럼 인덱스
CREATE INDEX idx_name ON employees(name);

-- 복합 인덱스
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- 유니크 인덱스
CREATE UNIQUE INDEX idx_email ON users(email);

-- 인덱스 삭제
DROP INDEX idx_name ON employees;
```

### 인덱스 장단점

**장점**

- 검색 속도 대폭 향상 (O(logN))
- ORDER BY, GROUP BY 성능 향상
- MIN/MAX 값 빠르게 조회

**단점**

- 추가 저장 공간 필요 (테이블 크기의 10% 정도)
- INSERT, UPDATE, DELETE 속도 저하
- 인덱스 재구성 비용 발생

### 인덱스 사용이 효과적인 경우

- WHERE 절에 자주 사용되는 컬럼
- JOIN에 사용되는 컬럼
- ORDER BY에 사용되는 컬럼
- 카디널리티가 높은 컬럼 (중복이 적은 컬럼)
- 데이터 변경이 적은 테이블
