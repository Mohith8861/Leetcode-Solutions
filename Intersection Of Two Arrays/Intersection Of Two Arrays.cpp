// https://leetcode.com/problems/intersection-of-two-arrays

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        set<int>s;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        vector<int> A; 
        int i = 0, j = 0;
        while(i < m && j < n)
        {
            if(nums1[i] == nums2[j])
            {
                s.insert(nums1[i]);
                i++;
                j++;
            }
            else if(nums1[i] < nums2[j])
            {
                i++;
            }
            else
            {
                j++;
            }
        }
        for (int u : s){
            A.push_back(u);
        }
        return A;
    }
};