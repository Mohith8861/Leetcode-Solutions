// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        k = len(s)
        C = [0] * (len(s)+1)
        C[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if(s[i] != "0"):
                C[i] += C[i+1]
            else:
                C[i] = 0
            if(i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'))):
                C[i] += C[i+2]
        return(C[0])