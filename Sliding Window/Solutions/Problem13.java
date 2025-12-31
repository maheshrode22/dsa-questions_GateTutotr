import java.io.*;
import java.util.*;

public class Problem13 {
    // Longest Repeating Character Replacement
    public static int characterReplacement(String s, int k) {
        int n = s.length();
        int[] count = new int[26];
        int left = 0;
        int maxCount = 0;
        int result = 0;
        for (int right = 0; right < n; right++) {
            count[s.charAt(right) - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
            if (right - left + 1 - maxCount > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        int k = Integer.parseInt(br.readLine().trim());
        System.out.print(characterReplacement(s, k));
    }
}