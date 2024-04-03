// https://leetcode.com/problems/chunk-array

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
  let A = [];
  if(size == 0 || arr == [])
  {
    return(A)
  }
  let j = Math.floor(arr.length/size);
  while(j != 0)
  {
    A.push(arr.splice(0,size))
    j-=1;
  }
  if(arr.length != 0)
  {
    A.push(arr)
  }
  return(A)
};