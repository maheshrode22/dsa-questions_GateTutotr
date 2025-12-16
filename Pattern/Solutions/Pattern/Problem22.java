import java.util.*;

class Problem22 {
    public void printPattern(int n) {
        int size = 2 * n - 1;
        for (int i = 0; i < size; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < size; j++) {
                int top = i;
                int left = j;
                int bottom = size - 1 - i;
                int right = size - 1 - j;
                int dist = Math.min(Math.min(top, bottom), Math.min(left, right));
                int val = n - dist;
                if (j > 0) row.append(' ');
                row.append(val);
            }
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem22().printPattern(n);
        }
    }
}
