import java.io.*;
import java.util.*;

public class Problem47 {
    // Binary Exponentiation
    public static long modPow(long a, long b, long m) {
        long result = 1;
        a %= m;
        while (b > 0) {
            if (b % 2 == 1) {
                result = (result * a) % m;
            }
            a = (a * a) % m;
            b /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().trim().split(" ");
        long a = Long.parseLong(parts[0]);
        long b = Long.parseLong(parts[1]);
        long m = Long.parseLong(parts[2]);
        System.out.print(modPow(a, b, m));
    }
}