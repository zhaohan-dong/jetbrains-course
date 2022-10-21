package encryptdecrypt;
import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String type = scanner.nextLine();
        String line = scanner.nextLine();
        int shift = scanner.nextInt();
        StringBuilder result = new StringBuilder();
        if (type.equals("enc")) {
            result = encryption(line, shift);
        } else if (type.equals("dec")) {
            result = decryption(line, shift);
        } else {
            result.append("Error");
        }
        System.out.println(result);
    }

    private static StringBuilder encryption(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c + shift));
        }
        return result;
    }

    private static StringBuilder decryption(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c - shift));
        }
        return result;
    }
}
