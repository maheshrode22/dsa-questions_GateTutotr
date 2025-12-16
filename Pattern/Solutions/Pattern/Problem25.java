import java.util.*;

class Problem25 {
    public void printPattern(int n) {
        int totalRows = 2 * n - 1;
        for (int i = 1; i <= totalRows; i++) {
            int row = i <= n ? i : (2 * n - i);
            int num = i <= n ? i : (2 * n - i);
            int innerSpaces = (n - row) * 2 + 1;
            // left stars
            for (int s = 0; s < row; s++) System.out.print("*");
            // spaces before number
            for (int s = 0; s < innerSpaces; s++) System.out.print(" ");
            System.out.print(num);
            // spaces after number
            for (int s = 0; s < innerSpaces; s++) System.out.print(" ");
            // right stars
            for (int s = 0; s < row; s++) System.out.print("*");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem25().printPattern(n);
        }
    }
}
