import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        int distance = Integer.MAX_VALUE;
        String s = scanner.nextLine();
        String[] strings = s.split(" ");
        for (String st: strings) {
            list.add(Integer.parseInt(st));
        }
        int N = scanner.nextInt();
        for (Integer n : list) {
            if (Math.abs(N - n) < distance) {
                result.clear();
                result.add(n);
                distance = Math.abs(N - n);
            } else if (Math.abs(N - n) == distance) {
                result.add(n);
            }
        }
        Collections.sort(result);
        result.forEach(n -> System.out.print(n + " "));
    }
}