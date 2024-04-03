// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(not s%2 == 0):
            return False
        s = s//2
        S = set()
        S.add(0)
        for i in range(len(nums) - 1, -1, -1):
            for j in S.copy():
                S.add(j + nums[i])
        return s in S
