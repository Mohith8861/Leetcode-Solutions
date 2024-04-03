// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        inter = sorted(intervals)
        R = []
        i = 0
        for j in range(len(inter)):
            if(inter[i][1] >= inter[j][0]):
                inter[i][1] = max(inter[j][1],inter[i][1])
                j = i + 1
            else:
                R.append(inter[i])
                i = j
                j += 1
        R.append(inter[i])
        return R