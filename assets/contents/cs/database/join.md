
# JOIN 연산

### INNER JOIN (내부 조인)

양쪽 테이블에 모두 존재하는 데이터만 조회

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;
```

### LEFT OUTER JOIN

왼쪽 테이블의 모든 데이터 + 오른쪽 테이블의 매칭 데이터

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

### RIGHT OUTER JOIN

오른쪽 테이블의 모든 데이터 + 왼쪽 테이블의 매칭 데이터

```sql
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

### FULL OUTER JOIN

양쪽 테이블의 모든 데이터 (MySQL은 UNION 사용)

```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;
```

### SELF JOIN

같은 테이블을 자기 자신과 조인

```sql
-- 직원과 그의 상사 조회
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```
