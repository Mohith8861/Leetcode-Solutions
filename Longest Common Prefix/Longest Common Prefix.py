// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        m = len(strs[0])
        S = ''
        for i in range(m):
            k = strs[0][i]
            f  = strs[0][i]
            for j in range(len(strs)):
                f = strs[j][i]
                if(k != f):
                    return S
            S += k
        return S