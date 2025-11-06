<script>
(function(){
  function handleSubmit(e){
    e.preventDefault();
    const form = e.currentTarget;
    const details = form.nextElementSibling;
    if (details && details.tagName === 'DETAILS') details.open = true;
  }
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('form.inline-answer').forEach(f=>{
      f.addEventListener('submit', handleSubmit);
      const btn = f.querySelector('button[data-action="show"]');
      const clr = f.querySelector('button[data-action="clear"]');
      if (btn) btn.addEventListener('click', ()=>f.dispatchEvent(new Event('submit')));
      if (clr) clr.addEventListener('click', ()=>{ f.querySelector('input').value=''; });
    });
  });
})();
</script>
<style>
.inline-answer{ margin:4px 0; display:flex; gap:2px; align-items:center; }
.inline-answer input{ padding:6px 10px; min-width:40px; max-width:400px;}
.inline-answer button{ padding:6px 10px; }
</style>

# 정보처리기사 키워드 130

**1. 시제품을 끊임없이 제작하며 사이클을 반복하는 개발방법론으로,<br/>워터폴과 대조적이며, 소프트웨어 개발을 넘어 기업 경영 전반에서 사용되고 있다. <br/>고객의 변화하는 요구사항과 환경 변화에 능동적인 이 소프트웨어 개발 방법론을 쓰시오.**
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 애자일 
</div>
</details>

<br/> <br/>
___   
**2. 소프트웨어 공학에서 리팩토링을 하는 목적에 대해 간략히 서술하시오**
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 리팩토링의 목적은 프로그램을 쉽게 이해하고 수정하여 빠르게 개발 할 수 있도록 하기 위함이다.
</div>
</details>

___   
<br/> <br/>

**3. 요구사항 확인에 대한 다음 설명에서 괄호 1, 2 에 들어갈 알맞은 용어를 쓰시오** 
- (1) 요구사항은 시스템이 무엇을 하는지, 어떤 기능을 하는지 등 사용자가 시스템을 통해 제공받기를 원하는   
기능이나 시스템이 반드시 수행해야 하는 기능을 의미한다. 
- (2) 요구사항은 품질이나 제약사항과 관련된 요구사항으로, 시스템의 장비 구성, 성능 인터페이스, 테스트,  
보안 등의 요구사항을 말한다.
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1) : 기능, (2): 비기능
</div>
</details>

___   
<br/> <br/>

**4. UML(Unified Modeling Language)에 관한 다음 설명에서 괄호에 공통으로<br> 들어갈 알맞은 용어를 쓰시오.**
( )다이어그램은 UML 다이어그램 중 객체(Object)들을 (  )로 추상화하여 표현하는 다이어그램으로  
대표적인 구조적 다이어그램이다. (  )는 각각의 객체들이 갖는 속성과 메소드를 표현한 것으로 3개의  
구획으로 나눠 이름, 속성, 메소드를 표기한다. 
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 클래스
</div>
</details>
<br/> <br/>

___   
**5. UML에 대한 다음 설명에서 괄호(1)~(3)에 들어갈 알맞은 용어를 쓰시오.**
```
UML은 시스템 분석, 설계, 구현 등 시스템 개발 과정에서 시스템 개발자와 고객 또는 개발자 상호 간의  
 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어로, 사물, (1),  
다이어그램으로 이루어져 있다.  
- ( 1 )는 사물과 사물 사이의 연관성을 표현하는 것으로, 연관, 집합, 포함, 일반화 등 다양한 형태의 
( 1 ) 가 존재한다.
-  ( 2 )는 UML에 표현되는 사물의 하나로, 객체가 갖는 속성과 동작을 표현한다. 일반적으로  
 직사각형으로 표현하며, 직사각형 안에 이름, 속성, 동작을 표기한다.
-  ( 3 )는 ( 2 )와 같은 UML에 표현되는 사물의 하나로, ( 2 )나 컴포넌트의 동작을 모아놓은   
것이며, 외부적으로 가시화되는 행동을 표현한다. 단독으로 사용하는 경우는 없으며 ( 3 )구현을 위한   
( 2 )또는 컴포넌트와 함께 사용된다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1): 관계, (2): 클래스, (3): 인터페이스
</div>
</details>
<br/> <br/>

___   

**6. UML의 관계(Relationships)에 관한 다음 설명에서 각 번호 1, 2 에 들어갈<br>알맞은 용어를 찾아 쓰시오.**
```
관계(Relationships)는 사물과 사물 사이의 연관성을 표현하는 것이다.
(1) - 하나의 사물이 다른 사물에 포함되어 있는 관계로, 전체와 부분으로 구분되어지며 서로 독립적이다.
(2) - 상위 모듈이 하위 모듈보다 더 일반적인 개념을 가지고 있으며, 하위 모듈이 상위 모듈보다 더  
    구체적인 개념을 가진다.
```
<보기>
```
- Association   - Aggregation   - Composition   - Generalization 
- Dependency    - Realization
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1):Aggregation(집합-약한결합)  (2):Generalization
</div>
</details>
<br/> <br/>

