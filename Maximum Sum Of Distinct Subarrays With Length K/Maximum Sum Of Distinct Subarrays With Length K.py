// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        q = []
        s = {}
        for i in range(k):
            q.append(nums[i])
            if nums[i] not in s:
                s[nums[i]] = 1
            else:
                s[nums[i]] += 1
        M = 0
        S = sum(q)
        if len(s) == k:
            M = S
        for i in range(k, len(nums)):
            S += (nums[i] - q[0])
            if nums[i] not in s:
                s[nums[i]] = 1
            else:
                s[nums[i]] += 1
            q.append(nums[i])
            if q[0] in s:
                s[q[0]] -= 1
                if s[q[0]] == 0:
                    del s[q[0]]
            q.pop(0)
            if len(s) == k:
                M = max(M, S)
        return M