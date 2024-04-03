// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        D = [[0 for i in range(n)] for j in range(m)]
        D[-1][-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (obstacleGrid[i][j] == 1):
                    D[i][j] = 0
                    continue
                if (i == m - 1 and j == n - 1):
                    continue
                if (i == m - 1):
                    D[i][j] = D[i][j + 1]
                    continue
                if (j == n - 1):
                    D[i][j] = D[i + 1][j]
                    continue
                else:
                    D[i][j] = D[i + 1][j] + D[i][j + 1]
        return D[0][0]