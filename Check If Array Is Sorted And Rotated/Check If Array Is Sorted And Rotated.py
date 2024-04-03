// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        j = 0
        for i in range(1,len(nums)):
            if(nums[i-1] > nums[i]):
                j += 1
        if(nums[-1] > nums[0]):
                j += 1
        return j <= 1