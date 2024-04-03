// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        while(i < j):
            x,y = abs(nums[i]),nums[j]
            if(nums[i] + nums[j] == 0):
                return x
            elif(x < y):
                j -= 1
            else:
                i += 1
        return -1