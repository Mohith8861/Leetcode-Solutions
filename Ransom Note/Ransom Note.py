// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        R, M = {}, {}
        for t in ransomNote:
            if t in R:
                R[t] += 1
            else:
                R[t] = 1
        for t in magazine:
            if t in M:
                M[t] += 1
            else:
                M[t] = 1
        i = 0
        for h in ransomNote:
            if h in M:
                if(M[h] >= R[h]):
                    i += 1
        return(i == len(ransomNote))