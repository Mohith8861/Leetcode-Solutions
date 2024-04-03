// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        D = {}
        def twoSum(S, i):
            if (i < 0):
                return 1 if S == target else 0
            if (i, S) in D.keys():
                return D[(i, S)]

            D[(i, S)] = twoSum(S + nums[i], i - 1) + twoSum(S - nums[i], i - 1)
            return D[(i, S)]
        return twoSum(0, len(nums) - 1)