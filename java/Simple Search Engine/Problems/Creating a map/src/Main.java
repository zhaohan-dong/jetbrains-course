import java.util.*;

public class Main {

    public static void main(String[] args) {    
        // write your code here
        SortedMap<String, Integer> map = new TreeMap<>(
                Map.of("Omega", 24, "Alpha", 1, "Gamma", 3));
        System.out.println(map);
    }
}