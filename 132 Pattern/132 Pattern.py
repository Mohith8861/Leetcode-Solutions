// https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        s = []
        i = 0
        m = float('inf') 
        while i < len(nums):
            while s and nums[i] >= s[-1][1]:
                s.pop()
            if s and nums[i] > s[-1][0]:
                return True
            s.append([m,nums[i]])
            m = min(m,nums[i])
            i += 1
        return False
                 