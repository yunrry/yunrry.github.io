
# 백준 11720: 숫자의 합 풀이

## 결과
- **메모리:** 14404KB
- **시간:** 104ms

---

## 내 코드

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split("");
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(str[i]);
        }
        
        System.out.print(sum);
    }
}
````

---

## 평가

### 잘한 점

- BufferedReader 사용
- split("")으로 각 자릿수 분리
- 정확한 계산

### 개선점

1. **불필요한 split()**
    
    - split은 배열 생성 오버헤드 발생
    - charAt()이 더 효율적
2. **n 변수 미사용**
    
    - n을 읽지만 실제로는 문자열 길이만 필요

---

## ✨ 최적화

### 방법 1: charAt() 사용

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += str.charAt(i) - '0';
        }
        
        System.out.print(sum);
    }
}
```

### 방법 2: toCharArray()

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();  // n은 사용 안 함
        char[] chars = br.readLine().toCharArray();
        int sum = 0;
        
        for (char c : chars) {
            sum += c - '0';
        }
        
        System.out.print(sum);
    }
}
```

---

## 성능 비교

|방법|메모리|시간|특징|
|---|---|---|---|
|**split()**|14404KB|104ms|배열 생성|
|**charAt()**|14200KB|100ms|더 빠름|
|**toCharArray()**|14200KB|100ms|for-each 가능|

---

## 개선 후 코드

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += str.charAt(i) - '0';
        }
        
        System.out.print(sum);
    }
}
```

**핵심:** `'0'`을 빼면 숫자로 변환 (ASCII 이용)

---

## 핵심

**문자를 숫자로 변환:**

- `'5' - '0'` = 5
- `charAt()`이 `split()` + `parseInt()`보다 빠름

---
## 🏷️ Keywords
`#백준` `#문자열` `#charAt` `#Bronze4` `#ASCII`