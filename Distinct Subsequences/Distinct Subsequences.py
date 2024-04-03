// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        D = [[-1 for x in range(len(t))] for _ in range(len(s))]
        def dfs(i,j):
            if (j >= len(t)):
                return 1
            if (i >= len(s)):
                return 0
            if(D[i][j] != -1):
                return D[i][j]
            if (s[i] == t[j]):
                D[i][j] = dfs(i + 1, j) + dfs(i + 1, j + 1)
                return D[i][j]
            return dfs(i + 1, j)
        return dfs(0,0)