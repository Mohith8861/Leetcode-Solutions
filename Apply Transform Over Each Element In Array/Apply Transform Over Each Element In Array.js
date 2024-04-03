// https://leetcode.com/problems/apply-transform-over-each-element-in-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let a = [];
    let i = 0;
    for(let x of arr)
    {
        a.push(fn(x,i));
        i += 1;
    }
    return a;
};