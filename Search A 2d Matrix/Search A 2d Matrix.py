// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        s,e = 0 , r*c-1
        mid = (s+e) // 2
        while(s <= e):
            if(matrix[mid//c][mid%c] == target):
                return True
            elif(matrix[mid//c][mid%c] < target):
                s = mid + 1  
            if(matrix[mid//c][mid%c] > target):
                e = mid - 1  
            mid = (s+e) // 2
        return False