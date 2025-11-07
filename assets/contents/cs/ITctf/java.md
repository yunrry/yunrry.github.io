# JAVA



## 자바 다형성(Polymorphism)과 변수 은닉(Variable Hiding)

[24년 3회 14번]
```java
public class Main{
    public static void main (String[] args){
        B a = new D();
        D b = new D();
        System.out.print(a.getX() + a.X + b.getX() + b.X);
    }
}

class B{
    int x = 3;
    int getX(){
        return x * 2;
    }
}

class D extends B{
    int x = 7;
    int getX(){
        return x * 3;
    }
}
```

### 실행 과정

**변수 및 객체 상태**

```java
B a = new D();  // 참조 타입: B, 실제 객체: D
D b = new D();  // 참조 타입: D, 실제 객체: D
```

| 표현식 | 값 | 설명 |
|--------|----|----|
| `a.getX()` | 21 | D의 메서드 호출 (7*3) - 오버라이딩 |
| `a.X` | 3 | B의 변수 참조 - 변수 은닉 |
| `b.getX()` | 21 | D의 메서드 호출 (7*3) |
| `b.X` | 7 | D의 변수 참조 |

**출력: 21 + 3 + 21 + 7 = 52**

### 핵심 개념

### 1. 메서드 오버라이딩(Method Overriding)
- **런타임 다형성(Runtime Polymorphism)**
- **실제 객체 타입**의 메서드 실행
- `B a = new D()` → D의 `getX()` 호출

### 2. 변수 은닉(Variable Hiding)
- **컴파일 타임 결정**
- **참조 타입**의 변수 사용
- `B a = new D()` → B의 `x` 참조

### 3. 동적 바인딩 vs 정적 바인딩
- **메서드**: 동적 바인딩(Dynamic Binding) - 실행 시점 결정
- **변수**: 정적 바인딩(Static Binding) - 컴파일 시점 결정

## 주의사항

1. 변수는 오버라이딩 안 됨, 은닉만 됨
2. 참조 타입에 따라 접근 가능한 멤버 결정
3. `instanceof` 확인 필요 시 사용

---

## 연습 문제

### 문제 1

```java
public class Main{
    public static void main(String[] args){
        A x = new C();
        C y = new C();
        System.out.print(x.getValue() + x.num + y.getValue() + y.num);
    }
}

class A{
    int num = 5;
    int getValue(){
        return num + 10;
    }
}

class C extends A{
    int num = 8;
    int getValue(){
        return num + 20;
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 69
> 
> - `x.getValue()`: 28 (C의 메서드, 8+20)
> - `x.num`: 5 (A의 변수)
> - `y.getValue()`: 28 (C의 메서드, 8+20)
> - `y.num`: 8 (C의 변수)
> - 합계: 28 + 5 + 28 + 8 = 69

</div>
</details>

### 문제 2

```java
public class Main{
    public static void main(String[] args){
        Parent p = new Child();
        Child c = new Child();
        System.out.print(p.calc() + p.value + c.calc() + c.value);
    }
}

class Parent{
    int value = 2;
    int calc(){
        return value * 5;
    }
}

