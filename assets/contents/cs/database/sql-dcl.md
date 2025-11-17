# DCL (Data Control Language)

> 데이터 제어 언어 
>- 데이터베이스 **권한(Privilege)** 관리
>- 사용자의 **접근 제어** 및 **보안** 관리
>- 주요 명령어: **GRANT**, **REVOKE**

---

## 1. GRANT (권한 부여)

### 기본 구문
```sql
GRANT 권한 [, 권한, ...]
ON 객체
TO 사용자 [, 사용자, ...]
[WITH GRANT OPTION];
```

### 테이블 권한 부여

#### 기본 권한
```sql
-- SELECT 권한
GRANT SELECT ON EMPLOYEE TO user1;

-- INSERT 권한
GRANT INSERT ON EMPLOYEE TO user1;

-- UPDATE 권한
GRANT UPDATE ON EMPLOYEE TO user1;

-- DELETE 권한
GRANT DELETE ON EMPLOYEE TO user1;

-- 다중 권한 동시 부여
GRANT SELECT, INSERT, UPDATE 
ON EMPLOYEE 
TO user1;

-- 모든 권한 부여
GRANT ALL PRIVILEGES ON EMPLOYEE TO user1;
```

#### 특정 컬럼에만 권한 부여
```sql
-- 특정 컬럼만 조회 가능
GRANT SELECT (EMP_ID, EMP_NAME) 
ON EMPLOYEE 
TO user1;

-- 특정 컬럼만 수정 가능
GRANT UPDATE (SALARY) 
ON EMPLOYEE 
TO user1;
```

### 다중 사용자에게 권한 부여
```sql
-- 여러 사용자에게 동시 부여
GRANT SELECT ON EMPLOYEE 
TO user1, user2, user3;

-- PUBLIC (모든 사용자)에게 부여
GRANT SELECT ON DEPARTMENT TO PUBLIC;
```

### WITH GRANT OPTION
```sql
-- 권한을 받은 사용자가 다른 사용자에게도 권한 부여 가능
GRANT SELECT ON EMPLOYEE 
TO user1 
WITH GRANT OPTION;

-- user1이 user2에게 권한 재부여 가능
-- (user1로 로그인)
GRANT SELECT ON EMPLOYEE TO user2;
```

### 스키마 권한
```sql
-- 스키마 내 모든 테이블 권한
GRANT SELECT ON SCHEMA hr TO user1;

-- 스키마 사용 권한
GRANT USAGE ON SCHEMA hr TO user1;
```

### 뷰 권한
```sql
-- 뷰 조회 권한
GRANT SELECT ON EMP_VIEW TO user1;

-- 뷰를 통한 수정 권한
GRANT UPDATE ON EMP_VIEW TO user1;
```

### 저장 프로시저/함수 권한
```sql
-- 프로시저 실행 권한
GRANT EXECUTE ON PROCEDURE calculate_salary TO user1;

-- 함수 실행 권한
GRANT EXECUTE ON FUNCTION get_employee_count TO user1;
```

---

## 2. REVOKE (권한 회수)

### 기본 구문
```sql
REVOKE 권한 [, 권한, ...]
ON 객체
FROM 사용자 [, 사용자, ...]
[CASCADE | RESTRICT];
```

### 테이블 권한 회수

#### 기본 회수
```sql
-- SELECT 권한 회수
REVOKE SELECT ON EMPLOYEE FROM user1;

-- INSERT 권한 회수
REVOKE INSERT ON EMPLOYEE FROM user1;

-- 다중 권한 회수
REVOKE SELECT, INSERT, UPDATE 
ON EMPLOYEE 
FROM user1;

-- 모든 권한 회수
REVOKE ALL PRIVILEGES ON EMPLOYEE FROM user1;
```

#### 특정 컬럼 권한 회수
```sql
-- 특정 컬럼 조회 권한 회수
REVOKE SELECT (SALARY) 
ON EMPLOYEE 
FROM user1;
```

### 다중 사용자 권한 회수
```sql
-- 여러 사용자에게서 동시 회수
REVOKE SELECT ON EMPLOYEE 
FROM user1, user2, user3;

-- PUBLIC에서 회수
REVOKE SELECT ON DEPARTMENT FROM PUBLIC;
```

### CASCADE vs RESTRICT

#### CASCADE
```sql
-- 연쇄 회수: 해당 사용자가 부여한 권한도 함께 회수
REVOKE SELECT ON EMPLOYEE 
FROM user1 
CASCADE;

-- user1 → user2에게 부여한 권한도 함께 회수됨
```

