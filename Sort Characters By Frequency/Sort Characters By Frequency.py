// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        D = {}
        for i in s:
            if i not in D:
                D[i] = 1
            else:
                D[i] += 1
        D = list(D.items())
        D.sort(key=lambda x: x[1], reverse=True)
        R = [i[0]*i[1] for i in D]
        return (''.join(R))