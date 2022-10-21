import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sequence = scanner.nextLine();
        char[] sequenceChar = sequence.toCharArray();
        long prevCount = 0L;
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < sequenceChar.length; i++) {
            if (i == 0) {
                result.append(sequenceChar[i]);
                prevCount++;
            } else if (sequenceChar[i] == sequenceChar[i-1]) {
                prevCount++;
            } else {
                result.append(prevCount);
                prevCount = 1L;
                result.append(sequenceChar[i]);
            }
        }
        result.append(prevCount);
        System.out.println(result);
    }
}
