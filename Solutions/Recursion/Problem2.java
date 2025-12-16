import java.util.*;

class Problem2 {
    public long sumN(int n) {
        if (n == 1) return 1;
        return n + sumN(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(new Problem2().sumN(n));
        }
    }
}
