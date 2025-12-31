import java.io.*;
import java.util.*;

public class Problem19 {
    // Longest Subarray of 1's After Deleting One Element
    public static int longestSubarray(int[] nums) {
        int maxLength = 0;
        int zeroCount = 0;
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeroCount++;
            while (zeroCount > 1 && left <= right) {
                if (nums[left] == 0) zeroCount--;
                left++;
            }
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength - 1; // Since we can delete one element
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] parts = br.readLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(parts[i]);
        System.out.print(longestSubarray(nums));
    }
}