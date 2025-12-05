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
    
    int deleteMax() {
        if (heap.empty()) return 0;
        int maxVal = heap[0];
        heap[0] = heap[heap.size() - 1];
        heap.pop_back();
        int idx = 0;
        while (idx < heap.size()) {
            int largest = idx;
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            
            if (left < heap.size() && heap[left] > heap[largest]) {
                largest = left;
            }
            if (right < heap.size() && heap[right] > heap[largest]) {
                largest = right;
            }
            
            if (largest == idx) break;
            swap(heap[idx], heap[largest]);
            idx = largest;
        }
        return maxVal;
    }
    
    vector<int> getHeap() {
        return heap;
    }
};

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    MaxHeap heap;
    for (int num : arr) heap.insert(num);
    int deleted = heap.deleteMax();
    vector<int> remaining = heap.getHeap();
    cout << deleted << endl;
    if (remaining.empty()) cout << "Heap is Empty";
    else {
        for (int i = 0; i < remaining.size(); i++) {
            cout << remaining[i];
            if (i < remaining.size() - 1) cout << " ";
        }
    }
    return 0;
}

