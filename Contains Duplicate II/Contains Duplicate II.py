// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        D = {}
        for i in range(l):
            if(nums[i] in D and abs(D[nums[i]] - i) <= k and nums[D[nums[i]]] == nums[i]):
                return True
            else:
                D[nums[i]] = i
        return False
        