___   
**7. UML을 이용한 다이어그램 중 다음 그림에 해당하는 다이어그램을 쓰시오**

![ITexam-7](/assets/images/ITexam-7.png)
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 패키지 다이어그램
</div>
</details>
<br/> <br/>
___   

**8. LOC 기법에 의하여 예측된 총 라인 수가 30,000라인, 개발에 참여할 프로그래머가 5명<br>프로그래머들의 평균 생산성이 월간 300라인일 때 개발에 소요되는 기간을 계산식과 함께 쓰시오 **
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 30000/(5*300) = 20개월 
</div>
</details>
<br/> <br/>
___   

**9. 데이터베이스 스키마(Schema)에 대해 간략히 서술하시오**
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 스키마는 데이터베이스의 구조와 제약 조건에 관한 전반적인 명세를 기술한 것이다. 
</div>
</details>
<br/> <br/>
___   

**10. 데이터베이스 설계에 대한 다음 설명에서 괄호(1~3)에 들어갈 알맞은 용어를 쓰시오.**
```
1. ( 1 ): 논리적 구조로 표현된 데이터를 디스크 등의 저장장치에 저장할 수 있는 데이터로
변환하는 과정으로, 파일의 저장 구조 및 액세스 경로를 결정하며, 테이블 정의서 및 명세서가 산출된다.
2. ( 2 ): 현실 세계에 대한 인식을 추상적 개념으로 표현하는 과정으로, 개념 스키마 모델링과
트랜잭션 모델링을 수행하며, 요구 조건 명세를 E-R 다이어그램으로 작성한다.
3. ( 3 ): 현실의 자료를 특정 DBMS가 지원하는 자료구조로 변환하는 과정으로, 트랜잭션의 인터페이스를 
설계하고, 정규화를 통해 스키마를 평가 및 정제한다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1):물리적 설계, (2):개념적 설계, (3):논리적 설계
</div>
</details>
<br/> <br/>
___   


**11. 다음은 데이터베이스 구축까지의 과정을 나열한 것이다. 괄호에 들어갈 알맞은 용어를 쓰시오.**
![ITexam-7](/assets/images/ITexam-11.png)
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 개념적 설계, 논리적 설계, 물리적 설계
</div>
</details>
<br/> <br/>
___   

**12. 데이터 모델의 구성 요소에 대한 다음 설명에서 괄호 (1, 2)에 들어갈 알맞은 용어를 쓰시오.**
```
1.( 1 )은 데이터베이스에 저장된 실제 데이터를 처리하는 작업에 대한 명세로서 데이터베이스를
조작하는 기본 도구에 해당한다.
2.( 2 )는 논리적으로 표현된 객체 타입들 간의 관계로서 데이터의 구성 및 정적 성질을 표현한다.
3. 제약 조건은 데이터베이스에 저장될 수 있는 실제 데이터의 논리적인 제약 조건을 의미한다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 연산(Operation), 구조(Structure)
</div>
</details>
<br/> <br/>
___   


**13. 다음 테이블에서 카디널리티(Cardinality)와 디그리(Degree)를 구하시오.**
| ID | 이름 | 거주지 | 신청강의 |
|---|---|---|---|
| 435345 | 백영헌 | 마포구 | E01 |
| 526524 | 차수인| 관악구 | S03 |
| 453252| 허채빈 |  서대문구| E02 |
| 636346 | 윤지호 |  광진구| S03 |
| 574ㅈ53 | 배서희 | 서대문구 | E02 |

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 5, 4
</div>
</details>
<br/> <br/>

'#카디널리티' '#Table'

___   

**14. 다음 E-R 다이어그램을 참고하여 괄호(1~5)의 설명의 적합한 요소를 찾아 기호(ㄱ~ㅁ)으로 쓰시오.**

![ITexam-7](/assets/images/ITexam-14.png)

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1):ㄴ (2):ㄷ (3):ㄱ (4):ㄹ (5):ㅁ
</div>
</details>
<br/> <br/>

'#E-R'

___   


