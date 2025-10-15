# 인덱스 Index

## 📌 인덱스란?

**데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조**

책의 "목차" 또는 "색인"과 같은 개념이다.

```
책에서 특정 단어 찾기:
❌ 인덱스 없음 → 1페이지부터 끝까지 전부 읽기 (Full Scan)
✅ 인덱스 있음 → 색인에서 페이지 번호 찾고 바로 이동
```

---

## 🌳 인덱스의 내부 구조: B-Tree (Balanced Tree)

### B-Tree 구조

```
                    [50]                  ← Root Node (루트)
                   /    \
                 /        \
            [20, 30]    [70, 90]          ← Branch Node (가지)
           /   |   \    /   |   \
         /     |     \ /     |     \
    [10,15] [25,28] [35,40] ...           ← Leaf Node (리프)
       ↓      ↓      ↓
    실제데이터 실제데이터 실제데이터          ← Data Pointer
```

### B-Tree의 특징

1. **균형 잡힌 트리**: 모든 리프 노드가 같은 레벨
2. **정렬된 상태 유지**: 항상 오름차순 정렬
3. **시간 복잡도**: O(log N) - 매우 빠름
4. **다중 자식 노드**: 한 노드에 여러 키 저장 (2개 이상)

### 검색 과정 예시

```sql
SELECT * FROM employees WHERE id = 35;
```

**인덱스 없을 때:**
```
행1 → 행2 → 행3 → ... → 행35 (35번 비교)
시간 복잡도: O(N)
```

**인덱스 있을 때:**
```
Root [50] → 35 < 50 → 왼쪽
Branch [20, 30] → 35 > 30 → 오른쪽
Leaf [35, 40] → 찾음! (3번 비교)
시간 복잡도: O(log N)
```

---

## 🔧 인덱스 생성 문법

### 1. 단일 컬럼 인덱스

```sql
-- 기본 인덱스 생성
CREATE INDEX idx_name ON employees(name);

-- 인덱스 이름 규칙: idx_테이블명_컬럼명
CREATE INDEX idx_employees_email ON employees(email);
```

### 2. 복합 인덱스 (Composite Index)

```sql
-- 여러 컬럼을 하나의 인덱스로
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- 순서가 중요! (department → salary 순으로 정렬)
```

**복합 인덱스 동작 원리:**

```
인덱스: (department, salary)

         [IT, 30000]
        /           \
   [IT, 35000]   [IT, 50000]
      /              \
 [IT, 35000, 김철수]  [IT, 50000, 이영희]
```

**복합 인덱스 사용 규칙 (Left-Most Rule):**

```sql
CREATE INDEX idx_abc ON table(a, b, c);

-- ✅ 인덱스 사용 O
WHERE a = 1
WHERE a = 1 AND b = 2
WHERE a = 1 AND b = 2 AND c = 3

-- ⚠️ 인덱스 일부만 사용
WHERE a = 1 AND c = 3  -- a만 인덱스 사용

-- ❌ 인덱스 사용 X (첫 컬럼 a가 없음)
WHERE b = 2
WHERE c = 3
WHERE b = 2 AND c = 3
```

### 3. 유니크 인덱스

```sql
-- 중복 값 허용 안 함
CREATE UNIQUE INDEX idx_email ON employees(email);

-- PRIMARY KEY는 자동으로 유니크 인덱스 생성
CREATE TABLE users (
    id INT PRIMARY KEY  -- 자동으로 유니크 인덱스
);
```

### 4. 전문 검색 인덱스 (Full-Text Index)

```sql
-- 텍스트 검색용 (LIKE '%keyword%' 대체)
CREATE FULLTEXT INDEX idx_content ON articles(content);

-- 사용
SELECT * FROM articles 
WHERE MATCH(content) AGAINST('검색어');
```

### 5. 인덱스 삭제

```sql
-- 인덱스 삭제
DROP INDEX idx_name ON employees;

-- MySQL
ALTER TABLE employees DROP INDEX idx_name;
```

