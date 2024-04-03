// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        L,temp = [],[]
        def combSum(candidates,target,i,n):
            if(target == 0):
                L.append(list(temp))
                return

            for j in range(i,n):
                if(target - candidates[j] >= 0):
                    temp.append(candidates[j])
                    combSum(candidates,target - candidates[j],j,n)
                    temp.pop()
            
        combSum(candidates,target,0,len(candidates))
        return L
