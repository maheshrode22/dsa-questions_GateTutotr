#include <bits/stdc++.h>
using namespace std;

class MinHeap {
private:
    vector<int> heap;
    
    void heapifyUp(int idx) {
        if (idx == 0) return;
        int parent = (idx - 1) / 2;
        if (heap[idx] < heap[parent]) {
            swap(heap[idx], heap[parent]);
            heapifyUp(parent);
        }
    }
    
public:
    void insert(int val) {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }
    
    vector<int> getHeap() {
        return heap;
    }
};

class Solution {
public:
    vector<int> createMinHeap(vector<int>& arr) {
        MinHeap heap;
        for (int num : arr) {
            heap.insert(num);
        }
        return heap.getHeap();
    }
};

int main() {
    int n; cin >> n;
    if (n == 0) {
        cout << "Heap is Empty";
        return 0;
    }
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    Solution sol;
    vector<int> ans = sol.createMinHeap(arr);
    if (ans.empty()) cout << "Heap is Empty";
    else {
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i];
            if (i < ans.size() - 1) cout << " ";
        }
    }
    return 0;
}

