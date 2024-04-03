// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j = int(a,2),int(b,2)
        l = str(bin(i+j))[2:]
        return(l)