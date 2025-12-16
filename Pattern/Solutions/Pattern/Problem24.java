import java.util.*;

class Problem24 {
    public void printPattern(int n) {
        int[][] a = new int[n][n];
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int val = 1;
        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; j++) a[top][j] = val++;
            top++;
            for (int i = top; i <= bottom; i++) a[i][right] = val++;
            right--;
            if (top <= bottom) {
                for (int j = right; j >= left; j--) a[bottom][j] = val++;
                bottom--;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) a[i][left] = val++;
                left++;
            }
        }
        for (int i = 0; i < n; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (j > 0) row.append(' ');
                row.append(a[i][j]);
            }
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem24().printPattern(n);
        }
    }
}
