import java.util.*;

class Problem15 {
    public void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            // Print spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            // Print letters
            for (int j = 0; j < 2 * i - 1; j++) {
                System.out.print((char)('A' + j));
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem15().printPattern(n);
        }
    }
}
