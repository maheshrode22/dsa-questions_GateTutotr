import java.util.*;

class Problem27 {
    public void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            for (int s = 0; s < n - i; s++) System.out.print(" ");
            for (int x = 1; x <= i; x++) System.out.print(x);
            for (int x = i - 1; x >= 1; x--) System.out.print(x);
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem27().printPattern(n);
        }
    }
}
