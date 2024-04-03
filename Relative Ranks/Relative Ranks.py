// https://leetcode.com/problems/relative-ranks

import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        A = {}
        for i,j in enumerate(score):
            A[j] = i
        R = [0]*len(A)
        for t,ele in enumerate(sorted(list(A.keys()),reverse = True)):
            if t == 0:
                R[A[ele]] = "Gold Medal"
            elif t == 1:
                R[A[ele]] = "Silver Medal"
            elif t == 2:
                R[A[ele]] = "Bronze Medal"
            else:
                R[A[ele]] = str(t+1)
        return R