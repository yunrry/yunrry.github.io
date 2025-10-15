
## SQL 기본 문법

### SELECT 문

```sql
-- 기본 조회
SELECT column1, column2 FROM table_name;

-- 모든 컬럼 조회
SELECT * FROM employees;

-- 중복 제거
SELECT DISTINCT department FROM employees;

-- 조건 검색
SELECT * FROM employees WHERE salary >= 50000;

-- 정렬
SELECT * FROM employees ORDER BY salary DESC;

-- 상위 N개 조회
SELECT * FROM employees LIMIT 10;
```

### WHERE 절 조건

```sql
-- 비교 연산자
WHERE age >= 30
WHERE name = '홍길동'
WHERE salary BETWEEN 30000 AND 50000

-- 논리 연산자
WHERE age >= 30 AND department = 'IT'
WHERE salary < 30000 OR salary > 80000

-- IN 연산자
WHERE department IN ('IT', 'HR', 'Sales')

-- LIKE 패턴 매칭
WHERE name LIKE '김%'     -- 김으로 시작
WHERE email LIKE '%@gmail.com'  -- gmail.com으로 끝
WHERE phone LIKE '010-____-____'  -- _는 한 글자
```
