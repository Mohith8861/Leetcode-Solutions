// https://leetcode.com/problems/maximum-subarray

class Solution(object):

    def maxSubArray(self, nums):
        
        curr_sum=0
        max_sum = -10**4

        for i in nums:

            if curr_sum<0:
                curr_sum=0
            curr_sum += i
            max_sum = max(max_sum,curr_sum)

        return max_sum



            
