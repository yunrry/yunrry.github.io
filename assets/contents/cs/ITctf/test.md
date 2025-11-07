# 소프트웨어 테스트

# 화이트박스 vs 블랙박스 테스트

## 블랙박스 테스트
- **내부 구조 모름**, 입출력만 검증
- 명세서 기반 테스트
- **종류**: 동등분할, 경계값 분석, 원인-결과 그래프, 오류 예측

## 화이트박스 테스트
- **내부 구조 알고** 검증
- 코드 기반 테스트
- **종류**: 구문 커버리지, 결정(분기) 커버리지, 조건 커버리지, 조건/결정 커버리지, 변경 조건/결정 커버리지, 다중 조건 커버리지

### 화이트박스 커버리지 구분

```c
if (A && B) {  // 결정문
    실행문;     // 참 경로
}
// 거짓 경로
```

**1. 구문(Statement) 커버리지**
- 모든 실행문을 최소 1번씩 수행
- 가장 약한 기준

**2. 결정(Decision/Branch) 커버리지**
- 각 분기의 참/거짓을 최소 1번씩 수행
- 조건문 전체 결과만 확인
- 프로그램에 있는 모든 결정 포인트 내의 전체 조건식이 적어도 한 번은 참과 거짓을 만족해야 한다

**3. 조건(Condition) 커버리지**
- 각 개별 조건(A, B)이 참/거짓을 최소 1번씩
- 조건 조합은 고려 안 함
- 프로그램에 있는 결정 포인트 내의 모든 개별 조건식이 적어도 한 번은 참과 거짓을 만족해야 한다

**4. 조건/결정(Condition/Decision) 커버리지**
- 조건 커버리지 + 결정 커버리지
- 프로그램에 있는 모든 결정 포인트 내의 전체 조건식이 적어도 한 번은 참과 거짓을 만족해야 한다
- 동시에 모든 개별 조건식도 적어도 한 번은 참과 거짓을 만족해야 한다

**5. 변경 조건/결정(MC/DC) 커버리지**
- 각 조건이 독립적으로 전체 결과에 영향
- 개별 조건식이 다른 개별 조건식의 영향을 받지 않고 전체 조건식의 결과에 독립적으로 영향을 주어야 한다
- 해당 개별 조건식이 전체 조건식의 결과에 영향을 주는 조건 조합을 찾아 테스트하는 방법이다
- 각 조건식이 전체 결과를 독립적으로 변경시킬 수 있음을 검증한다

**6. 다중 조건(Multiple Condition) 커버리지**
- 모든 조건 조합 테스트
- 가장 강한 기준
- 프로그램에 있는 결정 포인트 내의 모든 개별 조건식의 가능한 조합을 100% 테스트해야 한다

### 예시

```c
if (A || B) {
    printf("True");
}
```

| 테스트 | A | B | 결과 |
|--------|---|---|------|
| TC1 | T | T | T |
| TC2 | T | F | T |
| TC3 | F | T | T |
| TC4 | F | F | F |

- **결정 커버리지**: TC1, TC4 (참 1번, 거짓 1번)
- **조건 커버리지**: TC1, TC4 (A와 B 각각 T/F)
- **다중 조건 커버리지**: TC1~TC4 전부

---

# 예상 문제

## 문제 1
소프트웨어의 내부 구조를 모르는 상태에서 기능 명세를 기반으로 수행하는 테스트 기법은?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 블랙박스 테스트

</div>
</details>

## 문제 2
다음 중 블랙박스 테스트 기법이 아닌 것은?

1. 동등분할
2. 경계값 분석
3. 결정 커버리지
4. 원인-결과 그래프

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 3번 (결정 커버리지는 화이트박스 테스트)

</div>
</details>

## 문제 3
프로그램 내의 모든 명령문을 최소한 한 번 이상 수행하는 커버리지는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 구문(Statement) 커버리지

</div>
</details>

## 문제 4
다음 코드에서 결정(분기) 커버리지 100%를 달성하기 위한 최소 테스트 케이스 개수는?

```c
if (x > 0 && y < 10) {
    z = 1;
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 2개
> 
> - TC1: 참 (예: x=5, y=5)
> - TC2: 거짓 (예: x=-1, y=0)

</div>
</details>

## 문제 5
다음 코드에서 조건 커버리지 100%를 달성했지만 결정 커버리지는 100%가 아닌 테스트 케이스 조합은?

```c
if (A || B) {
    printf("True");
}
```

1. (T, T), (F, F)
2. (T, F), (F, T)
3. (T, T), (T, F)
4. (F, F), (T, T)

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 3번
> 
> - A: T(2번), F(0번) → 조건 커버 안 됨
> 
> 정답은 **없음** (문제 오류)
> 
> 올바른 답: **(T, F), (F, T)**
> - 조건: A(T,F), B(F,T) 모두 만족
> - 결정: 둘 다 True → 거짓 경로 미수행

</div>
</details>

## 문제 6
각 조건이 독립적으로 전체 결과에 영향을 주는지 확인하는 커버리지는?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> MC/DC (Modified Condition/Decision Coverage, 변경 조건/결정 커버리지)

</div>
</details>

## 문제 7
다음 코드에서 다중 조건 커버리지 100%를 위한 테스트 케이스 개수는?

```c
if (A && B && C) {
    x = 1;
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 8개
> 
> 3개 조건의 모든 조합: 2³ = 8
> - (T,T,T), (T,T,F), (T,F,T), (T,F,F)
> - (F,T,T), (F,T,F), (F,F,T), (F,F,F)

</div>
</details>

## 문제 8
화이트박스 테스트 커버리지 중 가장 강력한(엄격한) 기준은?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 다중 조건(Multiple Condition) 커버리지
> 
> **강도 순서:**
> 구문 < 결정 < 조건 < 조건/결정 < MC/DC < 다중 조건

</div>
</details>

## 문제 9
입력 값의 범위를 유사한 특성을 갖는 그룹으로 나누어 각 그룹에서 대표값을 선정하는 블랙박스 테스트 기법은?

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 동등분할(Equivalence Partitioning) 기법

</div>
</details>

## 문제 10
다음 코드의 결정 커버리지와 조건 커버리지를 모두 만족하는 최소 테스트 케이스는?

```c
if (x < 5 || y > 10) {
    z = x + y;
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 2개
> 
> - TC1: x=3, y=8 → (T, F) → 전체 True
> - TC2: x=7, y=15 → (F, T) → 전체 True
> 
> 또는
> 
> - TC1: x=3, y=15 → (T, T) → 전체 True
> - TC2: x=7, y=8 → (F, F) → 전체 False
> 
> 조건: x<5 (T,F), y>10 (T,F)
> 결정: 전체 결과 (T, F)

</div>
</details>