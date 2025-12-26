import java.util.*;

// Problem22: Last Digit of a^b
class Problem22 {
    private static int lastDigit(long a, long b) {
        if (b == 0) {
            // Define 0^0 as 1 per problem's test case
            return 1;
        }
        if (a == 0) return 0;
        int base = (int) ((a % 10 + 10) % 10);
        if (base == 0 || base == 1 || base == 5 || base == 6) {
            return base;
        }
        int cycleLen = 4;
        long e = (b - 1) % cycleLen + 1; // exponent within cycle
        int res = 1;
        for (int i = 0; i < e; i++) {
            res = (res * base) % 10;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            System.out.println(lastDigit(a, b));
        }
    }
}
