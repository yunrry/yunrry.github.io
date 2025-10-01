# 배열과 문자열 조작 완벽 가이드

## 📦 배열의 기본 연산

### 1. 배열 선언 및 초기화

{% raw %}
```java
// 1차원 배열
int[] arr1 = new int[5];                    // 크기 5, 기본값 0
int[] arr2 = {1, 2, 3, 4, 5};              // 선언과 동시에 초기화
int[] arr3 = new int[]{1, 2, 3, 4, 5};     // 명시적 초기화

// 2차원 배열
int[][] matrix = new int[3][4];             // 3x4 배열
int[][] matrix2 = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// 가변 배열 (Jagged Array)
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[4];
jagged[2] = new int[3];
```
{% endraw %}

---

### 2. Arrays 클래스 주요 메서드

{% raw %}
```java
import java.util.Arrays;

int[] arr = {5, 2, 8, 1, 9};

// 정렬
Arrays.sort(arr);                           // [1, 2, 5, 8, 9]
Arrays.sort(arr, 0, 3);                     // 부분 정렬 [0, 3)

// 역순 정렬 (Wrapper 클래스 필요)
Integer[] arr2 = {5, 2, 8, 1, 9};
Arrays.sort(arr2, Collections.reverseOrder());

// 이진 탐색 (정렬된 배열에서만 사용)
int index = Arrays.binarySearch(arr, 5);    // 2 반환

// 배열 채우기
Arrays.fill(arr, 0);                        // 모든 요소를 0으로
Arrays.fill(arr, 1, 4, -1);                 // [1, 4) 구간을 -1로

// 배열 복사
int[] copy1 = Arrays.copyOf(arr, arr.length);           // 전체 복사
int[] copy2 = Arrays.copyOfRange(arr, 1, 4);            // [1, 4) 구간 복사

// 배열 비교
boolean isEqual = Arrays.equals(arr, copy1);            // true

// 배열을 문자열로
String str = Arrays.toString(arr);                      // "[1, 2, 5, 8, 9]"

// 2차원 배열 출력
int[][] matrix = {{1, 2}, {3, 4}};
System.out.println(Arrays.deepToString(matrix));        // "[[1, 2], [3, 4]]"
```
{% endraw %}

---

### 3. 배열 순회 방법

```java
int[] arr = {1, 2, 3, 4, 5};

// 방법 1: 기본 for문
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

// 방법 2: 향상된 for문 (for-each)
for (int num : arr) {
    System.out.println(num);
}

// 방법 3: Stream (Java 8+)
Arrays.stream(arr).forEach(System.out::println);

// 역순 순회
for (int i = arr.length - 1; i >= 0; i--) {
    System.out.println(arr[i]);
}
```

---

### 4. 2차원 배열 순회

{% raw %}
```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// 기본 순회
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}

// 향상된 for문
for (int[] row : matrix) {
    for (int num : row) {
        System.out.print(num + " ");
    }
    System.out.println();
}

// 대각선 순회
for (int i = 0; i < matrix.length; i++) {
    System.out.print(matrix[i][i] + " ");      // 주 대각선
}
```
{% endraw %}

---

### 5. 배열 변환

{% raw %}
```java
// 배열 → List
Integer[] arr = {1, 2, 3, 4, 5};
List<Integer> list = Arrays.asList(arr);
List<Integer> list2 = new ArrayList<>(Arrays.asList(arr));  // 수정 가능한 리스트

// List → 배열
Integer[] arr2 = list.toArray(new Integer[0]);

// primitive 배열 → List (Stream 사용)
int[] primitiveArr = {1, 2, 3, 4, 5};
List<Integer> list3 = Arrays.stream(primitiveArr)
                            .boxed()
                            .collect(Collectors.toList());

// List → primitive 배열
int[] primitiveArr2 = list3.stream()
                           .mapToInt(Integer::intValue)
                           .toArray();
```
{% endraw %}

---

### 6. 자주 사용하는 배열 패턴

#### 최댓값/최솟값 찾기

