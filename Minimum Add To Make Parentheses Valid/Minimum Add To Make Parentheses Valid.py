// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        a,b = 0,0
        for i in s:
            if not st:
                st.append(i)
            elif st[-1] == '(' and i == ')':
                st.pop()
            else:
                st.append(i)
        return len(st)