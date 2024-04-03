// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1,n+1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += "Buzz"
            if s == '':
                s += str(i)
            a.append(s)
        return(a)