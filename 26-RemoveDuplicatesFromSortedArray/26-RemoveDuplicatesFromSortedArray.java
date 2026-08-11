// Last updated: 11/08/2026, 11:42:58
class Solution {
  public int removeDuplicates(int[] nums) {
    int i = 0;

    for ( int num : nums)
      if (i < 1 || num > nums[i - 1])
        nums[i++] = num;

    return i;
  }
}