import java.util.*;

class Problem6 {
    public String reverseString(String s) {
        if (s.length() <= 1) return s;
        return reverseString(s.substring(1)) + s.charAt(0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            System.out.println(new Problem6().reverseString(s));
        }
    }
}