---

## ✅ 인덱스의 장점

### 1. 검색 속도 대폭 향상

```sql
-- 100만 건 데이터에서 검색
-- 인덱스 없음: 0.5초 (Full Scan)
-- 인덱스 있음: 0.001초 (Index Scan)

SELECT * FROM employees WHERE id = 12345;
```

**성능 비교:**
```
데이터 건수 | Full Scan | Index Scan
---------|-----------|------------
1,000    | 1ms       | 0.01ms
10,000   | 10ms      | 0.01ms
100,000  | 100ms     | 0.02ms
1,000,000| 1,000ms   | 0.03ms
```

### 2. ORDER BY 성능 향상

```sql
-- 인덱스가 이미 정렬되어 있어서 빠름
CREATE INDEX idx_salary ON employees(salary);

SELECT * FROM employees ORDER BY salary;
-- 별도 정렬 작업 불필요 (Using index)
```

### 3. GROUP BY 성능 향상

```sql
CREATE INDEX idx_department ON employees(department);

SELECT department, COUNT(*) 
FROM employees 
GROUP BY department;
-- 인덱스를 활용한 빠른 그룹화
```

### 4. MIN/MAX 값 즉시 조회

```sql
CREATE INDEX idx_salary ON employees(salary);

-- 인덱스의 첫 번째/마지막 값만 읽으면 됨
SELECT MIN(salary) FROM employees;  -- 0.001초
SELECT MAX(salary) FROM employees;  -- 0.001초
```

### 5. JOIN 성능 향상

```sql
-- 외래키에 인덱스 생성
CREATE INDEX idx_dept_id ON employees(dept_id);

SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
-- JOIN 조건 컬럼에 인덱스 → 빠른 매칭
```

---

## ⚠️ 인덱스의 단점

### 1. 추가 저장 공간 필요

```
테이블 크기: 1GB
인덱스 크기: 약 100MB (테이블 크기의 10~15%)

인덱스 5개 → 500MB 추가 공간 필요
```

### 2. INSERT 성능 저하

```sql
INSERT INTO employees VALUES (101, '홍길동', 50000);
```

**작업 과정:**
1. 테이블에 데이터 삽입
2. **인덱스 1에 새 키 추가** (B-Tree 재정렬)
3. **인덱스 2에 새 키 추가**
4. **인덱스 3에 새 키 추가**
...

**성능 비교:**
```
인덱스 0개: INSERT 1ms
인덱스 3개: INSERT 4ms (4배 느림)
인덱스 10개: INSERT 15ms (15배 느림)
```

### 3. UPDATE 성능 저하

```sql
-- 인덱스 컬럼 수정 시 느림
UPDATE employees SET salary = 60000 WHERE id = 10;
```

**작업 과정:**
1. 테이블 데이터 수정
2. **salary 인덱스에서 기존 값 삭제**
3. **salary 인덱스에 새 값 추가** (B-Tree 재정렬)

**인덱스가 없는 컬럼 수정은 빠름:**
```sql
-- phone에 인덱스 없음 → 빠름
UPDATE employees SET phone = '010-1234-5678' WHERE id = 10;
```

### 4. DELETE 성능 저하

```sql
DELETE FROM employees WHERE id = 10;
```

**작업 과정:**
1. 테이블에서 데이터 삭제
2. **모든 인덱스에서 해당 키 삭제**
3. **B-Tree 재구성**

### 5. 인덱스 유지보수 비용

```sql
-- 데이터 변경이 많으면 인덱스 단편화 발생
-- 주기적으로 인덱스 재구성 필요
ALTER TABLE employees ENGINE=InnoDB;  -- 재구성

-- 또는
OPTIMIZE TABLE employees;  -- 최적화
```

---

## 🎯 인덱스 사용이 효과적인 경우

### 1. WHERE 절에 자주 사용되는 컬럼

