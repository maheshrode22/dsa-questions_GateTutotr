#include <bits/stdc++.h>
using namespace std;

class MaxHeap {
private:
    vector<int> heap;
    
    void heapifyUp(int idx) {
        if (idx == 0) return;
        int parent = (idx - 1) / 2;
        if (heap[idx] > heap[parent]) {
            swap(heap[idx], heap[parent]);
            heapifyUp(parent);
        }
    }
    
public:
    void insert(int val) {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }
    
    int findParent(int index) {
        if (index == 0) return -1;
        if (index < 0 || index >= heap.size()) return -1;
        int parentIdx = (index - 1) / 2;
        return heap[parentIdx];
    }
    
    vector<int> getHeap() {
        return heap;
    }
};

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int index; cin >> index;
    MaxHeap heap;
    for (int num : arr) heap.insert(num);
    int result = heap.findParent(index);
    cout << result;
    return 0;
}

