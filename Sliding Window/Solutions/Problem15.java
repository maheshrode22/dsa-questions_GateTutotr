import java.io.*;
import java.util.*;

public class Problem15 {
    // Get Equal Substrings Within Budget
    public static int equalSubstring(String s, String t, int maxCost) {
        int n = s.length();
        int[] costs = new int[n];
        for (int i = 0; i < n; i++) {
            costs[i] = Math.abs(s.charAt(i) - t.charAt(i));
        }
        int left = 0;
        int currentCost = 0;
        int maxLength = 0;
        for (int right = 0; right < n; right++) {
            currentCost += costs[right];
            while (currentCost > maxCost && left <= right) {
                currentCost -= costs[left++];
            }
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        String t = br.readLine().trim();
        int maxCost = Integer.parseInt(br.readLine().trim());
        System.out.print(equalSubstring(s, t, maxCost));
    }
}