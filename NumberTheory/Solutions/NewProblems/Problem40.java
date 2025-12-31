import java.io.*;
import java.util.*;

public class Problem40 {
    // Product Under Modulo
    public static long productModulo(long a, long b, long m) {
        return ((a % m) * (b % m)) % m;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().trim().split(" ");
        long a = Long.parseLong(parts[0]);
        long b = Long.parseLong(parts[1]);
        long m = Long.parseLong(parts[2]);
        System.out.print(productModulo(a, b, m));
    }
}