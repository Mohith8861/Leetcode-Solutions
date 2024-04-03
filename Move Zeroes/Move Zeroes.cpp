// https://leetcode.com/problems/move-zeroes

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0 , j = 0 , n = nums.size() , temp = 0;
        while(j < n ){
            if(nums[j] != 0 && nums[i] == 0){
                swap(nums[i], nums[j]);
                i++;
                j++;
            }
            else if(nums[i] != 0)
            {
                i++;
                j++;
            }
            else
                j++;
        }
    }
};