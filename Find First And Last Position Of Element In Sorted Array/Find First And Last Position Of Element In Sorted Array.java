// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        result[0] = first(nums, target);
        result[1] = second(nums, target);
        return result;
    };
        private int first(int[] nums, int target){
            int l = 0, h = nums.length - 1;
            int m = l + ((h - l) / 2);
            int k = -1;
            while (l <= h){
                if(nums[m] == target){
                    k = m;
                    h = m - 1;
                }
                else if(nums[m] < target){
                    l = m + 1;
                }
                else if(nums[m] > target){
                    h = m - 1;
                }
                m = l + ((h - l) / 2);
            };
            return k;
        };
        private int second(int[] nums, int target){
            int l = 0, h = nums.length - 1;
            int m = l + ((h - l) / 2);
            int k = -1;
            while (l <= h){
                if(nums[m] == target){
                    k = m;
                    l = m + 1;
                }
                else if(nums[m] < target){
                    l = m + 1;
                }
                else if(nums[m] > target){
                    h = m - 1;
                }
                m = l + ((h - l) / 2);
            };
            return k;
        };
};