// Last updated: 11/08/2026, 11:41:25
class Solution {
    public int hammingWeight(int n) {
        int count =0;
        while(n!=0){
            if(((n>>0)&1)==1)
        count++;
        n=n>>1;
       }
       return count;
    }

         
}