class Child extends Parent{
    int value = 4;
    int calc(){
        return value * 3;
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 30
> 
> - `p.calc()`: 12 (Child의 메서드, 4*3)
> - `p.value`: 2 (Parent의 변수)
> - `c.calc()`: 12 (Child의 메서드, 4*3)
> - `c.value`: 4 (Child의 변수)
> - 합계: 12 + 2 + 12 + 4 = 30

</div>
</details>

### 문제 3

```java
public class Main{
    public static void main(String[] args){
        Super s = new Sub();
        System.out.print(s.method() + s.x);
    }
}

class Super{
    int x = 10;
    int method(){
        return x;
    }
}

class Sub extends Super{
    int x = 20;
    int method(){
        return x;
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 30
> 
> - `s.method()`: 20 (Sub의 메서드, Sub.x=20 사용)
> - `s.x`: 10 (Super의 변수)
> - 합계: 20 + 10 = 30

</div>
</details>


## 제네릭(Generic) 타입 소거(Type Erasure)

[24년 3회 18번]
```java
class Printer {
    void print(Integer a){
        System.out.print("A" + a);
    }

    void print(Object a){
        System.out.print("B" + a);
    }

    void print(Number a){
        System.out.print("C" + a);
    }
}
public class Main{
    public static void main(String[] args){
        new Collection<>(0).print();
    }

    public static class Collection<T>{
        T value;
        public Collection(T t){
            value = t;
        }
        public void print(){
            new Printer().print(value);
        }
    }
}

```




### 문제 코드 분석

```java
new Collection<>(0)  // 타입 추론: Collection<Integer>
```

**컴파일 시 타입 소거 발생**
- `T value` → `Object value`
- `print(value)` → `print(Object)`
- **출력: B0**

### 핵심 개념

### 1. 타입 소거(Type Erasure)
- 컴파일 후 제네릭 타입 정보 삭제
- 런타임에는 `Object`로 처리
- 하위 호환성(Backward Compatibility) 유지

### 2. 메서드 오버로딩 해결 순서
1. **정확한 타입 매칭**
2. **박싱/언박싱(Boxing/Unboxing)**
3. **부모 타입으로 확장**

### 3. 상속 관계
```
Object (최상위)
  ↑
Number
  ↑
Integer
```

### 실행 과정

| 단계 | 타입 | 선택 메서드 |
|------|------|------------|
| 컴파일 전 | `T` (Integer) | - |
| 타입 소거 | `Object` | `print(Object)` |
| 런타임 | `Object` | B 출력 |

### 해결 방법

### 방법 1: 제네릭 경계 지정
```java
public static class Collection<T extends Number>{
    // T는 Number로 제한
    // 타입 소거 시 Object가 아닌 Number로 변환
}
```

### 방법 2: 명시적 캐스팅
```java
public void print(){
    if(value instanceof Integer){
        new Printer().print((Integer)value);
    }
}
```

### 방법 3: 타입 토큰(Type Token) 사용
```java
public static class Collection<T>{
    T value;
    Class<T> type;
    public Collection(T t, Class<T> clazz){
        value = t;
        type = clazz;
    }
}
```

---

# 연습 문제

## 문제 1

```java
class Processor {
    void process(String s){
        System.out.print("A");
    }
    void process(Object o){
        System.out.print("B");
    }
}

public class Main{
    public static void main(String[] args){
        new Box<>("Hello").run();
    }
    
    public static class Box<T>{
        T item;
        public Box(T t){
            item = t;
        }
        public void run(){
            new Processor().process(item);
        }
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> B
> 
> **이유:**
> - `T item` → 타입 소거 → `Object item`
> - `process(item)` → `process(Object)` 호출

</div>
</details>

## 문제 2

```java
class Handler {
    void handle(Integer i){
        System.out.print("X");
    }
    void handle(Number n){
        System.out.print("Y");
    }
    void handle(Object o){
        System.out.print("Z");
    }
}

public class Main{
    public static void main(String[] args){
        new Container<Integer>(10).execute();
    }
    
    public static class Container<T extends Number>{
        T data;
        public Container(T t){
            data = t;
        }
        public void execute(){
            new Handler().handle(data);
        }
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> Y
> 
> **이유:**
> - `<T extends Number>` → 타입 소거 시 `Number`로 변환
> - `handle(Number)` 호출

</div>
</details>

## 문제 3

```java
class Executor {
    void exec(Double d){
        System.out.print("1");
    }
    void exec(Number n){
        System.out.print("2");
    }
    void exec(Object o){
        System.out.print("3");
    }
}

public class Main{
    public static void main(String[] args){
        Wrapper<Double> w1 = new Wrapper<>(5.5);
        Wrapper w2 = new Wrapper(5.5);
        w1.call();
        w2.call();
    }
    
    public static class Wrapper<T>{
        T val;
        public Wrapper(T t){
            val = t;
        }
        public void call(){
            new Executor().exec(val);
        }
    }
}
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>
<details class="answer-box">
<summary>정답</summary>
<div markdown="1">

> 33
> 
> **이유:**
> - `w1`: `T` → 타입 소거 → `Object`, `exec(Object)` 호출 → 3
> - `w2`: Raw Type 사용, 타입 소거 → `Object`, `exec(Object)` 호출 → 3
> - 제네릭 타입은 컴파일 후 소거되므로 런타임에 Double 정보 없음

</div>
</details>


```java
class Connection{
    private static Connection _inst =null;
    private int count = 0;
    private static Connection get(){
        if(_inst == null){
            _inst = new Connection();
            return _inst;
        }
        return _inst;
    }
    public void count(){count++;}
    public int getCount(){return count;}
}

public class Test{
    public static void main(String[] args[]){
        Connection conn1 = Connection.get();
        conn1.count();
        Connection conn2 = Connection.get();
        conn2.count();
        Connection conn3 = Connection.get();
        conn3.count();
        conn1.count();
        SYstem.out.print(conn1.getCount());
    }
}
```

### Singleton 패턴 문제 해석

**실행 과정**

```
conn1 = get()  → _inst 생성 (최초)
conn1.count()  → count = 1

conn2 = get()  → 기존 _inst 반환 (같은 객체)
conn2.count()  → count = 2

conn3 = get()  → 기존 _inst 반환 (같은 객체)
conn3.count()  → count = 3

conn1.count()  → count = 4 (conn1, conn2, conn3 모두 같은 객체)
```

**출력: 4**

### 핵심 포인트

1. **Singleton 패턴**: 인스턴스가 단 하나만 생성
2. **static 변수**: 클래스 레벨에서 공유
3. **동일 객체**: conn1, conn2, conn3는 모두 같은 인스턴스 참조
4. **count 누적**: 하나의 count 변수를 공유하므로 4까지 증가


### 인스턴스가 하나만 생성되는 이유

**실제로는 모두 같은 객체**

```
메모리 주소: 0x1000 (Connection 인스턴스)

conn1 → 0x1000
conn2 → 0x1000  
conn3 → 0x1000
```

### 공유 리소스

**클래스 레벨 (static)**
- `_inst`: 모든 get() 호출이 공유

**인스턴스 레벨**
- `count`: conn1, conn2, conn3가 같은 인스턴스를 가리키므로 동일한 count 변수 공유

**핵심**: 참조 변수는 3개지만 실제 객체는 1개

---
<br>

## new를 직접 사용하는 경우

```java
Connection conn1 = new Connection();  // 컴파일 에러
```

**불가능한 이유**: 생성자가 `private`이므로 클래스 외부에서 `new` 사용 불가

### 만약 생성자가 public이라면?

```java
Connection conn1 = new Connection();  // 0x1000
Connection conn2 = new Connection();  // 0x2000
Connection conn3 = new Connection();  // 0x3000
```

각각 **독립된 인스턴스** 생성:

| 동작 | conn1.count | conn2.count | conn3.count |
|------|-------------|-------------|-------------|
| conn1.count() | 1 | 0 | 0 |
| conn2.count() | 1 | 1 | 0 |
| conn3.count() | 1 | 1 | 1 |
| conn1.count() | 2 | 1 | 1 |

**conn1.getCount() = 2** (각자 독립적)

### Singleton 패턴은 `private` 생성자로 외부 생성을 막는다.