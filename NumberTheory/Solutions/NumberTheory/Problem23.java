import java.util.*;

// Problem23: Count Distinct Prime Factors
class Problem23 {
    private static int countDistinctPrimes(long n) {
        if (n <= 1) return 0;
        int count = 0;
        // factor 2
        if (n % 2 == 0) {
            count++;
            while (n % 2 == 0) n /= 2;
        }
        for (long p = 3; p * p <= n; p += 2) {
            if (n % p == 0) {
                count++;
                while (n % p == 0) n /= p;
            }
        }
        if (n > 1) count++;
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            System.out.println(countDistinctPrimes(n));
        }
    }
}
