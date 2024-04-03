// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;
        while(i < j){
            if(numbers[i] + numbers[j] == target)
                break;
            if(numbers[i] + numbers[j] > target)
                j -= 1;
            else
                i += 1;
        }
        int[] A = {i+1,j+1};
        return A;
    }
}