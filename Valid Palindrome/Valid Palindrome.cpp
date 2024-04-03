// https://leetcode.com/problems/valid-palindrome

class Solution {
public:
    bool isPalindrome(string s) {
        string a ;
        for (auto i : s){
            if('a' <= i and i <= 'z')
                a += i;
            if('A' <= i and i <= 'Z')
                a += (i - 'A' + 'a');
            if('0' <= i and i <= '9')
                a += i;
            }
        return check(a);
    }
    bool check(string a){
        int i = 0,j = a.size()-1;
        while (i <= j){
            if(a[i] != a[j]){
                return false;
                }
            i++;
            j--;
        };
        return true;
    }
};