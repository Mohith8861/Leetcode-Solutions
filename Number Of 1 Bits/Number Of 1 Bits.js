// https://leetcode.com/problems/number-of-1-bits

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let i = 0;
    while(n != 0){
        i += (n % 2);
        n = n>>> 1;
    }
    return i;
};