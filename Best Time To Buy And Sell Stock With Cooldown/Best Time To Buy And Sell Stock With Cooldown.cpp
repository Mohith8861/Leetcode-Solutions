// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution {
public:
    int solve(int i, int flag,vector<int>& prices,vector<vector<int>>& D)
    {
        if (i >= prices.size())
            return 0;
        if (D[i][flag] != -1){
            return D[i][flag];
        }
        if (flag == 0) {
            D[i][flag] = max(-prices[i] + solve(i + 1, 1,prices,D), solve(i + 1, 0,prices,D));
            return D[i][flag];
        } else {
            D[i][flag] = max(solve(i + 2, 0,prices,D) + prices[i], solve(i + 1, 1,prices,D));
            return D[i][flag];
        }
    }


    int maxProfit(vector<int>& prices) {
        vector<vector<int>> D;
        for(int i = 0; i < prices.size();i++)
            D.push_back({-1,-1});
        return solve(0,0,prices,D);
    }
};