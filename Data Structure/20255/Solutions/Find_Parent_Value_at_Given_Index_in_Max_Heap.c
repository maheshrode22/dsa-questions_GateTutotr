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

int findParent(int index) {
    if (index == 0) return -1;
    if (index < 0 || index >= heapSize) return -1;
    int parentIdx = (index - 1) / 2;
    return heap[parentIdx];
}

int main() {
    int n; scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int index; scanf("%d", &index);
    heapSize = 0;
    for (int i = 0; i < n; i++) insert(arr[i]);
    int result = findParent(index);
    printf("%d", result);
    return 0;
}

