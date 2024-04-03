// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution {
public:
    vector<int> next(vector<int>& arr,int n){
        stack <int> s;
        vector <int> A(n);
        s.push(-1);
        for(int i = n-1; i >= 0; i--){
            while(s.top() != -1 && arr[s.top()] >= arr[i]){
                s.pop();
            }
            A[i] = s.top();
            s.push(i);
        }
        return A;
    }
    vector<int> prev(vector<int>& arr,int n){
        stack <int> s;
        vector <int> A(n);
        s.push(-1);
        for(int i = 0; i < n; i++){
            while(s.top() != -1 && arr[s.top()] >= arr[i]){
                s.pop();
            }
            A[i] = s.top();
            s.push(i);
        }
        return A;
    }
    int largestRectangleArea(vector<int>& heights) {
        int num = heights.size();
        int l,b,A = 0;
        vector <int> p(num);
        p = prev(heights,num);
        vector <int> n(num);
        n = next(heights,num);
        for (int i = 0 ; i < num; i++){
            l = heights[i];
            if(n[i] == -1)
                n[i] = num;
            b = n[i] - p[i] - 1;
            A = max(A,l*b);
        }
        return A;
    }
    
};