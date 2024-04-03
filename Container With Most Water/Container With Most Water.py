// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i,j = 0,len(height) - 1
        M = 0
        while i < j:
            M = max(min(height[i],height[j])*(j-i),M)
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return M