# HashMap, HashSet

HashMap과 HashSet은 **해시 테이블(Hash Table)** 기반의 자료구조로, **O(1)** 시간에 데이터를 저장하고 검색할 수 있습니다.

---

## 해시 자료구조 이해

### 해시 테이블의 원리

**해시 함수를 사용하여 키를 배열의 인덱스로 변환**

```
키(Key) → [해시 함수] → 해시 코드 → 배열 인덱스
  "apple"  →  hashCode()  →  12345  →  index 5
```

**구조:**
```
해시 테이블 (배열)
┌─────┬─────┬─────┬─────┬─────┐
│  0  │  1  │  2  │  3  │  4  │
└─────┴─────┴─────┴─────┴─────┘
                    ↓
                 [충돌 처리]
                 Linked List
```

---

### 해시 충돌 (Hash Collision)

**서로 다른 키가 같은 인덱스를 가리키는 경우**

{% raw %}
```java
// 예시: 서로 다른 키가 같은 해시 코드를 가질 수 있음
"Aa".hashCode();  // 2112
"BB".hashCode();  // 2112  ← 충돌!
```
{% endraw %}

#### 충돌 해결 방법

**1. Separate Chaining (분리 연결법)**
- Java HashMap의 기본 방식
- 같은 인덱스에 연결 리스트로 저장
- Java 8+: 리스트가 8개 이상이면 트리로 변환

```
인덱스 3: [Key1, Value1] → [Key2, Value2] → [Key3, Value3]
```

**2. Open Addressing (개방 주소법)**
- 충돌 시 다른 빈 공간을 찾음
- Linear Probing, Quadratic Probing 등

---

### HashMap 내부 구조

{% raw %}
```java
// HashMap 내부 (간단화)
public class HashMap<K, V> {
    // 내부 배열
    Node<K,V>[] table;
    
    // 저장된 요소 개수
    int size;
    
    // 임계값 (capacity * loadFactor)
    int threshold;
    
    // 기본 용량
    static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    // 로드 팩터 (75%)
    static final float DEFAULT_LOAD_FACTOR = 0.75f;
    
    // 노드 구조
    static class Node<K,V> {
        final int hash;
        final K key;
        V value;
        Node<K,V> next;  // 충돌 시 연결
    }
}
```
{% endraw %}

**동작 과정:**
1. `put(key, value)`: 
   - `key.hashCode()` 계산
   - 인덱스 결정: `hash & (capacity - 1)`
   - 해당 위치에 저장 (충돌 시 연결)

2. `get(key)`:
   - `key.hashCode()` 계산
   - 인덱스로 이동
   - `equals()`로 실제 키 비교

---

### Resize (재해싱)

**로드 팩터 초과 시 배열 크기를 2배로 확장**

{% raw %}
```java
// 현재 크기: 16, 로드 팩터: 0.75
// 임계값: 16 * 0.75 = 12

// 12개 저장 후 13번째 추가 시
// → 배열 크기 32로 확장
// → 모든 요소 재배치 (rehashing)
```
{% endraw %}

**시간복잡도:**
- 평균: O(1)
- Resize 발생: O(n)
- **Amortized O(1)**: 평균적으로 O(1)

---

## HashMap 사용법

### 기본 연산

{% raw %}
```java
import java.util.*;

public class HashMapExample {
    public static void main(String[] args) {
        // 생성
        HashMap<String, Integer> map = new HashMap<>();
        
        // 삽입 - O(1)
        map.put("apple", 100);
        map.put("banana", 200);
        map.put("orange", 300);
        
        // 조회 - O(1)
        System.out.println(map.get("apple"));  // 100
        System.out.println(map.get("grape"));  // null
        
        // 기본값과 함께 조회
        System.out.println(map.getOrDefault("grape", 0));  // 0
        
        // 존재 확인 - O(1)
        System.out.println(map.containsKey("banana"));   // true
        System.out.println(map.containsValue(200));      // true
        
        // 삭제 - O(1)
        map.remove("orange");
        
        // 크기
        System.out.println(map.size());  // 2
        
        // 비어있는지 확인
        System.out.println(map.isEmpty());  // false
    }
}
```
{% endraw %}

---

### 주요 메서드

