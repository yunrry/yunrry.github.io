# UML(Unified Modeling Language) 용어 정리

## 1. 다이어그램 종류

### 구조 다이어그램(Structure Diagram)
- **클래스 다이어그램(Class Diagram)**: 클래스 구조와 관계
- **객체 다이어그램(Object Diagram)**: 특정 시점의 객체 인스턴스
- **컴포넌트 다이어그램(Component Diagram)**: 컴포넌트 구조
- **배치 다이어그램(Deployment Diagram)**: 하드웨어 배치
- **패키지 다이어그램(Package Diagram)**: 패키지 구조
- **복합체 구조 다이어그램(Composite Structure Diagram)**: 내부 구조

### 행위 다이어그램(Behavior Diagram)
- **유스케이스 다이어그램(Use Case Diagram)**: 기능 요구사항
- **시퀀스 다이어그램(Sequence Diagram)**: 시간 순서 상호작용
- **커뮤니케이션 다이어그램(Communication Diagram)**: 객체 간 메시지
- **상태 다이어그램(State Diagram)**: 객체 상태 변화
- **활동 다이어그램(Activity Diagram)**: 업무 흐름
- **타이밍 다이어그램(Timing Diagram)**: 시간 제약

## 2. 클래스 다이어그램 관계

### 연관(Association)
- 기본 관계, 실선 `─`
- 방향성: `→` (단방향), `─` (양방향)
- 다중성(Multiplicity): `1`, `*`, `0..1`, `1..*`

### 집약(Aggregation) `◇─`
- 약한 소유, 빈 다이아몬드
- 부분이 독립적으로 존재 가능
- 예: 학교 ◇─ 학생

### 합성(Composition) `◆─`
- 강한 소유, 채운 다이아몬드
- 부분이 전체에 종속
- 예: 집 ◆─ 방

### 의존(Dependency) `- - ->`
- 일시적 관계, 점선 화살표
- 한 클래스가 다른 클래스를 사용
- 예: 메서드 파라미터, 지역변수

### 일반화(Generalization) `◁─`
- 상속 관계, 빈 삼각형
- 자식 → 부모
- IS-A 관계

### 실체화(Realization) `◁ - -`
- 인터페이스 구현, 점선 빈 삼각형
- 구현 클래스 → 인터페이스

## 3. 다중성(Multiplicity) 표기

| 표기 | 의미 |
|------|------|
| `1` | 정확히 1개 |
| `*` | 0개 이상 |
| `0..1` | 0개 또는 1개 |
| `1..*` | 1개 이상 |
| `n..m` | n개 이상 m개 이하 |

## 4. 클래스 표기법

```
┌─────────────────┐
│   클래스명       │  (클래스 이름)
├─────────────────┤
│ - 속성1: 타입   │  (속성/필드)
│ + 속성2: 타입   │
├─────────────────┤
│ + 메서드1()     │  (메서드/연산)
│ - 메서드2()     │
└─────────────────┘
```

**접근 제어자(Access Modifier)**:
- `+` Public
- `-` Private
- `#` Protected
- `~` Package

## 5. 유스케이스 다이어그램

### 액터(Actor)
- 시스템 외부 사용자/시스템
- 막대 인간 표시

### 유스케이스(Use Case)
- 시스템 기능
- 타원 표시

### 관계
- **포함(Include)** `<<include>>`: 필수적으로 포함
- **확장(Extend)** `<<extend>>`: 선택적으로 확장
- **일반화(Generalization)**: 액터/유스케이스 간 상속

## 6. 시퀀스 다이어그램

- **생명선(Lifeline)**: 객체의 존재 기간, 점선 `┆`
- **활성화(Activation)**: 실행 중인 상태, 직사각형 `▯`
- **메시지(Message)**: 
  - 동기(Synchronous): `→`
  - 비동기(Asynchronous): `⇢`
  - 반환(Return): `- - ->`

## 7. 상태 다이어그램

- **시작 상태(Initial State)**: 채운 원 `●`
- **종료 상태(Final State)**: 이중 원 `◉`
- **전이(Transition)**: 화살표 `→`
- **이벤트(Event)**: 전이를 일으키는 조건

## 8. 활동 다이어그램

- **시작 노드(Initial Node)**: `●`
- **종료 노드(Final Node)**: `◉`
- **액션(Action)**: 둥근 사각형
- **결정(Decision)**: `◇`
- **병합(Merge)**: `◇`
- **포크(Fork)**: 굵은 가로선 (병렬 시작)
- **조인(Join)**: 굵은 가로선 (병렬 종료)
- **스윔레인(Swimlane)**: 책임 영역 구분

## 9. 스테레오타입(Stereotype)

- 표준 요소를 확장하는 메커니즘
- 표기: `<<stereotype>>`
- 예: `<<interface>>`, `<<abstract>>`, `<<utility>>`