// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        S = []
        for i in range(len(s)):
            if len(S) == 0:
                S.append((s[i],1))
            else:
                if S[-1][0] == s[i]:
                    if S[-1][1] == k - 1:
                        while S and S[-1][0] == s[i]:
                            S.pop()
                    else:
                        S.append((s[i],S[-1][1]+1))
                else:
                    S.append((s[i],1))
        return ''.join([i[0] for i in S])