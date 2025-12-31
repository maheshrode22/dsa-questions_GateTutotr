import java.io.*;
import java.util.*;

public class Problem11 {
    // Maximum Vowels in Substring of Length K
    public static int maxVowels(String s, int k) {
        int n = s.length();
        int count = 0;
        for (int i = 0; i < k; i++) {
            if (isVowel(s.charAt(i))) count++;
        }
        int maxCount = count;
        for (int i = k; i < n; i++) {
            if (isVowel(s.charAt(i - k))) count--;
            if (isVowel(s.charAt(i))) count++;
            if (count > maxCount) maxCount = count;
        }
        return maxCount;
    }

    private static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        int k = Integer.parseInt(br.readLine().trim());
        System.out.print(maxVowels(s, k));
    }
}