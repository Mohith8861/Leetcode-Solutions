// https://leetcode.com/problems/unique-paths

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] D = new int[m][n];
        for(int i = 0; i < n; i++)
            D[m-1][i] = 1;
        for(int i = 0; i < m; i++)
            D[i][n-1] = 1;
        for(int i = m-2; i > -1; i--)
        {
            for(int j = n-2; j > -1; j--)
                D[i][j] = D[i+1][j] + D[i][j+1];
        }
        return D[0][0];
    }
}