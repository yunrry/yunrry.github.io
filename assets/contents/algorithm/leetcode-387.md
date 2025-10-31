
# LeetCode 387: First Unique Character in a String 풀이

## 📊 결과
- **소요시간:** 27분
- **Runtime:** 6ms
- **Memory:** 45.45MB

---

## 💻 내 코드

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int index = (int)s.charAt(i) - 97;
            count[index]++;
        }

        for (int i = 0; i < s.length(); i++) {
            int index = (int)s.charAt(i) - 97;
            if (count[index] == 1) return i;
        }

        return -1;
    }
}
````

---

## 📝 평가

### ✔ 잘한 점

- 빈도수 배열로 O(n) 해결
- Two-pass 접근 정확
- 공간복잡도 O(1) (고정 크기 26)

### ✦ 개선점

- 매직넘버 97 대신 'a' 사용
- 불필요한 (int) 캐스팅

---

## ✨ 최적화

### 개선 버전

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
```

### HashMap 버전

```java
class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> count = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (count.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|특징|
|---|---|---|---|
|**배열**|O(n)|O(1)|최적, 소문자만|
|**HashMap**|O(n)|O(n)|유니코드 대응|

---

## 🎯 개선 후 코드

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
```

**개선:** `97` → `'a'`, 불필요한 캐스팅 제거

---

## 💡 핵심

**고유 문자 찾기 = 빈도수 배열 + Two Pass**

1. 첫 번째 순회: 빈도수 계산
2. 두 번째 순회: 빈도수 1인 첫 문자 반환

---

## 🎓 다음 단계

- <a href="https://leetcode.com/problems/first-unique-character-in-a-string-ii/" target="_blank">LeetCode 387 Follow-up</a>
- <a href="https://leetcode.com/problems/sort-characters-by-frequency/" target="_blank">LeetCode 451: Sort Characters By Frequency</a>

---
## 🏷️ Keywords
`#LeetCode` `#HashMap` `#FrequencyCount` `#String` `#Easy` `#배열`