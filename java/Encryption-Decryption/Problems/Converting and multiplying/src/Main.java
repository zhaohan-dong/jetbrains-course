import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input;
        int out;
        while (scanner.hasNext()) {
            input = scanner.nextLine();
            if (input.equals("0")) {
                break;
            }
            try {
                out = Integer.parseInt(input);
                System.out.println(out * 10);
            } catch (Exception e) {
                System.out.println("Invalid user input: " + input);
            }
        }
    }
}