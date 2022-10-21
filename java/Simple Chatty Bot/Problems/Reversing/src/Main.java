import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int hundred = number / 100;
        int tenth = (number - hundred * 100) / 10;
        int digit = number - hundred * 100 - tenth * 10;
        System.out.println(digit * 100 + tenth * 10 + hundred);
    }
}