{% raw %}
```java
int[] arr = {5, 2, 8, 1, 9};

// 방법 1: 반복문
int max = arr[0];
int min = arr[0];
for (int num : arr) {
    max = Math.max(max, num);
    min = Math.min(min, num);
}

// 방법 2: Stream
int max2 = Arrays.stream(arr).max().getAsInt();
int min2 = Arrays.stream(arr).min().getAsInt();
```
{% endraw %}

#### 배열 회전

```java
// 왼쪽으로 k칸 회전
public void rotateLeft(int[] arr, int k) {
    k = k % arr.length;
    reverse(arr, 0, k - 1);
    reverse(arr, k, arr.length - 1);
    reverse(arr, 0, arr.length - 1);
}

private void reverse(int[] arr, int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
```

#### 부분 배열 합

{% raw %}
```java
// 누적 합 (Prefix Sum)
int[] arr = {1, 2, 3, 4, 5};
int[] prefixSum = new int[arr.length + 1];

for (int i = 0; i < arr.length; i++) {
    prefixSum[i + 1] = prefixSum[i] + arr[i];
}

// [i, j] 구간 합 = prefixSum[j+1] - prefixSum[i]
int sum = prefixSum[4] - prefixSum[1];  // arr[1]~arr[3]의 합
```
{% endraw %}

---

## 📝 문자열 조작

### 1. String 기본 메서드

```java
String str = "Hello World";

// 길이
int len = str.length();                     // 11

// 문자 접근
char ch = str.charAt(0);                    // 'H'

// 부분 문자열
String sub1 = str.substring(0, 5);          // "Hello"
String sub2 = str.substring(6);             // "World"

// 검색
int index = str.indexOf("World");           // 6
int lastIndex = str.lastIndexOf('o');       // 7
boolean contains = str.contains("llo");     // true

// 비교
boolean equals = str.equals("Hello World"); // true
boolean equalsIgnore = str.equalsIgnoreCase("hello world");  // true
int compare = str.compareTo("Hello");       // 양수

// 변환
String upper = str.toUpperCase();           // "HELLO WORLD"
String lower = str.toLowerCase();           // "hello world"
String trim = "  hello  ".trim();           // "hello"
String replace = str.replace("World", "Java");  // "Hello Java"

// 분리
String[] words = str.split(" ");            // ["Hello", "World"]
String[] chars = str.split("");             // ["H", "e", "l", "l", "o", ...]

// 문자열 → 문자 배열
char[] charArray = str.toCharArray();
```

---

### 2. StringBuilder 완벽 가이드

#### 왜 StringBuilder를 사용하는가?

```java
// ❌ String 연결 (비효율적 - O(n²))
String result = "";
for (int i = 0; i < 1000; i++) {
    result += i;  // 매번 새로운 String 객체 생성
}

// ✅ StringBuilder 사용 (효율적 - O(n))
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i);  // 내부 버퍼에 추가만
}
String result = sb.toString();
```

**핵심**: String은 불변(immutable)이므로 연결할 때마다 새 객체 생성!

---

#### StringBuilder 주요 메서드

```java
StringBuilder sb = new StringBuilder();

// 추가 (append)
sb.append("Hello");                         // "Hello"
sb.append(" ").append("World");             // "Hello World" (체이닝)
sb.append(123);                             // "Hello World123"
sb.append(true);                            // "Hello World123true"

// 삽입 (insert)
sb.insert(5, ",");                          // "Hello, World123true"
sb.insert(0, ">> ");                        // ">> Hello, World123true"

// 삭제 (delete)
sb.delete(0, 3);                            // "Hello, World123true"
sb.deleteCharAt(5);                         // "Hello World123true"

// 교체 (replace)
sb.replace(6, 11, "Java");                  // "Hello Java123true"

// 역순 (reverse)
sb.reverse();                               // "eurt321avaJ olleH"

// 길이 관련
int length = sb.length();                   // 현재 길이
int capacity = sb.capacity();               // 현재 용량
sb.setLength(5);                            // 길이를 5로 축소

// 문자 접근 및 수정
char ch = sb.charAt(0);                     // 'e'
sb.setCharAt(0, 'E');                       // "Eurt321avaJ olleH"

// String 변환
String result = sb.toString();
```

