// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int j = 0;
        int M = 0;
        map<char,int> D;
        for(auto i : s){
            D[i] = 0;
        }
        while (j < s.length()) {
            D[s[j]] += 1;
            if (D[s[j]] > 1){
                M = max(j-i,M);
                while( D[s[j]] != 1){
                    D[s[i]] -= 1;
                    i += 1;
                }
            }
            j += 1;
        }
        M = max(j-i,M);
        return M;
    }
};