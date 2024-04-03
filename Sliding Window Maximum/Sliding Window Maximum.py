// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q,R = [],[]
        j = 0
        for i in range(k):
            while Q and Q[-1] < nums[j]:
                Q.pop()
            Q.append(nums[j])
            j += 1
        R.append(Q[0])
        while j < len(nums):
            if (Q[0] == nums[j - k]):
                Q.pop(0)
            while Q and Q[-1] < nums[j]:
                Q.pop()
            Q.append(nums[j])
            R.append(Q[0])
            j += 1

        return R