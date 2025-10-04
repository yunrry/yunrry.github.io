
# LeetCode 20. Valid Parentheses

## 📊 결과
- **소요시간**: 15분
- **Runtime**: 2ms (Beats 98.84%)
- **Memory**: 42.12MB

---

## 💻 내 코드

```java
class Solution {
    public boolean isValid(String s) {
        if (s.length()==1) return false;
        Deque<Character> stack = new ArrayDeque<Character>();
        for(char c : s.toCharArray()){
            if(c=='('|| c=='{'|| c=='['){
                stack.push(c);
            }else{
                if(stack.isEmpty()) return false;
                char open = stack.pop();
                if(open=='(' && c!=')') return false;
                if(open=='{' && c!='}') return false;
                if(open=='[' && c!=']') return false;
            }
        }

        if(!stack.isEmpty()) return false;

        return true;
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

1. **스택 자료구조 선택**: 괄호 매칭 문제의 핵심인 LIFO 특성을 정확히 파악
2. **엣지 케이스 처리**: 길이가 1인 경우 조기 리턴
3. **빠른 실패(Fast Fail)**: 스택이 비었을 때 즉시 false 반환
4. **마지막 검증**: 스택이 비어있는지 확인하여 열린 괄호가 남지 않았는지 체크
5. **ArrayDeque 사용**: Stack 클래스보다 효율적인 Deque 사용

### 🔴 개선점

1. **코드 중복**: 세 개의 if문이 반복적인 패턴
2. **매직 넘버**: 괄호 문자들이 하드코딩되어 있음
3. **조기 리턴 최적화**: 홀수 길이는 무조건 false (길이 1만 체크)
4. **가독성**: Map을 활용하면 더 깔끔한 매칭 가능

---

## ✨ 최적화된 풀이

### 방법 1: HashMap을 활용한 깔끔한 매칭

```java
class Solution {
    public boolean isValid(String s) {
        // 홀수 길이는 무조건 false
        if (s.length() % 2 != 0) return false;
        
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
        );
        
        for (char c : s.toCharArray()) {
            if (pairs.containsValue(c)) {
                // 여는 괄호
                stack.push(c);
            } else {
                // 닫는 괄호
                if (stack.isEmpty() || stack.pop() != pairs.get(c)) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}
```

### 방법 2: Switch 문 활용 (가장 빠름)

```java
class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;
        
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(': stack.push(')'); break;
                case '{': stack.push('}'); break;
                case '[': stack.push(']'); break;
                default:
                    if (stack.isEmpty() || stack.pop() != c) return false;
            }
        }
        
        return stack.isEmpty();
    }
}
```

**💡 Switch 방법의 핵심 아이디어**: 여는 괄호를 만나면 **대응되는 닫는 괄호를 push**하여, 나중에 닫는 괄호를 만났을 때 단순 비교만 하면 됨!

### 방법 3: 배열 기반 스택 (메모리 최적화)

```java
class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;
        
        char[] stack = new char[s.length()];
        int top = -1;
        
        for (char c : s.toCharArray()) {
            if (c == '(') stack[++top] = ')';
            else if (c == '{') stack[++top] = '}';
            else if (c == '[') stack[++top] = ']';
            else if (top < 0 || stack[top--] != c) return false;
        }
        
        return top == -1;
    }
}
```

---

## 📊 성능 비교

|방법|시간복잡도|공간복잡도|Runtime|가독성|추천도|
|---|---|---|---|---|---|
|원본 코드|O(n)|O(n)|2ms|⭐⭐⭐|⭐⭐⭐|
|HashMap|O(n)|O(n)|2-3ms|⭐⭐⭐⭐⭐|⭐⭐⭐⭐|
|Switch|O(n)|O(n)|1-2ms|⭐⭐⭐⭐|⭐⭐⭐⭐⭐|
|배열 스택|O(n)|O(n)|1ms|⭐⭐⭐|⭐⭐⭐⭐|

**참고**: 모두 O(n) 복잡도지만, 실제 실행 시간은 상수 요인에 따라 차이 발생

---

## 💡 핵심 인사이트

### 배운 점

1. **스택의 활용**: LIFO 구조가 괄호 매칭에 완벽하게 맞는 이유
    
    - 가장 최근에 열린 괄호가 먼저 닫혀야 함
2. **조기 종료 최적화**: 홀수 길이 체크로 불필요한 연산 방지
    
3. **트레이드오프**: 가독성 vs 성능
    
    - HashMap: 확장성과 가독성 우수
    - Switch: 성능 최고
    - 배열: 메모리 효율적

### 핵심 개념

**스택(Stack) 문제의 전형적인 패턴**:

```
1. 여는 요소 → push
2. 닫는 요소 → pop하여 검증
3. 끝에 스택이 비어있어야 함
```

**괄호 문제의 실패 조건**:

- 닫는 괄호인데 스택이 비어있음 (여는 괄호 부족)
- 매칭되지 않는 괄호 쌍
- 모든 처리 후 스택에 남은 여는 괄호 존재

---

## 🎯 개선 후 코드

**추천: Switch 문 방식** (성능과 가독성의 균형)

```java
class Solution {
    public boolean isValid(String s) {
        // 홀수 길이는 무조건 매칭 불가
        if (s.length() % 2 != 0) return false;
        
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            // 여는 괄호면 대응되는 닫는 괄호를 push
            switch (c) {
                case '(': stack.push(')'); break;
                case '{': stack.push('}'); break;
                case '[': stack.push(']'); break;
                // 닫는 괄호면 스택 top과 비교
                default:
                    if (stack.isEmpty() || stack.pop() != c) {
                        return false;
                    }
            }
        }
        
