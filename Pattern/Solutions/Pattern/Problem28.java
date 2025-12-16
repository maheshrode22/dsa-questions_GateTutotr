import java.util.*;

class Problem28 {
    public void printPattern(int n) {
        int size = 2 * n - 1;
        int mid = size / 2;
        for (int i = 0; i < size; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < size; j++) {
                if (i == 0 || i == size - 1) {
                    row.append('*');
                } else {
                    // hourglass borders
                    int dist = Math.min(Math.min(i, size - 1 - i), Math.min(j, size - 1 - j));
                    if (i <= mid) {
                        // top half
                        if (j == i || j == size - 1 - i) row.append('*');
                        else if (j == mid) row.append(' ');
                        else row.append(' ');
                    } else {
                        // bottom half
                        int bi = size - 1 - i;
                        if (j == bi || j == size - 1 - bi) row.append('*');
                        else if (j == mid) row.append(' ');
                        else row.append(' ');
                    }
                }
            }
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            new Problem28().printPattern(n);
        }
    }
}
