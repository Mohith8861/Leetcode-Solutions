// https://leetcode.com/problems/remove-element

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        remove(nums,val);
        return nums.size();
    }
    void remove(vector<int>& st,int val){
        if(st.size() == 0)
            return;
        int x = st.back();
        st.pop_back();
        remove(st,val);
        if(x != val)
            st.push_back(x);
    }
};