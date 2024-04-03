// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1 + nums2
        x.sort()
        i = len(x)
        if i % 2 == 0:
            return((x[i//2-1]+int(x[i//2]))/2)
        else:
            return(x[i//2])