**15. 키(Key)에 대한 다음 설명에서 괄호(1,2)에 들어갈 알맞은 용어를 쓰시오**
```
키(Key)는 데이터베이스에서 조건에 만족하는 튜플을 찾거나 순서대로 정렬할 떄 기준이 되는 속성을
말한다.
- 슈퍼키(Super Key)는 한 릴레이션 내에 있는 속성들의 집합으로 구성된 키로, 릴레이션을 구성하는
모든 튜플에 대해 ( 1 )을 만족한다.
- 후보키(Candidate Key)는 릴레이션을 구성하는 속성들 중에서 튜플을 유일하게 식별하기 위해 사용
되는 속성들의 부분집합으로, ( 1 )과( 2 )을 만족하는 특징이 있다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1):유일성 (2):최소성
</div>
</details>
<br/> <br/>

'#슈퍼키' '#후보키'

___   


**16. 관계대수에 대한 다음 설명에서 괄호(1~5)에 들어갈 알맞은 용어를 쓰시오.**
```
관계대수는 관계형 데이터베이스에서 원하는 정보와 그 정보를 검색하기 위해서 어떻게 유도하는가를
기술하는 절차적인 언어이다. 관계대수에 사용되는 연산은 다음과 같다.
- 합집합(UNION)은 두 릴레이션에 존재하는 튜플의 합집합을 구하되, 결과로 생성된 릴레이션에서
중복되는 튜플은 제거되는 연산으로, 사용하는 기호는 ( 1 )이다.
- 차집합(DIFFERENCE)은 두 릴레이션에 존재하는 튜플의 차집합을 구하는 연산으로, 사용하는 기호는
( 2 )이다.
- 교차곱(CARTESIAN PRODUCT)은 두 릴레이션에 있는 튜플들의 순서쌍을 구하는 연산으로, 사용하는
기호는 ( 3 )이다.
- 프로젝트(PROJECT)는 주어진 릴레이션에서 속성 리스트(Attribut List)에 제시된 속성 값만을
추출하여 새로운 릴레이션을 만드는 연산으로, 사용하는 기호는 ( 4 )이다.
- 조인(JOIN)은 공통 속성을 중심으로 두 개의 릴레이션을 하나로 합쳐서 새로운 릴레이션을 만드는 
연산으로, 사용하는 기호는 ( 5 )이다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1):∪ (2):ㅡ (3):X (4):π (5):⋈
</div>
</details>
<br/> <br/>

'#관계대수'

___   

**17. 다음이 설명하고 있는 관계대수 연산자의 기호를 쓰시오.**
```
릴레이션 A, B가 있을 때 릴레이션 B의 조건에 맞는 것들만 릴레이션 A에서 분리하여 프로젝션을
하는 연산이다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> ÷ 디비전(division)
</div>
</details>
<br/> <br/>

'#관계대수'

___   


**18. 데이터베이스에 대한 다음 설명에서 괄호에 들어갈 알맞은 용어를 쓰시오.**
```
- ( )은 관계 데이터의 연산을 표현하는 방법으로, 관계 데이터 모델의 제안자인 코드(E. F. Codd)가
수학의 술어 해석(Predicate Calculus)에 기반을 두고 관계 데이터베이스를 위해 제안했다.
- 원하는 정보가 무엇이라는 것만 정의하는 비절차적 특성을 지니며, 원하는 정보를 정의할 때 계산 
수식을 사용한다.
- 튜플 해석식을 사용하는 튜플( )과 도메인 해석식을 사용하는 도메인 ( )으로 구분된다.
```
<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 관계해석 (Relational Calculus)
</div>
</details>
<br/> <br/>


___   


**19. 데이터의 중복으로 인해 테이블 조작 시 문제가 발생하는 현상을 이상(Anomaly)이라고 한다.<br>이상 중 삭제이상(Deletion Anomaly)에 대해 간략히 서술하시오.**

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 테이블에서 튜플을 삭제할 때 의도와는 상관없는 값들도 함께 삭제되는 현상이다.
</div>
</details>
<br/> <br/>


___   

**19. 데이터베이스의 이상(Anomaly)의 종류 3가지를 쓰시오.**

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> 삽입 이상, 갱신 이상, 삭제 이상
</div>
</details>
<br/> <br/>


___   

**21. 함수적 종속(Functional Dependency)에 대한 다음 설명에서 괄호(1~3)에 들어갈 알맞은<br>용어를 <보기>에서 찾아 기호(ㄱ~ㅁ)로 쓰시오 (단, 테이블 <R>의 속성 '학생'과 '학과'의 밑줄은 키(Key)임을 <br>의미한다.)**
| 학생 | 학과 | 성적 | 학년 |
|---|---|---|---|
| 이순신 | 컴퓨터공학 | A+ | 2 |
| 이순신 | 전기공학| B | 2 |
| 유관순| 경제학 |  B+| 1 |
| 강감찬 | 문예창작 |  C| 3 |
| 강감찬 | 한국사 | C+ | 3 |
| 홍길동 | 영문학 | B | 4 |
```
- 테이블 <R>에서 '성적'은 기본키인 {학생, 학과}에 대해 ( 1 ) Functional Dependency이다.
- 테이블 <R>에서 '학년'은 기본키인 {학생, 학과}중 '학생'만으로 식별이 가능하므로 기본키에 대해
( 2 ) Functional Dependency이다.
- 임의의 테이블에 속성 A, B, C가 있을 때, A -> B이고, B -> C일 때, A -> C인 관계는 ( 3 )
Functional Dependency이다.
```
<보기>
```
ㄱ. Hybrid      ㄴ. Multi Valued        ㄷ. Transitive       ㄹ. Full
ㅁ. Defined     ㅂ. Natural             ㅅ. Relational       ㅇ. Partial
```

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />

</form>
<details>
<summary>정답</summary>
<div markdown="1">

> (1): ㄹ  (2): ㅇ  (3): ㄷ
</div>
</details>
<br/> <br/>

'#함수적종속' '#FunctionalDependency'

___   