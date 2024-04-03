// https://leetcode.com/problems/word-search

class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        s = set()
        def dfs(board, word, i, j, k):
            if (k == len(word)):
                return True
            if (i >= m or j >= n or i < 0 or j < 0 or board[i][j] != word[k] or (i,j) in s):
                return False
            s.add((i,j))
            if (dfs(board, word, i, j + 1, k + 1) or dfs(board, word, i + 1, j, k + 1) or dfs(board, word, i - 1, j, k + 1) or dfs(board, word, i, j - 1, k + 1)):
                return True
            s.remove((i,j))

        def solve(board, word):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (dfs(board, word, i, j, 0)):
                        return True
            return False
            
        return solve(board, word)

        