// https://leetcode.com/problems/find-the-k-beauty-of-a-number

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        r = 0
        s = str(num)
        for i in range(k,len(s)+1):
            if(int(s[i-k:i]) != 0 and (num % int(s[i-k:i]) == 0)):
                r += 1
        return r
