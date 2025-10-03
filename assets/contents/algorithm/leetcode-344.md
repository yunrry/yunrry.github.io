
# LeetCode 344: Reverse String 풀이

## 📊 결과
- **소요시간:** 10분
- **Runtime:** 0ms (100%)
- **Memory:** 49.81MB

---

## 💻 내 코드

```java
class Solution {
    public void reverseString(char[] s) {
        for (int i = 0; i < s.length / 2; i++) {
            char temp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length - 1 - i] = temp;
        }
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

- Two Pointer 정석 풀이
- In-place 처리 (O(1) 공간)
- 최적 성능 (0ms)

### 🔴 개선점

없음. 완벽한 풀이.

---

## ✨ 다른 방법

### Two Pointer 명시적 버전

```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

### XOR Swap (비추천)

```java
class Solution {
    public void reverseString(char[] s) {
        for (int i = 0; i < s.length / 2; i++) {
            int j = s.length - 1 - i;
            s[i] ^= s[j];
            s[j] ^= s[i];
            s[i] ^= s[j];
        }
    }
}
```

---

## 📊 성능

|방법|시간|공간|
|---|---|---|
|**내 코드**|O(n)|O(1)|
|**Two Pointer**|O(n)|O(1)|
|**XOR**|O(n)|O(1)|

---

## 🎯 핵심

**In-place Reverse = Two Pointer Swap**

- `s.length / 2`만큼만 순회
- 양 끝을 swap하며 중앙으로 이동

---

#LeetCode #TwoPointer #String #Easy #InPlace