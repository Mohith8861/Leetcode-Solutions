// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = []
        o = 0
        for i in range(1,n+1):
          if(n%i == 0):
            a.append(i)
            o+=1
          if(o == k):
            return a[k-1]
        return -1