| 메서드 | 설명 | 시간복잡도 |
|--------|------|------------|
| `put(K key, V value)` | 키-값 쌍 저장 | O(1) |
| `get(Object key)` | 값 조회 | O(1) |
| `getOrDefault(K, V)` | 없으면 기본값 반환 | O(1) |
| `remove(Object key)` | 삭제 | O(1) |
| `containsKey(Object)` | 키 존재 확인 | O(1) |
| `containsValue(Object)` | 값 존재 확인 | O(n) |
| `size()` | 크기 반환 | O(1) |
| `isEmpty()` | 비어있는지 확인 | O(1) |
| `clear()` | 모두 삭제 | O(n) |

---

### 순회 방법

{% raw %}
```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("C", 3);

// 1. keySet() - 키만 순회
for (String key : map.keySet()) {
    System.out.println(key + ": " + map.get(key));
}

// 2. values() - 값만 순회
for (Integer value : map.values()) {
    System.out.println(value);
}

// 3. entrySet() - 키-값 쌍 순회 (가장 효율적!)
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// 4. forEach (Java 8+)
map.forEach((key, value) -> 
    System.out.println(key + ": " + value)
);
```
{% endraw %}

**추천:** `entrySet()` 사용 (한 번에 키와 값 모두 접근)

---

### 고급 메서드 (Java 8+)

{% raw %}
```java
HashMap<String, Integer> map = new HashMap<>();

// 1. putIfAbsent - 키가 없을 때만 추가
map.putIfAbsent("apple", 100);
map.putIfAbsent("apple", 200);  // 무시됨
System.out.println(map.get("apple"));  // 100

// 2. compute - 값을 계산하여 저장
map.compute("apple", (key, value) -> value == null ? 1 : value + 1);
System.out.println(map.get("apple"));  // 101

// 3. computeIfAbsent - 키가 없을 때만 계산
map.computeIfAbsent("banana", key -> 50);
System.out.println(map.get("banana"));  // 50

// 4. computeIfPresent - 키가 있을 때만 계산
map.computeIfPresent("apple", (key, value) -> value * 2);
System.out.println(map.get("apple"));  // 202

// 5. merge - 값 병합
map.merge("apple", 10, Integer::sum);  // 기존값 + 10
System.out.println(map.get("apple"));  // 212
```
{% endraw %}

---

## HashMap 문제 해결 패턴

### 패턴 1: 빈도수 세기 (Frequency Count)

{% raw %}
```java
// 문자 빈도수 세기
public Map<Character, Integer> countFrequency(String s) {
    Map<Character, Integer> map = new HashMap<>();
    
    for (char c : s.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
        // 또는: map.merge(c, 1, Integer::sum);
    }
    
    return map;
}

// 사용
Map<Character, Integer> freq = countFrequency("hello");
System.out.println(freq);  // {h=1, e=1, l=2, o=1}
```
{% endraw %}

**응용 문제:**
- 가장 많이 등장한 문자 찾기
- 아나그램 검사
- 문자열 패턴 매칭

---

### 패턴 2: Two Sum (투 포인터 대신 해시)

{% raw %}
```java
// 두 수의 합이 target이 되는 인덱스 찾기
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        
        if (map.containsKey(complement)) {
            return new int[] {map.get(complement), i};
        }
        
        map.put(nums[i], i);
    }
    
    return new int[] {-1, -1};
}

// 테스트
int[] nums = {2, 7, 11, 15};
int[] result = twoSum(nums, 9);
System.out.println(Arrays.toString(result));  // [0, 1]
```
{% endraw %}

**시간복잡도:** O(n) (배열 한 번 순회)

---

### 패턴 3: 그룹화 (Grouping)

{% raw %}
```java
// 아나그램 그룹화
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String str : strs) {
        // 정렬된 문자열을 키로 사용
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        String key = new String(chars);
        
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
    }
    
    return new ArrayList<>(map.values());
}

// 테스트
String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
List<List<String>> groups = groupAnagrams(words);
// [[eat, tea, ate], [tan, nat], [bat]]
```
{% endraw %}

---

### 패턴 4: 캐싱 (Memoization)

{% raw %}
```java
// 피보나치 수열 (메모이제이션)
class Fibonacci {
    private Map<Integer, Long> memo = new HashMap<>();
    
    public long fib(int n) {
        if (n <= 1) return n;
        
        // 캐시에 있으면 반환
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        
        // 계산 후 캐시에 저장
        long result = fib(n - 1) + fib(n - 2);
        memo.put(n, result);
        
        return result;
    }
}

// 사용
Fibonacci f = new Fibonacci();
System.out.println(f.fib(50));  // 빠르게 계산!
```
{% endraw %}

