import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int lengthDict = Integer.parseInt(scanner.nextLine());
        HashSet<String> stringHashSet = new HashSet<>();
        for (int i = 0; i < lengthDict; i++) {
            stringHashSet.add(scanner.nextLine().toLowerCase());
        }
        int lines = Integer.parseInt(scanner.nextLine());
        HashSet<String> lineSet = new HashSet<>();
        for (int i = 0; i < lines; i++) {
            lineSet.addAll(Arrays.asList(scanner.nextLine().toLowerCase().split(" ")));
        }

        lineSet.removeAll(stringHashSet);

        System.out.println(lineSet.toString().replace("[", "").replace("]", "")
                .replace(", ", "\n"));
    }
}