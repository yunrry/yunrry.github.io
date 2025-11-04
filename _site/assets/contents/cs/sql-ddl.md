
# DDL/DML/DCL

# DDL 
>Data Define Language
데이터 정의어 - 테이블 구조 관리


## DOMAIN

> 도메인이란 하나의 속성이 취할 수 있는 동일한 유형의 원자값들의 집합이다.  

### DDL로 DOMAIN 다루기
DDL {CREATE, ALTER, DROP}   

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




## TABLE

### CREATE TABLE

### 기본 구문
```sql
CREATE TABLE 테이블명 (
    컬럼명1 데이터타입 [제약조건],
    컬럼명2 데이터타입 [제약조건],
    ...
    [테이블_제약조건]
);
```

### 주요 제약조건
```sql
CREATE TABLE EMPLOYEE (
    -- PRIMARY KEY: 기본키 (NOT NULL + UNIQUE)
    EMP_ID INTEGER PRIMARY KEY,
    
    -- NOT NULL: 필수 입력
    EMP_NAME VARCHAR(50) NOT NULL,
    
    -- UNIQUE: 중복 불가
    EMAIL VARCHAR(100) UNIQUE,
    
    -- DEFAULT: 기본값
    HIRE_DATE DATE DEFAULT CURRENT_DATE,
    
    -- CHECK: 조건 검사
    SALARY NUMERIC(10, 2) CHECK(SALARY >= 0),
    AGE INTEGER CHECK(AGE >= 18 AND AGE <= 65),
    
    -- FOREIGN KEY: 외래키
    DEPT_ID INTEGER,
    CONSTRAINT FK_DEPT 
        FOREIGN KEY (DEPT_ID) 
        REFERENCES DEPARTMENT(DEPT_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### 복합 키
```sql
CREATE TABLE ENROLLMENT (
    STUDENT_ID INTEGER,
    COURSE_ID INTEGER,
    GRADE CHAR(1),
    -- 복합 기본키
    PRIMARY KEY (STUDENT_ID, COURSE_ID),
    -- 복합 외래키
    FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(STUDENT_ID),
    FOREIGN KEY (COURSE_ID) REFERENCES COURSE(COURSE_ID)
);
```

### 다른 테이블로부터 생성
```sql
-- 구조 + 데이터 복사
CREATE TABLE EMP_BACKUP AS
SELECT * FROM EMPLOYEE;

-- 구조만 복사
CREATE TABLE EMP_TEMPLATE AS
SELECT * FROM EMPLOYEE WHERE 1=0;
```

---

### ALTER TABLE

### 컬럼 추가
```sql
-- 기본
ALTER TABLE EMPLOYEE 
ADD COLUMN PHONE VARCHAR(20);

-- 제약조건 포함
ALTER TABLE EMPLOYEE 
ADD COLUMN BIRTH_DATE DATE NOT NULL DEFAULT '1990-01-01';
```

### 컬럼 삭제
```sql
-- 기본
ALTER TABLE EMPLOYEE 
DROP COLUMN PHONE;

-- CASCADE: 해당 컬럼 참조하는 제약조건도 함께 삭제
ALTER TABLE EMPLOYEE 
DROP COLUMN DEPT_ID CASCADE;

-- RESTRICT: 참조하는 객체 있으면 삭제 불가 (기본값)
ALTER TABLE EMPLOYEE 
DROP COLUMN DEPT_ID RESTRICT;
```

### 컬럼 수정
```sql
-- 데이터 타입 변경
ALTER TABLE EMPLOYEE 
ALTER COLUMN SALARY TYPE NUMERIC(15, 2);

-- 기본값 설정
ALTER TABLE EMPLOYEE 
ALTER COLUMN HIRE_DATE SET DEFAULT CURRENT_DATE;

-- 기본값 제거
ALTER TABLE EMPLOYEE 
ALTER COLUMN HIRE_DATE DROP DEFAULT;

-- NOT NULL 추가
ALTER TABLE EMPLOYEE 
ALTER COLUMN EMAIL SET NOT NULL;

