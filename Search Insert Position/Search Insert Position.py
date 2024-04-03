// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(nums, t):
            l, h = 0, len(nums) - 1
            m = (l + h) // 2
            while l <= h:
                if (nums[m] == t):
                    return m
                elif (nums[m] < t):
                    l = m + 1
                elif (nums[m] > t):
                    h = m - 1
                m = (l + h) // 2
            return m + 1
        return binary(nums, target)
        