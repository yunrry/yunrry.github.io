# 📝 자주 나오는 기출 유형

### 1. 부서별 최고 급여자 찾기

```sql
SELECT e.*
FROM employees e
WHERE (department, salary) IN (
    SELECT department, MAX(salary)
    FROM employees
    GROUP BY department
);
```

### 2. 순위 매기기 (RANK)

```sql
SELECT 
    name, 
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

### 3. 누적 합계

```sql
SELECT 
    name,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) AS cumulative_sum
FROM employees;
```

### 4. 날짜 함수

```sql
SELECT 
    NOW(),                          -- 현재 날짜시간
    CURDATE(),                      -- 현재 날짜
    DATE_ADD(NOW(), INTERVAL 7 DAY), -- 7일 후
    DATEDIFF(NOW(), hire_date)      -- 날짜 차이
FROM employees;
```

### 5. 문자열 함수

```sql
SELECT 
    CONCAT(first_name, ' ', last_name),  -- 문자열 결합
    SUBSTRING(phone, 1, 3),              -- 부분 문자열
    LENGTH(name),                        -- 길이
    UPPER(email),                        -- 대문자
    REPLACE(phone, '-', '')              -- 치환
FROM employees;
```

-----

**goal**: 각 개념을 반드시 직접 SQL로 실행해보기