#### RESTRICT (기본값)
```sql
-- 다른 사용자에게 권한을 부여했으면 회수 불가
REVOKE SELECT ON EMPLOYEE 
FROM user1 
RESTRICT;

-- user1이 다른 사용자에게 권한 부여했으면 오류 발생
```

### GRANT OPTION 회수
```sql
-- 재부여 권한만 회수
REVOKE GRANT OPTION FOR SELECT 
ON EMPLOYEE 
FROM user1;
-- user1은 여전히 SELECT 가능하지만 타인에게 부여 불가
```

---

## 3. 권한의 종류

### 테이블 권한
| 권한 | 설명 | 예시 |
|------|------|------|
| **SELECT** | 조회 | `SELECT * FROM EMPLOYEE` |
| **INSERT** | 삽입 | `INSERT INTO EMPLOYEE VALUES (...)` |
| **UPDATE** | 수정 | `UPDATE EMPLOYEE SET ...` |
| **DELETE** | 삭제 | `DELETE FROM EMPLOYEE WHERE ...` |
| **REFERENCES** | 외래키 참조 | `FOREIGN KEY ... REFERENCES` |
| **ALTER** | 구조 변경 | `ALTER TABLE EMPLOYEE ...` |
| **INDEX** | 인덱스 생성 | `CREATE INDEX ...` |
| **ALL** | 모든 권한 | - |

### 시스템 권한 (DBMS별 상이)
```sql
-- 데이터베이스 생성
GRANT CREATE DATABASE TO user1;

-- 테이블 생성
GRANT CREATE TABLE TO user1;

-- 뷰 생성
GRANT CREATE VIEW TO user1;

-- 시퀀스 생성
GRANT CREATE SEQUENCE TO user1;

-- 사용자 생성
GRANT CREATE USER TO user1;
```

---

## 4. 역할(ROLE) 관리

### ROLE 생성 및 사용
```sql
-- 역할 생성
CREATE ROLE hr_manager;
CREATE ROLE developer;
CREATE ROLE readonly;

-- 역할에 권한 부여
GRANT SELECT, INSERT, UPDATE, DELETE 
ON EMPLOYEE 
TO hr_manager;

GRANT SELECT ON EMPLOYEE TO readonly;

-- 사용자에게 역할 부여
GRANT hr_manager TO user1;
GRANT readonly TO user2, user3;

-- 역할 회수
REVOKE hr_manager FROM user1;

-- 역할 삭제
DROP ROLE hr_manager;
```

### 역할 계층 구조
```sql
-- 역할에 역할 부여 (계층 구조)
CREATE ROLE manager;
CREATE ROLE employee;

GRANT SELECT ON DEPARTMENT TO employee;
GRANT employee TO manager;  -- manager는 employee 권한 포함
GRANT INSERT, UPDATE, DELETE ON DEPARTMENT TO manager;

-- 사용자에게 역할 부여
GRANT manager TO user1;
GRANT employee TO user2;
```

---

## 5. 실무 예시

### 기본 권한 설정
```sql
-- 읽기 전용 사용자
CREATE USER readonly_user IDENTIFIED BY 'password123';
GRANT SELECT ON EMPLOYEE TO readonly_user;
GRANT SELECT ON DEPARTMENT TO readonly_user;
GRANT SELECT ON SALARY TO readonly_user;

-- 일반 직원 사용자
CREATE USER normal_user IDENTIFIED BY 'password456';
GRANT SELECT, INSERT, UPDATE ON EMPLOYEE TO normal_user;
GRANT SELECT ON DEPARTMENT TO normal_user;

-- 관리자 사용자
CREATE USER admin_user IDENTIFIED BY 'password789';
GRANT ALL PRIVILEGES ON EMPLOYEE TO admin_user WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON DEPARTMENT TO admin_user WITH GRANT OPTION;
```

