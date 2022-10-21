import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max = scanner.nextInt();
        int i = 1;
        while (i * i <= max) {
            System.out.println(i * i);
            i++;
        }
    }
}