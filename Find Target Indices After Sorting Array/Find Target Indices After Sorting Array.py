// https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        o = len(nums)
        nums.sort()
        if (nums == []) or (target not in nums):
            return []
        if o == 1 and nums[0] == target:
            return [0]
        if o == 2:
            if nums[0] == target and nums[1] == target:
                return [0,1]
            if nums[0] == target:
                return [0]
            if nums[1] == target:
                return [1]
        i = 0
        while nums[i] != target:
            i += 1
        l = [True for b in nums if b == target]   
        if len(l) == 1:
            return [i]
        return [x for x in range(i,i+len(l))]