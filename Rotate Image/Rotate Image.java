// https://leetcode.com/problems/rotate-image

class Solution {
    public void rotate(int[][] matrix) {
        int r = matrix.length, c = matrix[0].length;
        for(int i = 0 ; i < r;i++){
            for(int j = i ; j < c;j++){
                int t = 0;
                t = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = t;
            }
        }
        int left = 0,right = c-1;
        while(left < right){
            for(int i = 0 ; i < r;i++){
                int t = 0;
                t = matrix[i][right];
                matrix[i][right] = matrix[i][left];
                matrix[i][left] = t;
            }
            left += 1;
            right -= 1;
        }
    }
}