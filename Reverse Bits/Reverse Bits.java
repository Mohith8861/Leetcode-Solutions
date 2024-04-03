// https://leetcode.com/problems/reverse-bits

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int A) {
        int R = 0;
        for(int i =0; i < 32; i++){
            R = R << 1;
            int k = A & 1;
            A = A >> 1;
            R = R | k;
        }
        return R ;
    }
}