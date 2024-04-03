// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            n = len(nums)
            temp = [0]*n
            for i in range(n):
                temp[(i+k)%n] = nums[i]
            for j in range(n):
                nums[j] = temp[j]


            
            
                
                



        
        