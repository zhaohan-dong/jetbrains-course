import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int output = 1;
        String[] strings = scanner.nextLine().split(" ");
        for (int i=0; i<strings.length-1; i++) {
            if (output > strings[i + 1].compareTo(strings[i])) {
                output = strings[i + 1].compareTo(strings[i]);
            }
        }

        if (output > -1) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}