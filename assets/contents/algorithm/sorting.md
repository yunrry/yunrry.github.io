
# 정렬과 탐색

정렬과 탐색은 알고리즘의 기초이자 가장 자주 사용되는 기법입니다. 효율적인 정렬과 탐색을 통해 문제를 O(n²)에서 O(n log n) 또는 O(log n)으로 최적화할 수 있습니다.

---

## 📊 정렬 (Sorting)

### 왜 정렬이 중요한가?

**정렬된 데이터는:**
- 이진 탐색 가능 (O(log n))
- 중복 제거 쉬움
- 투포인터 적용 가능
- 그리디 알고리즘에 유리

---

## 🎯 Java 기본 정렬

### 1. Arrays.sort() - 배열 정렬

{% raw %}
```java
import java.util.Arrays;

public class ArraySortExample {
    public static void main(String[] args) {
        // 1. 기본형 배열 정렬 (오름차순)
        int[] arr = {5, 2, 8, 1, 9};
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));  // [1, 2, 5, 8, 9]
        
        // 2. 부분 정렬 (from ~ to-1)
        int[] arr2 = {5, 2, 8, 1, 9};
        Arrays.sort(arr2, 1, 4);  // 인덱스 1~3 정렬
        System.out.println(Arrays.toString(arr2));  // [5, 1, 2, 8, 9]
        
        // 3. 문자열 배열 정렬
        String[] strs = {"banana", "apple", "cherry"};
        Arrays.sort(strs);
        System.out.println(Arrays.toString(strs));
        // [apple, banana, cherry]
        
        // 4. 내림차순 정렬 (Integer[] 필요)
        Integer[] nums = {5, 2, 8, 1, 9};
        Arrays.sort(nums, Collections.reverseOrder());
        System.out.println(Arrays.toString(nums));  // [9, 8, 5, 2, 1]
    }
}
````

{% endraw %}

**시간복잡도:**

- 기본형 배열: O(n log n) - Dual-Pivot Quicksort
- 객체 배열: O(n log n) - Timsort

---

### 2. Collections.sort() - 리스트 정렬

{% raw %}

```java
import java.util.*;

public class CollectionsSortExample {
    public static void main(String[] args) {
        // 1. 리스트 정렬
        List<Integer> list = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 9));
        Collections.sort(list);
        System.out.println(list);  // [1, 2, 5, 8, 9]
        
        // 2. 내림차순 정렬
        Collections.sort(list, Collections.reverseOrder());
        System.out.println(list);  // [9, 8, 5, 2, 1]
        
        // 3. 문자열 리스트
        List<String> words = new ArrayList<>(Arrays.asList("banana", "apple", "cherry"));
        Collections.sort(words);
        System.out.println(words);  // [apple, banana, cherry]
        
        // 4. List.sort() 메서드 (Java 8+)
        list.sort(Comparator.naturalOrder());
        list.sort(Comparator.reverseOrder());
    }
}
```

{% endraw %}

**시간복잡도:** O(n log n) - Timsort

---

### 3. Comparator - 커스텀 정렬

{% raw %}

```java
import java.util.*;

public class ComparatorExample {
    public static void main(String[] args) {
        Integer[] arr = {5, 2, 8, 1, 9};
        
        // 1. 익명 클래스
        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return b - a;  // 내림차순
            }
        });
        
        // 2. 람다식 (Java 8+) ✅ 추천
        Arrays.sort(arr, (a, b) -> b - a);  // 내림차순
        Arrays.sort(arr, (a, b) -> a - b);  // 오름차순
        
        // 3. Comparator 메서드 체이닝
        Arrays.sort(arr, Comparator.reverseOrder());
        Arrays.sort(arr, Comparator.naturalOrder());
        
        // 4. 문자열 길이로 정렬
        String[] words = {"apple", "pie", "banana"};
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        System.out.println(Arrays.toString(words));  // [pie, apple, banana]
        
        // 5. 여러 조건 정렬
        Arrays.sort(words, 
            Comparator.comparingInt(String::length)  // 1순위: 길이
                      .thenComparing(Comparator.naturalOrder()));  // 2순위: 사전순
    }
}
```

{% endraw %}

---

### Comparator 핵심 패턴

{% raw %}

```java
// 1. 오름차순
(a, b) -> a - b
(a, b) -> a.compareTo(b)
Comparator.naturalOrder()

// 2. 내림차순
(a, b) -> b - a
(a, b) -> b.compareTo(a)
Comparator.reverseOrder()

// 3. 특정 필드로 정렬
(a, b) -> a.field - b.field
Comparator.comparing(obj -> obj.field)
Comparator.comparingInt(obj -> obj.field)

// 4. 여러 조건
Comparator.comparing(Obj::getField1)
          .thenComparing(Obj::getField2)
          .thenComparing(Obj::getField3)

// 5. null 처리
Comparator.nullsFirst(Comparator.naturalOrder())
Comparator.nullsLast(Comparator.naturalOrder())
```

{% endraw %}

---

### ⚠️ Comparator 주의사항

{% raw %}

```java
// ❌ 오버플로우 위험!
Arrays.sort(arr, (a, b) -> a - b);
// a = Integer.MAX_VALUE, b = -1이면
// a - b = overflow!

// ✅ 안전한 방법
Arrays.sort(arr, (a, b) -> Integer.compare(a, b));
Arrays.sort(arr, Comparator.comparingInt(x -> x));

// ❌ 일관성 없는 비교
(a, b) -> {
    if (a > b) return 1;
    if (a < b) return -1;
    return 1;  // 잘못됨! a==b일 때는 0 반환해야
}

// ✅ 올바른 비교
(a, b) -> Integer.compare(a, b)
```

{% endraw %}

---

## 🎨 실전 정렬 예제

### 예제 1: 2차원 배열 정렬

{% raw %}

```java
public class ArraySorting {
    public static void main(String[] args) {
        int[][] points = {{3, 4}, {1, 2}, {5, 1}, {1, 3}};
        
        // 1. x 좌표 기준 오름차순
        Arrays.sort(points, (a, b) -> a[0] - b[0]);
        // [[1,2], [1,3], [3,4], [5,1]]
        
        // 2. x 오름차순, x 같으면 y 오름차순
        Arrays.sort(points, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        // [[1,2], [1,3], [3,4], [5,1]]
        
        // 3. Comparator 체이닝 (더 깔끔!)
        Arrays.sort(points, 
            Comparator.comparingInt((int[] p) -> p[0])
                      .thenComparingInt(p -> p[1]));
        
        // 4. 거리 기준 정렬 (원점으로부터)
        Arrays.sort(points, (a, b) -> {
            int distA = a[0] * a[0] + a[1] * a[1];
            int distB = b[0] * b[0] + b[1] * b[1];
            return distA - distB;
        });
        
        for (int[] p : points) {
            System.out.println(Arrays.toString(p));
        }
    }
}
```

{% endraw %}

---

### 예제 2: 객체 정렬

{% raw %}

```java
class Student {
    String name;
    int score;
    int age;
    
