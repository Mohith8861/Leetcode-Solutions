// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        for i in nums:
            if i not in D:
                D[i] = 1
            else:
                D[i] += 1
        D = list(D.items())
        D.sort(key=lambda x: x[1], reverse=True)
        R = [D[i][0] for i in range(k)]
        return (R)
