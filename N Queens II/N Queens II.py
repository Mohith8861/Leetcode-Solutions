// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        B = [["."] * n for i in range(n)]
        A = []
        col = set()
        pos = set()
        neg = set()
        

        def solve(i):
            if (i == n):
                A.append([f.index(1)+1 for f in B])
                return
            for x in range(n):
                if x in col or (x + i) in pos or (x - i) in neg:
                    continue
                col.add(x)
                pos.add(x + i)
                neg.add(x - i)
                B[i][x] = 1
                solve(i + 1)
                col.remove(x)
                pos.remove(x + i)
                neg.remove(x - i)
                B[i][x] = 0
        solve(0)
        return len(A)
