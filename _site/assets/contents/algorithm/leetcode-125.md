
# LeetCode 125: Valid Palindrome 풀이

## 📊 결과
- **소요시간:** 10분
- **Runtime:** 3ms
- **Memory:** 48.82MB

---

## 💻 내 코드

```java
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
    
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        
        String str = sb.toString();
        int i = 0;
        int j = str.length() - 1;
        boolean answer = true;
        
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                answer = false;
                break;
            }
            i++;
            j--;
        }
        
        return answer;
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- StringBuilder로 전처리 (알파벳+숫자만 추출)
- Two Pointer로 O(n) 해결
- 로직 명확하고 정확

### ✦ 개선점

- **불필요한 메모리 사용**: O(n) 추가 공간
- **불필요한 변수**: `answer` 대신 직접 return
- **두 번 순회**: 전처리 + 비교

---

## ✨ 최적화

### 방법 1: Two Pointer (공간 O(1))

```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            if (Character.toLowerCase(s.charAt(left)) != 
                Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
}
```

### 방법 2: StringBuilder 개선

```java
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        
        return sb.toString().equals(sb.reverse().toString());
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|특징|
|---|---|---|---|
|**내 코드**|O(n)|O(n)|가독성 좋음|
|**방법 1**|O(n)|O(1)|최적|
|**방법 2**|O(n)|O(n)|가장 간결|

---

## 🎯 개선 후 코드

```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            if (Character.toLowerCase(s.charAt(left)) != 
                Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
}
```

**개선점:** 추가 메모리 없이 O(1) 공간복잡도

---

## 💡 핵심

**Palindrome 검증 = Two Pointer**

- 양 끝에서 중앙으로 이동
- 불필요한 문자는 skip
- 대소문자 무시

---

## 🎓 다음 단계

- <a href="https://leetcode.com/problems/valid-palindrome-ii/" target="_blank">LeetCode 680: Valid Palindrome II</a>
- <a href="https://leetcode.com/problems/palindrome-linked-list/" target="_blank">LeetCode 234: Palindrome Linked List</a>

---
## 🏷️ Keywords
`#LeetCode` `#TwoPointer` `#Palindrome` `#String` `#Easy` `#문자열처리`