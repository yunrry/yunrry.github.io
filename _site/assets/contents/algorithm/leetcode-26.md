

### try 1
17m | 18ms | 44.92MB
```java
class Solution {

	public int removeDuplicates(int[] nums) {
	
		List<Integer> list = new ArrayList<Integer>();
		for(int val : nums){
			if(!list.contains(val)){
				list.add(val);
			}
		}
		
	  int k = list.size();
	  
		for(int i=0; i<nums.length; i++){
			if(i<k){
				nums[i]=list.get(i);
			}else{
				nums[i]=0;

			}
		}
	
	return k;
	
	}
}
```


###  문제점

1. **`list.contains(val)` - O(n)**
    - 매번 리스트 전체를 순회
    - 전체 시간복잡도: **O(n²)**
2. **불필요한 추가 공간**
    - ArrayList 사용 (공간복잡도 O(n))
    - 문제는 **in-place** 해결 요구
3. **배열이 이미 정렬되어 있음을 활용 안 함**
    - 정렬된 배열에서는 중복이 연속됨!


### Two Pointer 

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        
        int k = 1;  // 고유한 요소 개수
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
}
```


### 비교

| 항목    | 기존 코드 | 최적화 코드 |
| ----- | ----- | ------ |
| 시간복잡도 | O(n²) | O(n)   |
| 공간복잡도 | O(n)  | O(1)   |
| 런타임   | 18ms  | 1ms    |

