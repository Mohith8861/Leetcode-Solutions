// https://leetcode.com/problems/filter-elements-from-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let a = arr.filter((e,index) => {return(fn(e,index))});
    return a;
};