```sql
-- email로 자주 검색
SELECT * FROM users WHERE email = 'hong@example.com';

-- 인덱스 생성
CREATE INDEX idx_email ON users(email);
```

### 2. 카디널리티가 높은 컬럼

**카디널리티 (Cardinality)**: 중복도가 낮은 정도

```sql
-- 높은 카디널리티 (인덱스 효과적) ✅
email    → 10,000명 중 10,000개 고유값 (100%)
주민번호  → 10,000명 중 10,000개 고유값 (100%)
전화번호  → 10,000명 중 9,800개 고유값 (98%)

-- 낮은 카디널리티 (인덱스 비효율) ❌
성별     → 10,000명 중 2개 고유값 (남/여)
결혼여부  → 10,000명 중 2개 고유값 (Y/N)
등급     → 10,000명 중 5개 고유값 (VIP, Gold, Silver...)
```

**카디널리티가 낮은 컬럼에 인덱스를 만들면?**
```sql
-- 성별 인덱스 생성 (비효율)
CREATE INDEX idx_gender ON employees(gender);

SELECT * FROM employees WHERE gender = 'M';
-- 전체의 50%를 조회 → Full Scan이 더 빠를 수 있음
```

### 3. 정렬(ORDER BY)에 자주 사용되는 컬럼

```sql
-- 최신 게시글 조회
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10;

-- 인덱스 생성
CREATE INDEX idx_created_at ON posts(created_at);
```

### 4. JOIN 조건에 사용되는 컬럼

```sql
-- 외래키에 인덱스 필수
CREATE INDEX idx_dept_id ON employees(dept_id);
CREATE INDEX idx_user_id ON orders(user_id);

-- JOIN 성능 향상
SELECT * FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

### 5. 데이터 변경이 적은 테이블

```sql
-- 조회는 많고, 수정은 적은 경우
-- 예: 코드 테이블, 카테고리 테이블, 지역 테이블
CREATE INDEX idx_code ON code_master(code);
```

---

## 🚫 인덱스 사용이 비효과적인 경우

### 1. 작은 테이블

```sql
-- 데이터 100건 미만 → 인덱스 불필요
-- Full Scan이 더 빠름
```

### 2. 데이터 변경이 빈번한 컬럼

```sql
-- 실시간 업데이트되는 컬럼 (재고 수량, 조회수 등)
UPDATE products SET view_count = view_count + 1;
-- 인덱스 재구성 비용 > 검색 성능 향상
```

### 3. WHERE 절에 잘 사용되지 않는 컬럼

```sql
-- 주소 컬럼은 검색 조건으로 거의 안 씀
CREATE INDEX idx_address ON users(address);  -- 불필요
```

### 4. 결과가 테이블의 대부분인 경우

```sql
-- 전체의 80% 이상 조회 → Full Scan이 더 빠름
SELECT * FROM employees WHERE salary > 30000;
-- 대부분의 직원이 3만원 이상 받으면 인덱스 무의미
```

---

## ❌ 인덱스를 사용하지 못하는 경우

### 1. 인덱스 컬럼에 함수 사용

```sql
-- ❌ 인덱스 사용 불가
CREATE INDEX idx_hire_date ON employees(hire_date);

SELECT * FROM employees WHERE YEAR(hire_date) = 2023;
-- hire_date에 함수 적용 → 인덱스 무용지물

-- ✅ 인덱스 사용 O
SELECT * FROM employees 
WHERE hire_date BETWEEN '2023-01-01' AND '2023-12-31';
```

### 2. 인덱스 컬럼에 연산

```sql
-- ❌ 인덱스 사용 불가
SELECT * FROM employees WHERE salary * 1.1 > 50000;

-- ✅ 인덱스 사용 O
SELECT * FROM employees WHERE salary > 50000 / 1.1;
```

### 3. LIKE의 중간/끝 매칭

```sql
CREATE INDEX idx_name ON employees(name);

-- ✅ 인덱스 사용 O
SELECT * FROM employees WHERE name LIKE '김%';

