/** package search;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

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

    static Dataset newDataset(String filepath) {
        File file = new File(filepath);
        int length = 0;
        ArrayList<String> fileData = new ArrayList<>();
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNext()) {
                fileData.add(scanner.nextLine());
                length++;
            }
        } catch (FileNotFoundException e) {
            System.out.println("No file found: " + filepath);
        }
        String[] data = new String[fileData.size()];
        data = fileData.toArray(data);
        return new Dataset(data, length);
    }

    static HashMap<String, Integer[]> createMap(Dataset dataset){
        String[] data = dataset.getData();
        LinkedHashMap<String, List<Integer>> map = new LinkedHashMap<>();
        HashMap<String, Integer[]> result = new HashMap<>();

        for (int i = 0; i < data.length; i++) {
            String[] subString = data[i].split(" ");
            for (String str: subString) {
                if (map.get(str.toLowerCase()) == null) {
                    map.put(str.toLowerCase(), new ArrayList<>());

                }
                map.get(str.toLowerCase()).add(i);
            }
        }

        for (String key : map.keySet()) {
            Integer[] array = map.get(key).toArray(new Integer[0]);
            result.put(key, array);
        }

        return result;
    }

    void query(Map map) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a name or email to search all suitable people.");
        String key = scanner.nextLine().toLowerCase();
        Integer[] indexArray = (Integer[]) map.get(key);
        if (indexArray == null) {
            System.out.println("No matching people found.");
        } else {
            System.out.println(String.format("%d persons found:", indexArray.length));
            for (int i = 0; i < indexArray.length; i++) {
                System.out.println(this.data[indexArray[i]]);
            }
        }
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

        // parsing arguments
        String filepath = null;
        if (args[0].equals("--data")) {
            filepath = args[1];
        }

        // create dataset
        Dataset dataset = Dataset.newDataset(filepath);
        Map<String, Integer[]> invertedIndexMap = Dataset.createMap(dataset);


        // run functions
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println();
            System.out.println("=== Menu ===");
            System.out.println("1. Find a person");
            System.out.println("2. Print all people");
            System.out.println("0. Exit");
            int select = scanner.nextInt();
            switch (select) {
                case 1:
                    dataset.query(invertedIndexMap);
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