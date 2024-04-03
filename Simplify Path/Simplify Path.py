// https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        temp = ""
        i = 0
        while i < len(path):
            if path[i] == "/":
                i += 1
                while i < len(path) and path[i] != "/":
                    temp += path[i]
                    i += 1
                if temp == "..":
                    if s: s.pop()
                    temp = ""
                if temp == ".":
                    temp = ""
                else:
                    if temp: s.append('/' + temp)
                    temp = ""
        c =  "".join(s)
        print(s)
        return c if  len(c) != 0 else "/"