### 부서별 권한 관리
```sql
-- HR 부서 역할
CREATE ROLE hr_role;
GRANT ALL PRIVILEGES ON EMPLOYEE TO hr_role;
GRANT ALL PRIVILEGES ON SALARY TO hr_role;
GRANT ALL PRIVILEGES ON ATTENDANCE TO hr_role;

-- IT 부서 역할
CREATE ROLE it_role;
GRANT ALL PRIVILEGES ON SYSTEM_LOG TO it_role;
GRANT SELECT ON EMPLOYEE TO it_role;
GRANT CREATE TABLE TO it_role;

-- 영업 부서 역할
CREATE ROLE sales_role;
GRANT ALL PRIVILEGES ON CUSTOMER TO sales_role;
GRANT ALL PRIVILEGES ON ORDERS TO sales_role;
GRANT SELECT ON PRODUCT TO sales_role;

-- 사용자에게 역할 부여
GRANT hr_role TO hr_user1, hr_user2;
GRANT it_role TO it_user1, it_user2;
GRANT sales_role TO sales_user1, sales_user2;
```

### 프로젝트별 권한 관리
```sql
-- 프로젝트 스키마 생성
CREATE SCHEMA project_a;
CREATE SCHEMA project_b;

-- 프로젝트 A 팀
CREATE ROLE project_a_team;
GRANT ALL PRIVILEGES ON SCHEMA project_a TO project_a_team;
GRANT project_a_team TO user1, user2, user3;

-- 프로젝트 B 팀
CREATE ROLE project_b_team;
GRANT ALL PRIVILEGES ON SCHEMA project_b TO project_b_team;
GRANT project_b_team TO user4, user5, user6;

-- 프로젝트 매니저 (모든 프로젝트 접근)
CREATE ROLE project_manager;
GRANT project_a_team TO project_manager;
GRANT project_b_team TO project_manager;
GRANT project_manager TO manager_user;
```

### 보안 강화 설정
```sql
-- 민감 정보 제한
-- 급여 정보는 HR만 조회 가능
REVOKE SELECT ON SALARY FROM PUBLIC;
GRANT SELECT ON SALARY TO hr_role;

-- 개인정보는 특정 컬럼만 조회 허용
GRANT SELECT (EMP_ID, EMP_NAME, DEPT_ID) 
ON EMPLOYEE 
TO general_user;

-- 급여 컬럼은 제외
REVOKE SELECT (SALARY, BONUS, BANK_ACCOUNT) 
ON EMPLOYEE 
FROM general_user;
```

### 임시 권한 부여
```sql
-- 감사 기간 동안 임시 권한
GRANT SELECT ON FINANCIAL_DATA TO auditor;

-- 감사 종료 후 회수
REVOKE SELECT ON FINANCIAL_DATA FROM auditor;
```

---

## 6. 권한 확인

### 사용자 권한 조회
```sql
-- 현재 사용자 권한 확인
SELECT * FROM USER_TAB_PRIVS;

-- 특정 테이블 권한 확인
SELECT * FROM TABLE_PRIVILEGES 
WHERE TABLE_NAME = 'EMPLOYEE';

-- 역할 권한 확인
SELECT * FROM ROLE_TAB_PRIVS;

-- 시스템 권한 확인
SELECT * FROM USER_SYS_PRIVS;
```

### 표준 SQL 방식
```sql
-- INFORMATION_SCHEMA 활용
SELECT * 
FROM INFORMATION_SCHEMA.TABLE_PRIVILEGES
WHERE GRANTEE = 'user1';

SELECT * 
FROM INFORMATION_SCHEMA.COLUMN_PRIVILEGES
WHERE TABLE_NAME = 'EMPLOYEE';
```

---

## 7. 권한 관리 모범 사례

### ✅ 최소 권한 원칙
```sql
-- ❌ 나쁜 예: 과도한 권한
GRANT ALL PRIVILEGES ON DATABASE company TO user1;

-- ✅ 좋은 예: 필요한 권한만
GRANT SELECT ON EMPLOYEE TO user1;
GRANT INSERT ON ORDERS TO user1;
```

### ✅ 역할(ROLE) 활용
```sql
-- ❌ 나쁜 예: 개별 권한 부여
GRANT SELECT ON TABLE1 TO user1;
GRANT SELECT ON TABLE2 TO user1;
GRANT SELECT ON TABLE3 TO user1;
-- ... (반복)

-- ✅ 좋은 예: 역할 사용
CREATE ROLE data_analyst;
GRANT SELECT ON TABLE1 TO data_analyst;
GRANT SELECT ON TABLE2 TO data_analyst;
GRANT SELECT ON TABLE3 TO data_analyst;
GRANT data_analyst TO user1, user2, user3;
```

### ✅ PUBLIC 사용 주의
```sql
-- ⚠️ 위험: 모든 사용자에게 권한
GRANT ALL PRIVILEGES ON EMPLOYEE TO PUBLIC;

-- ✅ 안전: 특정 역할/사용자에게만
GRANT SELECT ON EMPLOYEE TO readonly_role;
```

