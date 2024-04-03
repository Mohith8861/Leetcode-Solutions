// https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        a = chars[0]
        l = len(chars)
        chars.append(a)
        while(i < l):
            if(chars[0] != a):
                a = chars[0]
                if(j > 1):
                    chars += (list(str(j)))
                chars.append(a)
                j = 0
            chars.pop(0)
            j += 1
            i += 1
        if(j > 1):
            chars += (list(str(j)))
        return(len(chars))