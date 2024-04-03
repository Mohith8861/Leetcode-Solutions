// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ''
        L = []
        o,c = 0,0
        def paran(s,n,o,c):
            if(o == n and c == n):
                L.append(s)
                return
            if(o > c):
                paran(s + ')',n,o,c+1)
            if(o < n):
                paran(s + '(',n,o+1,c)
        paran(s,n,o,c)
        return L