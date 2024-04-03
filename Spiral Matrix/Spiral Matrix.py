// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right,top,bottom = 0,len(matrix[0]),0,len(matrix)
        R = []
        while(left < right and top < bottom):
            for i in range(left,right):
                R.append(matrix[top][i])
            top += 1  
            for i in range(top,bottom):
                R.append(matrix[i][right-1])
            right -= 1  
            if not (left < right and top < bottom):
                break
            for i in range(right-1,left-1,-1):
                R.append(matrix[bottom-1][i])
            bottom -= 1  
            for i in range(bottom-1,top-1,-1):
                R.append(matrix[i][left])
            left += 1
        return R