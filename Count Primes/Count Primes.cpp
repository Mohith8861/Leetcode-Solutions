// https://leetcode.com/problems/count-primes

class Solution {
public:
    int countPrimes(int n) {
        if(n <= 1)
            return 0;
        vector<int> a (n + 1,0);
        int A = 0;
        a[0] = 1;
        a[1] = 1;
        for(int i = 2; i < n; i++){
            if (! a[i]){
                int j = 2;
                A += 1;
                while (i * j < n){
                    a[i * j] = 1;
                    j += 1 ;
                }
           }
        }
        return A;
    }
};