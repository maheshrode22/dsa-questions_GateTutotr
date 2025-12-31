import java.io.*;
import java.util.*;
import java.math.*;

public class Problem45 {
    // Check Armstrong Number
    public static String isArmstrong(long n) {
        String s = String.valueOf(n);
        int len = s.length();
        long sum = 0;
        long temp = n;
        while (temp > 0) {
            long digit = temp % 10;
            sum += (long) Math.pow(digit, len);
            temp /= 10;
        }
        return (sum == n) ? "YES" : "NO";
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(isArmstrong(n));
    }
}