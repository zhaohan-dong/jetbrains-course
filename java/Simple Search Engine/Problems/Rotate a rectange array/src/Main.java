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
            if (scanner.hasNextLine()) { scanner.nextLine(); }
        }

        int[][] newArray = new int[b][a];
        for (int i = 0; i < b; i++) {
            for (int j = 0; j < a; j++) {
                newArray[i][j] = array[Math.abs(j-(a-1))][i];
            }
        }

        System.out.println(Arrays.deepToString(newArray).replace("[", "")
                .replace("], ", "\n").replace(",", "")
                .replace("]]", ""));
    }
}