    public Student(String name, int score, int age) {
        this.name = name;
        this.score = score;
        this.age = age;
    }
    
    @Override
    public String toString() {
        return name + "(" + score + ", " + age + ")";
    }
}

public class ObjectSorting {
    public static void main(String[] args) {
        List<Student> students = Arrays.asList(
            new Student("Alice", 85, 20),
            new Student("Bob", 92, 22),
            new Student("Charlie", 85, 21),
            new Student("David", 78, 20)
        );
        
        // 1. 점수 내림차순
        students.sort((a, b) -> b.score - a.score);
        
        // 2. 점수 내림차순, 같으면 나이 오름차순
        students.sort((a, b) -> {
            if (a.score != b.score) return b.score - a.score;
            return a.age - b.age;
        });
        
        // 3. Comparator 체이닝 (가독성 최고!)
        students.sort(
            Comparator.comparingInt((Student s) -> s.score).reversed()
                      .thenComparingInt(s -> s.age)
        );
        
        // 4. 이름 사전순
        students.sort(Comparator.comparing(s -> s.name));
        
        System.out.println(students);
        // [Bob(92, 22), Alice(85, 20), Charlie(85, 21), David(78, 20)]
    }
}
```

{% endraw %}

---

### 예제 3: 문자열 정렬

{% raw %}

```java
public class StringSorting {
    public static void main(String[] args) {
        String[] words = {"apple", "Banana", "cherry", "Date"};
        
        // 1. 기본 정렬 (대문자가 먼저)
        Arrays.sort(words);
        // [Banana, Date, apple, cherry]
        
        // 2. 대소문자 무시 정렬
        Arrays.sort(words, String.CASE_INSENSITIVE_ORDER);
        // [apple, Banana, cherry, Date]
        
        // 3. 길이 순 정렬
        Arrays.sort(words, Comparator.comparingInt(String::length));
        // [Date, apple, cherry, Banana]
        
        // 4. 길이 순, 같으면 사전순
        Arrays.sort(words, 
            Comparator.comparingInt(String::length)
                      .thenComparing(String.CASE_INSENSITIVE_ORDER));
        
        // 5. 특정 문자 개수로 정렬 (예: 'a' 개수)
        Arrays.sort(words, (a, b) -> {
            int countA = (int) a.chars().filter(ch -> ch == 'a').count();
            int countB = (int) b.chars().filter(ch -> ch == 'a').count();
            return countB - countA;  // 내림차순
        });
        
        System.out.println(Arrays.toString(words));
    }
}
```

{% endraw %}

---

## 🔍 이진 탐색 (Binary Search)

### 원리

**정렬된 배열에서 O(log n)에 탐색**

```
배열: [1, 3, 5, 7, 9, 11, 13, 15]
목표: 7 찾기

Step 1: mid = 4, arr[4] = 9 > 7  →  왼쪽 탐색
Step 2: mid = 1, arr[1] = 3 < 7  →  오른쪽 탐색
Step 3: mid = 2, arr[2] = 5 < 7  →  오른쪽 탐색
Step 4: mid = 3, arr[3] = 7 = 7  →  찾음!
```

---

### 기본 구현

{% raw %}

```java
public class BinarySearch {
    // 1. 반복문 버전 (추천)
    public int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;  // 오버플로우 방지
            
            if (arr[mid] == target) {
                return mid;  // 찾음
            } else if (arr[mid] < target) {
                left = mid + 1;  // 오른쪽 탐색
            } else {
                right = mid - 1;  // 왼쪽 탐색
            }
        }
        
        return -1;  // 못 찾음
    }
    
    // 2. 재귀 버전
    public int binarySearchRecursive(int[] arr, int target, int left, int right) {
        if (left > right) return -1;
        
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) {
            return binarySearchRecursive(arr, target, mid + 1, right);
        } else {
            return binarySearchRecursive(arr, target, left, mid - 1);
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
        BinarySearch bs = new BinarySearch();
        
        System.out.println(bs.binarySearch(arr, 7));   // 3
        System.out.println(bs.binarySearch(arr, 10));  // -1
    }
}
```

{% endraw %}

---

### Java 내장 이진 탐색

{% raw %}

```java
import java.util.*;

public class BuiltInBinarySearch {
    public static void main(String[] args) {
        // 1. Arrays.binarySearch() - 배열
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
        int idx1 = Arrays.binarySearch(arr, 7);      // 3
        int idx2 = Arrays.binarySearch(arr, 10);     // -6 (음수: 삽입 위치)
        
        // 음수 반환값의 의미: -(insertion point) - 1
        // idx2 = -6 → 삽입 위치 = 5
        int insertPos = -(idx2 + 1);  // 5
        
        // 2. 부분 배열 탐색
        int idx3 = Arrays.binarySearch(arr, 2, 6, 7);  // 인덱스 2~5에서 탐색
        
        // 3. Collections.binarySearch() - 리스트
        List<Integer> list = Arrays.asList(1, 3, 5, 7, 9, 11, 13, 15);
        int idx4 = Collections.binarySearch(list, 7);   // 3
        int idx5 = Collections.binarySearch(list, 10);  // -6
        
        // 4. Comparator 사용
        String[] words = {"apple", "banana", "cherry", "date"};
        int idx6 = Arrays.binarySearch(words, "cherry");  // 2
        
        // 길이로 정렬된 경우
        Arrays.sort(words, Comparator.comparingInt(String::length));
        int idx7 = Arrays.binarySearch(words, "date", 
            Comparator.comparingInt(String::length));
    }
}
```

{% endraw %}

---

### 이진 탐색 변형

#### 1. Lower Bound (target 이상의 첫 위치)

{% raw %}

```java
public int lowerBound(int[] arr, int target) {
    int left = 0;
    int right = arr.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;  // target 이상이면 right 이동
        }
    }
    
    return left;
}

