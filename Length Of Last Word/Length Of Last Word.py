// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if(len(s) == 1):
            return 1
        n = len(s) 
        i = 0
        while (n):
            if(s[n-1] == ' '):
                return(i)
            i += 1
            n -= 1
        return i