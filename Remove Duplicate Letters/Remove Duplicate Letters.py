// https://leetcode.com/problems/remove-duplicate-letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occ = {}
        stack = []
        visited = set()

        for i,c in enumerate(s):
            last_occ[c] = i

        for i,c in enumerate(s):

            if c not in visited:
                while (stack and stack[-1] > c and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())

                stack.append(c)
                visited.add(c)

        return ''.join(stack)