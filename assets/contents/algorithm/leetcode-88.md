
# LeetCode 88: Merge Sorted Array 

## 📊 결과
- **소요시간:** 1h
- **Runtime:** 0ms (100%)
- **Memory:** 42.29MB


## 💻 내 코드 (Try 1)

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int mIndex = 0;
        int nIndex = 0;
        int index = 0;
        int[] scan = new int[m];

        for (int i = 0; i < m; i++) {
            scan[i] = nums1[i];
        }

        while (true) {
            if (index == m + n) {
                break;
            }

            if (nIndex >= n && mIndex < m) {
                for (int i = 0; i < m - mIndex; i++) {
                    nums1[index + i] = scan[mIndex + i];
                }
                break;
            }

            if (mIndex >= m && nIndex < n) {
                for (int i = 0; i < n - nIndex; i++) {
                    nums1[index + i] = nums2[nIndex + i];
                }
                break;
            }

            if (scan[mIndex] <= nums2[nIndex]) {
                nums1[index] = scan[mIndex];
                mIndex++;
            } else {
                nums1[index] = nums2[nIndex];
                nIndex++;
            }
            index++;
        }
    }
}
````



## 📝 평가

### ✅ 잘한 점

1. **정확한 동작**
    
    - 두 정렬된 배열을 올바르게 병합
    - 모든 엣지 케이스 처리
2. **Two Pointer 활용**
    
    - 병합 정렬의 핵심 아이디어 이해
    - mIndex, nIndex로 각 배열 추적
3. **임시 배열 사용**
    
    - nums1이 덮어씌워지는 문제 해결
    - scan 배열로 원본 값 보존

---

## 🔴 개선점

### 1. 불필요한 복잡성

```java
// ❌ while(true) + 복잡한 break 조건
while (true) {
    if (index == m + n) break;
    if (nIndex >= n && mIndex < m) { ... break; }
    if (mIndex >= m && nIndex < n) { ... break; }
    // ...
}

// ✅ 명확한 조건문
while (mIndex < m && nIndex < n) {
    // 메인 로직
}
// 남은 요소 처리
```

### 2. 공간 복잡도 비효율

- **현재:** O(m) - scan 배열 사용
- **최적:** O(1) - 뒤에서부터 채우기

### 3. 중복 코드

```java
// 남은 요소를 복사하는 로직이 중복됨
for (int i = 0; i < m - mIndex; i++) {
    nums1[index + i] = scan[mIndex + i];
}
// vs
for (int i = 0; i < n - nIndex; i++) {
    nums1[index + i] = nums2[nIndex + i];
}
```

---

## ✨ 최적화된 풀이

### 방법 1: 뒤에서부터 채우기 (추천!)

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;      // nums1의 마지막 요소
        int j = n - 1;      // nums2의 마지막 요소
        int k = m + n - 1;  // 채울 위치
        
        // 뒤에서부터 큰 값부터 채우기
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}
```

**장점:**

- 공간복잡도 O(1)
- 코드 간결
- nums1을 덮어쓸 걱정 없음 (뒤부터 채우므로)

---

### 방법 2: 앞에서부터 (내 방식 개선)

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] copy = Arrays.copyOf(nums1, m);  // 더 간결
        int i = 0, j = 0, k = 0;
        
        // 메인 병합
        while (i < m && j < n) {
            if (copy[i] <= nums2[j]) {
                nums1[k++] = copy[i++];
            } else {
                nums1[k++] = nums2[j++];
            }
        }
        
        // 남은 요소 처리 (System.arraycopy 활용)
        if (i < m) {
            System.arraycopy(copy, i, nums1, k, m - i);
        }
        if (j < n) {
            System.arraycopy(nums2, j, nums1, k, n - j);
        }
    }
}
```

---

## 📊 성능 비교

|방법|시간복잡도|공간복잡도|코드 길이|
|---|---|---|---|
|**내 코드**|O(m+n)|O(m)|30줄|
|**방법 1 (뒤에서)**|O(m+n)|O(1) ⭐|10줄|
|**방법 2 (개선)**|O(m+n)|O(m)|15줄|

---

## 💡 핵심 인사이트

### 배운 점

1. **뒤에서부터 채우는 발상**
    - In-place 알고리즘에서 자주 사용
    - 덮어쓰기 문제 해결

2. **코드 간결성**
    - `while(true)` 대신 명확한 조건
    - 중복 로직 제거

3. **System.arraycopy 활용**
    - Java 내장 메서드로 더 빠름
    - 가독성 향상

---

## 🎯 개선 후 코드 (Try 1)

```java
class Solution {

	public void merge(int[] nums1, int m, int[] nums2, int n) {

		int p = m+n-1;
		int np = n-1;
		int mp = m-1;

		while(np>=0){
			if(mp>=0 && nums1[mp]>nums2[np]){
				nums1[p--]=nums1[mp--];
			}else{
				nums1[p--]=nums2[np--];
			}
		}
	}
}
```

**변경 사항:**

- ✂️ scan 배열 제거 (공간 절약)
- 🔄 뒤에서부터 채우기로 변경
- 📉 코드 길이 70% 감소
- 🚀 공간복잡도 O(m) → O(1)

---

## 📚 관련 개념

### Two Pointer 패턴

- **앞에서 만나기:** Two Sum, Container With Most Water
- **뒤에서 만나기:** Merge Sorted Array ⭐
- **빠른/느린 포인터:** Linked List Cycle

### In-Place 알고리즘

- 추가 공간 최소화
- 원본 배열 활용
- 뒤에서부터 처리가 핵심

---

## 🎓 다음 단계

### 비슷한 문제

1. <a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank">LeetCode 88: Merge Sorted Array</a>
2. <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">LeetCode 21: Merge Two Sorted Lists</a>
3. <a href="https://leetcode.com/problems/sort-colors/" target="_blank">LeetCode 75: Sort Colors</a> (Dutch Flag)

### 연습 포인트

- [ ] 뒤에서부터 채우는 방식 숙달
- [ ] In-place 알고리즘 이해
- [ ] Two Pointer 다양한 패턴 학습

---

#LeetCode #TwoPointer #MergeSortedArray #알고리즘 #코딩테스트 #Java #InPlace