        // 모든 괄호가 매칭되었으면 스택이 비어있어야 함
        return stack.isEmpty();
    }
}
```

**개선 포인트**:

- ✅ 홀수 길이 조기 체크
- ✅ Switch 문으로 깔끔한 분기
- ✅ "대응 괄호 push" 트릭으로 비교 간소화
- ✅ 주석으로 의도 명확화

---

## 📚 관련 개념

### 알고리즘 패턴

- **스택(Stack)**: LIFO 구조
- **괄호 매칭(Bracket Matching)**: 컴파일러 구문 분석의 기초
- **균형 잡힌 문자열(Balanced String)**

### 연관 개념

1. **재귀와의 관계**: 스택 = 재귀의 명시적 구현
2. **DFS**: 스택 기반 탐색
3. **백트래킹**: 스택으로 상태 관리
4. **파싱(Parsing)**: 컴파일러의 괄호 검증

### 실무 활용

- JSON/XML 유효성 검사
- 수식 파싱 (후위 표기법)
- HTML 태그 검증
- 코드 에디터의 괄호 하이라이팅

---

## 🎓 다음 단계

### 비슷한 문제

1. **[LeetCode 22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)** ⭐⭐⭐
    
    - 유효한 괄호 조합 생성 (백트래킹)
2. **[LeetCode 32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)** ⭐⭐⭐⭐⭐
    
    - 가장 긴 유효한 괄호 부분 문자열
3. **[LeetCode 921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)** ⭐⭐
    
    - 최소 추가 괄호 개수
4. **[LeetCode 1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)** ⭐⭐
    
    - 최소 제거로 유효한 괄호 만들기
5. **[LeetCode 856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)** ⭐⭐⭐
    
    - 괄호의 점수 계산

### 연습 포인트 체크리스트

- [ ] HashMap 버전으로 다시 구현해보기
- [ ] 배열 기반 스택으로 메모리 최적화 시도
- [ ] 재귀 버전으로도 풀어보기
- [ ] 여러 종류의 괄호 추가 (< >, « » 등)
- [ ] 에러 위치 반환하는 버전으로 확장
- [ ] 괄호 생성 문제(#22)로 난이도 업그레이드

---

## 🏷️ Keywords

#Stack #Deque #BracketMatching #StringValidation #LeetCodeEasy #ArrayDeque #HashMap #Switch #LIFO #DataStructures #Parsing #BalancedString #TwoPointer #FastFail #EdgeCase #코딩테스트 #알고리즘 #자료구조