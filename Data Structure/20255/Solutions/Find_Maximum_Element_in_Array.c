#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int findMaximum(int arr[], int n){
    if(n == 0) return INT_MIN;
    int max = arr[0];
    for(int i = 1; i < n; i++){
        if(arr[i] > max) max = arr[i];
    }
    return max;
}

int main(){
    int n; scanf("%d", &n);
    if(n == 0){
        printf("Array is Empty");
        return 0;
    }
    int arr[n];
    for(int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = findMaximum(arr, n);
    printf("%d", result);
    return 0;
}

