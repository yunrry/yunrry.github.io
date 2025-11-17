# SQL-DOMAIN

> 도메인이란 하나의 속성이 취할 수 있는 동일한 유형의 원자값들의 집합이다.  

### DDL로 DOMAIN 다루기
DDL(Data Define Language) {CREATE, ALTER, DROP}   

## CREATE DOMAIN
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

## ALTER DOMAIN
```sql
ALTER DOMAIN SALARY
    ADD CONSTRAINT MIN_SALARY CHECK(VALUE>=1000000);
```

## DROP DOMAIN
```sql
DROP DOMAIN SEX CASCADE;
```
CASCADE : 해당 도메인을 사용하는 모든 컬럼도 함께 처리

## DOMAIN 사용 예시

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