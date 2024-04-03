// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R = [1]*len(nums)
        for i in range(len(nums)-1):
            R[i+1] = R[i] * nums[i]
        h = 1
        for j in range(len(nums)-1,-1,-1):
            R[j] *= h 
            h *= nums[j]
        return R