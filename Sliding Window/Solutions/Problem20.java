import java.io.*;
import java.util.*;

public class Problem20 {
    // Number of Substrings Containing All Three Characters
    public static int numberOfSubstrings(String s) {
        int n = s.length();
        int[] last = new int[3];
        Arrays.fill(last, -1);
        int count = 0;
        for (int i = 0; i < n; i++) {
            last[s.charAt(i) - 'a'] = i;
            if (last[0] != -1 && last[1] != -1 && last[2] != -1) {
                count += Math.min(last[0], Math.min(last[1], last[2])) + 1;
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String s = br.readLine().trim();
        System.out.print(numberOfSubstrings(s));
    }
}