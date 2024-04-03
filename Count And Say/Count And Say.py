// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 0:
            return ''
        if n == 1:
            return "1"
        else:
            i = 0
            S = ''
            st =[ ]
            s = self.countAndSay(n - 1)
            while i < len(s):
                if st and st[-1] != s[i]:
                    S += str(len(st)) + st[-1]
                    st.clear()
                st.append(s[i])
                i += 1
            if st:
                S += str(len(st)) + st[-1]
                st.clear()
            return S