-- ❌ 인덱스 사용 불가
SELECT * FROM employees WHERE name LIKE '%길동';
SELECT * FROM employees WHERE name LIKE '%길%';
```

**이유:** 인덱스는 왼쪽부터 정렬되어 있음

```
인덱스 내부:
강민수
김철수
김태희
박영희
이순신

'김%' → 김철수부터 시작해서 연속 검색 가능 ✅
'%동' → 어디서 시작할지 모름, 전체 스캔 필요 ❌
```

### 4. NOT, !=, <> 사용

```sql
-- ❌ 인덱스 사용 불가 (대부분의 DBMS)
SELECT * FROM employees WHERE department != 'IT';
SELECT * FROM employees WHERE NOT department = 'IT';

-- ✅ 인덱스 사용 O
SELECT * FROM employees WHERE department = 'IT';
```

### 5. OR 조건 (일부 경우)

```sql
-- ❌ 인덱스 효율 떨어짐
SELECT * FROM employees 
WHERE name = '홍길동' OR email = 'hong@example.com';

-- ✅ UNION으로 대체 (각각 인덱스 사용)
SELECT * FROM employees WHERE name = '홍길동'
UNION
SELECT * FROM employees WHERE email = 'hong@example.com';
```

### 6. 데이터 타입 불일치

```sql
-- ❌ 인덱스 사용 불가
CREATE INDEX idx_phone ON users(phone);  -- VARCHAR 타입

SELECT * FROM users WHERE phone = 01012345678;
-- 숫자를 문자와 비교 → 암시적 형변환 → 인덱스 무용지물

-- ✅ 인덱스 사용 O
SELECT * FROM users WHERE phone = '01012345678';
```

---

## 🔍 인덱스 확인 방법

### 1. 테이블의 인덱스 확인

```sql
-- MySQL
SHOW INDEX FROM employees;

-- 결과
Table      | Key_name        | Column_name | Index_type
-----------|-----------------|-------------|------------
employees  | PRIMARY         | id          | BTREE
employees  | idx_department  | department  | BTREE
employees  | idx_email       | email       | BTREE
```

### 2. 실행 계획 확인 (EXPLAIN)

```sql
EXPLAIN SELECT * FROM employees WHERE department = 'IT';
```

**주요 컬럼 해석:**

```
id | select_type | table     | type  | key           | rows | Extra
---|-------------|-----------|-------|---------------|------|-------
1  | SIMPLE      | employees | ref   | idx_department| 25   | NULL
```

**type 컬럼 (성능 순서):**
- `system` > `const` > `eq_ref` > `ref` > `range` > `index` > `ALL`

```
✅ 좋은 성능:
- const: PRIMARY KEY나 UNIQUE로 1건 조회
- eq_ref: JOIN에서 PRIMARY/UNIQUE로 매칭
- ref: 일반 인덱스 사용

⚠️ 주의 필요:
- range: 범위 검색 (BETWEEN, >, <)
- index: 인덱스 전체 스캔

❌ 나쁜 성능:
- ALL: 테이블 전체 스캔 (Full Scan)
```

**key 컬럼:**
```
key = idx_department  → 인덱스 사용 ✅
key = NULL           → 인덱스 미사용 ❌
```

**rows 컬럼:**
```
rows = 1        → 매우 효율적 ✅
rows = 100      → 적당함
rows = 10,000   → 비효율적 ❌
```

**Extra 컬럼:**
```
Using index        → 커버링 인덱스 (최고 성능) ✅
Using where        → WHERE 조건 필터링
Using filesort     → 정렬 필요 (느림) ⚠️
Using temporary    → 임시 테이블 사용 (느림) ⚠️
```

---

## 💡 인덱스 최적화 팁

### 1. 커버링 인덱스 (Covering Index)

쿼리에 필요한 모든 컬럼이 인덱스에 포함된 경우

```sql
-- 복합 인덱스 생성
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- 커버링 인덱스 활용
SELECT department, salary 
FROM employees 
WHERE department = 'IT';
-- 테이블 접근 없이 인덱스만으로 조회 (최고 성능!)

