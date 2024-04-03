// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        A = []
        D = {i:0 for i in nums}
        for i in nums:
            D[i] += 1
        l = []
        def perm(i,n,nums):
            if(len(l) == len(nums)):
                A.append(l.copy())
                return
            for j in D:   
                if(D[j] > 0):
                    l.append(j)
                    D[j] -= 1
                    perm(j+1,n,nums)
                    l.pop()
                    D[j] += 1
        perm(0,len(nums),nums)
        return A