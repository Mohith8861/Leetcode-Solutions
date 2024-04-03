// https://leetcode.com/problems/house-robber

class Solution {
    public int rob(int[] nums) {
        int c1 = 0, c2 = 0, n = nums.length, temp = 0;
        for(int i = 0; i < n; i++){
            temp = Math.max(c1 + nums[i], c2);
            c1 = c2;
            c2 = temp;
        }
        return temp;
    }
}