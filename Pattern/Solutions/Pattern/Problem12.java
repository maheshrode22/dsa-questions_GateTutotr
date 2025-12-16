import java.util.*;

class Problem12 {
    public void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            // Print spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            // Print numbers - each row starts from 1
            int num = 1;
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print(num);
                num++;
                if (num > 9) num = 0;
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem12().printPattern(n);
        }
    }
}
