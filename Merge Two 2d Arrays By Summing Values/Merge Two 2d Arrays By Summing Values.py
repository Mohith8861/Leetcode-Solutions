// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        R = []
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i][0] == nums2[j][0]):
                R.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            else:
                if(nums1[i][0] < nums2[j][0]):
                    R.append([nums1[i][0],nums1[i][1]])
                    i += 1
                elif(nums1[i][0] > nums2[j][0]):
                    R.append([nums2[j][0],nums2[j][1]])
                    j += 1
        while(i < len(nums1)):
            R.append([nums1[i][0],nums1[i][1]])
            i += 1
        while(j < len(nums2)):
            R.append([nums2[j][0],nums2[j][1]])
            j += 1
        return R
        