// Last updated: 11/08/2026, 11:39:59
class Solution {
  public int arraySign(int[] nums) {
    var sign = 1;

    for (var n : nums) {
      if (n == 0) return 0;
      sign *= n > 0 ? 1 : -1;
    }
    return sign;
  }
}