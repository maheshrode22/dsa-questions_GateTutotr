#include <stdio.h>
#include <stdlib.h>

int heap[1000], heapSize = 0;

void heapifyUp(int idx) {
    if (idx == 0) return;
    int parent = (idx - 1) / 2;
    if (heap[idx] < heap[parent]) {
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

void createMinHeap(int arr[], int n) {
    heapSize = 0;
    for (int i = 0; i < n; i++) {
        insert(arr[i]);
    }
}

int main() {
    int n; scanf("%d", &n);
    if (n == 0) {
        printf("Heap is Empty");
        return 0;
    }
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    createMinHeap(arr, n);
    if (heapSize == 0) printf("Heap is Empty");
    else {
        for (int i = 0; i < heapSize; i++) {
            printf("%d", heap[i]);
            if (i < heapSize - 1) printf(" ");
        }
    }
    return 0;
}

