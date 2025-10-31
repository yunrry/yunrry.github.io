

# LeetCode 151: Reverse Words in a String 풀이

## 📊 결과
- **소요시간:** 18분
- **Runtime:** 5ms (91.22%)
- **Memory:** 43.86MB (25.22%)

---

## 💻 내 코드

```java
class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        s = s.strip();
        String[] arr = s.split(" ");
        
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i].equals("")) {
                continue;
            } else {
                sb.append(arr[i]);
                sb.append(" ");
            }
        }
        
        return sb.toString().strip();
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- split으로 단어 분리 후 역순 처리
- StringBuilder 사용
- 빈 문자열 필터링

### ✦ 개선점

1. **불필요한 strip() 중복**
    
    ```java
    s = s.strip();  // 앞뒤 공백 제거
    // ...
    return sb.toString().strip();  // 또 제거
    ```
    
2. **마지막 공백 처리**
    
    - 매번 공백 추가 후 마지막에 제거
    - 조건문으로 처리 가능
3. **정규식 활용 부족**
    
    ```java
    split(" ")  // 연속 공백 처리 안 됨
    split("\\s+")  // 더 안전
    ```
    

---

## ✨ 최적화된 풀이

### 방법 1: 깔끔한 버전

```java
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i > 0) {
                sb.append(" ");
            }
        }
        
        return sb.toString();
    }
}
```

### 방법 2: Collections.reverse

```java
class Solution {
    public String reverseWords(String s) {
        List<String> words = Arrays.asList(s.trim().split("\\s+"));
        Collections.reverse(words);
        return String.join(" ", words);
    }
}
```

### 방법 3: 스택 활용

```java
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        Stack<String> stack = new Stack<>();
        
        for (String word : words) {
            stack.push(word);
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
            if (!stack.isEmpty()) {
                sb.append(" ");
            }
        }
        
        return sb.toString();
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|특징|
|---|---|---|---|
|**내 코드**|O(n)|O(n)|동작함|
|**방법 1**|O(n)|O(n)|깔끔|
|**방법 2**|O(n)|O(n)|가장 간결|
|**방법 3**|O(n)|O(n)|명시적|

---

## 🎯 개선 후 코드

```java
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i > 0) {
                sb.append(" ");
            }
        }
        
        return sb.toString();
    }
}
```

**개선:**

- `strip()` → `trim()` (관례)
- `split(" ")` → `split("\\s+")` (연속 공백 처리)
- 마지막 strip() 제거
- 조건문으로 마지막 공백 방지

---

## 💡 핵심

**문자열 단어 역순 = split + 역순 순회**

- `trim()`: 앞뒤 공백 제거
- `split("\\s+")`: 하나 이상의 공백으로 분리
- 마지막 단어 뒤 공백 처리 주의

---

## 다음 단계

- <a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/" target="_blank">LeetCode 186: Reverse Words in a String II</a>
- <a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/" target="_blank">LeetCode 557: Reverse Words in a String III</a>

---
## 🏷️ Keywords

`#LeetCode` `#String` `#StringBuilder` `#Split` `#Medium` `#정규식`