// https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for i in num:
            while s and k > 0 and int(i) < int(s[-1]):
                s.pop()
                k -= 1
            s.append(i)
        while k > 0:
            s.pop()
            k -= 1
        while s and s[0] == "0":
            s.pop(0)
        return ''.join(s).lstrip('0') if s else '0'