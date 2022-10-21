import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class count {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("/users/zhaohan_dong/desktop/dataset_91065.txt");
        Scanner scanner = new Scanner(file);
        int evenNumbers = 0;
        while (scanner.hasNext()) {
            int next = scanner.nextInt();
            if (next == 0) {
                break;
            } else if (next % 2 == 0) {
                evenNumbers++;
            }
        }
        System.out.println(evenNumbers);
    }
}