// 테스트
int[] arr = {1, 2, 2, 2, 3, 4, 5};
System.out.println(lowerBound(arr, 2));  // 1 (첫 2의 위치)
System.out.println(lowerBound(arr, 6));  // 7 (없으면 삽입 위치)
```

{% endraw %}

---

#### 2. Upper Bound (target 초과의 첫 위치)

{% raw %}

```java
public int upperBound(int[] arr, int target) {
    int left = 0;
    int right = arr.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] <= target) {
            left = mid + 1;  // target 이하면 left 이동
        } else {
            right = mid;
        }
    }
    
    return left;
}

// 테스트
int[] arr = {1, 2, 2, 2, 3, 4, 5};
System.out.println(upperBound(arr, 2));  // 4 (2 다음 위치)
System.out.println(upperBound(arr, 5));  // 7
```

{% endraw %}

---

#### 3. 범위 찾기 (특정 값의 시작과 끝)

{% raw %}

```java
public int[] searchRange(int[] arr, int target) {
    int[] result = {-1, -1};
    
    // Lower Bound로 시작 위치
    int left = lowerBound(arr, target);
    if (left == arr.length || arr[left] != target) {
        return result;  // 없음
    }
    
    // Upper Bound로 끝 위치
    int right = upperBound(arr, target) - 1;
    
    result[0] = left;
    result[1] = right;
    return result;
}

