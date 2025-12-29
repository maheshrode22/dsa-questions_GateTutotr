import java.util.*;
import java.io.*;

class LinearProbing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            int[] table = new int[m];
            Arrays.fill(table, -1);
            for (int i = 0; i < n; i++) {
                int key = sc.nextInt();
                int idx = key % m;
                for (int j = 0; j < m; j++) {
                    int curr = (idx + j) % m;
                    if (table[curr] == -1) {
                        table[curr] = key;
                        break;
                    }
                }
            }
            for (int i = 0; i < m; i++) {
                System.out.print(table[i] + (i == m - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}

class QuadraticProbing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            int[] table = new int[m];
            Arrays.fill(table, -1);
            for (int i = 0; i < n; i++) {
                int key = sc.nextInt();
                int idx = key % m;
                for (int j = 0; j < m; j++) {
                    int curr = (int)((idx + (long)j * j) % m);
                    if (table[curr] == -1) {
                        table[curr] = key;
                        break;
                    }
                }
            }
            for (int i = 0; i < m; i++) {
                System.out.print(table[i] + (i == m - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}

class DoubleHashing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int p = sc.nextInt();
            int n = sc.nextInt();
            int[] table = new int[m];
            Arrays.fill(table, -1);
            for (int i = 0; i < n; i++) {
                int key = sc.nextInt();
                int h1 = key % m;
                int h2 = p - (key % p);
                for (int j = 0; j < m; j++) {
                    int curr = (int)((h1 + (long)j * h2) % m);
                    if (table[curr] == -1) {
                        table[curr] = key;
                        break;
                    }
                }
            }
            for (int i = 0; i < m; i++) {
                System.out.print(table[i] + (i == m - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}

class SeparateChaining {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            List<Integer>[] table = new ArrayList[m];
            for (int i = 0; i < m; i++) table[i] = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int key = sc.nextInt();
                table[key % m].add(key);
            }
            for (int i = 0; i < m; i++) {
                System.out.print("Index " + i + ": ");
                for (int j = 0; j < table[i].size(); j++) {
                    System.out.print(table[i].get(j) + (j == table[i].size() - 1 ? "" : " "));
                }
                System.out.println();
            }
        }
    }
}

class CountDistinct {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Set<Integer> set = new HashSet<>();
            for (int i = 0; i < n; i++) set.add(sc.nextInt());
            System.out.println(set.size());
        }
    }
}

class FirstRepeating {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            Map<Integer, Integer> counts = new HashMap<>();
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
                counts.put(arr[i], counts.getOrDefault(arr[i], 0) + 1);
            }
            int res = -1;
            for (int x : arr) {
                if (counts.get(x) > 1) {
                    res = x;
                    break;
                }
            }
            System.out.println(res);
        }
    }
}
