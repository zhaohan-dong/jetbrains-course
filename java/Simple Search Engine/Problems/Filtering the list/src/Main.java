import java.util.*;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        List<String> list = Arrays.asList(scanner.nextLine().split(" "));
        ArrayList<String> arrayList = new ArrayList<>();
        for (int i = 1; i < list.size(); i += 2) {
            arrayList.add(list.get(i));
        }
        Collections.reverse(arrayList);
        System.out.println(arrayList.toString().replace("[", "").replace("]", "")
                .replace(",", ""));
    }
}