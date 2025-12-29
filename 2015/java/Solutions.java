import java.util.*;

class RecursiveFactorial {
    public static long factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(factorial(n));
        }
    }
}

class RecursiveSumOfDigits {
    public static int sumOfDigits(long n) {
        if (n == 0) return 0;
        return (int)(n % 10) + sumOfDigits(n / 10);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            System.out.println(sumOfDigits(n));
        }
    }
}

class RecursiveFibonacci {
    public static int fibonacci(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(fibonacci(n));
        }
    }
}

class RecursivePower {
    public static long power(int a, int b) {
        if (b == 0) return 1;
        long half = power(a, b / 2);
        if (b % 2 == 0) return half * half;
        return a * half * half;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(power(a, b));
        }
    }
}

class TowerOfHanoi {
    public static void towerOfHanoi(int n, int source, int destination, int auxiliary) {
        if (n == 1) {
            System.out.println("Move disk 1 from rod " + source + " to rod " + destination);
            return;
        }
        towerOfHanoi(n - 1, source, auxiliary, destination);
        System.out.println("Move disk " + n + " from rod " + source + " to rod " + destination);
        towerOfHanoi(n - 1, auxiliary, destination, source);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            towerOfHanoi(n, 1, 3, 2);
        }
    }
}

class RecursiveStringReversal {
    public static String reverseString(String s) {
        if (s == null || s.length() <= 1) return s;
        return reverseString(s.substring(1)) + s.charAt(0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            System.out.println(reverseString(s));
        }
    }
}

class RecursiveCheckSorted {
    public static boolean isSorted(int[] arr, int n) {
        if (n <= 1) return true;
        if (arr[n - 2] > arr[n - 1]) return false;
        return isSorted(arr, n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            if (isSorted(arr, n)) System.out.println("Yes");
            else System.out.println("No");
        }
    }
}

class StringPermutations {
    public static void generatePermutations(char[] chars, boolean[] used, StringBuilder current, Set<String> result) {
        if (current.length() == chars.length) {
            result.add(current.toString());
            return;
        }
        for (int i = 0; i < chars.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.append(chars[i]);
            generatePermutations(chars, used, current, result);
            current.deleteCharAt(current.length() - 1);
            used[i] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            Set<String> result = new LinkedHashSet<>();
            generatePermutations(chars, new boolean[chars.length], new StringBuilder(), result);
            for (String p : result) System.out.println(p);
        }
    }
}

class NQueensCount {
    private static int count = 0;

    public static void solve(int row, int n, boolean[] cols, boolean[] diag1, boolean[] diag2) {
        if (row == n) {
            count++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[row + col] || diag2[row - col + n - 1]) continue;
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = true;
            solve(row + 1, n, cols, diag1, diag2);
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            count = 0;
            solve(0, n, new boolean[n], new boolean[2 * n], new boolean[2 * n]);
            System.out.println(count);
        }
    }
}

class SubsetSum {
    public static boolean isSubsetSum(int[] arr, int n, int k) {
        if (k == 0) return true;
        if (n == 0) return false;
        if (arr[n - 1] > k) return isSubsetSum(arr, n - 1, k);
        return isSubsetSum(arr, n - 1, k) || isSubsetSum(arr, n - 1, k - arr[n - 1]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int k = sc.nextInt();
            if (isSubsetSum(arr, n, k)) System.out.println("Yes");
            else System.out.println("No");
        }
    }
}
