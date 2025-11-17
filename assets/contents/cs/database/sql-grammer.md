
# SQL 기본 문법

## SQL-DOMAIN

> 도메인이란 하나의 속성이 취할 수 있는 동일한 유형의 원자값들의 집합이다.  

### DDL로 DOMAIN 다루기
DDL(Data Define Language) {CREATE, ALTER, DROP}   

### CREATE DOMAIN
**1. 성별도메인**
```sql
CREATE DOMAIN SEX CHAR(1)
    DEFAULT '남'  
    CONSTRAINT VALID-SEX CHECK(VALUE('남', '여'));  
```

**2. 이메일 도메인**
```sql
CREATE DOMAIN EMAIL VARCHAR(100)  
    CONSTRAINT VALID-EMAIL CHECK(VALUE LIKE '%@%.%);
```
**3. 나이 도메인**
```sql
CREATE DOMAIN AGE INTEGER
    DEFAULT 0
    CONATRAINT VALID_AGE CHECK(VALUE >= 0 AND VALUE <= 150);
```
**4. 전화번호 도메인**
```sql
CREATE DOMAIN PHONE_NUMBER CHAR(13)  
    CONSTRAINT VALID_PHONE CHECK(VALUE LIKE '___-____-____');
 
```

**5. 급여 도메인**
```sql
CREATE DOMAIN SALARY DECIMAL(10, 2)
    DEFAULT 0.00
    CONSTRAINT VALID_SALARY CHECK(VALUE >= 0)
```

**6. 학점 도메인**
```sql
CREATE DOMAIN GRADE CAHR(1)
    CONSTRAINT VALID_GRADE CHECK (VALUE IN ('A', 'B', 'C', 'D', 'F'))
```

**7. 우편번호 도메인**
```sql
CREATE DOMAIN POSTAL_CODE CHAR(5)
    CONSTRAINT VALID_POSTAL CHECK(VALUE SIMILAR TO '[0-9]{5});
```

**8. URL 도메인**
```sql
CREATE DOMIAN URL VARCHAR(255)
    CONSTRAINT VALID_URL CHECK(VALUE LIKE 'http://%' OR VALUE LIKE 'https://%');
```

**9. 백분율 도메인**
```sql
CREATE DOMAIN PERCENTAGE NUMERIC(5, 2)
    DEFAULT 0.00
    CONSTRAINT VALID_PERCENTAGE CHECK(VALUE >= 0.00 AND VALUE <== 100.00>);
```

**10. 상태 코드 도메인**
```sql
CREATE DOMAIN STATUS_CODE CHAR(2)
    DEFAULT 'AC'
    CONSTRAINT VALID_STATUS CHECK(VALUE IN ('AC', 'IN', 'PE', 'CL'));
```

### ALTER DOMAIN
```sql
ALTER DOMAIN SALARY
    ADD CONSTRAINT MIN_SALARY CHECK(VALUE>=1000000);
```

### DROP DOMAIN
```sql
DROP DOMAIN SEX CASCADE;
```
CASCADE : 해당 도메인을 사용하는 모든 컬럼도 함께 처리

### DOMAIN 사용 예시
```sql
CREATE TABLE EMPLOYEE (
    EMP_ID INTEGER PRIMARY KEY,
    EMP_NAME VARCHAR(50) NOT NULL,
    EMP_SEX SEX,
    EMP_AGE AGE,
    EMP_EMAIL EMAIL,
    EMP_PHONE PHONE_NUMBER,
    EMP_SALARY SALARY
);
```

참고: MySQL은 DOMAIN을 지원하지 않으므로, CHECK 제약조건을 테이블 레벨에서 직접 사용해야 한다.



### NUMERIC vs DECIMAL  
표준 SQL에서는 NUMERIC과 DECIMAL이 동일하다:  
```sql
NUMERIC(10, 2) = DECIMAL(10, 2)
```
권장사항
1. 개인/팀 선호도에 따라 선택
2. 일관성 유지가 중요 (프로젝트 내에서 하나만 사용)
3. 일반적으로 DECIMAL이 더 널리 사용됨


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





## AS (별칭, Alias)

### 🎯 핵심 목적: **가독성 향상**

-----

### 1. 컬럼명을 알아보기 쉽게

```sql
-- AS 없이
SELECT COUNT(*) FROM employees;
-- 결과 컬럼명: COUNT(*)  ← 이게 뭔지 한눈에 안 들어옴

-- AS 사용
SELECT COUNT(*) AS 총직원수 FROM employees;
-- 결과 컬럼명: 총직원수  ← 명확함!
```

-----

### 2. 복잡한 계산식 이름 붙이기

```sql
-- AS 없이
SELECT salary * 12 FROM employees;
-- 결과 컬럼명: salary * 12  ← 무슨 의미인지 불명확

-- AS 사용
SELECT salary * 12 AS 연봉 FROM employees;
-- 결과 컬럼명: 연봉  ← 의미 명확!
```

-----

### 3. 테이블명 줄이기 (JOIN에서 필수)

```sql
-- AS 없이 (너무 길어서 불편)
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments 
ON employees.dept_id = departments.dept_id;

-- AS 사용 (간결함)
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.dept_id = d.dept_id;
```

-----

### 4. 같은 테이블 구분하기 (SELF JOIN)

```sql
-- 직원과 상사를 구분하기 위해 별칭 필수
SELECT 
    e1.name AS 직원,
    e2.name AS 상사
FROM employees e1
LEFT JOIN employees e2 
ON e1.manager_id = e2.id;
```

-----

### 💡 정리

|AS 사용 위치 |목적       |생략 가능?      |
|---------|---------|------------|
|SELECT 컬럼|결과 컬럼명 변경|⭕ (AS 생략 가능)|
|FROM 테이블 |테이블명 줄이기 |⭕ (AS 생략 가능)|
|SELF JOIN|같은 테이블 구분|❌ (필수)      |

**AS는 생략 가능하지만, 명확성을 위해 쓰는 게 좋음**

```sql
-- 둘 다 동일하게 동작
SELECT COUNT(*) AS cnt FROM employees;
SELECT COUNT(*) cnt FROM employees;  -- AS 생략

-- 하지만 AS를 쓰는 게 더 명확함
```
