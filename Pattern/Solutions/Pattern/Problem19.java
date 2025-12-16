import java.util.*;

class Problem19 {
    public void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            StringBuilder line = new StringBuilder();
            int lastStar = -1;
            for (int j = 1; j <= n; j++) {
                if (i == j || j == n - i + 1) {
                    line.append("*");
                    lastStar = line.length() - 1;
                } else {
                    line.append(" ");
                }
            }
            // Print only up to the last star (remove trailing spaces)
            if (lastStar >= 0) {
                System.out.println(line.substring(0, lastStar + 1));
            } else {
                System.out.println();
            }
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem19().printPattern(n);
        }
    }
}
