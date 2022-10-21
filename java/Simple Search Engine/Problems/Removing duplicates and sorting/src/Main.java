import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int length = Integer.parseInt(scanner.nextLine());
        SortedSet<String> sortedSet = new TreeSet<>();
        for (int i = 0; i < length; i++) {
            sortedSet.add(scanner.nextLine());
        }
        System.out.println(sortedSet.toString().replace("[", "").replace("]", "")
                .replace(", ", "\n"));
    }
}