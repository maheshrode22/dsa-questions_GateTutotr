import java.io.*;
import java.util.*;

public class Problem14 {
    // Contains Duplicate II
    public static String containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                if (i - map.get(nums[i]) <= k) {
                    return "true";
                }
            }
            map.put(nums[i], i);
        }
        return "false";
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().trim().split(" ");
        int n = Integer.parseInt(first[0]);
        int k = Integer.parseInt(first[1]);
        String[] parts = br.readLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(parts[i]);
        System.out.print(containsNearbyDuplicate(nums, k));
    }
}