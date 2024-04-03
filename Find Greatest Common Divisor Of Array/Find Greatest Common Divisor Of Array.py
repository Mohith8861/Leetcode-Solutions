// https://leetcode.com/problems/find-greatest-common-divisor-of-array

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        i,j = 1000000,-1
        for a in nums:
            i = min(i,a)
            j = max(j,a)
        return gcd(i,j)