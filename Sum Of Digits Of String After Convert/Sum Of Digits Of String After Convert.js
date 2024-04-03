// https://leetcode.com/problems/sum-of-digits-of-string-after-convert

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let o = "";
    S = "+abcdefghijklmnopqrstuvwxyz";
    for (let x of s)
    {
        o += S.indexOf(x);
    }
    for (let i = 0; i < k; i++)
    {
        h = 0
        for (let x of o)
        {
            h += parseInt(x);
        }
        o = String(h);
    }
    return(parseInt(o));
};
