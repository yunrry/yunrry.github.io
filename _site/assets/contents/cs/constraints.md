## 제약조건

### PRIMARY KEY (기본키)

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50)
);

-- 복합 키
CREATE TABLE enrollment (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)
);
```

### FOREIGN KEY (외래키)

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

**ON DELETE/UPDATE 옵션**

- CASCADE: 참조되는 행 삭제/수정 시 함께 삭제/수정
- SET NULL: 참조되는 행 삭제 시 NULL로 설정
- NO ACTION: 참조되는 행 삭제/수정 불가
- RESTRICT: NO ACTION과 동일

### UNIQUE (중복 방지)

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) UNIQUE
);
```

### NOT NULL (NULL 방지)

```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

### CHECK (조건 검증)

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    age INT CHECK (age >= 18),
    salary DECIMAL(10, 2) CHECK (salary > 0)
);
```

### DEFAULT (기본값)

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
