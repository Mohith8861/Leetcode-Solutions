// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        R = [[1]]
        if numRows == 1:
            return [[1]]
        for x in range(numRows-1):
            c = []
            c.append(1)
            i,j = 0,1
            while j < len(R[-1]):
                c.append(R[-1][i]+R[-1][j])
                i+=1
                j+=1
            c.append(1)
            R.append(c)
        return R
        