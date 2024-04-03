// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(p) > len(s)): return[]
        R = []
        P = {}
        S = {}
        for i in range(len(p)):
            P[p[i]] = 1 + P.get(p[i], 0)
            S[s[i]] = 1 + S.get(s[i], 0)
        R = [0] if P == S else []
        for i in range(len(p), len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            S[s[i - len(p)]] -= 1
            if S[s[i - len(p)]] == 0 : del S[s[i - len(p)]]
            if P == S:
                print(i - len(p) + 1)
                R.append(i - len(p) + 1)
        return R