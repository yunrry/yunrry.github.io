# 조인(JOIN) 종류

## 조건 기준 분류

### 1. 동등 조인(Equi Join)
- `=` 연산자 사용
- 가장 일반적

```sql
SELECT * FROM A JOIN B ON A.id = B.id;
```

### 2. 비동등 조인(Non-Equi Join)
- `>, <, >=, <=, BETWEEN` 사용

```sql
SELECT * FROM 학생 JOIN 성적등급 
ON 학생.점수 BETWEEN 성적등급.최소 AND 성적등급.최대;
```

### 3. 세타 조인(Theta Join)
- 모든 비교 연산자 사용 가능 (=, >, <, >=, <=, !=)
- 동등 조인 + 비동등 조인 포함하는 상위 개념

### 4. 자연 조인(Natural Join)
- 같은 이름의 컬럼 자동 매칭
- 중복 컬럼 제거

```sql
SELECT * FROM A NATURAL JOIN B;
```

## 결과 범위 분류

- **INNER JOIN**: 교집합
- **LEFT OUTER JOIN**: 왼쪽 전체
- **RIGHT OUTER JOIN**: 오른쪽 전체
- **FULL OUTER JOIN**: 합집합
- **CROSS JOIN**: 카티션 곱
- **SELF JOIN**: 자기 자신

## 암기 구조

```
세타 조인 (상위 개념)
├─ 동등 조인 (=)
│  └─ 자연 조인 (자동 매칭)
└─ 비동등 조인 (>, <, >=, <=)
```

**핵심**: 세타 > 동등/비동등, 자연은 동등의 특수 케이스