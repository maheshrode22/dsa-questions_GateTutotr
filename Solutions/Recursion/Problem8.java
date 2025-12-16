import java.util.*;

class Problem8 {
    public boolean isPalindrome(String s, int l, int r) {
        if (l >= r) return true;
        if (s.charAt(l) != s.charAt(r)) return false;
        return isPalindrome(s, l + 1, r - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Problem8 sol = new Problem8();
            System.out.println(sol.isPalindrome(s, 0, s.length() - 1) ? "YES" : "NO");
        }
    }
}
