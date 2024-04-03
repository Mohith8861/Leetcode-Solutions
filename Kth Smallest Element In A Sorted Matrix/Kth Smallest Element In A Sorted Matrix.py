// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        A = []
        for i in range(len(matrix)):
            A.extend(matrix[i])
        A.sort()
        return A[k-1]