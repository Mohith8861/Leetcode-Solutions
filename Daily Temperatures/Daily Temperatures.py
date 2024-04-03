// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        A = [0] * len(temperatures)
        S = []
        for i, j in enumerate(temperatures):
            while (len(S) > 0 and S[-1][0] < temperatures[i]):
                x = S.pop()
                A[x[1]] = i - x[1]
            S.append((temperatures[i], i))
        return A