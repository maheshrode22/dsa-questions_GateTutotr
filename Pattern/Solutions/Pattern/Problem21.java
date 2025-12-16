import java.util.*;

class Problem21 {
    public void printPattern(int n) {
        int height = 2 * n - 1;
        for (int i = 1; i <= height; i++) {
            int r = (i <= n) ? i : (2 * n - i);
            int spaces = (i <= n) ? (n - i) : (i - n);
            // leading spaces
            for (int s = 0; s < spaces; s++) System.out.print(" ");
            if (r == 1) {
                System.out.println("1");
            } else {
                int inner = 2 * r - 3;
                System.out.print(r);
                for (int s = 0; s < inner; s++) System.out.print(" ");
                System.out.println(r);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem21().printPattern(n);
        }
    }
}
