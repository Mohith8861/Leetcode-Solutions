// https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        D = defaultdict(int)
        for i in range(len(s)-9):
            D[s[i:i+10]] += 1
        R = [ x for x in D.keys() if D[x] > 1]
        return R