-- NOT NULL 제거
ALTER TABLE EMPLOYEE 
ALTER COLUMN EMAIL DROP NOT NULL;
```

### 컬럼명 변경
```sql
ALTER TABLE EMPLOYEE 
RENAME COLUMN OLD_NAME TO NEW_NAME;
```

### 제약조건 추가
```sql
-- PRIMARY KEY 추가
ALTER TABLE EMPLOYEE 
ADD PRIMARY KEY (EMP_ID);

-- FOREIGN KEY 추가
ALTER TABLE EMPLOYEE 
ADD CONSTRAINT FK_DEPT 
    FOREIGN KEY (DEPT_ID) 
    REFERENCES DEPARTMENT(DEPT_ID)
    ON DELETE CASCADE;

-- UNIQUE 추가
ALTER TABLE EMPLOYEE 
ADD CONSTRAINT UK_EMAIL UNIQUE (EMAIL);

-- CHECK 추가
ALTER TABLE EMPLOYEE 
ADD CONSTRAINT CHK_SALARY CHECK(SALARY >= 0);
```

### 제약조건 삭제
```sql
-- 이름으로 삭제
ALTER TABLE EMPLOYEE 
DROP CONSTRAINT FK_DEPT;

-- PRIMARY KEY 삭제
ALTER TABLE EMPLOYEE 
DROP PRIMARY KEY;

-- CASCADE로 연관 제약조건도 함께 삭제
ALTER TABLE EMPLOYEE 
DROP CONSTRAINT FK_DEPT CASCADE;
```

### 테이블명 변경
```sql
ALTER TABLE OLD_TABLE_NAME 
RENAME TO NEW_TABLE_NAME;
```

---

### DROP TABLE

### 기본 삭제
```sql
-- 기본 (RESTRICT 동작)
DROP TABLE EMPLOYEE;

-- 명시적 RESTRICT: 참조하는 객체 있으면 삭제 불가
DROP TABLE EMPLOYEE RESTRICT;
```

### CASCADE 삭제
```sql
-- 참조하는 모든 외래키, 뷰 등도 함께 삭제
DROP TABLE DEPARTMENT CASCADE;
```

### 안전한 삭제
```sql
-- 테이블 존재 시에만 삭제 (오류 방지)
DROP TABLE IF EXISTS EMPLOYEE;

