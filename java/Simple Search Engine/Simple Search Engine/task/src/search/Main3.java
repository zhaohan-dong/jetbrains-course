package search;
import java.util.Arrays;
import java.util.Scanner;
/**
class Dataset extends DatasetAbstract {

    public Dataset(String[] data, int length) {
        this.data = data;
        this.length = length;
    }

    @Override
    public String[] getData() {
        return this.data;
    }

    @Override
    public int getLength() {
        return this.length;
    }
}

abstract class DatasetAbstract {
    protected String[] data;
    protected int length;

    abstract String[] getData();
    abstract int getLength();

    static Dataset newDataset() {
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

    void query() {
        boolean found = false;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a name or email to search all suitable people.");
        String key = scanner.nextLine();
        for (String s: this.data) {
            if (s.toLowerCase().contains(key.toLowerCase())) {
                if (!found) {
                    found = true;
                }
                System.out.println(s);
            }
        }
        if (!found) { System.out.println("No matching people found."); }
    }

    void print() {
        final String result = Arrays.toString(this.data)
                .replace(", ", "\n")
                .replace("[", "")
                .replace("]", "");
        System.out.println("=== List of people ===");
        System.out.print(result);
    }
}

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Dataset dataset = Dataset.newDataset();

        while (true) {
            System.out.println();
            System.out.println("=== Menu ===");
            System.out.println("1. Find a person");
            System.out.println("2. Print all people");
            System.out.println("0. Exit");
            int select = scanner.nextInt();
            switch (select) {
                case 1:
                    dataset.query();
                    break;
                case 2:
                    dataset.print();
                    break;
                case 0:
                    break;
                default:
                    System.out.println("Incorrect option! Try again.");
                    break;
            }
            System.out.println();
            if (select == 0) { break; }
        }
        System.out.println("Bye!");
    }
}
 */