import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int num3 = scanner.nextInt();
        int i = 0;
        if(num1 > 0) {
            i++;
        }
        if (num2 > 0) {
            i++;
        }
        if (num3 > 0) {
            i++;
        }
        System.out.println(i == 1);
    }
}