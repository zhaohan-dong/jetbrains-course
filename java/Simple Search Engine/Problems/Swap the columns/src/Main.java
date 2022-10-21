import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.nextLine();
        int[][] array = new int[a][b];
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                array[i][j] = scanner.nextInt();
            }
            scanner.nextLine();
        }

        int columnI = scanner.nextInt();
        int columnJ = scanner.nextInt();
        int[][] newArray = new int[a][b];
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if (j != columnI && j != columnJ) {
                    newArray[i][j] = array[i][j];
                } else if (j == columnI) {
                    newArray[i][j] = array[i][columnJ];
                } else {
                    newArray[i][j] = array[i][columnI];
                }
            }
        }

        System.out.println(Arrays.deepToString(newArray).replace("[", "")
                .replace("], ", "\n").replace(",", "")
                .replace("]]", ""));
    }
}