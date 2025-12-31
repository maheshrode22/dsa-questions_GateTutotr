import java.io.*;
import java.util.*;

public class Problem41 {
    // Check If Number Is Divisible By Another
    public static String isDivisible(long a, long b) {
        return (a % b == 0) ? "YES" : "NO";
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().trim().split(" ");
        long a = Long.parseLong(parts[0]);
        long b = Long.parseLong(parts[1]);
        System.out.print(isDivisible(a, b));
    }
}