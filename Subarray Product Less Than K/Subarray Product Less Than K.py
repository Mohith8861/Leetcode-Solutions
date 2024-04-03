// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k <= 1):
            return 0
        P = 1
        i,j = 0,0
        R = 0
        while(j < len(nums)):
            P *= nums[j]
            while(P >= k and i <= j):
                P /= nums[i]
                i += 1
            R += (j-i+1)
            j += 1
        return R