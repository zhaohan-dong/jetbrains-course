import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line1 = scanner.nextLine();
        String line2 = scanner.nextLine();
        line1 = line1.replace(" ", "");
        line2 = line2.replace(" ", "");
        System.out.println(line1.equals(line2));
    }
}