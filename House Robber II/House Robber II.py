// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        if(k <= 2):
                return max(nums)
        def helper(nums):
            k = len(nums)
            D = [0]*k
            D[0],D[1] = 0,0
            for i in range(k):
                D[i] = max(nums[i] + D[i-2], D[i-1])
            return D[-1]
        return max(helper(nums[:-1]),helper(nums[1:]))