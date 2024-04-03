// https://leetcode.com/problems/group-anagrams

class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        R = defaultdict(list)
        for s in strs:
            A = [0]*26
            for c in s:
                A[ord(c)-97] += 1
            R[tuple(A)].append(s)
        return R.values()
            

