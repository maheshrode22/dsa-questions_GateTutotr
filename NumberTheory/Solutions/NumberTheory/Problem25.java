import java.util.*;

// Problem25: Count Non-Negative Solutions of ax + by = n
class Problem25 {
    private static long countSolutions(long a, long b, long n) {
        if (a <= 0 || b <= 0 || n < 0) return 0;
        long count = 0;
        long maxX = n / a;
        for (long x = 0; x <= maxX; x++) {
            long rem = n - a * x;
            if (rem < 0) break;
            if (rem % b == 0) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            long n = sc.nextLong();
            System.out.println(countSolutions(a, b, n));
        }
    }
}
