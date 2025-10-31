# GROUP BY & 집계함수

## 📌 집계함수 (Aggregate Functions)

### 1. COUNT() - 개수 세기

```sql
-- 전체 행 개수
SELECT COUNT(*) FROM employees;
-- 결과: 100

-- 특정 컬럼의 NULL이 아닌 값 개수
SELECT COUNT(commission) FROM employees;
-- 결과: 35 (commission이 NULL인 직원 제외)

-- 중복 제거한 개수
SELECT COUNT(DISTINCT department) FROM employees;
-- 결과: 5 (중복된 부서명 제외)

-- 조건부 카운트
SELECT COUNT(*) FROM employees WHERE salary >= 50000;
-- 결과: 42
```

**COUNT(*) vs COUNT(column) 차이점:**

- `COUNT(*)`: 모든 행을 센다 (NULL 포함)
- `COUNT(column)`: NULL 값을 제외하고 센다
- `COUNT(DISTINCT column)`: 중복과 NULL을 제외하고 센다

-----

### 2. SUM() - 합계

```sql
-- 전체 급여 합계
SELECT SUM(salary) FROM employees;
-- 결과: 4850000

-- 특정 부서의 급여 합계
SELECT SUM(salary) FROM employees WHERE department = 'IT';
-- 결과: 1250000

-- NULL 값은 자동으로 무시됨
SELECT SUM(commission) FROM employees;
-- commission이 NULL인 행은 계산에서 제외

-- 조건부 합계 (CASE 활용)
SELECT SUM(CASE WHEN gender = 'M' THEN salary ELSE 0 END) AS male_salary_sum
FROM employees;
```

**주의사항:**

- SUM()은 숫자형 데이터에만 사용 가능
- NULL 값은 자동으로 무시됨 (0으로 취급하지 않음)
- 모든 값이 NULL이면 결과도 NULL

-----

### 3. AVG() - 평균

```sql
-- 전체 평균 급여
SELECT AVG(salary) FROM employees;
-- 결과: 48500.00

-- 소수점 자리수 조절
SELECT ROUND(AVG(salary), 2) FROM employees;
-- 결과: 48500.00

-- NULL 제외하고 평균 계산
SELECT AVG(commission) FROM employees;
-- commission이 NULL인 직원은 평균 계산에서 제외

-- 평균보다 높은 급여를 받는 직원
SELECT name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**AVG() 계산 방식:**

```sql
-- 예시 데이터
-- salary: 50000, 60000, NULL, 40000

AVG(salary) = (50000 + 60000 + 40000) / 3 = 50000
-- NULL은 개수에서도 제외됨 (4가 아닌 3으로 나눔)
```

-----

### 4. MAX() / MIN() - 최대값 / 최소값

```sql
-- 최고 급여
SELECT MAX(salary) FROM employees;
-- 결과: 95000

-- 최저 급여
SELECT MIN(salary) FROM employees;
-- 결과: 28000

-- 최고 급여를 받는 직원 정보 (서브쿼리 활용)
SELECT name, salary 
FROM employees 
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 부서별 최고/최저 급여 차이
SELECT 
    department,
    MAX(salary) - MIN(salary) AS salary_gap
FROM employees
GROUP BY department;

-- 날짜형에도 사용 가능
SELECT MAX(hire_date) AS latest_hire FROM employees;
-- 결과: 2024-12-15 (가장 최근 입사일)

-- 문자열에도 사용 가능 (사전순)
SELECT MIN(name) FROM employees;
-- 결과: 'A'로 시작하는 이름 중 가장 앞선 이름
```

-----

### 5. 여러 집계함수 동시 사용

```sql
SELECT 
    COUNT(*) AS 총직원수,
    COUNT(DISTINCT department) AS 부서수,
    SUM(salary) AS 급여총액,
    AVG(salary) AS 평균급여,
    MAX(salary) AS 최고급여,
    MIN(salary) AS 최저급여,
    MAX(salary) - MIN(salary) AS 급여차이
