// https://leetcode.com/problems/maximum-erasure-value

class Solution:
    from collections import defaultdict
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        w = []
        m = 0
        D = defaultdict(int)
        for i in range(len(nums)):
            w.append(nums[i])
            D[nums[i]] += 1
            while(w and D[nums[i]] > 1):
                D[w.pop(0)] -= 1                
            m = max(m, sum(w))
        return m