---

### 패턴 5: 중복 제거 (Deduplication)

{% raw %}
```java
// 중복되지 않는 첫 번째 문자 찾기
public int firstUniqChar(String s) {
    Map<Character, Integer> count = new HashMap<>();
    
    // 1. 빈도수 세기
    for (char c : s.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) + 1);
    }
    
    // 2. 첫 번째 고유 문자 찾기
    for (int i = 0; i < s.length(); i++) {
        if (count.get(s.charAt(i)) == 1) {
            return i;
        }
    }
    
    return -1;
}

// 테스트
System.out.println(firstUniqChar("leetcode"));     // 0 (l)
System.out.println(firstUniqChar("loveleetcode")); // 2 (v)
```
{% endraw %}

---

### 패턴 6: 윈도우 내 요소 추적

{% raw %}
```java
// 연속된 K개의 고유 정수
public int lengthOfLongestSubstringKDistinct(String s, int k) {
    Map<Character, Integer> map = new HashMap<>();
    int left = 0, maxLen = 0;
    
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        map.put(c, map.getOrDefault(c, 0) + 1);
        
        // 고유 문자가 k개 초과하면 왼쪽 축소
        while (map.size() > k) {
            char leftChar = s.charAt(left);
            map.put(leftChar, map.get(leftChar) - 1);
            if (map.get(leftChar) == 0) {
                map.remove(leftChar);
            }
            left++;
        }
        
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
}
```
{% endraw %}

---

## HashSet 사용법

### 기본 개념

**HashSet = HashMap의 Key만 사용**

{% raw %}
```java
// 내부 구조
public class HashSet<E> {
    private HashMap<E, Object> map;  // Value는 더미 객체
    private static final Object PRESENT = new Object();
    
    public boolean add(E e) {
        return map.put(e, PRESENT) == null;
    }
}
```
{% endraw %}

---

### 기본 연산

{% raw %}
```java
import java.util.*;

public class HashSetExample {
    public static void main(String[] args) {
        // 생성
        HashSet<String> set = new HashSet<>();
        
        // 추가 - O(1)
        set.add("apple");
        set.add("banana");
        set.add("orange");
        set.add("apple");  // 중복, 무시됨
        
        System.out.println(set);  // [banana, orange, apple]
        
        // 존재 확인 - O(1)
        System.out.println(set.contains("apple"));  // true
        
        // 삭제 - O(1)
        set.remove("banana");
        
        // 크기
        System.out.println(set.size());  // 2
        
        // 순회
        for (String item : set) {
            System.out.println(item);
        }
        
        // 모두 삭제
        set.clear();
    }
}
```
{% endraw %}

---

### 주요 메서드

| 메서드 | 설명 | 시간복잡도 |
|--------|------|------------|
| `add(E e)` | 요소 추가 | O(1) |
| `remove(Object o)` | 요소 삭제 | O(1) |
| `contains(Object o)` | 존재 확인 | O(1) |
| `size()` | 크기 반환 | O(1) |
| `isEmpty()` | 비어있는지 확인 | O(1) |
| `clear()` | 모두 삭제 | O(n) |

---

### 집합 연산

{% raw %}
```java
HashSet<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
HashSet<Integer> set2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));

// 1. 합집합 (Union)
HashSet<Integer> union = new HashSet<>(set1);
union.addAll(set2);
System.out.println(union);  // [1, 2, 3, 4, 5, 6, 7, 8]

// 2. 교집합 (Intersection)
HashSet<Integer> intersection = new HashSet<>(set1);
intersection.retainAll(set2);
System.out.println(intersection);  // [4, 5]

// 3. 차집합 (Difference)
HashSet<Integer> difference = new HashSet<>(set1);
difference.removeAll(set2);
System.out.println(difference);  // [1, 2, 3]

// 4. 부분집합 확인
HashSet<Integer> subset = new HashSet<>(Arrays.asList(1, 2));
System.out.println(set1.containsAll(subset));  // true
```
{% endraw %}

---

## HashSet 문제 해결 패턴

### 패턴 1: 중복 제거

