import java.util.*;

class Problem5 {
    public void print1ToN(int n) {
        if (n == 0) return;
        print1ToN(n - 1);
        System.out.println(n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem5().print1ToN(n);
        }
    }
}
