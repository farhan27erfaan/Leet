// Last updated: 11/08/2026, 11:40:00
class Solution {
    public int numIdenticalPairs(int[] nums) {
        int n = nums.length;
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j] && i < j) {
                    count++;
                }
            }

        }

        return count;
    }
}