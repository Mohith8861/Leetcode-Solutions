// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        A = []
        i = 0
        n = len(intervals)
        while i < n and newInterval[0] > intervals[i][1]:
            A.append(intervals[i])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1
        A.append(newInterval)
        while i < n:
            A.append(intervals[i])
            i += 1


        return A