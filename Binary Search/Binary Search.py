// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def Binary(A,t,l,h):
            if(l > h):
                return -1
            m = (l+h)//2
            if A[m] == t:
                return m
            if(A[m] < t):
                return Binary(A,t,m+1,h)
            if(A[m] > t):
                return Binary(A,t,l,m-1)
        return(Binary(nums,target,0,len(nums)-1))