// 테스트
int[] arr = {1, 2, 2, 2, 3, 4, 5};
int[] range = searchRange(arr, 2);
System.out.println(Arrays.toString(range));  // [1, 3]
```

{% endraw %}

---

### 이진 탐색 응용

#### 1. 회전된 배열에서 탐색

{% raw %}

```java
public int searchRotated(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        
        // 왼쪽이 정렬되어 있는 경우
        if (arr[left] <= arr[mid]) {
            if (arr[left] <= target && target < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // 오른쪽이 정렬되어 있는 경우
        else {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    
    return -1;
}

// 테스트: [4,5,6,7,0,1,2]에서 0 찾기
int[] arr = {4, 5, 6, 7, 0, 1, 2};
System.out.println(searchRotated(arr, 0));  // 4
```

{% endraw %}

---

#### 2. 정답의 범위를 찾는 파라메트릭 서치

{% raw %}

```java
// 예: 나무 자르기 (백준 2805)
// H 높이로 자를 때 M 이상의 나무를 얻을 수 있는 최대 H는?
public int cutTrees(int[] trees, long target) {
    int left = 0;
    int right = Arrays.stream(trees).max().getAsInt();
    int result = 0;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        long sum = 0;
        
        // mid 높이로 자르면 얻는 나무 양
        for (int tree : trees) {
            if (tree > mid) {
                sum += tree - mid;
            }
        }
        
        if (sum >= target) {
            result = mid;  // 가능하면 더 높이 자르기 시도
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

{% endraw %}

---

## 👉 투포인터 (Two Pointers)

### 원리

**두 개의 포인터로 배열/리스트를 효율적으로 탐색**

```
배열: [1, 2, 3, 4, 5, 6, 7, 8, 9]
목표: 합이 10인 쌍 찾기

left = 0, right = 8
합 = 1 + 9 = 10  ✓ 찾음!

left = 1, right = 8
합 = 2 + 9 = 11 > 10  →  right--

left = 1, right = 7
합 = 2 + 8 = 10  ✓ 찾음!
```

---

### 패턴 1: 양쪽 끝에서 시작

{% raw %}

```java
public class TwoPointers1 {
    // 정렬된 배열에서 합이 target인 두 수 찾기
    public int[] twoSum(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            int sum = arr[left] + arr[right];
            
            if (sum == target) {
                return new int[]{left, right};
            } else if (sum < target) {
                left++;  // 합이 작으면 왼쪽 포인터 증가
            } else {
                right--;  // 합이 크면 오른쪽 포인터 감소
            }
        }
        
        return new int[]{-1, -1};
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        TwoPointers1 tp = new TwoPointers1();
        int[] result = tp.twoSum(arr, 10);
        System.out.println(Arrays.toString(result));  // [0, 8] (1+9=10)
    }
}
```

{% endraw %}

---

### 패턴 2: 같은 방향으로 이동

{% raw %}

```java
public class TwoPointers2 {
    // 부분 배열의 합이 target 이상인 최소 길이
    public int minSubArrayLen(int target, int[] arr) {
        int left = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;
        
        for (int right = 0; right < arr.length; right++) {
            sum += arr[right];
            
            // 합이 target 이상이면 left 이동
            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= arr[left];
                left++;
            }
        }
        
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 3, 1, 2, 4, 3};
        TwoPointers2 tp = new TwoPointers2();
        System.out.println(tp.minSubArrayLen(7, arr));  // 2 ([4,3])
    }
}
```

{% endraw %}|알고리즘|시간복잡도|공간복잡도|특징|
|---|---|---|---|
|**정렬**||||
|Arrays.sort() (기본형)|O(n log n)|O(log n)|Dual-Pivot Quicksort|
|Arrays.sort() (객체)|O(n log n)|O(n)|Timsort|
|Collections.sort()|O(n log n)|O(n)|Timsort|
|**탐색**||||
|선형 탐색|O(n)|O(1)|정렬 불필요|
|이진 탐색|O(log n)|O(1)|정렬 필수|
|**투포인터**||||
|Two Sum (정렬됨)|O(n)|O(1)|양쪽 끝에서 시작|
|Sliding Window|O(n)|O(1)|같은 방향 이동|

---

## 💡 알고리즘 선택 가이드

### 언제 무엇을 사용할까?

|상황|알고리즘|시간복잡도|
|---|---|---|
|**정렬된 배열에서 값 찾기**|이진 탐색|O(log n)|
|**정렬 안 된 배열에서 값 찾기**|선형 탐색|O(n)|
|**두 수의 합 찾기 (정렬됨)**|투포인터|O(n)|
|**두 수의 합 찾기 (정렬 안 됨)**|HashMap|O(n)|
|**연속 부분 배열의 합**|투포인터 (슬라이딩 윈도우)|O(n)|
|**K번째 큰/작은 수**|QuickSelect 또는 Heap|O(n) avg|
|**정답 범위 찾기**|파라메트릭 서치|O(n log M)|

---

## 🎯 핵심 패턴 정리

### 1. 정렬 후 이진 탐색

{% raw %}

```java
// 패턴: 정렬 → 이진 탐색으로 O(n²) → O(n log n) 최적화
public boolean hasPairWithSum(int[] arr, int target) {
    Arrays.sort(arr);  // O(n log n)
    
    for (int i = 0; i < arr.length; i++) {
        int complement = target - arr[i];
        int idx = Arrays.binarySearch(arr, i + 1, arr.length, complement);
        if (idx >= 0) return true;
    }
    
    return false;
}
```

{% endraw %}

---

### 2. 정렬 후 투포인터

{% raw %}

```java
// 패턴: 정렬 → 투포인터로 효율적 탐색
public List<List<Integer>> threeSum(int[] arr) {
    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(arr);  // 필수!
    
    for (int i = 0; i < arr.length - 2; i++) {
        if (i > 0 && arr[i] == arr[i-1]) continue;  // 중복 제거
        
        int left = i + 1;
        int right = arr.length - 1;
        
        while (left < right) {
            int sum = arr[i] + arr[left] + arr[right];
            
            if (sum == 0) {
                result.add(Arrays.asList(arr[i], arr[left], arr[right]));
                
                // 중복 제거
                while (left < right && arr[left] == arr[left+1]) left++;
                while (left < right && arr[right] == arr[right-1]) right--;
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}
```

{% endraw %}

---

### 3. 슬라이딩 윈도우 (투포인터 변형)

{% raw %}

```java
// 패턴: 윈도우 크기를 동적으로 조절
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0;
    int maxLen = 0;
    
    for (int right = 0; right < s.length(); right++) {
        // 중복 제거할 때까지 left 이동
        while (set.contains(s.charAt(right))) {
            set.remove(s.charAt(left));
            left++;
        }
        
        set.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
}

// 테스트
System.out.println(lengthOfLongestSubstring("abcabcbb"));  // 3 (abc)
System.out.println(lengthOfLongestSubstring("bbbbb"));     // 1 (b)
System.out.println(lengthOfLongestSubstring("pwwkew"));    // 3 (wke)
```

{% endraw %}

---

### 4. 파라메트릭 서치

{% raw %}

```java
// 패턴: 정답의 범위를 이진 탐색으로 좁히기
// 예: 블루레이 만들기 - M개 이하로 나눌 수 있는 최소 크기
public int minBluraySizes(int[] lessons, int m) {
    int left = Arrays.stream(lessons).max().getAsInt();  // 최소: 가장 긴 레슨
    int right = Arrays.stream(lessons).sum();             // 최대: 전체 합
    int result = right;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // mid 크기로 m개 이하로 나눌 수 있는지 확인
        if (canDivide(lessons, m, mid)) {
            result = mid;
            right = mid - 1;  // 더 작은 크기 시도
        } else {
            left = mid + 1;
        }
    }
    
    return result;
}

private boolean canDivide(int[] lessons, int m, int maxSize) {
    int count = 1;
    int sum = 0;
    
    for (int lesson : lessons) {
        if (sum + lesson > maxSize) {
            count++;
            sum = lesson;
            if (count > m) return false;
        } else {
            sum += lesson;
        }
    }
    
    return true;
}
```

{% endraw %}

---

## 🏆 코딩테스트 단골 문제 유형

### 정렬 문제

1. **[LeetCode 56] Merge Intervals** ⭐⭐
    
    - 겹치는 구간 합치기
2. **[LeetCode 148] Sort List** ⭐⭐
    
    - 연결 리스트 정렬
3. **[LeetCode 179] Largest Number** ⭐⭐
    
    - 커스텀 정렬
4. **[프로그래머스] H-Index** ⭐⭐
    
    - 정렬 후 조건 확인
5. **[백준 11650] 좌표 정렬하기** ⭐
    
    - 2차원 배열 정렬

---

### 이진 탐색 문제

1. **[LeetCode 33] Search in Rotated Sorted Array** ⭐⭐
    - 회전된 배열 탐색
2. **[LeetCode 153] Find Minimum in Rotated Sorted Array** ⭐⭐
    - 최솟값 찾기
3. **[LeetCode 34] Find First and Last Position** ⭐⭐
    - Lower/Upper Bound
4. **[백준 2805] 나무 자르기** ⭐⭐
    - 파라메트릭 서치
5. **[백준 1654] 랜선 자르기** ⭐⭐
    - 파라메트릭 서치

---

### 투포인터 문제

1. **[LeetCode 15] 3Sum** ⭐⭐
    - 세 수의 합 = 0
2. **[LeetCode 11] Container With Most Water** ⭐⭐
    - 최대 면적
3. **[LeetCode 42] Trapping Rain Water** ⭐⭐⭐
    - 빗물 가두기
4. **[LeetCode 209] Minimum Size Subarray Sum** ⭐⭐
    - 슬라이딩 윈도우
5. **[백준 2003] 수들의 합 2** ⭐⭐
    - 부분 합

---

## 🎨 실전 문제 풀이

### 문제 1: K개의 가장 가까운 점 (LeetCode 973)

{% raw %}

```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // 거리로 정렬
        Arrays.sort(points, (a, b) -> {
            int distA = a[0] * a[0] + a[1] * a[1];
            int distB = b[0] * b[0] + b[1] * b[1];
            return distA - distB;
        });
        
        // 앞에서 k개 반환
        return Arrays.copyOf(points, k);
    }
}

// 테스트
int[][] points = {{1,3}, {-2,2}, {5,8}, {0,1}};
int[][] result = kClosest(points, 2);
// [[0,1], [-2,2]]
```

{% endraw %}

---

### 문제 2: 두 배열의 교집합 II (LeetCode 350)

{% raw %}

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                result.add(nums1[i]);
                i++;
                j++;
            }
        }
        
        return result.stream().mapToInt(x -> x).toArray();
    }
}

// 테스트
int[] nums1 = {1, 2, 2, 1};
int[] nums2 = {2, 2};
System.out.println(Arrays.toString(intersect(nums1, nums2)));  // [2, 2]
```

{% endraw %}

---

### 문제 3: 구간 합 구하기 (백준 11659)

{% raw %}

```java
import java.io.*;
import java.util.*;

public class PrefixSum {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        // 누적 합 배열
        int[] prefixSum = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i-1] + Integer.parseInt(st.nextToken());
        }
        
        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < m; q++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            
            // [i, j] 구간 합 = prefixSum[j] - prefixSum[i-1]
            sb.append(prefixSum[j] - prefixSum[i-1]).append("\n");
        }
        
        System.out.print(sb);
    }
}
```

{% endraw %}

---

### 문제 4: 수 찾기 (백준 1920)

{% raw %}

```java
import java.io.*;
import java.util.*;

