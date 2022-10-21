import java.util.Scanner;
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        char[] wordArray = word.toCharArray();
        boolean palindrome = true;
        for (int i = 0; i <= wordArray.length / 2; i++) {
            if (wordArray[i] != wordArray[wordArray.length - 1 - i]) {
                palindrome = false;
                break;
            }
        }
        if (palindrome) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}