DROP TABLE IF EXISTS EMPLOYEE CASCADE;
```

---

## 4. 주요 차이점 비교

| 명령어 | 용도 | 데이터 | 롤백 가능 | 속도 |
|--------|------|--------|-----------|------|
| **CREATE TABLE** | 테이블 생성 | - | 가능 (DDL) | - |
| **ALTER TABLE** | 테이블 구조 변경 | 유지 | 가능 (DDL) | 빠름 |
| **DROP TABLE** | 테이블 삭제 | 삭제 | 가능 (DDL) | 빠름 |
| **TRUNCATE TABLE** | 데이터만 삭제 | 삭제 | 불가능 | 매우 빠름 |
| **DELETE** | 데이터 삭제 | 선택 삭제 | 가능 (DML) | 느림 |

---

## 5. 실무 예시

### 초기 테이블 생성
```sql
CREATE TABLE CUSTOMER (
    CUSTOMER_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE,
    PHONE VARCHAR(20),
    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 나중에 컬럼 추가
```sql
-- 주소 컬럼 추가
ALTER TABLE CUSTOMER 
ADD COLUMN ADDRESS VARCHAR(200);

-- 포인트 컬럼 추가 (기본값 0)
ALTER TABLE CUSTOMER 
ADD COLUMN POINTS INTEGER DEFAULT 0 CHECK(POINTS >= 0);
```

### 외래키 추가
```sql
-- 주문 테이블 생성
CREATE TABLE ORDERS (
    ORDER_ID INTEGER PRIMARY KEY,
    ORDER_DATE DATE NOT NULL,
    CUSTOMER_ID INTEGER
);

-- 외래키 제약조건 추가
ALTER TABLE ORDERS 
ADD CONSTRAINT FK_CUSTOMER 
    FOREIGN KEY (CUSTOMER_ID) 
    REFERENCES CUSTOMER(CUSTOMER_ID)
    ON DELETE CASCADE;
```

### 테이블 삭제 (안전하게)
```sql
-- 1. 참조 확인
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
WHERE TABLE_NAME = 'CUSTOMER';

-- 2. 외래키 먼저 삭제
ALTER TABLE ORDERS DROP CONSTRAINT FK_CUSTOMER;

-- 3. 테이블 삭제
DROP TABLE CUSTOMER;

-- 또는 한 번에 CASCADE
DROP TABLE CUSTOMER CASCADE;
```

---

## 6. 주의사항

### CREATE TABLE
- ✔ 테이블명, 컬럼명은 명확하게
- ✔ 적절한 데이터 타입 선택
- ✔ NOT NULL, PRIMARY KEY 등 제약조건 명시
- !! 너무 많은 컬럼은 정규화 검토

### ALTER TABLE
- ✔ 운영 중인 테이블 수정 시 주의
- ✔ NOT NULL 추가 전 기존 데이터 확인
- !! 데이터 타입 변경 시 데이터 손실 가능
- !! 대용량 테이블은 시간 오래 걸림

### DROP TABLE
- !! **데이터 영구 삭제 - 복구 불가**
- ✔ 운영 환경에서는 백업 필수
- ✔ CASCADE 사용 시 영향 범위 확인
- ✔ IF EXISTS로 오류 방지

---

## 7. 빠른 참조

```sql
-- 생성
CREATE TABLE 테이블명 (컬럼 정의...);

-- 수정
ALTER TABLE 테이블명 ADD COLUMN 컬럼명 타입;
ALTER TABLE 테이블명 DROP COLUMN 컬럼명;
ALTER TABLE 테이블명 ALTER COLUMN 컬럼명 TYPE 새타입;
ALTER TABLE 테이블명 ADD CONSTRAINT 제약조건명 제약조건;
ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건명;

-- 삭제
DROP TABLE 테이블명;
DROP TABLE 테이블명 CASCADE;
DROP TABLE IF EXISTS 테이블명;
```


# SQL 스키마/뷰/인덱스 핵심 정리

## 1. CREATE SCHEMA (스키마 생성)

### 기본 개념
- **스키마**: 데이터베이스 객체들(테이블, 뷰, 인덱스 등)의 논리적 그룹
- **네임스페이스** 역할 (이름 충돌 방지)
- **권한 관리** 용이

### 기본 구문
```sql
-- 단순 생성
CREATE SCHEMA 스키마명;

-- 소유자 지정
CREATE SCHEMA 스키마명 AUTHORIZATION 사용자명;

-- 스키마와 객체 동시 생성
CREATE SCHEMA 스키마명
    CREATE TABLE EMPLOYEE (
        EMP_ID INTEGER PRIMARY KEY,
        EMP_NAME VARCHAR(50)
    )
    CREATE VIEW EMP_VIEW AS
        SELECT EMP_ID, EMP_NAME FROM EMPLOYEE;
```

### 실무 예시
```sql
-- 회사 부서별 스키마
CREATE SCHEMA HR AUTHORIZATION hr_manager;
CREATE SCHEMA SALES AUTHORIZATION sales_manager;
CREATE SCHEMA FINANCE AUTHORIZATION finance_manager;

-- 개발 환경별 스키마
CREATE SCHEMA DEV;
CREATE SCHEMA TEST;
CREATE SCHEMA PROD;
```

### 스키마 사용
```sql
-- 테이블 생성 시 스키마 지정
CREATE TABLE HR.EMPLOYEE (
    EMP_ID INTEGER PRIMARY KEY,
    EMP_NAME VARCHAR(50)
);

-- 테이블 조회 시 스키마 지정
SELECT * FROM HR.EMPLOYEE;
SELECT * FROM SALES.CUSTOMER;

-- 기본 스키마 설정
SET SCHEMA HR;
SELECT * FROM EMPLOYEE;  -- HR.EMPLOYEE를 의미
```

### 스키마 삭제
```sql
-- 빈 스키마만 삭제
DROP SCHEMA HR RESTRICT;

-- 스키마 내 모든 객체 함께 삭제
DROP SCHEMA HR CASCADE;
```

---

## 2. CREATE VIEW (뷰 생성)

### 기본 개념
- **뷰**: 가상 테이블 (SELECT 쿼리 결과를 테이블처럼 사용)
- **데이터 저장 안 함** (쿼리만 저장)
- 보안, 복잡한 쿼리 단순화에 유용

### 기본 구문
```sql
CREATE VIEW 뷰명 AS
SELECT 컬럼1, 컬럼2, ...
FROM 테이블명
WHERE 조건;
```

### 단순 뷰
```sql
-- 특정 컬럼만 보이는 뷰
CREATE VIEW EMP_BASIC AS
SELECT EMP_ID, EMP_NAME, DEPT_ID
FROM EMPLOYEE;

-- 특정 조건의 데이터만 보이는 뷰
CREATE VIEW HIGH_SALARY_EMP AS
SELECT EMP_ID, EMP_NAME, SALARY
FROM EMPLOYEE
WHERE SALARY >= 5000000;

-- 특정 부서 직원만 보이는 뷰
CREATE VIEW IT_DEPARTMENT AS
SELECT *
FROM EMPLOYEE
WHERE DEPT_ID = 10;
```

### 복잡한 뷰
```sql
-- 조인 뷰
CREATE VIEW EMP_DEPT_VIEW AS
SELECT E.EMP_ID, E.EMP_NAME, D.DEPT_NAME
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.DEPT_ID = D.DEPT_ID;

-- 집계 함수 뷰
CREATE VIEW DEPT_SALARY_STAT AS
SELECT 
    DEPT_ID,
    COUNT(*) AS EMP_COUNT,
    AVG(SALARY) AS AVG_SALARY,
    MAX(SALARY) AS MAX_SALARY,
    MIN(SALARY) AS MIN_SALARY
FROM EMPLOYEE
GROUP BY DEPT_ID;

-- 서브쿼리 뷰
CREATE VIEW TOP_EARNERS AS
SELECT EMP_ID, EMP_NAME, SALARY
FROM EMPLOYEE
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE);
```

### 뷰 컬럼명 지정
```sql
-- 컬럼명 변경
CREATE VIEW EMP_INFO (ID, NAME, SAL) AS
SELECT EMP_ID, EMP_NAME, SALARY
FROM EMPLOYEE;

-- 계산된 컬럼
CREATE VIEW EMP_ANNUAL_SALARY AS
SELECT 
    EMP_ID,
    EMP_NAME,
    SALARY,
    SALARY * 12 AS ANNUAL_SALARY
FROM EMPLOYEE;
```

### WITH CHECK OPTION
```sql
-- 뷰를 통한 INSERT/UPDATE 시 WHERE 조건 강제
CREATE VIEW HIGH_SALARY_EMP AS
SELECT EMP_ID, EMP_NAME, SALARY
FROM EMPLOYEE
WHERE SALARY >= 5000000
WITH CHECK OPTION;

-- 이 경우 SALARY < 5000000인 데이터 입력/수정 불가
-- INSERT INTO HIGH_SALARY_EMP VALUES (1, 'Kim', 3000000);  -- 오류!
```

### 뷰 사용
```sql
-- 일반 테이블처럼 조회
SELECT * FROM EMP_DEPT_VIEW;

SELECT * FROM DEPT_SALARY_STAT
WHERE EMP_COUNT > 10;

-- 뷰를 이용한 다른 뷰 생성
CREATE VIEW SENIOR_EMP AS
SELECT * FROM EMP_BASIC
WHERE EMP_ID < 1000;
```

### 뷰 수정/삭제
```sql
-- 뷰 수정 (기존 뷰 대체)
CREATE OR REPLACE VIEW EMP_BASIC AS
SELECT EMP_ID, EMP_NAME, DEPT_ID, HIRE_DATE
FROM EMPLOYEE;

-- 뷰 삭제
DROP VIEW EMP_BASIC;

-- CASCADE: 해당 뷰를 참조하는 뷰도 함께 삭제
DROP VIEW EMP_BASIC CASCADE;
```

### 뷰의 장단점

#### 장점 ✅
```sql
-- 1. 보안: 민감한 컬럼 숨김
CREATE VIEW PUBLIC_EMP AS
SELECT EMP_ID, EMP_NAME, DEPT_ID
FROM EMPLOYEE;  -- SALARY, SSN 등 제외

-- 2. 복잡한 쿼리 단순화
CREATE VIEW MONTHLY_SALES_REPORT AS
SELECT 
    P.PRODUCT_NAME,
    EXTRACT(YEAR FROM O.ORDER_DATE) AS YEAR,
    EXTRACT(MONTH FROM O.ORDER_DATE) AS MONTH,
    SUM(OI.QUANTITY * OI.PRICE) AS TOTAL_SALES
FROM ORDERS O
JOIN ORDER_ITEMS OI ON O.ORDER_ID = OI.ORDER_ID
JOIN PRODUCTS P ON OI.PRODUCT_ID = P.PRODUCT_ID
GROUP BY P.PRODUCT_NAME, YEAR, MONTH;

-- 사용: 간단하게 조회
SELECT * FROM MONTHLY_SALES_REPORT WHERE YEAR = 2024;

-- 3. 데이터 독립성
-- 테이블 구조 변경 시 뷰만 수정하면 응용 프로그램 영향 최소화
```

#### 단점 ⚠️
- 복잡한 뷰는 성능 저하
- 일부 뷰는 UPDATE/INSERT 불가
- 인덱스 생성 불가

---

## 3. CREATE INDEX (인덱스 생성)

### 기본 개념
- **인덱스**: 테이블 데이터의 빠른 검색을 위한 구조
- **책의 색인**과 유사
- SELECT 성능 향상, INSERT/UPDATE/DELETE 성능 저하

### 기본 구문
```sql
CREATE INDEX 인덱스명
ON 테이블명 (컬럼명);
```

### 단일 컬럼 인덱스
```sql
-- 자주 검색되는 컬럼
CREATE INDEX IDX_EMP_NAME
ON EMPLOYEE (EMP_NAME);

-- 외래키 컬럼
CREATE INDEX IDX_EMP_DEPT
ON EMPLOYEE (DEPT_ID);

-- 날짜 컬럼
CREATE INDEX IDX_ORDER_DATE
ON ORDERS (ORDER_DATE);
```

### 복합 인덱스 (다중 컬럼)
```sql
-- 두 컬럼을 함께 검색하는 경우
CREATE INDEX IDX_EMP_DEPT_NAME
ON EMPLOYEE (DEPT_ID, EMP_NAME);

-- 세 컬럼 복합 인덱스
CREATE INDEX IDX_ORDER_SEARCH
ON ORDERS (CUSTOMER_ID, ORDER_DATE, STATUS);
```

### UNIQUE 인덱스
```sql
-- 중복 값 허용 안 함
CREATE UNIQUE INDEX IDX_EMP_EMAIL
ON EMPLOYEE (EMAIL);

-- 복합 유니크 인덱스
CREATE UNIQUE INDEX IDX_ENROLLMENT
ON ENROLLMENT (STUDENT_ID, COURSE_ID);
```

### 정렬 방향 지정
```sql
-- 오름차순 (기본값)
CREATE INDEX IDX_SALARY_ASC
ON EMPLOYEE (SALARY ASC);

-- 내림차순
CREATE INDEX IDX_SALARY_DESC
ON EMPLOYEE (SALARY DESC);

-- 복합 인덱스에서 각각 다른 정렬
CREATE INDEX IDX_DEPT_SALARY
ON EMPLOYEE (DEPT_ID ASC, SALARY DESC);
```

### 부분 인덱스 (조건부)
```sql
-- 특정 조건의 데이터만 인덱싱
CREATE INDEX IDX_ACTIVE_EMP
ON EMPLOYEE (EMP_NAME)
WHERE STATUS = 'ACTIVE';

-- 최근 데이터만 인덱싱
CREATE INDEX IDX_RECENT_ORDERS
ON ORDERS (ORDER_DATE)
WHERE ORDER_DATE >= '2024-01-01';
```

### 함수 기반 인덱스
```sql
-- 대소문자 구분 없이 검색
CREATE INDEX IDX_UPPER_NAME
ON EMPLOYEE (UPPER(EMP_NAME));

-- 날짜의 연도만 인덱싱
CREATE INDEX IDX_ORDER_YEAR
ON ORDERS (EXTRACT(YEAR FROM ORDER_DATE));
```

### 인덱스 삭제
```sql
DROP INDEX IDX_EMP_NAME;

-- CASCADE: 관련 제약조건도 함께 삭제
DROP INDEX IDX_EMP_EMAIL CASCADE;
```

### 인덱스 사용 예시

#### Before (인덱스 없음)
```sql
-- 전체 테이블 스캔 (느림)
SELECT * FROM EMPLOYEE WHERE EMP_NAME = 'Kim';
-- 1,000,000 rows 중 1개 찾기 위해 전체 스캔
```

#### After (인덱스 있음)
```sql
CREATE INDEX IDX_EMP_NAME ON EMPLOYEE (EMP_NAME);

-- 인덱스를 통한 빠른 검색
SELECT * FROM EMPLOYEE WHERE EMP_NAME = 'Kim';
-- 인덱스를 통해 직접 접근 (매우 빠름)
```

### 인덱스 설계 가이드

#### 인덱스 생성이 유리한 경우 ✅
```sql
-- 1. WHERE 절에 자주 사용되는 컬럼
CREATE INDEX IDX_STATUS ON ORDERS (STATUS);
SELECT * FROM ORDERS WHERE STATUS = 'PENDING';

-- 2. JOIN에 자주 사용되는 컬럼
CREATE INDEX IDX_CUSTOMER_ID ON ORDERS (CUSTOMER_ID);
SELECT * FROM ORDERS O
JOIN CUSTOMER C ON O.CUSTOMER_ID = C.CUSTOMER_ID;

-- 3. ORDER BY에 자주 사용되는 컬럼
CREATE INDEX IDX_ORDER_DATE ON ORDERS (ORDER_DATE);
SELECT * FROM ORDERS ORDER BY ORDER_DATE DESC;

-- 4. 범위 검색이 많은 컬럼
CREATE INDEX IDX_SALARY ON EMPLOYEE (SALARY);
SELECT * FROM EMPLOYEE WHERE SALARY BETWEEN 3000000 AND 5000000;

-- 5. 카디널리티(고유값 비율)가 높은 컬럼
CREATE INDEX IDX_EMAIL ON EMPLOYEE (EMAIL);  -- 대부분 고유값
```

#### 인덱스 생성을 피해야 하는 경우 ⚠️
```sql
-- 1. 카디널리티가 낮은 컬럼 (성별, 불린 등)
-- CREATE INDEX IDX_GENDER ON EMPLOYEE (GENDER);  -- 비추천

-- 2. 자주 변경되는 컬럼
-- CREATE INDEX IDX_LAST_LOGIN ON USER (LAST_LOGIN_TIME);  -- 비추천

-- 3. 작은 테이블 (수백 행 이하)
-- 전체 스캔이 더 빠를 수 있음

-- 4. INSERT/UPDATE/DELETE가 많은 테이블
-- 인덱스 유지 비용이 큼
```

---

## 4. 종합 실무 예시

### 프로젝트 초기 설정
```sql
-- 1. 스키마 생성
CREATE SCHEMA ECOMMERCE AUTHORIZATION admin;

-- 2. 스키마 내 테이블 생성
CREATE TABLE ECOMMERCE.CUSTOMER (
    CUSTOMER_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE,
    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ECOMMERCE.ORDERS (
    ORDER_ID INTEGER PRIMARY KEY,
    CUSTOMER_ID INTEGER,
    ORDER_DATE DATE NOT NULL,
    STATUS VARCHAR(20) DEFAULT 'PENDING',
    TOTAL_AMOUNT NUMERIC(12, 2),
    CONSTRAINT FK_CUSTOMER 
        FOREIGN KEY (CUSTOMER_ID) 
        REFERENCES ECOMMERCE.CUSTOMER(CUSTOMER_ID)
);

-- 3. 인덱스 생성
CREATE INDEX IDX_CUSTOMER_EMAIL 
ON ECOMMERCE.CUSTOMER (EMAIL);

CREATE INDEX IDX_ORDER_CUSTOMER 
ON ECOMMERCE.ORDERS (CUSTOMER_ID);

CREATE INDEX IDX_ORDER_DATE 
ON ECOMMERCE.ORDERS (ORDER_DATE);

CREATE INDEX IDX_ORDER_STATUS 
ON ECOMMERCE.ORDERS (STATUS);

-- 4. 뷰 생성
CREATE VIEW ECOMMERCE.CUSTOMER_ORDER_SUMMARY AS
SELECT 
    C.CUSTOMER_ID,
    C.NAME,
    C.EMAIL,
    COUNT(O.ORDER_ID) AS TOTAL_ORDERS,
    SUM(O.TOTAL_AMOUNT) AS TOTAL_SPENT,
    MAX(O.ORDER_DATE) AS LAST_ORDER_DATE
FROM ECOMMERCE.CUSTOMER C
LEFT JOIN ECOMMERCE.ORDERS O ON C.CUSTOMER_ID = O.CUSTOMER_ID
GROUP BY C.CUSTOMER_ID, C.NAME, C.EMAIL;

-- 5. 보안 뷰 (민감 정보 제외)
CREATE VIEW ECOMMERCE.PUBLIC_CUSTOMER AS
SELECT CUSTOMER_ID, NAME
FROM ECOMMERCE.CUSTOMER;
```

### 사용
```sql
-- 기본 스키마 설정
SET SCHEMA ECOMMERCE;

-- 뷰 조회
SELECT * FROM CUSTOMER_ORDER_SUMMARY
WHERE TOTAL_ORDERS > 10;

-- 인덱스를 활용한 빠른 검색
SELECT * FROM ORDERS 
WHERE STATUS = 'PENDING'
AND ORDER_DATE >= '2024-01-01';
```

---

## 5. 비교 요약

| 항목 | CREATE SCHEMA | CREATE VIEW | CREATE INDEX |
|------|---------------|-------------|--------------|
| **목적** | 객체 그룹화 | 쿼리 단순화 | 검색 성능 향상 |
| **저장 내용** | 메타데이터 | 쿼리 정의 | 인덱스 구조 |
| **물리적 저장** | 없음 | 없음 | 있음 |
| **SELECT 성능** | - | 동일/느림 | 빠름 |
| **INSERT 성능** | - | - | 느림 |
| **주 사용처** | 권한/네임스페이스 | 보안/추상화 | 성능 최적화 |

---

## 6. 빠른 참조

```sql
-- SCHEMA
CREATE SCHEMA 스키마명;
DROP SCHEMA 스키마명 CASCADE;

-- VIEW
CREATE VIEW 뷰명 AS SELECT ...;
CREATE OR REPLACE VIEW 뷰명 AS SELECT ...;
DROP VIEW 뷰명 CASCADE;

-- INDEX
CREATE INDEX 인덱스명 ON 테이블명 (컬럼명);
CREATE UNIQUE INDEX 인덱스명 ON 테이블명 (컬럼명);
DROP INDEX 인덱스명;
```

**핵심**: 스키마는 조직화, 뷰는 단순화, 인덱스는 최적화!



# DROP 명령어 핵심 정리

## 기본 개념
- **DROP**: 데이터베이스 객체를 완전히 삭제
- **영구 삭제** - 복구 불가 (주의!)
- DDL(Data Definition Language) 명령어

---

## 주요 DROP 명령어

### 1. DROP TABLE
```sql
-- 기본
DROP TABLE 테이블명;

-- 안전하게 (존재할 때만 삭제)
DROP TABLE IF EXISTS 테이블명;

-- 참조 객체도 함께 삭제
DROP TABLE 테이블명 CASCADE;

-- 참조 있으면 삭제 불가 (기본값)
DROP TABLE 테이블명 RESTRICT;
```

### 2. DROP SCHEMA
```sql
-- 빈 스키마만 삭제
DROP SCHEMA 스키마명;

-- 스키마 내 모든 객체 함께 삭제
DROP SCHEMA 스키마명 CASCADE;
```

### 3. DROP VIEW
```sql
-- 뷰 삭제
DROP VIEW 뷰명;

-- 해당 뷰를 참조하는 뷰도 함께 삭제
DROP VIEW 뷰명 CASCADE;
```

### 4. DROP INDEX
```sql
-- 인덱스 삭제
DROP INDEX 인덱스명;
```

### 5. DROP DOMAIN
```sql
-- 도메인 삭제
DROP DOMAIN 도메인명;

-- 해당 도메인 사용 컬럼도 함께 처리
DROP DOMAIN 도메인명 CASCADE;
```

### 6. DROP DATABASE
```sql
-- 데이터베이스 전체 삭제
DROP DATABASE 데이터베이스명;
```

---

## CASCADE vs RESTRICT

### RESTRICT (기본값)
```sql
-- 다른 객체가 참조하면 삭제 불가
DROP TABLE DEPARTMENT RESTRICT;
-- → EMPLOYEE 테이블이 참조하면 오류 발생
```

### CASCADE
```sql
-- 참조하는 모든 객체도 함께 삭제
DROP TABLE DEPARTMENT CASCADE;
-- → EMPLOYEE의 외래키, 관련 뷰 등도 모두 삭제
```

---

## DROP vs 다른 명령어

| 명령어 | 대상 | 복구 | 속도 | 롤백 |
|--------|------|------|------|------|
| **DROP** | 구조+데이터 | 불가 | 빠름 | 가능(DDL) |
| **TRUNCATE** | 데이터만 | 불가 | 매우 빠름 | 불가 |
| **DELETE** | 데이터(조건) | 가능 | 느림 | 가능(DML) |

```sql
-- DROP: 테이블 자체가 사라짐
DROP TABLE EMPLOYEE;

-- TRUNCATE: 테이블은 남고 데이터만 삭제
TRUNCATE TABLE EMPLOYEE;

-- DELETE: 조건에 맞는 행만 삭제
DELETE FROM EMPLOYEE WHERE DEPT_ID = 10;
```

---

## 주의사항 ⚠️

### 1. 영구 삭제
```sql
DROP TABLE CUSTOMER;
-- 모든 데이터와 구조가 영구 삭제!
-- 백업 없으면 복구 불가!
```

### 2. CASCADE의 위험성
```sql
DROP TABLE DEPARTMENT CASCADE;
-- 예상치 못한 다른 테이블/뷰도 삭제될 수 있음
-- 미리 영향 범위 확인 필수!
```

### 3. 운영 환경 주의
```sql
-- ❌ 위험
DROP TABLE ORDERS;

-- ✅ 안전
-- 1. 백업 먼저
-- 2. 영향 범위 확인
-- 3. IF EXISTS 사용
DROP TABLE IF EXISTS ORDERS_BACKUP;
```

---

## 안전한 삭제 절차

```sql
-- 1단계: 백업
CREATE TABLE EMPLOYEE_BACKUP AS
SELECT * FROM EMPLOYEE;

-- 2단계: 참조 확인
SELECT * 
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'EMPLOYEE';

-- 3단계: 외래키 먼저 제거
ALTER TABLE ORDERS DROP CONSTRAINT FK_EMPLOYEE;

-- 4단계: 안전하게 삭제
DROP TABLE IF EXISTS EMPLOYEE;
```

---

## 실무 예시

### 테스트 환경 정리
```sql
-- 임시 테이블들 삭제
DROP TABLE IF EXISTS TEMP_DATA;
DROP TABLE IF EXISTS TEST_TABLE;
DROP TABLE IF EXISTS BACKUP_OLD;
```

### 스키마 전체 삭제
```sql
-- 개발 환경 초기화
DROP SCHEMA DEV CASCADE;
CREATE SCHEMA DEV;
```

### 뷰 재생성
```sql
-- 뷰 삭제 후 재생성
DROP VIEW IF EXISTS EMP_SUMMARY;
CREATE VIEW EMP_SUMMARY AS
SELECT EMP_ID, EMP_NAME FROM EMPLOYEE;
```

---

## 핵심 요약

```sql
-- 객체 삭제
DROP TABLE 테이블명;
DROP VIEW 뷰명;
DROP INDEX 인덱스명;
DROP SCHEMA 스키마명;

-- 옵션
IF EXISTS          -- 존재할 때만 삭제
CASCADE           -- 참조 객체도 함께 삭제
RESTRICT          -- 참조 있으면 삭제 불가
```

**⚠️ DROP은 영구 삭제입니다. 신중하게 사용하세요!**




# DML 
>Data Manipulation Language

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

# DCL 
>Data Control Language

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