public class BinarySearchExample {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(arr);  // 정렬 필수!
        
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            int result = Arrays.binarySearch(arr, target);
            sb.append(result >= 0 ? 1 : 0).append("\n");
        }
        
        System.out.print(sb);
    }
}
```

{% endraw %}

---

## 💡 실전 팁

### 1. 정렬 전략

{% raw %}

```java
// Tip 1: 정렬이 필요한지 판단
// - 이진 탐색? → 필수
// - 투포인터? → 대부분 필요
// - 그리디? → 자주 필요
// - DP? → 상황에 따라

// Tip 2: 정렬 비용 고려
// O(n log n) 정렬 vs O(n²) 완전 탐색
// n이 작으면 정렬 안 해도 됨

// Tip 3: 안정 정렬 필요 시
Arrays.sort(arr);  // 객체는 안정 정렬 (Timsort)
// 기본형은 불안정 정렬 (Quicksort)
```

{% endraw %}

---

### 2. 이진 탐색 주의사항

{% raw %}

```java
// ❌ 오버플로우 위험
int mid = (left + right) / 2;

// ✅ 안전한 방법
int mid = left + (right - left) / 2;

// ❌ 무한 루프 위험
while (left < right) {
    int mid = (left + right) / 2;
    if (check(mid)) {
        left = mid;  // 위험! left가 증가 안 할 수 있음
    } else {
        right = mid - 1;
    }
}

// ✅ 올바른 방법
while (left < right) {
    int mid = (left + right + 1) / 2;  // 올림
    if (check(mid)) {
        left = mid;
    } else {
        right = mid - 1;
    }
}
```

{% endraw %}

---

### 3. 투포인터 디버깅

{% raw %}

```java
// 디버깅 팁: 포인터 움직임 출력
public void twoPointerDebug(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left < right) {
        System.out.printf("left=%d, right=%d, sum=%d%n", 
            left, right, arr[left] + arr[right]);
        
        int sum = arr[left] + arr[right];
        if (sum == target) return;
        else if (sum < target) left++;
        else right--;
    }
}
```

{% endraw %}

---

## 📚 학습 순서

### 초급 (기초 다지기)

1. **Arrays.sort() 사용법** 익히기
2. **Comparator** 람다식으로 작성
3. **이진 탐색** 기본 구현
4. **투포인터** Two Sum 풀기

### 중급 (응용)

1. **2차원 배열 정렬** 연습
2. **Lower/Upper Bound** 구현
3. **슬라이딩 윈도우** 패턴 익히기
4. **파라메트릭 서치** 이해

### 고급 (심화)

1. **커스텀 정렬** 복잡한 조건
2. **회전된 배열** 이진 탐색
3. **세 포인터** 이상 활용
4. **정렬 + 이진 탐색 + 투포인터** 조합

---

## 🎯 추천 문제

### 정렬 (난이도별)

**⭐ Easy**

- LeetCode 88: Merge Sorted Array
- LeetCode 242: Valid Anagram
- LeetCode 349: Intersection of Two Arrays
- 백준 2750: 수 정렬하기

**⭐⭐ Medium**

- LeetCode 75: Sort Colors
- LeetCode 147: Insertion Sort List
- LeetCode 215: Kth Largest Element
- 백준 11399: ATM

**⭐⭐⭐ Hard**

- LeetCode 315: Count of Smaller Numbers After Self
- LeetCode 493: Reverse Pairs

---

### 이진 탐색 (난이도별)

**⭐ Easy**

- LeetCode 704: Binary Search
- LeetCode 35: Search Insert Position
- 백준 10815: 숫자 카드
- 백준 1920: 수 찾기

**⭐⭐ Medium**

- LeetCode 74: Search a 2D Matrix
- LeetCode 162: Find Peak Element
- 백준 1654: 랜선 자르기
- 백준 2805: 나무 자르기

**⭐⭐⭐ Hard**

- LeetCode 4: Median of Two Sorted Arrays
- LeetCode 410: Split Array Largest Sum
- 백준 1300: K번째 수

---

### 투포인터 (난이도별)

**⭐ Easy**

- LeetCode 125: Valid Palindrome
- LeetCode 283: Move Zeroes
- 백준 2470: 두 용액

**⭐⭐ Medium**

- LeetCode 3: Longest Substring Without Repeating Characters
- LeetCode 167: Two Sum II
- 백준 1806: 부분합
- 백준 2003: 수들의 합 2

**⭐⭐⭐ Hard**

- LeetCode 76: Minimum Window Substring
- LeetCode 42: Trapping Rain Water
- 백준 2143: 두 배열의 합

---

## 📝 핵심 체크리스트

### 정렬

- [ ] Arrays.sort() 기본 사용법
- [ ] Comparator 람다식 작성
- [ ] 2차원 배열 정렬
- [ ] 여러 조건 정렬 (thenComparing)
- [ ] 안정/불안정 정렬 차이

### 이진 탐색

- [ ] 기본 이진 탐색 구현
- [ ] Lower Bound 구현
- [ ] Upper Bound 구현
- [ ] 파라메트릭 서치 패턴
- [ ] 회전된 배열 탐색

### 투포인터

- [ ] 양쪽 끝에서 시작 패턴
- [ ] 같은 방향 이동 패턴
- [ ] 슬라이딩 윈도우 패턴
- [ ] 세 포인터 이상 활용
- [ ] 중복 제거 로직

---

## 🔑 암기 필수 코드

### 1. 정렬 템플릿

{% raw %}

```java
// 오름차순
Arrays.sort(arr);

// 내림차순
Arrays.sort(arr, Collections.reverseOrder());

// 커스텀
Arrays.sort(arr, (a, b) -> a.field - b.field);

// 여러 조건
Arrays.sort(arr, 
    Comparator.comparing(Obj::getField1)
              .thenComparing(Obj::getField2));
```

{% endraw %}

---

### 2. 이진 탐색 템플릿

{% raw %}

```java
// 기본
int left = 0, right = arr.length - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}

