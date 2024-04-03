// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        D = {
            '{':'}',
            '(':')',
            '[':']'
        }
        st.append(s[0])
        for v in s[1:]:
            if st:
                if st[-1] == '{' and v == '}':
                    st.pop()
                elif st[-1] == '[' and v == ']':
                    st.pop()
                elif st[-1] == '(' and v == ')':
                    st.pop()
                else:
                    st.append(v)
            else:
                st.append(v)
        if not st:
            return True
        else:
            return False
