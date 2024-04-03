// https://leetcode.com/problems/n-queens

class Solution {
public:
    vector<vector<string>> A;
    void solve(vector<string> &D, int n, int j){
        if (n == 0)
            return;
        if(j == n){
            A.push_back(D);
            return;
        }
        for(int i = 0; i < n; i++){
            if(check(i,j,D,n)){
                D[i][j] = 'Q';
                solve(D,n,j+1);
                D[i][j] = '.';
            }
                
        }

    }
    bool check(int i,int j,vector<string> &D,int n){
            if (i > n-1 && j > n-1)
                return false;
            if (i < 0 || j < 0)
                return false;
            int a = i,b = j;
            while (a >= 0 && b >= 0){
                if (D[a][b] == 'Q')
                    return false;
                a -= 1;
                b -= 1;                
            }
            a = i;
            b = j;
            while(a <= n-1 && b >= 0){
                if(D[a][b] == 'Q')
                    return false;
                a += 1;
                b -= 1;                
            }
            a = i;
            b = j;
            while (b >= 0){
                if(D[a][b] == 'Q')
                    return false;       
                b -= 1;                             
            }
            return true;            
        }    

    vector<vector<string>> solveNQueens(int n) {
        vector<string> D(n,string(n,'.'));
        solve(D,n,0);
        return A;
    }


};