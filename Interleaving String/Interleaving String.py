// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        M = {}
        def solve(i,j,k):
            if l == k:
                return True
            if (i, j) in M:
                return M[(i, j)]
            ans = False
            if i < m and s1[i] == s3[k]:
                ans = ans or solve(i + 1, j, k + 1)
            if j < n and s2[j] == s3[k]:
                ans = ans or solve(i, j + 1, k + 1)
            M[(i, j)] = ans
            return ans
        return solve(0,0,0)