// Last updated: 11/08/2026, 11:41:57
class Solution {
    public int singleNumber(int[] nums) {
        int ans=0; 
        for(int i=0; i<nums.length; i++){
            ans ^= nums[i];   
        }
        return ans;    
    }
}