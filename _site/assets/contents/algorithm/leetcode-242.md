
# LeetCode 242: Valid Anagram 풀이

## 📊 결과
- **소요시간:** 5분
- **Runtime:** 4ms
- **Memory:** 44.98MB

---

## 💻 내 코드

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);
        
        return Arrays.equals(arr1, arr2);
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

- 길이 체크로 조기 종료
- 정렬 접근법 - 가장 직관적
- 간결하고 명확한 코드

### 🔴 개선점

- 정렬 시간복잡도: O(n log n)
- HashMap 사용 시 O(n) 가능

---

## ✨ 최적화

### 방법 1: 빈도수 배열 (O(n))

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) return false;
        }
        
        return true;
    }
}
```

### 방법 2: HashMap

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        Map<Character, Integer> map = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) - 1);
            if (map.get(c) < 0) return false;
        }
        
        return true;
    }
}
```

---

## 📊 성능 비교

|방법|시간|공간|특징|
|---|---|---|---|
|**정렬**|O(n log n)|O(n)|간결|
|**배열**|O(n)|O(1)|최적 (소문자만)|
|**HashMap**|O(n)|O(n)|유니코드 대응|

---

## 🎯 개선 후 코드

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) return false;
        }
        
        return true;
    }
}
```

**개선:** O(n log n) → O(n)

---

## 💡 핵심

**Anagram = 같은 문자 빈도**

- 정렬: 간단하지만 느림
- 빈도수: 빠르지만 배열/맵 필요

---

## 🎓 다음 단계

- <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">LeetCode 49: Group Anagrams</a>
- <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/" target="_blank">LeetCode 438: Find All Anagrams in a String</a>

---

#LeetCode #Anagram #HashMap #Sorting #String #Easy