{% raw %}
```java
// 배열에서 중복 제거
public int[] removeDuplicates(int[] nums) {
    HashSet<Integer> set = new HashSet<>();
    for (int num : nums) {
        set.add(num);
    }
    
    return set.stream().mapToInt(Integer::intValue).toArray();
}

// 또는 간단하게
public List<Integer> removeDuplicates(List<Integer> list) {
    return new ArrayList<>(new HashSet<>(list));
}
```
{% endraw %}

---

### 패턴 2: 존재 여부 빠른 확인

{% raw %}
```java
// 배열에 중복이 있는지 확인
public boolean containsDuplicate(int[] nums) {
    HashSet<Integer> set = new HashSet<>();
    
    for (int num : nums) {
        if (!set.add(num)) {  // add()가 false를 반환하면 중복
            return true;
        }
    }
    
    return false;
}

// 테스트
int[] nums1 = {1, 2, 3, 1};
System.out.println(containsDuplicate(nums1));  // true

int[] nums2 = {1, 2, 3, 4};
System.out.println(containsDuplicate(nums2));  // false
```
{% endraw %}

---

### 패턴 3: 두 배열의 교집합

{% raw %}
```java
// 두 배열의 교집합 (중복 제거)
public int[] intersection(int[] nums1, int[] nums2) {
    HashSet<Integer> set1 = new HashSet<>();
    HashSet<Integer> result = new HashSet<>();
    
    for (int num : nums1) {
        set1.add(num);
    }
    
    for (int num : nums2) {
        if (set1.contains(num)) {
            result.add(num);
        }
    }
    
    return result.stream().mapToInt(Integer::intValue).toArray();
}

// 테스트
int[] nums1 = {1, 2, 2, 1};
int[] nums2 = {2, 2};
int[] result = intersection(nums1, nums2);
System.out.println(Arrays.toString(result));  // [2]
```
{% endraw %}

---

### 패턴 4: 가장 긴 연속 수열

{% raw %}
```java
// 정렬하지 않고 가장 긴 연속 수열 길이 찾기
public int longestConsecutive(int[] nums) {
    HashSet<Integer> set = new HashSet<>();
    for (int num : nums) {
        set.add(num);
    }
    
    int longest = 0;
    
    for (int num : set) {
        // 시퀀스의 시작점인지 확인
        if (!set.contains(num - 1)) {
            int currentNum = num;
            int currentStreak = 1;
            
            // 연속된 숫자 카운트
            while (set.contains(currentNum + 1)) {
                currentNum++;
                currentStreak++;
            }
            
            longest = Math.max(longest, currentStreak);
        }
    }
    
    return longest;
}

// 테스트
int[] nums = {100, 4, 200, 1, 3, 2};
System.out.println(longestConsecutive(nums));  // 4 (1,2,3,4)
```
{% endraw %}

**시간복잡도:** O(n) - 각 숫자는 시작점일 때만 확인

---

### 패턴 5: 해피 넘버 (사이클 감지)

{% raw %}
```java
// 해피 넘버: 각 자릿수 제곱의 합이 1이 되는지
public boolean isHappy(int n) {
    HashSet<Integer> seen = new HashSet<>();
    
    while (n != 1 && !seen.contains(n)) {
        seen.add(n);
        n = getNext(n);
    }
    
    return n == 1;
}

private int getNext(int n) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

// 테스트
System.out.println(isHappy(19));  // true (1²+9²=82 → 8²+2²=68 → ... → 1)
System.out.println(isHappy(2));   // false (사이클)
```
{% endraw %}

---

## HashMap vs HashSet vs TreeMap vs TreeSet

| 특성 | HashMap | HashSet | TreeMap | TreeSet |
|------|---------|---------|---------|---------|
| **구조** | Key-Value | Key만 | Key-Value 정렬 | Key만 정렬 |
| **순서** | 없음 | 없음 | 정렬됨 | 정렬됨 |
| **중복 Key** | 불가 | 불가 | 불가 | 불가 |
| **null 허용** | 1개 | 1개 | 불가 | 불가 |
| **삽입/검색** | O(1) | O(1) | O(log n) | O(log n) |
| **사용 시점** | 빠른 검색 | 중복 제거 | 정렬 필요 | 정렬 필요 |

---

## ⚠️ 주의사항

### 1. equals()와 hashCode() 오버라이드

