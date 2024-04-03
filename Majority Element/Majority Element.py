// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {i:0 for i in nums}
        for i in nums:
            d[i] += 1
        for x in d:
            if(d[x] > n/2):
                return (x)
        
