// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        int H[26] = {0};
        for (auto i : s) {
            H[i - 97] += 1;
            };
        for (auto i : t) {
            H[i - 97] -= 1;
            };
        for (auto i : H) {
            if(i != 0)
                return false;
            };
        return true;
    }
};