{% raw %}
```java
// ✘ 잘못된 예
class Person {
    String name;
    int age;
    
    // equals와 hashCode 미구현
}

Person p1 = new Person("John", 25);
Person p2 = new Person("John", 25);

HashSet<Person> set = new HashSet<>();
set.add(p1);
set.add(p2);
System.out.println(set.size());  // 2 (같은 사람인데 중복!)


// ✔ 올바른 예
class Person {
    String name;
    int age;
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Objects.equals(name, person.name);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}

set.add(p1);
set.add(p2);
System.out.println(set.size());  // 1 (올바르게 중복 제거)
```
{% endraw %}

---

### 2. Mutable 객체를 Key로 사용 금지

{% raw %}
```java
// ✘ 위험한 코드
class MutableKey {
    int value;
    
    public void setValue(int value) {
        this.value = value;
    }
    
    // equals, hashCode 구현...
}

MutableKey key = new MutableKey();
key.value = 10;

HashMap<MutableKey, String> map = new HashMap<>();
map.put(key, "value");

key.value = 20;  // Key 변경!
System.out.println(map.get(key));  // null! (해시 코드 변경됨)
```
{% endraw %}

**해결책:** Immutable 객체 사용 (String, Integer 등)

---

### 3. Thread-Safety

{% raw %}
```java
// HashMap은 Thread-Safe하지 않음

// 방법 1: ConcurrentHashMap 사용
Map<String, Integer> map = new ConcurrentHashMap<>();

// 방법 2: Collections.synchronizedMap
Map<String, Integer> syncMap = 
    Collections.synchronizedMap(new HashMap<>());
```
{% endraw %}

---

## 💡 성능 최적화 팁

### 1. 초기 용량 지정

{% raw %}
```java
// ✘ 기본 용량 (16)
HashMap<String, Integer> map1 = new HashMap<>();

// ✔ 예상 크기만큼 미리 할당
HashMap<String, Integer> map2 = new HashMap<>(1000);

// 재할당 횟수 감소 → 성능 향상
```
{% endraw %}

---

### 2. 로드 팩터 조정

{% raw %}
```java
// 기본 로드 팩터: 0.75 (75%)
HashMap<String, Integer> map1 = new HashMap<>();

// 메모리 절약 (충돌 증가)
HashMap<String, Integer> map2 = new HashMap<>(16, 0.9f);

// 속도 우선 (메모리 증가)
HashMap<String, Integer> map3 = new HashMap<>(16, 0.5f);
```
{% endraw %}

---

### 3. containsValue() 사용 주의

{% raw %}
```java
// ✘ O(n) - 느림
if (map.containsValue(100)) {
    // ...
}

// ✔ 값으로도 검색이 필요하면 역방향 Map 유지
HashMap<String, Integer> nameToAge = new HashMap<>();
HashMap<Integer, String> ageToName = new HashMap<>();

nameToAge.put("John", 25);
ageToName.put(25, "John");

// O(1)로 양방향 검색 가능
```
{% endraw %}

---

## 코딩테스트 단골 문제

### HashMap 문제
1. **Two Sum** - LeetCode 1
2. **Group Anagrams** - LeetCode 49
3. **Subarray Sum Equals K** - LeetCode 560
4. **LRU Cache** - LeetCode 146
5. **First Unique Character** - LeetCode 387

### HashSet 문제
1. **Contains Duplicate** - LeetCode 217
2. **Intersection of Two Arrays** - LeetCode 349
3. **Longest Consecutive Sequence** - LeetCode 128
4. **Happy Number** - LeetCode 202
5. **Valid Sudoku** - LeetCode 36

---

## 핵심 정리

### 언제 사용할까?

**HashMap:**
- 키-값 매핑이 필요할 때
- 빈도수 계산
- 빠른 검색/삽입/삭제
- 캐싱, 메모이제이션

**HashSet:**
- 중복 제거
- 존재 여부만 확인
- 집합 연산 (합집합, 교집합)
- 방문 체크

### 기억할 것

1. **평균 O(1)** 시간복잡도
2. **순서 보장 안 됨** (LinkedHashMap 사용 시 가능)
3. **equals()와 hashCode() 필수**
4. **Key는 Immutable 권장**
5. **초기 용량 지정**으로 성능 향상

---

## 실전 문제 풀이

