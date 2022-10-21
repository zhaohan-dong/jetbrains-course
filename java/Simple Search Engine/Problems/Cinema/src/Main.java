import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] seats = new int[n][m];
        int result = 0;
        boolean counting = true;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                seats[i][j] = scanner.nextInt();
            }
            scanner.nextLine();
        }

        int conSeat = scanner.nextInt();

        for (int i = 0; i < n && counting; i++) {
            for (int j = 0; j <= m - conSeat && counting; j++) {
                if (seats[i][j] == 0) {
                    int sum = 0;
                    for (int k = j + 1; k < j + conSeat; k++) {
                        sum += seats[i][k];
                    }
                    if (sum == 0) {
                        result = i + 1;
                        counting = false;
                    }
                }
            }
        }

        System.out.println(result);
    }
}