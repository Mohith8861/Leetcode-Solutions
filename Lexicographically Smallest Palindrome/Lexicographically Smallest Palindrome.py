// https://leetcode.com/problems/lexicographically-smallest-palindrome

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i,j = 0,len(s)-1
        arr = list(s)
        while(i<j):
            if(arr[j] <= arr[i]):
                arr[i] = arr[j]
            else:
                arr[j] = arr[i] 
            i += 1
            j -= 1
        return ''.join(arr)