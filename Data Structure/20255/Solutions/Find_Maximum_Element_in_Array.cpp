#include <bits/stdc++.h>
using namespace std;
class Solution{
public:
    int findMaximum(vector<int>& arr){
        if(arr.empty()) return 0;
        int maxVal = arr[0];
        for(int i = 1; i < arr.size(); i++){
            if(arr[i] > maxVal) maxVal = arr[i];
        }
        return maxVal;
    }
};
int main(){
    int n; cin >> n;
    if(n == 0){
        cout << "Array is Empty";
        return 0;
    }
    vector<int> arr(n);
    for(int i = 0; i < n; i++) cin >> arr[i];
    Solution sol;
    int ans = sol.findMaximum(arr);
    cout << ans;
    return 0;
}

