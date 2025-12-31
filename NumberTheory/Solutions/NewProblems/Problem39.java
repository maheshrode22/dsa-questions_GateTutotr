import java.io.*;
import java.util.*;

public class Problem39 {
    // Sum of First N Natural Numbers
    public static long sumOfN(long n) {
        return n * (n + 1) / 2;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(sumOfN(n));
    }
}