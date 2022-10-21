import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int min = Integer.MAX_VALUE;
        int arraySize = Integer.parseInt(scanner.nextLine());
        int[] array = new int[arraySize];
        String[] arrayStr = scanner.nextLine().split(" ");
        for (int i=0; i<arraySize; i++) {
            array[i] = Integer.parseInt(arrayStr[i]);
        }
        for (int i=0; i<arraySize; i++) {
            if (min > array[i]) {
                min = array[i];
            }
        }
        System.out.println(min);
    }
}