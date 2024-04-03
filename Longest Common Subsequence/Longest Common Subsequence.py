// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a ,b = text1,text2
        s = ''
        m, n = len(a), len(b)
        D = [[0] * (n + 1) for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (a[i - 1] == b[j - 1]):
                    D[i][j] = (1 + D[i - 1][j - 1])
                else:
                    D[i][j] = max(D[i][j - 1], D[i - 1][j])
        return(D[-1][-1])