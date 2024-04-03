// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        D = {}
        A = []
        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for j in D.keys():
            if(D[j] == 2):
                A.append(j)
        return A