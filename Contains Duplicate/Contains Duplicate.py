// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        D ={}
        for i in nums:
            if(i in D):
                return True
            else:
                D[i] = 1
        return False