// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        p = 1
        m = 0
        for i in range(len(nums)):
            p = p * nums[i]
            m = max(m, p)
            if nums[i] == 0:
                p = 1
        p = 1
        for i in range(len(nums)-1,-1,-1):
            p = p * nums[i]
            m = max(m, p)
            if nums[i] == 0:
                p = 1
        return m