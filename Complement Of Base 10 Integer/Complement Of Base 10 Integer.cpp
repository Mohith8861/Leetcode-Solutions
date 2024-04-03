// https://leetcode.com/problems/complement-of-base-10-integer

class Solution {
public:
    int bitwiseComplement(int n) {
        int i = 0, s = 0;
        if(n == 0){
            return 1;
        }
        while(n > 0){
            if((n % 2) == 0){
                s += pow(2,i);
            }
            i += 1;
            n = n >> 1;
        }
        return s;
    }
};