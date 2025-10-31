---
title: "Sql&DB"
date: 2025-02-15
tags: 
  - sql
  - database
categories: 
  - CS
layout: category-split
permalink: /categories/cs/database/
taxonomy: cs/database/
sidebar:
  nav: "categories"
---


## SQL & DataBase

### 목록

#### <a href="#" data-content="/assets/contents/cs/sql-grammer.md"><span style="color: #9bd6bd;">♡</span> SQL 기본 문법</a>

#### <a href="#" data-content="/assets/contents/cs/join.md"><span style="color: #9bd6bd;">♡</span> JOIN 연산</a>

#### <a href="#" data-content="/assets/contents/cs/group-by.md"><span style="color: #9bd6bd;">♡</span> GROUP BY & 집계함수</a>

#### <a href="#" data-content="/assets/contents/cs/sub-query.md"><span style="color: #9bd6bd;">♡</span> 서브쿼리</a>

#### <a href="#" data-content="/assets/contents/cs/ddl-dml-dcl.md"><span style="color: #9bd6bd;">♡</span> DDL/DML/DCL</a>

#### <a href="#" data-content="/assets/contents/cs/constraints.md"><span style="color: #9bd6bd;">♡</span> 제약조건</a>

#### <a href="#" data-content="/assets/contents/cs/index.md"><span style="color: #9bd6bd;">♡</span> 인덱스</a>

#### <a href="#" data-content="/assets/contents/cs/view.md"><span style="color: #9bd6bd;">♡</span> 뷰(View)</a>

#### <a href="#" data-content="/assets/contents/cs/transaction.md"><span style="color: #9bd6bd;">♡</span> 트랜잭션</a>

#### <a href="#" data-content="/assets/contents/cs/normalize.md"><span style="color: #9bd6bd;">♡</span> 정규화</a>

#### <a href="#" data-content="/assets/contents/cs/sql-interview.md"><span style="color: #9bd6bd;">♡</span> 면접필수개념</a>


---


## 📝 자주 나오는 기출 유형

### 1. 부서별 최고 급여자 찾기

```sql
SELECT e.*
FROM employees e
WHERE (department, salary) IN (
    SELECT department, MAX(salary)
    FROM employees
    GROUP BY department
);
```

### 2. 순위 매기기 (RANK)

```sql
SELECT 
    name, 
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

### 3. 누적 합계

```sql
SELECT 
    name,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) AS cumulative_sum
FROM employees;
```

### 4. 날짜 함수

```sql
SELECT 
    NOW(),                          -- 현재 날짜시간
    CURDATE(),                      -- 현재 날짜
    DATE_ADD(NOW(), INTERVAL 7 DAY), -- 7일 후
    DATEDIFF(NOW(), hire_date)      -- 날짜 차이
FROM employees;
```

### 5. 문자열 함수

```sql
SELECT 
    CONCAT(first_name, ' ', last_name),  -- 문자열 결합
    SUBSTRING(phone, 1, 3),              -- 부분 문자열
    LENGTH(name),                        -- 길이
    UPPER(email),                        -- 대문자
    REPLACE(phone, '-', '')              -- 치환
FROM employees;
```

-----

**goal**: 각 개념을 반드시 직접 SQL로 실행해보기

