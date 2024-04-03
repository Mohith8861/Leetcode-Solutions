// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        lef = 0
        i = 0
        while nums:
            h = nums.pop(0)
            i += 1
            S -= (h)
            if lef == S:
                return(i - 1)
            lef += h
        return -1
