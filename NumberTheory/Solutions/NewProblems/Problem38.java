import java.io.*;
import java.util.*;

public class Problem38 {
    // Check If Number Is Even Or Odd
    public static String checkEvenOdd(long n) {
        return (n % 2 == 0) ? "EVEN" : "ODD";
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());
        System.out.print(checkEvenOdd(n));
    }
}