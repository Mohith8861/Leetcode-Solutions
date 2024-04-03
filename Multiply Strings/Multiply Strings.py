// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        A,B = 0,0
        for i in num1:
            A *= 10     
            A += int(i) 
        for i in num2:
            B *= 10
            B += int(i) 
        return str(A*B)