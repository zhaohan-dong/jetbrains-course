package encryptdecrypt;

public class Main4 {
    public static void main(String[] args) {
        String mode = "enc";
        int key = 0;
        String data = "";
        StringBuilder result = new StringBuilder();
        for (int i = 1; i < args.length; i++) {
            if (args[i - 1].equals("-mode") && !args[i].equals("-key") && !args[i].equals("-data")) {
                mode = args[i];
            }
            if (args[i - 1].equals("-key") && !args[i].equals("-mode") && !args[i].equals("-data")) {
                key = Integer.parseInt(args[i]);
            }
            if (args[i - 1].equals("-data") && !args[i].equals("-key") && !args[i].equals("-mode")) {
                data = args[i];
            }
        }
        if (mode.equals("enc")) {
            result = encryption(data, key);
        } else if (mode.equals("dec")) {
            result = decryption(data, key);
        }
        System.out.println(result);
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
