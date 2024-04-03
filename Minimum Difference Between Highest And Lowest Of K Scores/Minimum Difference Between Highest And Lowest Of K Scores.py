// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if(len(nums) == 1):
            return 0
        nums.sort()
        d = 1000000
        for i in range(len(nums)-k+1):
            d = min(nums[i+k-1] - nums[i],d)
        return d
