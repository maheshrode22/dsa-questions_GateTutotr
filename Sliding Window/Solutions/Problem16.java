import java.io.*;
import java.util.*;

public class Problem16 {
    // Minimum Operations to Reduce X to Zero
    public static int minOperations(int[] nums, int x) {
        int total = 0;
        for (int num : nums) total += num;
        int target = total - x;
        if (target < 0) return -1;
        if (target == 0) return nums.length;

        int left = 0;
        int currentSum = 0;
        int maxLength = -1;
        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];
            while (currentSum > target && left <= right) {
                currentSum -= nums[left++];
            }
            if (currentSum == target) {
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }
        return maxLength == -1 ? -1 : nums.length - maxLength;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().trim().split(" ");
        int n = Integer.parseInt(first[0]);
        int x = Integer.parseInt(first[1]);
        String[] parts = br.readLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(parts[i]);
        System.out.print(minOperations(nums, x));
    }
}