// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int n = arr.length -1, i = 0;
        int m = (i+n)/2;
        while(i < n){
            if(arr[m] < arr[m+1]){
                i = m+1;
            }
            else{
                n = m;
            };
            m = (i+n)/2;
        };
        return i;
    };
}