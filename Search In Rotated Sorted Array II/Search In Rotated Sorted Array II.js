// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
  if(nums.length == 1){
    if(nums[0] == target){
      return true;
    }
    else{
      return false;
    }
  }
  if(nums.length == 2){
    if(nums[0] == target){
      return true;
    }
    else if(nums[1] == target){
      return true;
    }
    else{
      return false;
    }
  }
  if (nums.at(-1) <= nums[0]) {
    while(nums.length){
      if(nums.at(-1) == target)
        return true;
      nums.pop();
    }
    return false;
  }
  else{
    let i = 0;
    while(nums.length){
      if(nums[0] == target)
        return true;
      if(nums[0] > target)
        return false;
      nums.shift();
      i++;
    }
    return false;
  }
};
