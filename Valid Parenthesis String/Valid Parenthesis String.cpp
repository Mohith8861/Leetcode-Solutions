// https://leetcode.com/problems/valid-parenthesis-string

class Solution {
public:

    bool solve(string& s, int i, int l, vector<vector<int>>& dp)
    {
        if(i == s.length())
        {
            if(l == 0)
            return true;
            return false;
        }
        if(l<0)
        {
            return false;
        }
        if(dp[i][l]!=-1)
        {
            return dp[i][l];
        }
        if(s[i] == '(')
        {
            return dp[i][l] = solve(s,i+1,l+1,dp);
        }
        if(s[i] == ')')
        {
            return dp[i][l] = solve(s,i+1,l-1,dp);
        }

        return dp[i][l] = solve(s,i+1,l+1,dp) || solve(s,i+1,l-1,dp) || solve(s,i+1,l,dp);
    }

    bool checkValidString(string s) 
    {
        vector<vector<int>> dp(s.length()+1,vector<int>(s.length()+1,-1));
        return solve(s,0,0,dp);
    }
};