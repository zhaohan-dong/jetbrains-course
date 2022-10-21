import java.util.Scanner;
import java.lang.*;



public class Main {

    public static boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        char[] arr = {'a', 'e', 'i', 'o', 'u'};
        for (char c: arr) {
            if (c == ch) {
                return true;
            }
        }
        return false;
    }

    /* Do not change code below */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char letter = scanner.nextLine().charAt(0);
        System.out.println(isVowel(letter) ? "YES" : "NO");
    }
}