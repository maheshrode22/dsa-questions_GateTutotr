import java.util.*;

class Problem26 {
    public void printPattern(int n) {
        if (n <= 0) return;
        int rows = 3;
        // approximate columns: for safety, use n + (n - 1)
        int cols = n + (n - 1);
        char[][] grid = new char[rows][cols];
        for (int i = 0; i < rows; i++) Arrays.fill(grid[i], ' ');
        int row = 0;
        boolean down = true;
        int col = 0;
        int cur = 1;
        for (int k = 0; k < n; k++) {
            char ch = (char)('0' + ((cur - 1) % 9 + 1));
            grid[row][col] = ch;
            cur++;
            if (down) {
                row++;
                if (row == rows) {
                    row = rows - 2;
                    down = false;
                }
            } else {
                row--;
                if (row < 0) {
                    row = 1;
                    down = true;
                }
            }
            col += 2;
            if (col >= cols && k != n - 1) {
                // expand columns if needed
                cols += 2;
                char[][] newGrid = new char[rows][cols];
                for (int i = 0; i < rows; i++) {
                    Arrays.fill(newGrid[i], ' ');
                    System.arraycopy(grid[i], 0, newGrid[i], 0, grid[i].length);
                }
                grid = newGrid;
            }
        }
        for (int i = 0; i < rows; i++) {
            String line = new String(grid[i]);
            int last = line.length() - 1;
            while (last >= 0 && line.charAt(last) == ' ') last--;
            if (last < 0) System.out.println();
            else System.out.println(line.substring(0, last + 1));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem26().printPattern(n);
        }
    }
}
