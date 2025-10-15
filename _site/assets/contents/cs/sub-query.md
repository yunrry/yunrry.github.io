
## 서브쿼리

### 단일 행 서브쿼리

```sql
-- 평균 급여보다 많이 받는 직원
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 다중 행 서브쿼리

```sql
-- IT 부서 직원들과 같은 급여를 받는 다른 부서 직원
SELECT name, department
FROM employees
WHERE salary IN (
    SELECT salary FROM employees WHERE department = 'IT'
)
AND department != 'IT';
```

### 인라인 뷰 (FROM 절 서브쿼리)

```sql
SELECT dept, avg_sal
FROM (
    SELECT department AS dept, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department
) AS dept_avg
WHERE avg_sal > 50000;
```

### 스칼라 서브쿼리 (SELECT 절)

```sql
SELECT 
    name,
    salary,
    (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees;
```

### 상관 서브쿼리

```sql
-- 자기 부서 평균보다 급여가 높은 직원
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```
