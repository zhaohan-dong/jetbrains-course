import java.util.Scanner;
import java.util.SortedMap;
import java.util.TreeMap;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int startInclusive = scanner.nextInt();
        int endInclusive = Integer.parseInt(scanner.nextLine().replace(" ", ""));
        int lineNumber = Integer.parseInt(scanner.nextLine());
        SortedMap<Integer, String> map = new TreeMap<>();
        for (int i = 0; i < lineNumber; i++) {
            int key = scanner.nextInt();
            String value = scanner.nextLine().replace(" ", "");
            map.put(key, value);
        }

        System.out.println(map.subMap(startInclusive, endInclusive + 1).toString()
                .replace("{", "").replace("}", "")
                .replace("=", " ").replace(", ", "\n"));
    }
}