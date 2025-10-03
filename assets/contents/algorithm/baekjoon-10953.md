
# 백준 10953: A+B - 6 풀이

## 📊 결과
- **메모리:** 14112KB
- **시간:** 104ms

---

## 💻 내 코드

```java
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(",");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            sb.append(Integer.toString(a + b)).append("\n");
        }
        
        System.out.print(sb);
    }
}
````

---

## 📝 평가

### ✅ 잘한 점

- BufferedReader로 빠른 입력 처리
- StringBuilder로 출력 최적화
- 정확한 로직

### 🔴 개선점

1. **불필요한 Integer.toString()**
    
    ```java
    sb.append(Integer.toString(a + b))  // 불필요
    sb.append(a + b)  // 자동 변환됨
    ```
    
2. **public class 권장**
    
    ```java
    class Main  // 동작하지만 비권장
    public class Main  // 백준 표준
    ```
    

---

## 🎯 개선 후 코드

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(",");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            sb.append(a + b).append("\n");
        }
        
        System.out.print(sb);
    }
}
```

**개선:** `Integer.toString()` 제거, `public class` 사용

---

## 💡 핵심

**백준 입출력 최적화:**

- BufferedReader: Scanner보다 빠름
- StringBuilder: 여러 줄 출력 시 필수
- `split(",")`로 쉼표 구분 입력 처리

---

#백준 #입출력 #BufferedReader #StringBuilder #Bronze3