// Lower Bound
int left = 0, right = arr.length;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] < target) left = mid + 1;
    else right = mid;
}
```

{% endraw %}

---

### 3. 투포인터 템플릿

{% raw %}

```java
// 양쪽 끝
int left = 0, right = arr.length - 1;
while (left < right) {
    if (check(arr[left], arr[right])) {
        // 처리
        left++; right--;
    } else if (need_increase) {
        left++;
    } else {
        right--;
    }
}

// 슬라이딩 윈도우
int left = 0;
for (int right = 0; right < arr.length; right++) {
    // right 추가
    while (invalid_condition) {
        // left 제거
        left++;
    }
    // 답 갱신
}
```

{% endraw %}

---

#Java #정렬 #탐색 #이진탐색 #BinarySearch #투포인터 #TwoPointers #알고리즘 #코딩테스트 #Comparator #Sliding Window #파라메트릭서치

---

### 패턴 3: 세 포인터

{% raw %}

```java
public class ThreePointers {
    // 세 수의 합이 target에 가장 가까운 값
    public int threeSumClosest(int[] arr, int target) {
        Arrays.sort(arr);
        int closest = arr[0] + arr[1] + arr[2];
        
        for (int i = 0; i < arr.length - 2; i++) {
            int left = i + 1;
            int right = arr.length - 1;
            
            while (left < right) {
                int sum = arr[i] + arr[left] + arr[right];
                
                // 더 가까운 값 갱신
                if (Math.abs(sum - target) < Math.abs(closest - target)) {
                    closest = sum;
                }
                
                if (sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    return sum;  // 정확히 일치
                }
            }
        }
        
        return closest;
    }
    
