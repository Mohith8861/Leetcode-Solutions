// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits == ''):
            return []
        s = ''
        L = []
        D = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        def lettercomb(digits,s,i,n):
            if(i == n):
                L.append(s)
                return
            for j in D[digits[i]]:
                s += j
                lettercomb(digits,s,i+1,n)
                s = s[:-1]
        lettercomb(digits,s,0,len(digits))
        return(L)