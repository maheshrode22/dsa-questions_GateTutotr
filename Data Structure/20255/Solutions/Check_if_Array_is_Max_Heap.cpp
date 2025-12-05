#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMaxHeap(vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            
            if (left < n && arr[i] < arr[left]) {
                return false;
            }
            if (right < n && arr[i] < arr[right]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    Solution sol;
    bool result = sol.isMaxHeap(arr);
    if (result) cout << "YES";
    else cout << "NO";
    return 0;
}




