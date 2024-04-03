// https://leetcode.com/problems/find-the-middle-index-in-array

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        lef = 0
        i = 0
        while nums:
            h = nums.pop(0)
            i += 1
            S -= (h)
            if lef == S:
                return (i-1)
            lef += h
        return (-1)