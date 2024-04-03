// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        A = []
        S = []

        def rev(s, l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def solve(i):
            if i >= len(s):
                A.append(S.copy())
                return
            for j in range(i, len(s)):
                if (rev(s, i, j)):
                    print(s[i:j])
                    S.append(s[i:j + 1])
                    solve(j + 1)
                    S.pop()

        solve(0)
        return A