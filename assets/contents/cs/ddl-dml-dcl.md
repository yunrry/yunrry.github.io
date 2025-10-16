
# DDL/DML/DCL

### DDL (Data Definition Language)

데이터 정의어 - 테이블 구조 관리

```sql
-- CREATE: 생성
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2),
    hire_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- ALTER: 수정
ALTER TABLE employees ADD phone VARCHAR(20);
ALTER TABLE employees MODIFY salary DECIMAL(12, 2);
ALTER TABLE employees DROP COLUMN phone;
ALTER TABLE employees RENAME TO staff;

-- DROP: 삭제 (구조와 데이터 모두 삭제)
DROP TABLE employees;

-- TRUNCATE: 데이터만 삭제 (구조 유지, 빠름)
TRUNCATE TABLE employees;
```

### DML (Data Manipulation Language)

데이터 조작어 - 데이터 관리

```sql
-- INSERT: 삽입
INSERT INTO employees (name, email, salary) 
VALUES ('홍길동', 'hong@example.com', 50000);

-- 여러 행 삽입
INSERT INTO employees (name, salary) 
VALUES ('김철수', 45000), ('이영희', 55000);

-- UPDATE: 수정
UPDATE employees 
SET salary = salary * 1.1 
WHERE department = 'IT';

-- DELETE: 삭제
DELETE FROM employees WHERE id = 10;
```

### DCL (Data Control Language)

데이터 제어어 - 권한 관리

```sql
-- GRANT: 권한 부여
GRANT SELECT, INSERT ON employees TO 'user1'@'localhost';
GRANT ALL PRIVILEGES ON company.* TO 'admin'@'localhost';

-- REVOKE: 권한 회수
REVOKE INSERT ON employees FROM 'user1'@'localhost';

-- COMMIT: 트랜잭션 확정
COMMIT;

-- ROLLBACK: 트랜잭션 취소
ROLLBACK;
```
