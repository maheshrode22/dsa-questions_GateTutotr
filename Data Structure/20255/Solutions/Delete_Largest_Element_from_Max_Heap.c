#include <stdio.h>
#include <stdlib.h>

int heap[1000], heapSize = 0;

void heapifyUp(int idx) {
    if (idx == 0) return;
    int parent = (idx - 1) / 2;
    if (heap[idx] > heap[parent]) {
        int temp = heap[idx];
        heap[idx] = heap[parent];
        heap[parent] = temp;
        heapifyUp(parent);
    }
}

void insert(int val) {
    heap[heapSize] = val;
    heapifyUp(heapSize);
    heapSize++;
}

int deleteMax() {
    if (heapSize == 0) return 0;
    int maxVal = heap[0];
    heap[0] = heap[heapSize - 1];
    heapSize--;
    int idx = 0;
    while (idx < heapSize) {
        int largest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;
        
        if (left < heapSize && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heapSize && heap[right] > heap[largest]) {
            largest = right;
        }
        
        if (largest == idx) break;
        int temp = heap[idx];
        heap[idx] = heap[largest];
        heap[largest] = temp;
        idx = largest;
    }
    return maxVal;
}

int main() {
    int n; scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    heapSize = 0;
    for (int i = 0; i < n; i++) insert(arr[i]);
    int deleted = deleteMax();
    printf("%d\n", deleted);
    if (heapSize == 0) printf("Heap is Empty");
    else {
        for (int i = 0; i < heapSize; i++) {
            printf("%d", heap[i]);
            if (i < heapSize - 1) printf(" ");
        }
    }
    return 0;
}