---

#### StringBuilder 초기화

```java
// 방법 1: 기본 생성자 (용량 16)
StringBuilder sb1 = new StringBuilder();

// 방법 2: 초기 용량 지정
StringBuilder sb2 = new StringBuilder(100);

// 방법 3: 문자열로 초기화
StringBuilder sb3 = new StringBuilder("Hello");

// 방법 4: 다른 CharSequence로 초기화
StringBuilder sb4 = new StringBuilder(sb3);
```

---

#### 실전 활용 예제

**예제 1: 배열을 문자열로 변환**

{% raw %}
```java
int[] arr = {1, 2, 3, 4, 5};

// 방법 1: StringBuilder
StringBuilder sb = new StringBuilder();
sb.append("[");
for (int i = 0; i < arr.length; i++) {
    sb.append(arr[i]);
    if (i < arr.length - 1) {
        sb.append(", ");
    }
}
sb.append("]");
String result = sb.toString();  // "[1, 2, 3, 4, 5]"

// 방법 2: String.join (Java 8+)
String result2 = Arrays.stream(arr)
                       .mapToObj(String::valueOf)
                       .collect(Collectors.joining(", ", "[", "]"));
```
{% endraw %}

**예제 2: 문자열 뒤집기**

```java
String str = "Hello World";

// 방법 1: StringBuilder.reverse()
String reversed = new StringBuilder(str).reverse().toString();

// 방법 2: 직접 구현
char[] chars = str.toCharArray();
for (int i = 0; i < chars.length / 2; i++) {
    char temp = chars[i];
    chars[i] = chars[chars.length - 1 - i];
    chars[chars.length - 1 - i] = temp;
}
String reversed2 = new String(chars);
```

**예제 3: 팰린드롬 체크**

```java
public boolean isPalindrome(String s) {
    // 알파벳과 숫자만 추출 후 소문자 변환
    StringBuilder sb = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            sb.append(Character.toLowerCase(c));
        }
    }
    
    String cleaned = sb.toString();
    String reversed = sb.reverse().toString();
    
    return cleaned.equals(reversed);
}
```

**예제 4: 문자열 압축 (Run-Length Encoding)**

```java
public String compress(String s) {
    if (s.length() == 0) return s;
    
    StringBuilder sb = new StringBuilder();
    int count = 1;
    
    for (int i = 1; i < s.length(); i++) {
        if (s.charAt(i) == s.charAt(i - 1)) {
            count++;
        } else {
            sb.append(s.charAt(i - 1));
            if (count > 1) {
                sb.append(count);
            }
            count = 1;
        }
    }
    
    // 마지막 문자 처리
    sb.append(s.charAt(s.length() - 1));
    if (count > 1) {
        sb.append(count);
    }
    
    return sb.length() < s.length() ? sb.toString() : s;
}

// "aaabbcccc" → "a3b2c4"
```

---

### 3. String vs StringBuilder vs StringBuffer

| 특성 | String | StringBuilder | StringBuffer |
|------|--------|---------------|--------------|
| **가변성** | 불변 | 가변 | 가변 |
| **Thread-Safe** | Yes | No | Yes |
| **성능** | 느림 | 빠름 | 중간 |
| **사용 시점** | 변경 없음 | 단일 스레드 | 멀티 스레드 |

**코딩테스트에서는 StringBuilder 사용!**

---

### 4. 문자열 처리 자주 사용하는 패턴

#### 문자 빈도수 세기

```java
String s = "hello world";
int[] freq = new int[26];  // 알파벳 소문자

for (char c : s.toCharArray()) {
    if (c >= 'a' && c <= 'z') {
        freq[c - 'a']++;
    }
}

// HashMap 사용
Map<Character, Integer> map = new HashMap<>();
for (char c : s.toCharArray()) {
    map.put(c, map.getOrDefault(c, 0) + 1);
}
```

