/* Please, do not rename it */
class Problem {

    public static void main(String[] args) {
        String operator = args[0];
        // write your code here
        int[] numbers = new int[args.length - 1];
        for (int i = 0; i < args.length - 1; i++) {
            numbers[i] = Integer.parseInt(args[i + 1]);
        }
        int result = 0;
        switch (operator) {
            case "MAX":
                result = max(numbers);
                break;
            case "MIN":
                result = min(numbers);
                break;
            case "SUM":
                result = sum(numbers);
                break;
        }
        System.out.println(result);

    }

    private static int max(int[] numbers) {
        int maxNum = numbers[0];
        for (int n : numbers) {
            if (n > maxNum) {
                maxNum = n;
            }
        }
        return maxNum;
    }

    private static int min(int[] numbers) {
        int minNum = numbers[0];
        for (int n : numbers) {
            if (n < minNum) {
                minNum = n;
            }
        }
        return minNum;
    }

    private static int sum(int[] numbers) {
        int sumNum = 0;
        for (int n : numbers) {
            sumNum += n;
        }
        return sumNum;
    }
}