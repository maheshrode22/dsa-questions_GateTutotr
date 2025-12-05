#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isMaxHeap(int arr[], int n) {
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

int main() {
    int n; scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    bool result = isMaxHeap(arr, n);
    if (result) printf("YES");
    else printf("NO");
    return 0;
}




