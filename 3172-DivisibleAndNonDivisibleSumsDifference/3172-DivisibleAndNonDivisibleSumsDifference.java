// Last updated: 11/08/2026, 11:39:33
class Solution {
    public int differenceOfSums(int n, int m) {
        int dsum=0,sum=0;
        for(int i =1;i<=n;i++){
            if(i % m ==0){
                dsum+=i; 
            }
            else
                sum+=i;
        }
        return (sum-dsum);
    }
}