FROM employees;
```

결과:

```
총직원수 | 부서수 | 급여총액  | 평균급여 | 최고급여 | 최저급여 | 급여차이
--------|-------|----------|---------|---------|---------|--------
  100   |   5   | 4850000  |  48500  |  95000  |  28000  |  67000
```

-----

## 📊 GROUP BY - 그룹화

### 1. 기본 GROUP BY

```sql
-- 부서별 직원 수
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```

결과:

```
department | employee_count
-----------|---------------
IT         | 25
HR         | 15
Sales      | 30
Marketing  | 20
Finance    | 10
```

**동작 원리:**

1. department 값이 같은 행들을 하나의 그룹으로 묶음
1. 각 그룹에 대해 COUNT(*) 계산
1. 그룹당 하나의 결과 행 반환

-----

### 2. 다중 컬럼 GROUP BY

```sql
-- 부서별, 직급별 그룹화
SELECT 
    department, 
    position, 
    COUNT(*) AS cnt,
    AVG(salary) AS avg_sal
FROM employees
GROUP BY department, position
ORDER BY department, position;
```

결과:

```
department | position | cnt | avg_sal
-----------|----------|-----|--------
IT         | Junior   | 10  | 35000
IT         | Senior   | 15  | 65000
HR         | Junior   | 8   | 32000
HR         | Senior   | 7   | 55000
Sales      | Junior   | 18  | 30000
Sales      | Senior   | 12  | 50000
```

**그룹화 순서:**

- 먼저 department로 그룹화
- 같은 department 내에서 다시 position으로 그룹화

-----

### 3. GROUP BY 사용 시 주의사항

```sql
-- ✘ 잘못된 쿼리 (에러 발생)
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department;
```

**에러 이유:**

- GROUP BY에 없는 컬럼(name)을 SELECT에 사용
- 한 부서에 여러 직원이 있는데, 어떤 name을 출력해야 할지 모호함

```sql
-- ✔ 올바른 쿼리 1: 집계함수 사용
SELECT department, COUNT(*) AS cnt
FROM employees
GROUP BY department;

-- ✔ 올바른 쿼리 2: GROUP BY에 포함
SELECT department, name, salary
FROM employees
GROUP BY department, name, salary;

-- ✔ 올바른 쿼리 3: 서브쿼리로 최고 급여자만 선택
SELECT department, name, salary
FROM employees e1
WHERE salary = (
    SELECT MAX(salary) 
    FROM employees e2 
    WHERE e2.department = e1.department
);
```

-----

### 4. GROUP BY와 WHERE 함께 사용

```sql
-- 급여가 40000 이상인 직원들만 부서별로 그룹화
SELECT 
    department, 
    COUNT(*) AS high_earners,
    AVG(salary) AS avg_salary
FROM employees
WHERE salary >= 40000  -- 그룹화 전 필터링
GROUP BY department;
```

**실행 순서:**

1. WHERE 조건으로 행 필터링 (salary >= 40000)
1. 필터링된 결과를 department로 그룹화
1. 각 그룹에 대해 집계 계산

-----

## 🔍 HAVING - 그룹 필터링

### 1. HAVING 기본 사용법

```sql
-- 평균 급여가 50000 이상인 부서만 조회
SELECT 
    department, 
    AVG(salary) AS avg_salary,
    COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING AVG(salary) >= 50000;
```

결과:

```
department | avg_salary | emp_count
-----------|------------|----------
IT         | 55000      | 25
Finance    | 62000      | 10
```

-----

### 2. WHERE vs HAVING 비교

```sql
-- WHERE: 그룹화 전 행 필터링
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary >= 50000  -- 개별 행 조건
GROUP BY department;