-- EXPLAIN 결과: Extra = "Using index"
```

### 2. 선택도 높은 컬럼을 앞에

```sql
-- ❌ 비효율
CREATE INDEX idx_gender_email ON users(gender, email);
-- gender는 선택도 낮음 (M/F 2개)

-- ✅ 효율적
CREATE INDEX idx_email_gender ON users(email, gender);
-- email은 선택도 높음 (거의 유니크)
```

### 3. 인덱스 개수 제한

```sql
-- ❌ 과도한 인덱스
CREATE INDEX idx1 ON employees(name);
CREATE INDEX idx2 ON employees(email);
CREATE INDEX idx3 ON employees(phone);
CREATE INDEX idx4 ON employees(department);
CREATE INDEX idx5 ON employees(salary);
CREATE INDEX idx6 ON employees(hire_date);
-- INSERT/UPDATE 성능 급격히 저하

-- ✅ 필요한 것만 생성 (3~5개 권장)
```

### 4. 불필요한 인덱스 삭제

```sql
-- 사용하지 않는 인덱스 찾기 (MySQL)
SELECT * FROM sys.schema_unused_indexes;

-- 삭제
DROP INDEX idx_unused ON employees;
```

---

## 📊 실전 예제

### 예제 1: 복합 인덱스 활용

```sql
-- 자주 실행되는 쿼리
SELECT * FROM orders 
WHERE customer_id = 100 
AND order_date >= '2024-01-01'
ORDER BY order_date DESC;

-- 최적 인덱스
CREATE INDEX idx_customer_date 
ON orders(customer_id, order_date);
-- customer_id로 필터 → order_date로 정렬 (정렬 불필요)
```

### 예제 2: 페이징 최적화

```sql
-- 느린 페이징
SELECT * FROM posts 
ORDER BY created_at DESC 
LIMIT 10000, 10;  -- 10,000개 건너뛰고 10개 조회

-- 빠른 페이징 (커버링 인덱스)
SELECT * FROM posts p
JOIN (
    SELECT id FROM posts 
    ORDER BY created_at DESC 
    LIMIT 10000, 10
) t ON p.id = t.id;
```

### 예제 3: 다중 조건 최적화

```sql
-- 자주 실행되는 쿼리
SELECT * FROM products 
WHERE category = 'Electronics' 
AND price BETWEEN 100000 AND 500000
AND stock > 0;

-- 최적 인덱스
CREATE INDEX idx_category_price_stock 
ON products(category, price, stock);
```

---

## 🎓 핵심 정리

### 인덱스 생성 체크리스트

```
✅ WHERE 절에 자주 사용되는가?
✅ JOIN 조건에 사용되는가?
✅ ORDER BY/GROUP BY에 사용되는가?
✅ 카디널리티가 높은가? (중복 값 적은가?)
✅ 데이터 변경이 적은가?
❌ 테이블이 너무 작은가? (100건 미만)
❌ 이미 비슷한 인덱스가 있는가?
```

### 성능 비교 요약

| 작업 | 인덱스 없음 | 인덱스 있음 |
|------|------------|------------|
| SELECT (검색) | 느림 O(N) | **빠름 O(log N)** ✅ |
| INSERT | 빠름 | 느림 ❌ |
| UPDATE (인덱스 컬럼) | 빠름 | 느림 ❌ |
| DELETE | 빠름 | 느림 ❌ |
| ORDER BY | 느림 (정렬 필요) | **빠름 (정렬 불필요)** ✅ |

---

**핵심:** 인덱스는 검색 성능 향상을 위한 도구이지만, 무분별하게 생성하면 오히려 성능 저하를 초래한다. **자주 조회하고, 카디널리티가 높으며, 변경이 적은 컬럼**에만 선택적으로 생성하기