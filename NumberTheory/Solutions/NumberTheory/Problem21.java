import java.util.*;

// Problem21: Check Composite Number
class Problem21 {
    private static boolean isComposite(int n) {
        if (n <= 3) return false; // 1,2,3 are not composite
        if (n % 2 == 0) return n > 2;
        int limit = (int) Math.sqrt(n);
        for (int i = 3; i <= limit; i += 2) {
            if (n % i == 0) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(isComposite(n) ? "YES" : "NO");
        }
    }
}
