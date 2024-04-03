// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num)) != 1):
            x = [int(x) for x in str(num)]
            num = sum(x)
        return(num)