// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if (nums[i] < nums[j]):
                    l[i] = max(l[i], 1 + l[j])
        return max(l)