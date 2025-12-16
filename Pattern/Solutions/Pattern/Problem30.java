import java.util.*;

class Problem30 {
    public void printPattern(int n) {
        int height = 2 * n - 1;
        int mid = n - 1;
        char[][] grid = new char[height][height];
        for (int i = 0; i < height; i++) Arrays.fill(grid[i], ' ');
        // compute border coordinates
        List<int[]> border = new ArrayList<>();
        for (int i = 0; i < height; i++) {
            int offset = Math.abs(mid - i);
            int left = mid - (n - 1 - offset);
            int right = mid + (n - 1 - offset);
            if (left == right) {
                border.add(new int[]{i, left});
            } else {
                border.add(new int[]{i, left});
                border.add(new int[]{i, right});
            }
        }
        // order border roughly as perimeter walk (top to middle left, middle bottom, back up right)
        border.sort(Comparator.comparingInt((int[] a) -> a[0]).thenComparingInt(a -> a[1]));
        int val = 1;
        for (int[] cell : border) {
            grid[cell[0]][cell[1]] = (char)('0' + (val % 10));
            val++;
        }
        for (int i = 0; i < height; i++) {
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
            new Problem30().printPattern(n);
        }
    }
}