#### 아나그램 체크

```java
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
```

#### 부분 문자열 찾기 (KMP 알고리즘 간단 버전)

```java
public int strStr(String haystack, String needle) {
    if (needle.isEmpty()) return 0;
    
    // indexOf() 사용
    return haystack.indexOf(needle);
    
    // 직접 구현
    for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        if (haystack.substring(i, i + needle.length()).equals(needle)) {
            return i;
        }
    }
    return -1;
}
```

---

## 🎯 성능 비교

### String 연결 성능 테스트

```java
// 1. String + 연산자 (가장 느림)
long start = System.currentTimeMillis();
String result = "";
for (int i = 0; i < 10000; i++) {
    result += "a";
}
System.out.println("String +: " + (System.currentTimeMillis() - start) + "ms");

// 2. StringBuilder (가장 빠름)
start = System.currentTimeMillis();
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 10000; i++) {
    sb.append("a");
}
result = sb.toString();
System.out.println("StringBuilder: " + (System.currentTimeMillis() - start) + "ms");

// 3. StringBuffer (중간)
start = System.currentTimeMillis();
StringBuffer sbf = new StringBuffer();
for (int i = 0; i < 10000; i++) {
    sbf.append("a");
}
result = sbf.toString();
System.out.println("StringBuffer: " + (System.currentTimeMillis() - start) + "ms");
```

**결과 예시**

```
String +: 1234ms
StringBuilder: 2ms
StringBuffer: 3ms
```

---

## 💡 코딩테스트 꿀팁

### 1. 입력 처리

```java
import java.io.*;
import java.util.*;

// Scanner (느림)
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
String s = sc.next();

// BufferedReader (빠름) ⭐ 추천
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
int n = Integer.parseInt(br.readLine());
String[] input = br.readLine().split(" ");
```

### 2. 출력 처리

```java
// System.out.println (느림)
for (int i = 0; i < 10000; i++) {
    System.out.println(i);
}

// StringBuilder (빠름) ⭐ 추천
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 10000; i++) {
    sb.append(i).append("\n");
}
System.out.print(sb);
```

### 3. 자주 쓰는 변환

```java
// String → int
int num = Integer.parseInt("123");

// int → String
String str = String.valueOf(123);
String str2 = Integer.toString(123);

// char → int
char c = '5';
int digit = c - '0';  // 5

// int → char
int num = 5;
char ch = (char)(num + '0');  // '5'

// String → char[]
char[] chars = str.toCharArray();

// char[] → String
String str = new String(chars);
```

---

## 📚 연습 문제

### 배열
- LeetCode 1: Two Sum
- LeetCode 26: Remove Duplicates from Sorted Array
- LeetCode 88: Merge Sorted Array
- LeetCode 121: Best Time to Buy and Sell Stock

### 문자열
- LeetCode 125: Valid Palindrome
- LeetCode 242: Valid Anagram
- LeetCode 344: Reverse String
- LeetCode 387: First Unique Character in a String

### StringBuilder 활용
- LeetCode 443: String Compression
- LeetCode 151: Reverse Words in a String
- 백준 10953: A+B - 6
- 백준 11720: 숫자의 합

---

## 🔑 핵심 정리

### 배열
- `Arrays.sort()`, `Arrays.binarySearch()` 자주 사용
- 2차원 배열은 `matrix[row][col]` 순서 주의
- List ↔ Array 변환 패턴 숙지

### 문자열
- String은 불변 → 변경 많으면 StringBuilder
- `charAt()`, `substring()`, `split()` 자주 사용
- 문자 빈도수는 `int[26]` 또는 `HashMap` 활용

### StringBuilder
- 문자열 연결이 많을 때 필수
- `append()`, `reverse()`, `toString()` 핵심
- 코딩테스트 출력 최적화에 활용

---

#Java #알고리즘 #코딩테스트 #배열 #문자열 #StringBuilder #Arrays #String #자료구조 #입출력최적화 #BufferedReader #성능최적화 #LeetCode #백준