// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x,y = 0, 0
        D = {(i,j):-1 for i in range(len(s)+1) for j in range(len(p)+1)}
        def search(T, P, i, j):
            if j >= len(P) and i >= len(T):
                return True
            if j >= len(P):
                return False
            if(D[(i,j)] != -1):
                return D[(i,j)]
            if i < len(T) and (P[j] == "?" or P[j] == T[i]):
                D[(i,j)] = search(T, P, i + 1, j + 1)
                return D[(i,j)]
            if P[j] == "*":
                D[(i,j)] = search(T, P, i, j + 1) or (i < len(T) and search(T, P, i + 1, j))
                return D[(i,j)]
            return False
        return(search(s, p, x, y))
