import java.util.*;

class Problem29 {
    public void printPattern(int n) {
        for (int i = 0; i < n; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    row.append(i + 1);
                } else if (i + j == n - 1) {
                    row.append(n - i);
                } else {
                    row.append('.');
                }
            }
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem29().printPattern(n);
        }
    }
}
