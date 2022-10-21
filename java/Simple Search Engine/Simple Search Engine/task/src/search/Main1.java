package search;
/**
import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        String target = scanner.nextLine();
        String[] stringArray = string.split(" ");
        String output = "Not found";
        for (int i=0; i<stringArray.length; i++) {
            if (stringArray[i].equals(target)) {
                output = Integer.toString(i + 1);
            }
        }
        System.out.println(output);
    }
}
 */