    public static void main(String[] args) {
        int[] arr = {-1, 2, 1, -4};
        ThreePointers tp = new ThreePointers();
        System.out.println(tp.threeSumClosest(arr, 1));  // 2 (-1+2+1)
    }
}
```

{% endraw %}

---

### 투포인터 실전 예제

#### 1. 컨테이너에 가장 많은 물 담기

{% raw %}

```java
public int maxArea(int[] height) {
    int left = 0;
    int right = height.length - 1;
    int maxArea = 0;
    
    while (left < right) {
        // 면적 = 너비 × 높이
        int width = right - left;
        int h = Math.min(height[left], height[right]);
        maxArea = Math.max(maxArea, width * h);
        
        // 더 낮은 쪽 포인터 이동
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}

// 테스트
int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
System.out.println(maxArea(height));  // 49
```

{% endraw %}

---

#### 2. 중복 제거

{% raw %}

```java
public int removeDuplicates(int[] arr) {
    if (arr.length == 0) return 0;
    
    int slow = 0;  // 고유한 요소의 끝
    
    for (int fast = 1; fast < arr.length; fast++) {
        if (arr[fast] != arr[slow]) {
            slow++;
            arr[slow] = arr[fast];
        }
    }
    
    return slow + 1;  // 고유한 요소 개수
}

// 테스트
int[] arr = {1, 1, 2, 2, 2, 3, 4, 4, 5};
int len = removeDuplicates(arr);
System.out.println(len);  // 5
System.out.println(Arrays.toString(Arrays.copyOf(arr, len)));
// [1, 2, 3, 4, 5]
```

{% endraw %}

---

#### 3. 부분 배열의 곱이 k 미만

{% raw %}

```java
public int numSubarrayProductLessThanK(int[] arr, int k) {
    if (k <= 1) return 0;
    
    int left = 0;
    int product = 1;
    int count = 0;
    
    for (int right = 0; right < arr.length; right++) {
        product *= arr[right];
        
        // 곱이 k 이상이면 left 이동
        while (product >= k) {
            product /= arr[left];
            left++;
        }
        
        // [left, right] 사이의 모든 부분 배열
        count += right - left + 1;
    }
    
    return count;
}

// 테스트
int[] arr = {10, 5, 2, 6};
System.out.println(numSubarrayProductLessThanK(arr, 100));  // 8
```

{% endraw %}

---

## 📊 성능 비교

### 시간복잡도

|알고리즘|시간복잡도|공간복잡도|특징|
|---|---|---|---|
|**정렬**||||
|Arrays.sort() (기본형)|O(n log n)|O(log n)|Dual-Pivot Quicksort|
|Arrays.sort() (객체)|O(n log n)|O(n)|Timsort|
|Collections.sort()|O(n log n)|O(n)|Timsort|
|**탐색**||||
|선형 탐색|O(n)|O(1)|정렬 불필요|
|이진 탐색|O(log n)|O(1)|정렬 필수|
|**투포인터**||||
|Two Sum (정렬됨)|O(n)|O(1)|양쪽 끝에서 시작|
|Sliding Window|O(n)|O(1)|같은 방향 이동|

---

## 💡 알고리즘 선택 가이드

### 언제 무엇을 사용할까?

|상황|알고리즘|시간복잡도|
|---|---|---|
|**정렬된 배열에서 값 찾기**|이진 탐색|O(log n)|
|**정렬 안 된 배열에서 값 찾기**|선형 탐색|O(n)|
|**두 수의 합 찾기 (정렬됨)**|투포인터|O(n)|
|**두 수의 합 찾기 (정렬 안 됨)**|HashMap|O(n)|
|**연속 부분 배열의 합**|투포인터 (슬라이딩 윈도우)|O(n)|
|**K번째 큰/작은 수**|QuickSelect 또는 Heap|O(n) avg|
|**정답 범위 찾기**|파라메트릭 서치|O(n log M)|

---

## 🎯 핵심 패턴 정리

### 1. 정렬 후 이진 탐색

{% raw %}

```java
// 패턴: 정렬 → 이진 탐색으로 O(n²) → O(n log n) 최적화
public boolean hasPairWithSum(int[] arr, int target) {
    Arrays.sort(arr);  // O(n log n)
    
    for (int i = 0; i < arr.length; i++) {
        int complement = target - arr[i];
        int idx = Arrays.binarySearch(arr, i + 1, arr.length, complement);
        if (idx >= 0) return true;
    }
    
    return false;
}
```

{% endraw %}

---

### 2. 정렬 후 투포인터

{% raw %}

```java
// 패턴: 정렬 → 투포인터로 효율적 탐색
public List<List<Integer>> threeSum(int[] arr) {
    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(arr);  // 필수!
    
    for (int i = 0; i < arr.length - 2; i++) {
        if (i > 0 && arr[i] == arr[i-1]) continue;  // 중복 제거
        
        int left = i + 1;
        int right = arr.length - 1;
        
        while (left < right) {
            int sum = arr[i] + arr[left] + arr[right];
            
            if (sum == 0) {
                result.add(Arrays.asList(arr[i], arr[left], arr[right]));
                
                // 중복 제거
                while (left < right && arr[left] == arr[left+1]) left++;
                while (left < right && arr[right] == arr[right-1]) right--;
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}
```

{% endraw %}

---

### 3. 슬라이딩 윈도우 (투포인터 변형)

{% raw %}

```java
// 패턴: 윈도우 크기를 동적으로 조절
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0;
    int maxLen = 0;
    
    for (int right = 0; right < s.length(); right++) {
        // 중복 제거할 때까지 left 이동
        while (set.contains(s.charAt(right))) {
            set.remove(s.charAt(left));
            left++;
        }
        
        set.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
}

// 테스트
System.out.println(lengthOfLongestSubstring("abcabcbb"));  // 3 (abc)
System.out.println(lengthOfLongestSubstring("bbbbb"));     // 1 (b)
System.out.println(lengthOfLongestSubstring("pwwkew"));    // 3 (wke)
```

{% endraw %}

---

### 4. 파라메트릭 서치

{% raw %}

```java
// 패턴: 정답의 범위를 이진 탐색으로 좁히기
// 예: 블루레이 만들기 - M개 이하로 나눌 수 있는 최소 크기
public int minBluraySizes(int[] lessons, int m) {
    int left = Arrays.stream(lessons).max().getAsInt();  // 최소: 가장 긴 레슨
    int right = Arrays.stream(lessons).sum();             // 최대: 전체 합
    int result = right;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // mid 크기로 m개 이하로 나눌 수 있는지 확인
        if (canDivide(lessons, m, mid)) {
            result = mid;
            right = mid - 1;  // 더 작은 크기 시도
        } else {
            left = mid + 1;
        }
    }
    
    return result;
}

private boolean canDivide(int[] lessons, int m, int maxSize) {
    int count = 1;
    int sum = 0;
    
    for (int lesson : lessons) {
        if (sum + lesson > maxSize) {
            count++;
            sum = lesson;
            if (count > m) return false;
        } else {
            sum += lesson;
        }
    }
    
    return true;
}
```

{% endraw %}

---

## 🏆 코딩테스트 단골 문제 유형

### 정렬 문제

1. **[LeetCode 56] Merge Intervals** ⭐⭐
    
    - 겹치는 구간 합치기
2. **[LeetCode 148] Sort List** ⭐⭐
    
    - 연결 리스트 정렬
3. **[LeetCode 179] Largest Number** ⭐⭐
    
    - 커스텀 정렬
4. **[프로그래머스] H-Index** ⭐⭐
    
    - 정렬 후 조건 확인
5. **[백준 11650] 좌표 정렬하기** ⭐
    
    - 2차원 배열 정렬

---

### 이진 탐색 문제

1. **[LeetCode 33] Search in Rotated Sorted Array** ⭐⭐
    - 회전된 배열 탐색
2. **[LeetCode 153] Find Minimum in Rotated Sorted Array** ⭐⭐
    - 최솟값 찾기
3. **[LeetCode 34] Find First and Last Position** ⭐⭐
    - Lower/Upper Bound
4. **[백준 2805] 나무 자르기** ⭐⭐
    - 파라메트릭 서치
5. **[백준 1654] 랜선 자르기** ⭐⭐
    - 파라메트릭 서치

---

### 투포인터 문제

1. **[LeetCode 15] 3Sum** ⭐⭐
    - 세 수의 합 = 0
2. **[LeetCode 11] Container With Most Water** ⭐⭐
    - 최대 면적
3. **[LeetCode 42] Trapping Rain Water** ⭐⭐⭐
    - 빗물 가두기
4. **[LeetCode 209] Minimum Size Subarray Sum** ⭐⭐
    - 슬라이딩 윈도우
5. **[백준 2003] 수들의 합 2** ⭐⭐
    - 부분 합

---

## 🎨 실전 문제 풀이

### 문제 1: K개의 가장 가까운 점 (LeetCode 973)

{% raw %}

```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // 거리로 정렬
        Arrays.sort(points, (a, b) -> {
            int distA = a[0] * a[0] + a[1] * a[1];
            int distB = b[0] * b[0] + b[1] * b[1];
            return distA - distB;
        });
        
        // 앞에서 k개 반환
        return Arrays.copyOf(points, k);
    }
}

// 테스트
int[][] points = {{1,3}, {-2,2}, {5,8}, {0,1}};
int[][] result = kClosest(points, 2);
// [[0,1], [-2,2]]
```

{% endraw %}

---

### 문제 2: 두 배열의 교집합 II (LeetCode 350)

{% raw %}

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                result.add(nums1[i]);
                i++;
                j++;
            }
        }
        
        return result.stream().mapToInt(x -> x).toArray();
    }
}

// 테스트
int[] nums1 = {1, 2, 2, 1};
int[] nums2 = {2, 2};
System.out.println(Arrays.toString(intersect(nums1, nums2)));  // [2, 2]
```

{% endraw %}

---

### 문제 3: 구간 합 구하기 (백준 11659)

{% raw %}

```java
import java.io.*;
import java.util.*;

public class PrefixSum {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        // 누적 합 배열
        int[] prefixSum = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i-1] + Integer.parseInt(st.nextToken());
        }
        
        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < m; q++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            
            // [i, j] 구간 합 = prefixSum[j] - prefixSum[i-1]
            sb.append(prefixSum[j] - prefixSum[i-1]).append("\n");
        }
        
        System.out.print(sb);
    }
}
```

{% endraw %}

---

### 문제 4: 수 찾기 (백준 1920)

{% raw %}

```java
import java.io.*;
import java.util.*;

public class BinarySearchExample {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(arr);  // 정렬 필수!
        
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            int result = Arrays.binarySearch(arr, target);
            sb.append(result >= 0 ? 1 : 0).append("\n");
        }
        
        System.out.print(sb);
    }
}
```

{% endraw %}

---

## 💡 실전 팁

### 1. 정렬 전략

{% raw %}

```java
// Tip 1: 정렬이 필요한지 판단
// - 이진 탐색? → 필수
// - 투포인터? → 대부분 필요
// - 그리디? → 자주 필요
// - DP? → 상황에 따라

// Tip 2: 정렬 비용 고려
// O(n log n) 정렬 vs O(n²) 완전 탐색
// n이 작으면 정렬 안 해도 됨

// Tip 3: 안정 정렬 필요 시
Arrays.sort(arr);  // 객체는 안정 정렬 (Timsort)
// 기본형은 불안정 정렬 (Quicksort)
```

{% endraw %}

---

### 2. 이진 탐색 주의사항

{% raw %}

```java
// ❌ 오버플로우 위험
int mid = (left + right) / 2;

// ✅ 안전한 방법
int mid = left + (right - left) / 2;

// ❌ 무한 루프 위험
while (left < right) {
    int mid = (left + right) / 2;
    if (check(mid)) {
        left = mid;  // 위험! left가 증가 안 할 수 있음
    } else {
        right = mid - 1;
    }
}

// ✅ 올바른 방법
while (left < right) {
    int mid = (left + right + 1) / 2;  // 올림
    if (check(mid)) {
        left = mid;
    } else {
        right = mid - 1;
    }
}
```

{% endraw %}

---

### 3. 투포인터 디버깅

{% raw %}

```java
// 디버깅 팁: 포인터 움직임 출력
public void twoPointerDebug(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left < right) {
        System.out.printf("left=%d, right=%d, sum=%d%n", 
            left, right, arr[left] + arr[right]);
        
        int sum = arr[left] + arr[right];
        if (sum == target) return;
        else if (sum < target) left++;
        else right--;
    }
}
```

{% endraw %}

---

## 📚 학습 순서

### 초급 (기초 다지기)

1. **Arrays.sort() 사용법** 익히기
2. **Comparator** 람다식으로 작성
3. **이진 탐색** 기본 구현
4. **투포인터** Two Sum 풀기

### 중급 (응용)

1. **2차원 배열 정렬** 연습
2. **Lower/Upper Bound** 구현
3. **슬라이딩 윈도우** 패턴 익히기
4. **파라메트릭 서치** 이해

### 고급 (심화)

1. **커스텀 정렬** 복잡한 조건
2. **회전된 배열** 이진 탐색
3. **세 포인터** 이상 활용
4. **정렬 + 이진 탐색 + 투포인터** 조합

---

## 🎯 추천 문제

### 정렬 (난이도별)

**⭐ Easy**

- LeetCode 88: Merge Sorted Array
- LeetCode 242: Valid Anagram
- LeetCode 349: Intersection of Two Arrays
- 백준 2750: 수 정렬하기

**⭐⭐ Medium**

- LeetCode 75: Sort Colors
- LeetCode 147: Insertion Sort List
- LeetCode 215: Kth Largest Element
- 백준 11399: ATM

**⭐⭐⭐ Hard**

- LeetCode 315: Count of Smaller Numbers After Self
- LeetCode 493: Reverse Pairs

---

### 이진 탐색 (난이도별)

**⭐ Easy**

- LeetCode 704: Binary Search
- LeetCode 35: Search Insert Position
- 백준 10815: 숫자 카드
- 백준 1920: 수 찾기

**⭐⭐ Medium**

- LeetCode 74: Search a 2D Matrix
- LeetCode 162: Find Peak Element
- 백준 1654: 랜선 자르기
- 백준 2805: 나무 자르기

**⭐⭐⭐ Hard**

- LeetCode 4: Median of Two Sorted Arrays
- LeetCode 410: Split Array Largest Sum
- 백준 1300: K번째 수

---

### 투포인터 (난이도별)

**⭐ Easy**

- LeetCode 125: Valid Palindrome
- LeetCode 283: Move Zeroes
- 백준 2470: 두 용액

**⭐⭐ Medium**

- LeetCode 3: Longest Substring Without Repeating Characters
- LeetCode 167: Two Sum II
- 백준 1806: 부분합
- 백준 2003: 수들의 합 2

**⭐⭐⭐ Hard**

- LeetCode 76: Minimum Window Substring
- LeetCode 42: Trapping Rain Water
- 백준 2143: 두 배열의 합

---

## 📝 핵심 체크리스트

### 정렬

- [ ] Arrays.sort() 기본 사용법
- [ ] Comparator 람다식 작성
- [ ] 2차원 배열 정렬
- [ ] 여러 조건 정렬 (thenComparing)
- [ ] 안정/불안정 정렬 차이

### 이진 탐색

- [ ] 기본 이진 탐색 구현
- [ ] Lower Bound 구현
- [ ] Upper Bound 구현
- [ ] 파라메트릭 서치 패턴
- [ ] 회전된 배열 탐색

### 투포인터

- [ ] 양쪽 끝에서 시작 패턴
- [ ] 같은 방향 이동 패턴
- [ ] 슬라이딩 윈도우 패턴
- [ ] 세 포인터 이상 활용
- [ ] 중복 제거 로직

---

## 🔑 암기 필수 코드

### 1. 정렬 템플릿

{% raw %}

```java
// 오름차순
Arrays.sort(arr);

// 내림차순
Arrays.sort(arr, Collections.reverseOrder());

// 커스텀
Arrays.sort(arr, (a, b) -> a.field - b.field);

// 여러 조건
Arrays.sort(arr, 
    Comparator.comparing(Obj::getField1)
              .thenComparing(Obj::getField2));
```

{% endraw %}

---

### 2. 이진 탐색 템플릿

{% raw %}

```java
// 기본
int left = 0, right = arr.length - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}

// Lower Bound
int left = 0, right = arr.length;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] < target) left = mid + 1;
    else right = mid;
}
```

{% endraw %}

---

### 3. 투포인터 템플릿

{% raw %}

```java
// 양쪽 끝
int left = 0, right = arr.length - 1;
while (left < right) {
    if (check(arr[left], arr[right])) {
        // 처리
        left++; right--;
    } else if (need_increase) {
        left++;
    } else {
        right--;
    }
}

// 슬라이딩 윈도우
int left = 0;
for (int right = 0; right < arr.length; right++) {
    // right 추가
    while (invalid_condition) {
        // left 제거
        left++;
    }
    // 답 갱신
}
```

{% endraw %}

---

#Java #정렬 #탐색 #이진탐색 #BinarySearch #투포인터 #TwoPointers #알고리즘 #코딩테스트 #Comparator #SlidingWindow #파라메트릭서치