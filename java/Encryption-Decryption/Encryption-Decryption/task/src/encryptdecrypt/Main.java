package encryptdecrypt;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;


interface Algorithm {
    StringBuilder encrypt(String string, int shift);

    StringBuilder decrypt(String string, int shift);
}

class Calculation {
    private Algorithm algorithm;

    public Calculation(String alg) {
        if (alg.equals("unicode")) {
            this.algorithm = new Unicode();
        } else if (alg.equals("shift")) {
            this.algorithm = new Shift();
        }
    }
    StringBuilder encrypt(String string, int shift) { return this.algorithm.encrypt(string, shift); }
    StringBuilder decrypt(String string, int shift) {
        return this.algorithm.decrypt(string, shift);
    }
}

class Unicode implements Algorithm {
    @Override
    public StringBuilder encrypt(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c + shift));
        }
        return result;
    }

    @Override
    public StringBuilder decrypt(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : stringChar) {
            result.append((char) (c - shift));
        }
        return result;
    }
}

class Shift implements Algorithm {
    @Override
    public StringBuilder encrypt(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        char tempRes;
        for (char c : stringChar) {
            if (c >= 65 && c <= 90) {
                if (c + shift > 90) {
                    tempRes = (char) (c + shift - 26);
                } else {
                    tempRes = (char) (c + shift);
                }
            } else if (c >= 97 && c <= 122) {
                if (c + shift > 122) {
                    tempRes = (char) (c + shift - 26);
                } else {
                    tempRes = (char) (c + shift);
                }
            } else {
                tempRes = c;
            }
            result.append(tempRes);
        }
        return result;
    }

    @Override
    public StringBuilder decrypt(String string, int shift) {
        char[] stringChar = string.toCharArray();
        StringBuilder result = new StringBuilder();
        char tempRes;
        for (char c : stringChar) {
            if (c >= 65 && c <= 90) {
                if (c - shift < 65) {
                    tempRes = (char) (c - shift + 26);
                } else {
                    tempRes = (char) (c - shift);
                }
            } else if (c >= 97 && c <= 122) {
                if (c - shift < 97) {
                    tempRes = (char) (c - shift + 26);
                } else {
                    tempRes = (char) (c - shift);
                }
            } else {
                tempRes = c;
            }
            result.append(tempRes);
        }
        return result;
    }
}


public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        String mode = "enc";
        int key = 0;
        String data = "";
        String in = "";
        String out = "";
        String alg = "shift";
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
                case "-alg":
                    alg = args[i + 1];
                    break;
            }
        }


        if (!in.isEmpty() && data.isEmpty()) {
            File inFile = new File(in);
            try (Scanner scanner = new Scanner(inFile)) {
                data = scanner.nextLine();
            }
        }

        Calculation calculation = new Calculation(alg);

        if (mode.equals("enc")) {
            result = calculation.encrypt(data, key);
        } else if (mode.equals("dec")) {
            result = calculation.decrypt(data, key);
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
}