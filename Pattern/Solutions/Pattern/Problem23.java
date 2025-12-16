import java.util.*;

class Problem23 {
    public void printPattern(int n) {
        int[][] pascal = new int[n][n];
        for (int i = 0; i < n; i++) {
            pascal[i][0] = pascal[i][i] = 1;
            for (int j = 1; j < i; j++) {
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
            }
        }
        int maxWidth = (2 * (n - 1)) + 1; // rough centering via spaces
        for (int i = 0; i < n; i++) {
            int numCount = i + 1;
            int leadingSpaces = maxWidth - (2 * numCount - 1);
            for (int s = 0; s < leadingSpaces; s++) System.out.print(" ");
            for (int j = 0; j <= i; j++) {
                if (j > 0) System.out.print(" ");
                System.out.print(pascal[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem23().printPattern(n);
        }
    }
}
