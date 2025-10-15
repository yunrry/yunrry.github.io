
## GROUP BY & 집계함수

### 기본 집계함수

```sql
SELECT 
    COUNT(*) AS 총개수,
    COUNT(DISTINCT department) AS 부서수,
    SUM(salary) AS 급여합계,
    AVG(salary) AS 평균급여,
    MAX(salary) AS 최고급여,
    MIN(salary) AS 최저급여
FROM employees;
```

### GROUP BY

```sql
-- 부서별 평균 급여
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- 부서별, 직급별 그룹화
SELECT department, position, COUNT(*) AS cnt
FROM employees
GROUP BY department, position;
```

### HAVING (그룹 조건)

```sql
-- 평균 급여가 50000 이상인 부서만
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) >= 50000;
```

**WHERE vs HAVING 차이**

- WHERE: 그룹화 **전** 행 필터링
- HAVING: 그룹화 **후** 그룹 필터링
