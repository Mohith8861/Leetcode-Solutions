// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution {
    public int dfs(int[][] matrix,int i, int j, int P,int[][] D){
        if (i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || P >= matrix[i][j])
            return 0;
        if(D[i][j] != -1)
            return D[i][j];
        D[i][j] = 1;
        D[i][j] = Math.max(D[i][j], 1 + dfs(matrix, i, j + 1, matrix[i][j],D));
        D[i][j] = Math.max(D[i][j], 1 + dfs(matrix, i + 1, j, matrix[i][j],D));
        D[i][j] = Math.max(D[i][j], 1 + dfs(matrix, i, j - 1, matrix[i][j],D));
        D[i][j] = Math.max(D[i][j], 1 + dfs(matrix, i - 1, j, matrix[i][j],D));
        return D[i][j];
    }
    public int longestIncreasingPath(int[][] matrix) {
        int[][] D = new int[matrix.length][matrix[0].length];
        for (int[] row : D) 
            Arrays.fill(row, -1); 
        int R = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++)
                R = Math.max(R, dfs(matrix, i, j, -1,D));
        }
        return R;
    }
}
     
        