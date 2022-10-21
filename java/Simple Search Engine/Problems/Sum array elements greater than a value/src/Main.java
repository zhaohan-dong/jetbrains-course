import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int arraySize = Integer.parseInt(scanner.nextLine());
        int[] array = new int[arraySize];
        int sum = 0;
        String[] arrayStr = scanner.nextLine().split(" ");
        for (int i=0; i<arraySize; i++) {
            array[i] = Integer.parseInt(arrayStr[i]);
        }
        int max = scanner.nextInt();
        for (int i=0; i<arraySize; i++) {
            if (max < array[i]) {
                sum += array[i];
            }
        }
        System.out.println(sum);
    }
}