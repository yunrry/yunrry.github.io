
# LeetCode 443: String Compression 풀이

## 📊 결과
- **소요시간:** 2시간
- **Runtime:** 1ms
- **Memory:** 44.09MB

---

## 💻 내 코드

```java
class Solution {
    public int compress(char[] chars) {
        char current = chars[0];
        int count = 1;
        int p = 1;
        
        for (int i = 1; i < chars.length; i++) {
            if (chars[i] == chars[i-1]) {
                count++;
            } else {
                current = chars[i];             
                if (count == 1) {
                    chars[p] = current;
                    p++;
                    continue;
                } else {
                    char[] countChar = String.valueOf(count).toCharArray();
                    for (char c : countChar) {
                        chars[p] = c;    
                        p++;
                    }
                    chars[p] = current;
                    p++;
                }
                count = 1;
            }
        }

        if (count != 1) {
            char[] countChar = String.valueOf(count).toCharArray();
            int j = 0;
            for (char c : countChar) {
                chars[p] = c;    
                p++;
            }            
        }
        
        return p;
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- In-place 처리 (추가 배열 없음)
- Two Pointer 개념 사용
- 숫자가 여러 자릿수인 경우 처리

### ✦ 개선점

1. **복잡한 로직 흐름**
    
    - if-else 중첩이 깊음
    - continue 사용으로 가독성 저하
2. **중복 코드**
    
    ```java
    // 루프 안
    char[] countChar = String.valueOf(count).toCharArray();
    
    // 루프 밖 (마지막 처리)
    char[] countChar = String.valueOf(count).toCharArray();
    ```

3. **count == 1일 때 비효율**
    
    - 문자를 미리 쓰지 않고 다음 루프에서 씀

---

## ✨ 최적화된 풀이

### 방법 1: 깔끔한 버전

```java
class Solution {
    public int compress(char[] chars) {
        int write = 0;  // 쓰기 위치
        int i = 0;      // 읽기 위치
        
        while (i < chars.length) {
            char current = chars[i];
            int count = 0;
            
            // 같은 문자 개수 세기
            while (i < chars.length && chars[i] == current) {
                i++;
                count++;
            }
            
            // 문자 쓰기
            chars[write++] = current;
            
            // 개수가 2 이상이면 숫자 쓰기
            if (count > 1) {
                for (char c : String.valueOf(count).toCharArray()) {
                    chars[write++] = c;
                }
            }
        }
        
        return write;
    }
}
```

### 방법 2: 더 간결한 버전

```java
class Solution {
    public int compress(char[] chars) {
        int write = 0;
        
        for (int read = 0; read < chars.length; ) {
            char current = chars[read];
            int count = 0;
            
            while (read < chars.length && chars[read] == current) {
                read++;
                count++;
            }
            
            chars[write++] = current;
            
            if (count > 1) {
                for (char c : Integer.toString(count).toCharArray()) {
                    chars[write++] = c;
                }
            }
        }
        
        return write;
    }
}
```

---

## 📊 성능 비교

| 방법       | 시간   | 공간   | 가독성   |
| -------- | ---- | ---- | ----- |
| **내 코드** | O(n) | O(1) | 보통    |
| **방법 1** | O(n) | O(1) | 좋음    |
| **방법 2** | O(n) | O(1) | 매우 좋음 |

---

## 💡 핵심 인사이트

### 배운 점

1. **Two Pointer 패턴**
    - `read`: 현재 확인 중인 위치
    - `write`: 결과를 쓸 위치
2. **In-place 알고리즘**
    - 읽기 포인터가 쓰기 포인터보다 항상 앞섬
    - 덮어써도 안전함
3. **중복 제거**
    - 마지막 처리를 별도로 하지 않고
    - 루프 안에서 통합 처리

### 핵심 개념

**Run-Length Encoding (RLE)**

```
입력: ['a','a','b','b','c','c','c']
과정: a(2), b(2), c(3)
출력: ['a','2','b','2','c','3']
```

---

## 🎯 개선 후 코드

```java
class Solution {
    public int compress(char[] chars) {
        int write = 0;
        int read = 0;
        
        while (read < chars.length) {
            char current = chars[read];
            int count = 0;
            
            // 같은 문자 개수 세기
            while (read < chars.length && chars[read] == current) {
                read++;
                count++;
            }
            
            // 문자 쓰기
            chars[write++] = current;
            
            // 개수가 2 이상이면 숫자 쓰기
            if (count > 1) {
                for (char c : String.valueOf(count).toCharArray()) {
                    chars[write++] = c;
                }
            }
        }
        
        return write;
    }
}
```

**개선 사항:**

- 중복 코드 제거
- 로직 흐름 단순화
- 변수명 명확화 (p → write, i → read)
- 마지막 처리 통합

---

## 📚 관련 개념

### Run-Length Encoding (RLE)

- 연속된 데이터를 압축하는 기법
- 이미지 압축, 데이터 전송에 사용
- 간단하지만 효과적

### Two Pointer 응용

- 읽기/쓰기 포인터 분리
- In-place 수정 시 자주 사용
- 공간복잡도 O(1) 달성

---

## 🎓 다음 단계

### 비슷한 문제

- <a href="https://leetcode.com/problems/count-and-say/" target="_blank">LeetCode 38: Count and Say</a>
- <a href="https://leetcode.com/problems/encode-and-decode-strings/" target="_blank">LeetCode 271: Encode and Decode Strings</a>
- <a href="https://leetcode.com/problems/design-compressed-string-iterator/" target="_blank">LeetCode 604: Design Compressed String Iterator</a>

### 연습 포인트

- [ ] Two Pointer 패턴 숙달
- [ ] In-place 알고리즘 이해
- [ ] 중복 코드 리팩토링 연습
- [ ] 엣지 케이스 처리 (빈 배열, 단일 문자)

---
## 🏷️ Keywords
`#LeetCode` `#TwoPointer` `#String` `#InPlace` `#RLE` `#Compression` `#Medium`   `#StringBuilder`
