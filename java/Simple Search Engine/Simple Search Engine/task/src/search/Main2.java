package search;
import java.util.Scanner;
/**
class Dataset {
    private final String[] data;
    private final int length;

    public static Dataset newDataset() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of people:");
        int length = Integer.parseInt(scanner.nextLine());
        System.out.println("Enter all people:");
        String[] data = new String[length];
        for (int i = 0; i < length; i++) {
            data[i] = scanner.nextLine();
        }
        return new Dataset(data, length);
    }

    public static void query(Dataset dataset) {
        boolean found = false;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of search queries:");
        int n = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < n; i++) {
            System.out.println("Enter data to search people:");
            String key = scanner.nextLine();
            for (String s: dataset.data) {
                if (s.toLowerCase().contains(key.toLowerCase())) {
                    if (!found) {
                        System.out.println("Found people:");
                        found = true;
                    }
                    System.out.println(s);
                }
            }
            if (!found) { System.out.println("No matching people found."); }
            System.out.println();
        }
    }
    public Dataset(String[] data, int length) {
        this.data = data;
        this.length = length;
    }
}

*/
/**
public class Main2 {

    public static void main(String[] args) {
        Dataset dataset = Dataset.newDataset();
        Dataset.query(dataset);
    }
}
 */