// Last updated: 11/08/2026, 11:41:05
class Solution {
    public int missingNumber(int[] nums) {
      Arrays.sort(nums);
        
        for(int i=0;i<nums.length;i++) {
        	if(nums[i] != i) {
        		return i;
        	}
        }
        return nums.length;  
    }
}