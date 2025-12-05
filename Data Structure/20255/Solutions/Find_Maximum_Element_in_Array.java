import java.util.*;
class Solution{
    Integer findMaximum(int[] arr){
        if(arr == null || arr.length == 0) return null;
        int max = arr[0];
        for(int i = 1; i < arr.length; i++){
            if(arr[i] > max) max = arr[i];
        }
        return max;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) arr[i] = sc.nextInt();
        Solution sol = new Solution();
        Integer ans = sol.findMaximum(arr);
        if(ans == null) System.out.println("Array is Empty");
        else System.out.println(ans);
    }
}

