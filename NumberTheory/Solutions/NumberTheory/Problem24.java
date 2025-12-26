import java.util.*;

// Problem24: Largest Coprime Divisor
class Problem24 {
    private static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private static long largestCoprimeDivisor(long A, long B) {
        long g;
        while ((g = gcd(A, B)) > 1) {
            A /= g;
        }
        return A;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long A = sc.nextLong();
            long B = sc.nextLong();
            System.out.println(largestCoprimeDivisor(A, B));
        }
    }
}
