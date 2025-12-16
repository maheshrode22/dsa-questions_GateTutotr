import java.util.*;

class Problem13 {
    public void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            // Print stars
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            // Print spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem13().printPattern(n);
        }
    }
}