### 문제 1: 로마 숫자를 정수로 변환

{% raw %}
```java
public int romanToInt(String s) {
    Map<Character, Integer> map = new HashMap<>();
    map.put('I', 1);
    map.put('V', 5);
    map.put('X', 10);
    map.put('L', 50);
    map.put('C', 100);
    map.put('D', 500);
    map.put('M', 1000);
    
    int result = 0;
    int prevValue = 0;
    
    for (int i = s.length() - 1; i >= 0; i--) {
        int currentValue = map.get(s.charAt(i));
        
        if (currentValue < prevValue) {
            result -= currentValue;  // IV = 5 - 1
        } else {
            result += currentValue;
        }
        
        prevValue = currentValue;
    }
    
    return result;
}

// 테스트
System.out.println(romanToInt("III"));     // 3
System.out.println(romanToInt("LVIII"));   // 58
System.out.println(romanToInt("MCMXCIV")); // 1994
```
{% endraw %}

---

### 문제 2: 부분 배열의 합이 K인 경우의 수

{% raw %}
```java
// Prefix Sum + HashMap
public int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> prefixSumCount = new HashMap<>();
    prefixSumCount.put(0, 1);  // 초기값
    
    int count = 0;
    int sum = 0;
    
    for (int num : nums) {
        sum += num;
        
        // sum - k가 이전에 나왔다면
        // 그 지점부터 현재까지의 합이 k
        if (prefixSumCount.containsKey(sum - k)) {
            count += prefixSumCount.get(sum - k);
        }
        
        prefixSumCount.put(sum, prefixSumCount.getOrDefault(sum, 0) + 1);
    }
    
    return count;
}

// 테스트
int[] nums = {1, 1, 1};
System.out.println(subarraySum(nums, 2));  // 2 ([1,1], [1,1])

int[] nums2 = {1, 2, 3};
System.out.println(subarraySum(nums2, 3)); // 2 ([1,2], [3])
```
{% endraw %}

**시간복잡도:** O(n)
**핵심:** Prefix Sum을 HashMap에 저장하여 부분합 빠르게 계산

---

### 문제 3: 가장 많이 등장한 K개의 요소

{% raw %}
```java
public int[] topKFrequent(int[] nums, int k) {
    // 1. 빈도수 계산
    Map<Integer, Integer> count = new HashMap<>();
    for (int num : nums) {
        count.put(num, count.getOrDefault(num, 0) + 1);
    }
    
    // 2. 우선순위 큐 (빈도수 기준 최대 힙)
    PriorityQueue<Map.Entry<Integer, Integer>> pq = 
        new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
    
    pq.addAll(count.entrySet());
    
    // 3. 상위 K개 추출
    int[] result = new int[k];
    for (int i = 0; i < k; i++) {
        result[i] = pq.poll().getKey();
    }
    
    return result;
}

// 테스트
int[] nums = {1, 1, 1, 2, 2, 3};
int[] result = topKFrequent(nums, 2);
System.out.println(Arrays.toString(result));  // [1, 2]
```
{% endraw %}

---

### 문제 4: 이진 트리의 수직 순회

{% raw %}
```java
public List<List<Integer>> verticalOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    // 열 번호 → 노드 값 리스트
    Map<Integer, List<Integer>> map = new HashMap<>();
    
    // BFS + 열 번호 추적
    Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
    queue.offer(new Pair<>(root, 0));
    
    int minCol = 0, maxCol = 0;
    
    while (!queue.isEmpty()) {
        Pair<TreeNode, Integer> pair = queue.poll();
        TreeNode node = pair.getKey();
        int col = pair.getValue();
        
        map.computeIfAbsent(col, k -> new ArrayList<>()).add(node.val);
        
        minCol = Math.min(minCol, col);
        maxCol = Math.max(maxCol, col);
        
        if (node.left != null) {
            queue.offer(new Pair<>(node.left, col - 1));
        }
        if (node.right != null) {
            queue.offer(new Pair<>(node.right, col + 1));
        }
    }
    
    // 열 순서대로 결과 생성
    for (int i = minCol; i <= maxCol; i++) {
        result.add(map.get(i));
    }
    
    return result;
}
```
{% endraw %}

---

### 문제 5: 랜섬 노트 (Ransom Note)

