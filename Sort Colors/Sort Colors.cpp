// https://leetcode.com/problems/sort-colors

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int z = 0,o = 0,t = 0;
        for(auto i : nums){
            if(i == 0)
                z += 1;
            if(i == 1)
                o += 1;
            if(i == 2)
                t += 1;
        }
        int i = 0;
        while(z > 0)
        {
            nums[i] = 0;
            z -= 1;
            i += 1;
        }
        while(o > 0)
        {
            nums[i] = 1;
            o -= 1;
            i += 1;
        }
        while(t > 0)
        {
            nums[i] = 2;
            t -= 1;
            i += 1;
        }
    }
};