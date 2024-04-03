// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        S = 0
        n = len(costs)
        for x in range(n//2):
            S += costs[x][0]
        for x in range(n//2,n):
            S += costs[x][1]
        return S