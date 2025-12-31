import java.io.*;
import java.util.*;

public class Problem42 {
    // Smallest Prime Factor
    public static long smallestPrimeFactor(long n) {
        if (n % 2 == 0) return 2;
        for (long i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return i;
        }
        return n;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(smallestPrimeFactor(n));
    }
}