{% raw %}
```java
// magazine의 글자로 ransomNote를 만들 수 있는지
public boolean canConstruct(String ransomNote, String magazine) {
    Map<Character, Integer> count = new HashMap<>();
    
    // magazine 글자 세기
    for (char c : magazine.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) + 1);
    }
    
    // ransomNote 글자 확인
    for (char c : ransomNote.toCharArray()) {
        if (!count.containsKey(c) || count.get(c) == 0) {
            return false;
        }
        count.put(c, count.get(c) - 1);
    }
    
    return true;
}

// 테스트
System.out.println(canConstruct("a", "b"));        // false
System.out.println(canConstruct("aa", "aab"));     // true
System.out.println(canConstruct("aa", "ab"));      // false
```
{% endraw %}

**최적화:** 알파벳만 사용한다면 `int[26]` 배열이 더 빠름

{% raw %}
```java
public boolean canConstructOptimized(String ransomNote, String magazine) {
    int[] count = new int[26];
    
    for (char c : magazine.toCharArray()) {
        count[c - 'a']++;
    }
    
    for (char c : ransomNote.toCharArray()) {
        if (--count[c - 'a'] < 0) {
            return false;
        }
    }
    
    return true;
}
```
{% endraw %}

---

### 문제 6: 동형 문자열 (Isomorphic Strings)

{% raw %}
```java
// s와 t가 동형인지 확인 (일대일 매핑)
public boolean isIsomorphic(String s, String t) {
    if (s.length() != t.length()) return false;
    
    Map<Character, Character> mapS = new HashMap<>();
    Map<Character, Character> mapT = new HashMap<>();
    
    for (int i = 0; i < s.length(); i++) {
        char c1 = s.charAt(i);
        char c2 = t.charAt(i);
        
        // s → t 매핑 확인
        if (mapS.containsKey(c1)) {
            if (mapS.get(c1) != c2) return false;
        } else {
            mapS.put(c1, c2);
        }
        
        // t → s 매핑 확인 (양방향)
        if (mapT.containsKey(c2)) {
            if (mapT.get(c2) != c1) return false;
        } else {
            mapT.put(c2, c1);
        }
    }
    
    return true;
}

// 테스트
System.out.println(isIsomorphic("egg", "add"));   // true
System.out.println(isIsomorphic("foo", "bar"));   // false
System.out.println(isIsomorphic("paper", "title")); // true
```
{% endraw %}

---

### 문제 7: 단어 패턴 (Word Pattern)

{% raw %}
```java
public boolean wordPattern(String pattern, String s) {
    String[] words = s.split(" ");
    if (pattern.length() != words.length) return false;
    
    Map<Character, String> charToWord = new HashMap<>();
    Map<String, Character> wordToChar = new HashMap<>();
    
    for (int i = 0; i < pattern.length(); i++) {
        char c = pattern.charAt(i);
        String word = words[i];
        
        // 문자 → 단어 매핑
        if (charToWord.containsKey(c)) {
            if (!charToWord.get(c).equals(word)) return false;
        } else {
            charToWord.put(c, word);
        }
        
        // 단어 → 문자 매핑
        if (wordToChar.containsKey(word)) {
            if (wordToChar.get(word) != c) return false;
        } else {
            wordToChar.put(word, c);
        }
    }
    
    return true;
}

// 테스트
System.out.println(wordPattern("abba", "dog cat cat dog"));  // true
System.out.println(wordPattern("abba", "dog cat cat fish")); // false
System.out.println(wordPattern("aaaa", "dog cat cat dog"));  // false
```
{% endraw %}

---

## 고급 패턴

### 패턴 1: LRU Cache 구현

{% raw %}
```java
class LRUCache {
    private int capacity;
    private LinkedHashMap<Integer, Integer> cache;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        // accessOrder = true → 접근 순서 유지
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > capacity;
            }
        };
    }
    
    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        cache.put(key, value);
    }
}

// 사용
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
System.out.println(cache.get(1));    // 1
cache.put(3, 3);                     // 2 제거됨
System.out.println(cache.get(2));    // -1
```
{% endraw %}

---

### 패턴 2: Trie를 HashMap으로 구현

{% raw %}
```java
class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;
    
    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return true;
    }
}
```
{% endraw %}

---

### 패턴 3: Union-Find를 HashMap으로

