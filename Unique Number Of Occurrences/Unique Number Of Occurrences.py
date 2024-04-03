// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        D = {}
        for i in arr:
            if(i in D):
                D[i] += 1
            else:
                D[i] = 1
        R = len(D.values())
        L = len(set(D.values()))
        return R == L