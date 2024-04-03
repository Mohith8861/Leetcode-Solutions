// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            if(i == ']'):
                s = ''
                while st[-1] != '[':
                    s = st.pop() + s
                st.pop()
                k = ''
                while st and st[-1] in '0123456789':
                    k = st.pop() + k
                s = s*int(k)
                st.append(s)
            else:
                st.append(i)
        return ''.join(st)