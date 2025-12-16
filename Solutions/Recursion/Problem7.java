import java.util.*;

class Problem7 {
    public int countDigits(int n) {
        if (n == 0) return 1;
        if (n < 10) return 1;
        return 1 + countDigits(n / 10);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(new Problem7().countDigits(n));
        }
    }
}
