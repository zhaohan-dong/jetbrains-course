import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sequence = scanner.nextLine();
        sequence = sequence.toLowerCase();
        long count = 0L;
        char[] sequenceChar = sequence.toCharArray();
        for (int i = 0; i < sequence.length(); i++) {
            if (sequenceChar[i] == 'g' || sequenceChar[i] == 'c') {
                count++;
            }
        }
        double GCContent = (double) count / sequenceChar.length * 100;
        System.out.println(GCContent);
    }
}