// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        R = 0
        for i in range(len(nums)):
            R ^= i^nums[i]
        R ^= len(nums)
        return R

        