-- HAVING: 그룹화 후 그룹 필터링
SELECT department, COUNT(*) AS cnt
FROM employees
GROUP BY department
HAVING COUNT(*) >= 10;  -- 그룹 조건
```

**차이점 정리:**

|구분   |WHERE|HAVING|
|-----|-----|------|
|적용 시점|그룹화 전|그룹화 후 |
|대상   |개별 행 |그룹    |
|집계함수 |사용 불가|사용 가능 |
|실행 순서|2번째  |4번째   |

-----

### 3. WHERE와 HAVING 함께 사용

```sql
-- 2020년 이후 입사자 중, 부서별 평균 급여가 45000 이상인 부서
SELECT 
    department, 
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2020-01-01'  -- 개별 행 필터링 (그룹화 전)
GROUP BY department
HAVING AVG(salary) >= 45000;     -- 그룹 필터링 (그룹화 후)
```

**실행 순서:**

1. FROM employees
1. WHERE hire_date >= ‘2020-01-01’ (행 필터링)
1. GROUP BY department (그룹화)
1. HAVING AVG(salary) >= 45000 (그룹 필터링)
1. SELECT (결과 출력)

-----

### 4. HAVING에서 다양한 조건 사용

```sql
-- 직원이 5명 이상이고, 최고 급여가 80000 이상인 부서
SELECT 
    department,
    COUNT(*) AS emp_count,
    MAX(salary) AS max_salary
FROM employees
GROUP BY department
HAVING COUNT(*) >= 5 AND MAX(salary) >= 80000;

-- 급여 표준편차가 큰 부서 (급여 편차가 심한 부서)
SELECT 
    department,
    STDDEV(salary) AS salary_stddev
FROM employees
GROUP BY department
HAVING STDDEV(salary) > 15000;

-- 급여 합계가 상위 3개 부서
SELECT 
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY SUM(salary) DESC
LIMIT 3;
```

-----

## 🎯 실전 예제

### 예제 1: 부서별 급여 분석

```sql
SELECT 
    department AS 부서,
    COUNT(*) AS 직원수,
    ROUND(AVG(salary), 0) AS 평균급여,
    MAX(salary) AS 최고급여,
    MIN(salary) AS 최저급여,
    MAX(salary) - MIN(salary) AS 급여편차,
    SUM(salary) AS 급여총액
FROM employees
GROUP BY department
HAVING COUNT(*) >= 5  -- 5명 이상인 부서만
ORDER BY 평균급여 DESC;
```

-----

### 예제 2: 입사년도별, 부서별 통계

```sql
SELECT 
    YEAR(hire_date) AS 입사년도,
    department AS 부서,
    COUNT(*) AS 입사자수,
    ROUND(AVG(salary), 0) AS 평균초봉
FROM employees
WHERE hire_date >= '2020-01-01'
GROUP BY YEAR(hire_date), department
HAVING COUNT(*) >= 3
ORDER BY 입사년도 DESC, 부서;
```

-----

### 예제 3: 성별, 직급별 급여 분석

```sql
SELECT 
    gender AS 성별,
    position AS 직급,
    COUNT(*) AS 인원,
    AVG(salary) AS 평균급여,
    MIN(salary) AS 최저급여,
    MAX(salary) AS 최고급여
FROM employees
GROUP BY gender, position
ORDER BY gender, position;
```

결과:

```
성별 | 직급   | 인원 | 평균급여 | 최저급여 | 최고급여
----|--------|------|---------|---------|--------
F   | Junior | 25   | 32000   | 28000   | 38000
F   | Senior | 20   | 58000   | 45000   | 75000
M   | Junior | 30   | 33000   | 28000   | 40000
M   | Senior | 25   | 62000   | 48000   | 95000
```

-----

### 예제 4: 조건부 집계 (CASE 활용)

```sql
-- 급여 구간별 직원 수
SELECT 
    department,
    COUNT(*) AS 총인원,
    SUM(CASE WHEN salary < 40000 THEN 1 ELSE 0 END) AS 저급여,
    SUM(CASE WHEN salary BETWEEN 40000 AND 60000 THEN 1 ELSE 0 END) AS 중급여,
    SUM(CASE WHEN salary > 60000 THEN 1 ELSE 0 END) AS 고급여,
    ROUND(AVG(CASE WHEN salary < 40000 THEN salary END), 0) AS 저급여평균
