// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k ,l = 0,0
        for i in  range(len(nums)-1):
            if(nums[i] < nums[i+1]):
                k = max(k,i)
        for i in  range(k,len(nums)):
            if(nums[k] < nums[i]):
                l = max(l,i)            
        nums[k],nums[l] = nums[l],nums[k]
        nums[k+1:] = nums[k+1:][::-1]
        if not (k < l):
            nums.sort()
