// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n == 1):
            return True
        f = n - 1
        for i in range(n-1,-1,-1):
            if(f <= i + nums[i]):
                f = i
        return (f == 0)