FROM employees
GROUP BY department;
```

-----

### 예제 5: 서브쿼리와 GROUP BY

```sql
-- 각 부서의 평균 급여보다 높은 급여를 받는 직원 수
SELECT 
    e.department,
    COUNT(*) AS 평균이상직원수
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE department = e.department
)
GROUP BY e.department;
```

-----

## 💡 고급 활용

### 1. ROLLUP - 소계와 총계

```sql
-- 부서별 소계 + 전체 총계
SELECT 
    department,
    COUNT(*) AS cnt,
    SUM(salary) AS total
FROM employees
GROUP BY department WITH ROLLUP;
```

결과:

```
department | cnt | total
-----------|-----|--------
IT         | 25  | 1375000
HR         | 15  | 675000
Sales      | 30  | 1350000
Marketing  | 20  | 900000
Finance    | 10  | 550000
NULL       | 100 | 4850000  ← 총계
```

-----

### 2. 윈도우 함수와 비교

```sql
-- GROUP BY: 그룹당 하나의 행
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
-- 결과: 5개 행 (부서 수만큼)

-- 윈도우 함수: 모든 행 유지
SELECT 
    name, 
    department, 
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;
-- 결과: 100개 행 (전체 직원 수만큼)
```

-----

### 3. HAVING에서 별칭(Alias) 사용 불가

```sql
-- ✘ 에러 발생
SELECT 
    department, 
    AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING avg_sal > 50000;  -- 별칭 사용 불가

-- ✔ 올바른 방법
SELECT 
    department, 
    AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;  -- 원본 식 사용
```

-----

## 📝 SQL 실행 순서 (중요!)

```sql
SELECT department, COUNT(*) AS cnt    -- 5. 결과 출력
FROM employees                        -- 1. 테이블 선택
WHERE salary >= 40000                 -- 2. 행 필터링
GROUP BY department                   -- 3. 그룹화
HAVING COUNT(*) >= 10                 -- 4. 그룹 필터링
ORDER BY cnt DESC                     -- 6. 정렬
LIMIT 3;                              -- 7. 행 수 제한
```

**실행 순서:**

1. FROM - 테이블 선택
1. WHERE - 개별 행 필터링
1. GROUP BY - 그룹화
1. HAVING - 그룹 필터링
1. SELECT - 컬럼 선택 및 집계
1. ORDER BY - 정렬
1. LIMIT - 행 수 제한

-----

## ⚠️ 자주 하는 실수

### 1. GROUP BY 없이 집계함수 사용

```sql
-- ✘ 에러 (MySQL 5.7 이상)
SELECT department, COUNT(*)
FROM employees;

-- ✔ 올바른 방법
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

### 2. WHERE에서 집계함수 사용

```sql
-- ✘ 에러
SELECT department
FROM employees
WHERE AVG(salary) > 50000
GROUP BY department;

-- ✔ HAVING 사용
SELECT department
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

### 3. SELECT의 모든 컬럼이 GROUP BY에 없음

```sql
-- ✘ 에러
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department;

-- ✔ 집계함수 사용 또는 GROUP BY에 추가
SELECT department, COUNT(name) AS name_count
FROM employees
GROUP BY department;
```

-----

## 🎓 실전 연습 문제

### 문제 1

부서별로 평균 급여가 가장 높은 상위 3개 부서를 조회하세요.

<details>
<summary>정답 보기</summary>

```sql
SELECT 
    department,
    ROUND(AVG(salary), 0) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 3;
```

</details>

### 문제 2

2020년 이후 입사자 중, 부서별 인원이 5명 이상인 부서의 평균 급여를 조회하세요.

<details>
<summary>정답 보기</summary>

```sql
SELECT 
    department,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2020-01-01'
GROUP BY department
HAVING COUNT(*) >= 5;
```

</details>

### 문제 3

직급별로 남성과 여성의 평균 급여 차이를 조회하세요.

<details>
<summary>정답 보기</summary>

```sql
SELECT 
    position,
    AVG(CASE WHEN gender = 'M' THEN salary END) AS male_avg,
    AVG(CASE WHEN gender = 'F' THEN salary END) AS female_avg,
    AVG(CASE WHEN gender = 'M' THEN salary END) - 
    AVG(CASE WHEN gender = 'F' THEN salary END) AS gap
FROM employees
GROUP BY position;
```

</details>

