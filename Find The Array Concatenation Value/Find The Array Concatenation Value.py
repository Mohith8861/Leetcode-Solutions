// https://leetcode.com/problems/find-the-array-concatenation-value

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        x = len(nums)
        i,j = 0,x-1
        C = 0
        while(i < j):
            R = str(nums[i]) + str(nums[j])
            C += int(R)
            i += 1
            j -= 1
        if(x%2):
            C += nums[x//2]
        return C