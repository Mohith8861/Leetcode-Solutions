// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        D = {}
        M = 0
        while j < len(s):
            if s[j] not in D:
                D[s[j]] = 1
            else:
                D[s[j]] += 1
            if ((j - i + 1) - max(D.values())) <= k:
                print(D)
                M = max(M, j - i + 1)
            else:
                D[s[i]] -= 1
                i += 1
            j += 1
        return M