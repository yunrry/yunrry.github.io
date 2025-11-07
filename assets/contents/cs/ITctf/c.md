# C언어

[24년 3회 문제6]
```C
#include <stdio.h>
int func() {
    static int x =0;
    x += 2;
    return x;
}

int main(){
    int x = 0;
    int sum = 0;
    for(int i =0; i<4; i++){
        x++;
        sum += func();
    }
    printf("%d", sum);
    return 0;
}
```

### x변수 구별과 상태 변화

### 변수 구분
1. **func() 내부의 static int x**: 함수가 끝나도 값 유지, 프로그램 종료까지 존재
2. **main() 내부의 int x**: main 함수 내에서만 존재하는 지역 변수  
이 둘은 **완전히 다른 변수**이다.
- main의 x: 반복문에서 1씩 증가만 하고 (1→2→3→4), 어디에도 사용되지 않음  
sum: 오직 func()의 반환값(static x)만 누적됨  
main의 x는 "함정 변수"로, 실제 계산과 무관.


### 실행 과정

| 반복 | main의 x | func()의 static x | func() 반환값 | sum |
|------|----------|-------------------|---------------|-----|
| 초기 | 0 | 0 | - | 0 |
| i=0 | 1 | 2 | 2 | 2 |
| i=1 | 2 | 4 | 4 | 6 |
| i=2 | 3 | 6 | 6 | 12 |
| i=3 | 4 | 8 | 8 | 20 |

**출력: 20**

핵심: static 변수는 함수 호출 간 값이 누적됨

---

## 연습 문제

### 문제 1

```c
#include <stdio.h>
int func() {
    static int a = 1;
    a *= 2;
    return a;
}

int main(){
    int a = 5;
    int result = 0;
    for(int i = 0; i < 3; i++){
        a--;
        result += func();
    }
    printf("%d", result);
    return 0;
}
```


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 14
> 
> **과정:**
> - i=0: func()의 static a = 2, result = 2, main의 a = 4
> - i=1: func()의 static a = 4, result = 6, main의 a = 3
> - i=2: func()의 static a = 8, result = 14, main의 a = 2

</div>
</details>


## 문제 2

```c
#include <stdio.h>
int func() {
    static int count = 0;
    count += 3;
    return count;
}

int main(){
    int count = 10;
    int total = 0;
    for(int i = 0; i < 5; i++){
        count -= 2;
        if(i % 2 == 0){
            total += func();
        }
    }
    printf("%d", total);
    return 0;
}
```


<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 18
> 
> **과정:**
> - i=0 (짝수): func() 호출, static count = 3, total = 3
> - i=1 (홀수): func() 호출 안 함
> - i=2 (짝수): func() 호출, static count = 6, total = 9
> - i=3 (홀수): func() 호출 안 함
> - i=4 (짝수): func() 호출, static count = 9, total = 18

</div>
</details>




## 포인터(Pointer) 연산자 정리

### 기본 개념

**변수(Variable)**: 값을 저장하는 메모리 공간
**주소(Address)**: 메모리 공간의 위치
**포인터(Pointer)**: 주소를 저장하는 변수

### 연산자 3가지

### 1. `&` (주소 연산자, Address Operator)
- **의미**: "~의 주소"
- **사용**: 변수의 메모리 주소를 가져옴

```c
int x = 10;
int *p = &x;  // x의 주소를 p에 저장
```

### 2. `*` (간접 참조 연산자, Dereference Operator)
- **의미**: "~가 가리키는 곳의 값"
- **사용**: 포인터가 가리키는 주소의 실제 값에 접근

```c
int x = 10;
int *p = &x;
printf("%d", *p);  // 10 출력 (p가 가리키는 x의 값)
```

### 3. `**` (이중 포인터, Double Pointer)
- **의미**: "포인터를 가리키는 포인터"
- **사용**: 포인터의 주소를 저장

```c
int x = 10;
int *p = &x;      // x의 주소
int **pp = &p;    // p의 주소
```

### 핵심 구분

```c
int x = 10;
int *p = &x;
int **pp = &p;
```

