// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        S = []
        l = []
        nums.sort()
        n = len(nums)
        S.append(l)
        def subset(A,i,l):
            if(i >= n):
                return
            l.append(A[i])
            S.append(l.copy())
            subset(A,i+1,l)
            l.pop()
            while(i+1 < n and A[i] == A[i+1]):
                i += 1
            subset(A,i+1,l)    
        subset(nums,0,l)
        return S