// https://leetcode.com/problems/first-missing-positive

class Solution {
    public int firstMissingPositive(int[] nums) {
        int s = 1 , n = nums.length;
        for(int i = 0; i < n; i++){
            while(nums[i] >= 1 && nums[i] <= n && (nums[nums[i] - 1] != nums[i])){
                int temp = nums[i];
                nums[i] = nums[nums[i] - 1];
                nums[temp - 1] = temp;
            }
        }
        for(int i = 0; i < n; i++)
        {
            if(s == nums[i])
                s += 1;
        }          
        return s;
    }
}