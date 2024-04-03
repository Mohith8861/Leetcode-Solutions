// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        A = []
        for i in points:
            x = ((i[0]**2) + (i[1]**2))**0.5
            A.append([x, i])
        A.sort(key=lambda x: x[0])
        R = [i[1] for i in A[:k]]
        return R