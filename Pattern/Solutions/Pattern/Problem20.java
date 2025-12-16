import java.util.*;

class Problem20 {
    public void printPattern(int n) {
        int mid = n / 2 + 1;
        for (int i = 1; i <= n; i++) {
            StringBuilder line = new StringBuilder();
            int lastStar = -1;
            for (int j = 1; j <= n; j++) {
                if (i == mid || j == mid) {
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
            new Problem20().printPattern(n);
        }
    }
}
