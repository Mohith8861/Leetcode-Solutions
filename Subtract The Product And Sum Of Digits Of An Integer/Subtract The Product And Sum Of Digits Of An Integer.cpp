// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution {
public:
    int subtractProductAndSum(int n) {
        int a = 0 , b = 1;
        for(;n > 0;n /= 10){
            a += n % 10;
            b *= n % 10;
        }
        return b - a;
    }
};