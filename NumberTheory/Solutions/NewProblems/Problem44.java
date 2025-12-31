import java.io.*;
import java.util.*;

public class Problem44 {
    // Reverse a Number
    public static long reverseNumber(long n) {
        long reversed = 0;
        while (n != 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return reversed;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(reverseNumber(n));
    }
}