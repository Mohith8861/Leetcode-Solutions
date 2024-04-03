// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        A = []
        S = []
        candidates.sort(reverse=True)
 
        def dfs(S, A, candidates, target):
            if (target == 0):
                if (S in A):
                    return
                A.append(S.copy())
                return
            if (target < 0):
                return
            p = -100
            for i in range(len(candidates)):
                if( p == candidates[i]):
                    continue
                S.append(candidates[i])
                dfs(S, A, candidates[i + 1:], target - candidates[i])
                S.pop()
                p = candidates[i]
        dfs(S, A, candidates, target)
        return A
