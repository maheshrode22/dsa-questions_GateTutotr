import java.io.*;
import java.util.*;

public class Problem46 {
    // Find Next Prime Number
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    public static int nextPrime(int n) {
        if (n <= 1) return 2;
        int candidate = n + 1;
        while (true) {
            if (isPrime(candidate)) return candidate;
            candidate++;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        System.out.print(nextPrime(n));
    }
}