// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max1 = max(nums)
        min1 = min(nums)
        A = [0 for i in range(abs(min1) + max1 + 1)]
        for i in nums:
            A[i] += 1
        j = 0
        for i in range(min1, max1 + 1):
            if(A[i] != 0):
                while(A[i] != 0):
                    nums[j] = i
                    A[i] -= 1
                    j += 1
        return nums