{% raw %}
```java
class UnionFind {
    private Map<Integer, Integer> parent;
    private Map<Integer, Integer> rank;
    
    public UnionFind() {
        parent = new HashMap<>();
        rank = new HashMap<>();
    }
    
    public void add(int x) {
        if (!parent.containsKey(x)) {
            parent.put(x, x);
            rank.put(x, 0);
        }
    }
    
    public int find(int x) {
        if (parent.get(x) != x) {
            parent.put(x, find(parent.get(x)));  // 경로 압축
        }
        return parent.get(x);
    }
    
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            // Rank 기반 합치기
            if (rank.get(rootX) < rank.get(rootY)) {
                parent.put(rootX, rootY);
            } else if (rank.get(rootX) > rank.get(rootY)) {
                parent.put(rootY, rootX);
            } else {
                parent.put(rootY, rootX);
                rank.put(rootX, rank.get(rootX) + 1);
            }
        }
    }
    
    public boolean connected(int x, int y) {
        return find(x) == find(y);
    }
}
```
{% endraw %}

---

## 성능 비교 실험

{% raw %}
```java
public class HashPerformanceTest {
    public static void main(String[] args) {
        int n = 1000000;
        
        // HashMap 성능 테스트
        long start = System.currentTimeMillis();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, i);
        }
        for (int i = 0; i < n; i++) {
            map.get(i);
        }
        System.out.println("HashMap: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // TreeMap 성능 테스트
        start = System.currentTimeMillis();
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            treeMap.put(i, i);
        }
        for (int i = 0; i < n; i++) {
            treeMap.get(i);
        }
        System.out.println("TreeMap: " + 
            (System.currentTimeMillis() - start) + "ms");
        
        // ArrayList 검색 성능 (비교용)
        start = System.currentTimeMillis();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(i);
        }
        for (int i = 0; i < n; i++) {
            list.contains(i);
        }
        System.out.println("ArrayList: " + 
            (System.currentTimeMillis() - start) + "ms");
    }
}

/* 예상 출력 (100만 건):
HashMap: 150ms    (O(1))
TreeMap: 800ms    (O(log n))
ArrayList: 매우 느림 (O(n²))
*/
```
{% endraw %}

---

## 면접 준비 핵심 질문

### Q1: HashMap의 시간복잡도가 항상 O(1)인가요?

**답변:**
- **평균:** O(1)
- **최악:** O(n) (모든 키가 같은 버킷에 충돌)
- **Java 8+:** 버킷이 트리로 변환되면 O(log n)

### Q2: HashMap과 Hashtable의 차이는?

| 특성 | HashMap | Hashtable |
|------|---------|-----------|
| Null 키/값 | 허용 | 불가 |
| 동기화 | X | O (느림) |
| 상속 | AbstractMap | Dictionary (레거시) |
| 사용 | 권장 | 비권장 |

### Q3: 언제 TreeMap을 사용하나요?

**TreeMap 사용 시기:**
- 키의 정렬이 필요할 때
- 범위 검색이 필요할 때 (`subMap()`, `headMap()`, `tailMap()`)
- 최소/최대 키가 필요할 때 (`firstKey()`, `lastKey()`)

---

## 추가 학습 자료

### 관련 자료구조
- **LinkedHashMap**: 삽입 순서 유지
- **ConcurrentHashMap**: Thread-safe
- **WeakHashMap**: 약한 참조로 메모리 관리
- **IdentityHashMap**: 객체 동일성(`==`)으로 비교

### 학습 순서
1. HashMap/HashSet 기본 (이 문서)
2. TreeMap/TreeSet (정렬된 맵)
3. LinkedHashMap (순서 유지)
4. ConcurrentHashMap (동시성)

---

## 최종 체크리스트

- [ ] HashMap의 내부 구조 이해
- [ ] 해시 충돌 해결 방법 숙지
- [ ] equals()와 hashCode() 관계 이해
- [ ] 6가지 HashMap 패턴 암기
- [ ] 5가지 HashSet 패턴 암기
- [ ] LRU Cache 구현 가능
- [ ] 시간복잡도 분석 가능
- [ ] 실전 문제 10개 이상 풀이

---
## 🏷️ Keywords
`#Java` `#자료구조` `#HashMap` `#HashSet` `#해시테이블` `#알고리즘` `#코딩테스트`  
 `#LeetCode` `#시간복잡도` `#해시충돌` `#면접준비`