| 표현 | 의미 | 값 |
|------|------|-----|
| `x` | x의 값 | 10 |
| `&x` | x의 주소 | 0x1000 (예시) |
| `p` | p의 값 (x의 주소) | 0x1000 |
| `*p` | p가 가리키는 값 | 10 |
| `&p` | p의 주소 | 0x2000 (예시) |
| `pp` | pp의 값 (p의 주소) | 0x2000 |
| `*pp` | pp가 가리키는 값 (p의 값) | 0x1000 |
| `**pp` | pp가 가리키는 포인터가 가리키는 값 | 10 |

### 시각적 이해

```
메모리 주소    변수    값
0x1000       x       10
0x2000       p       0x1000  (x의 주소를 가리킴)
0x3000       pp      0x2000  (p의 주소를 가리킴)

x    = 10
*p   = 10  (p가 가리키는 곳 = x)
**pp = 10  (pp가 가리키는 p가 가리키는 곳 = x)
```

### 선언 vs 사용

```c
// 선언할 때 *
int *p;      // p는 int를 가리키는 포인터
int **pp;    // pp는 int*를 가리키는 포인터

// 사용할 때 *
*p = 20;     // p가 가리키는 곳에 20 대입
**pp = 30;   // pp가 가리키는 포인터가 가리키는 곳에 30 대입
```

### 예제 문제

```c
#include <stdio.h>
int main() {
    int a = 5;
    int *p = &a;
    int **pp = &p;
    
    *p = 10;
    printf("%d\n", a);      // ?
    printf("%d\n", *p);     // ?
    printf("%d\n", **pp);   // ?
    
    **pp = 20;
    printf("%d", a);        // ?
    return 0;
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 10
> 10
> 10
> 20
> 
> **해설:**
> - `*p = 10`: p가 가리키는 a를 10으로 변경
> - `a`, `*p`, `**pp` 모두 같은 메모리(a)를 참조
> - `**pp = 20`: pp→p→a 순서로 접근하여 a를 20으로 변경

</div>
</details>



```c
#include <stdio.h>
void func(int** arr, int size){
    for (int i =0; i< size; i++){
        *(*arr + i) = (*(*arr + i) + i) % size;
    }
}

int main(){
    int arr[] = {3, 1, 4, 1, 5}
    int* p = arr;
    int** pp = &p;
    int num = 6;
    func(pp, 5);
    num = arr[2];
    printf("%d", num);
    return 0;
}
```

### 초기 상태
```c
arr[] = {3, 1, 4, 1, 5}
p = arr (배열 시작 주소)
pp = &p (p의 주소)
```

### 포인터 표기법 동치 관계

```c
int** arr  // 이중 포인터
*arr       // int* 타입 (배열 시작 주소)
*arr + i   // i번째 요소의 주소
*(*arr + i) // i번째 요소의 값
```

### 단계별 분석

```c
arr      // int** (포인터의 주소)
*arr     // int* (배열 시작 주소, &arr[0]과 같음)
*arr + i // &arr[i] (i번째 주소)
*(*arr + i) // arr[i] (i번째 값)
```

### 배열 포인터 규칙

- `arr[i]` = `*(arr + i)`
- `*arr`이 배열 시작 주소이므로
- `*(*arr + i)` = `*(배열시작 + i)` = `arr[i]`

**핵심:** `*arr`은 일반 포인터 `p`와 같고, `*(p + i)`는 `p[i]`이다.

### func() 실행 과정

`*(*arr + i)`는 `arr[i]`와 동일

| i | 원래 값 | 계산 | 결과 |
|---|---------|------|------|
| 0 | arr[0]=3 | (3+0)%5 | 3 |
| 1 | arr[1]=1 | (1+1)%5 | 2 |
| 2 | arr[2]=4 | (4+2)%5 | 1 |
| 3 | arr[3]=1 | (1+3)%5 | 4 |
| 4 | arr[4]=5 | (5+4)%5 | 4 |

### 최종
```c
arr[] = {3, 2, 1, 4, 4}
num = arr[2] = 1
```

**출력: 1**