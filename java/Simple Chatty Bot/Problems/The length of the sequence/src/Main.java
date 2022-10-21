import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num;
        int i = 0;
        do {
            num = scanner.nextInt();
            i++;
        } while (num != 0);
        System.out.println(i - 1);
    }
}