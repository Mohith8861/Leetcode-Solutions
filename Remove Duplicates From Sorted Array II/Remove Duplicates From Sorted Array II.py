// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if(len(nums) <= 2):
                return
            if(nums[-1] == nums[-2]):
                if(nums[-1] == nums[0]):
                    nums.pop(0)
                else:
                    nums.append(nums.pop(0))
            else:
                nums.append(nums.pop(0))

