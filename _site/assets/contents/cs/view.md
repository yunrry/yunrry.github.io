## 뷰(View)

### 뷰란?

가상 테이블, SELECT 쿼리를 저장한 객체

```sql
-- 뷰 생성
CREATE VIEW high_salary_employees AS
SELECT name, department, salary
FROM employees
WHERE salary >= 70000;

-- 뷰 사용
SELECT * FROM high_salary_employees;

-- 뷰 수정
CREATE OR REPLACE VIEW high_salary_employees AS
SELECT name, department, salary, hire_date
FROM employees
WHERE salary >= 70000;

-- 뷰 삭제
DROP VIEW high_salary_employees;
```

### 뷰의 장점

- 복잡한 쿼리 단순화
- 보안성 향상 (특정 컬럼만 노출)
- 논리적 독립성 제공

### 뷰의 단점

- 성능 저하 가능 (매번 쿼리 실행)
- 인덱스 사용 불가
- INSERT/UPDATE 제한적