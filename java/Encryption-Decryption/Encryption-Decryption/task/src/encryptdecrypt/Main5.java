package encryptdecrypt;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main5 {
    public static void main(String[] args) throws FileNotFoundException {
        String mode = "enc";
        int key = 0;
        String data = "";
        String in = "";
        String out = "";
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < args.length; i += 2) {
            switch (args[i]) {
                case "-mode":
                    mode = args[i + 1];
                    break;
                case "-key":
                    key = Integer.parseInt(args[i + 1]);
                    break;
                case "-data":
                    data = args[i + 1];
                    break;
                case "-in":
                    in = args[i + 1];
                    break;
                case "-out":
                    out = args[i + 1];
                    break;
            }
        }


        if (!in.isEmpty() && data.isEmpty()) {
            File inFile = new File(in);
            try (Scanner scanner = new Scanner(inFile)) {
                data = scanner.nextLine();
            }
        }


        if (mode.equals("enc")) {
            result = encryption(data, key);
        } else if (mode.equals("dec")) {
            result = decryption(data, key);
        }


        if (out.isEmpty()) {
            System.out.println(result);
        } else {
            File outFile = new File(out);
            try (FileWriter writer = new FileWriter(outFile)) {
                writer.write(String.valueOf(result));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }


    private static StringBuilder encryption(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c + shift));
        }
        return result;
    }


    private static StringBuilder decryption(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c - shift));
        }
        return result;
    }
}
