import java.io.*;
import java.util.*;

public class Problem43 {
    // Count Digits in a Number
    public static int countDigits(long n) {
        if (n == 0) return 1;
        int count = 0;
        while (n != 0) {
            n /= 10;
            count++;
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(countDigits(n));
    }
}