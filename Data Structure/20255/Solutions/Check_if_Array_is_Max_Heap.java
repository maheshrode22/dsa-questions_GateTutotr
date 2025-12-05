import java.util.*;

class Solution {
    boolean isMaxHeap(int[] arr) {
        int n = arr.length;
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
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        Solution sol = new Solution();
        boolean result = sol.isMaxHeap(arr);
        if (result) System.out.println("YES");
        else System.out.println("NO");
    }
}




