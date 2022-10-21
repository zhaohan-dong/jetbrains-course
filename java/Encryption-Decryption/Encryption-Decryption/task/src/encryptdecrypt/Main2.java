package encryptdecrypt;
import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        int shift = scanner.nextInt();
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        char tempRes;
        for (char c : stringChar) {
            if (c == ' ') {
                tempRes = ' ';
            } else if (c + shift > 122) {
                tempRes = (char) (c + shift - 26);
            } else {
                tempRes = (char) (c + shift);
            }
            result.append(tempRes);
        }
        System.out.println(result);
    }
}
