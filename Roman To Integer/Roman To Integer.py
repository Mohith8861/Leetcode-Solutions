// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, st: str) -> int:
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        A = 0
        for x in range(0,len(st)):
            if(x > 0 and r[st[x]] > r[st[x-1]]):
                A = A + (r[st[x]] - (2*r[st[x-1]]))
            else:
                A = A + r[st[x]]
        return A
        