### ✅ WITH GRANT OPTION 신중히 사용
```sql
-- ⚠️ 주의: 권한 확산 가능
GRANT SELECT ON EMPLOYEE TO user1 WITH GRANT OPTION;
-- user1이 무분별하게 권한 재부여 가능

-- ✅ 관리자만 사용
GRANT ALL PRIVILEGES ON EMPLOYEE TO admin WITH GRANT OPTION;
```

### ✅ 정기적인 권한 검토
```sql
-- 사용하지 않는 권한 회수
REVOKE UPDATE ON EMPLOYEE FROM user1;

-- 퇴사자 권한 즉시 회수
REVOKE ALL PRIVILEGES ON DATABASE company FROM ex_employee CASCADE;
```

---

## 8. 보안 시나리오

### 시나리오 1: 신입 사원 입사
```sql
-- 1. 사용자 생성
CREATE USER new_employee IDENTIFIED BY 'temp_password';

-- 2. 기본 역할 부여
GRANT employee_role TO new_employee;

-- 3. 부서별 추가 권한
GRANT sales_role TO new_employee;

-- 4. 비밀번호 변경 강제
ALTER USER new_employee PASSWORD EXPIRE;
```

### 시나리오 2: 부서 이동
```sql
-- 1. 기존 부서 역할 회수
REVOKE sales_role FROM employee1;

-- 2. 새 부서 역할 부여
GRANT marketing_role TO employee1;
```

### 시나리오 3: 퇴사 처리
```sql
-- 1. 모든 권한 회수 (연쇄 회수)
REVOKE ALL PRIVILEGES ON DATABASE company 
FROM ex_employee 
CASCADE;

-- 2. 역할 회수
REVOKE employee_role FROM ex_employee CASCADE;

-- 3. 계정 잠금 또는 삭제
ALTER USER ex_employee ACCOUNT LOCK;
-- 또는
DROP USER ex_employee CASCADE;
```

### 시나리오 4: 외부 감사
```sql
-- 1. 임시 감사자 계정 생성
CREATE USER auditor_2024 IDENTIFIED BY 'audit_password';

-- 2. 읽기 전용 권한만 부여
GRANT SELECT ON SCHEMA company TO auditor_2024;

-- 3. 기간 제한 (애플리케이션 레벨에서 관리)

-- 4. 감사 종료 후 삭제
DROP USER auditor_2024 CASCADE;
```

---

## 9. DBMS별 차이점

### MySQL
```sql
-- 권한 부여
GRANT SELECT, INSERT ON company.employee TO 'user1'@'localhost';

-- 권한 회수
REVOKE SELECT ON company.employee FROM 'user1'@'localhost';

-- 권한 적용
FLUSH PRIVILEGES;
```

### PostgreSQL
```sql
-- 스키마 사용 권한
GRANT USAGE ON SCHEMA public TO user1;

-- 테이블 권한
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user1;

-- 시퀀스 권한
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO user1;
```

### Oracle
```sql
-- 시스템 권한
GRANT CREATE SESSION TO user1;
GRANT CREATE TABLE TO user1;

-- 객체 권한
GRANT SELECT ON hr.employees TO user1;

-- 역할
GRANT dba TO user1;  -- DBA 역할 부여
```

---

## 10. 빠른 참조

```sql
-- 권한 부여
GRANT 권한 ON 객체 TO 사용자;
GRANT SELECT, INSERT ON EMPLOYEE TO user1;
GRANT ALL PRIVILEGES ON EMPLOYEE TO user1;
GRANT SELECT ON EMPLOYEE TO user1 WITH GRANT OPTION;

-- 권한 회수
REVOKE 권한 ON 객체 FROM 사용자;
REVOKE SELECT ON EMPLOYEE FROM user1;
REVOKE ALL PRIVILEGES ON EMPLOYEE FROM user1;
REVOKE SELECT ON EMPLOYEE FROM user1 CASCADE;

-- 역할
CREATE ROLE 역할명;
GRANT 권한 TO 역할명;
GRANT 역할명 TO 사용자;
REVOKE 역할명 FROM 사용자;
DROP ROLE 역할명;

-- 권한 확인
SELECT * FROM TABLE_PRIVILEGES;
SELECT * FROM USER_TAB_PRIVS;
```

**핵심**: 최소 권한 원칙, 역할 활용, 정기 검토!