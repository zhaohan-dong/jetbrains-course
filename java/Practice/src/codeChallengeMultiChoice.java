import java.util.Scanner;

public class codeChallengeMultiChoice {

    public static void main(String[] args) {
        String question = "Which is the largest planet in our solar system?";
        String choiceOne = "earth";
        String choiceTwo = "jupiter";
        String choiceThree = "saturn";

        String correctAnswer = choiceTwo;

        System.out.println(question);
        System.out.println(choiceOne);
        System.out.println(choiceTwo);
        System.out.println(choiceThree);
        System.out.println("Please select: ");
        Scanner input = new Scanner(System.in);
        String userInput = input.next().toLowerCase();
        if(userInput.equals(correctAnswer)) {
            System.out.println("Congrats!");
        } else {
            System.out.println("Wrong answer");
        }



    }
}