import java.io.*;
import java.util.*;

public class Problem10 {
    // Count anagram substrings
    public static int countAnagramSubstrings(String s, String p) {
        int n = s.length();
        int m = p.length();
        if (m > n) return 0;
        int[] need = new int[256];
        for (int i = 0; i < m; i++) {
            need[p.charAt(i)]++;
        }
        int[] win = new int[256];
        int count = 0;
        for (int i = 0; i < n; i++) {
            win[s.charAt(i)]++;
            if (i >= m) {
                win[s.charAt(i - m)]--;
            }
            if (i >= m - 1) {
                boolean ok = true;
                for (int c = 0; c < 256; c++) {
                    if (win[c] != need[c]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) count++;
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;
        s = s.trim();
        String p = br.readLine();
        if (p == null) return;
        p = p.trim();
        System.out.print(countAnagramSubstrings(s, p));
    }
}