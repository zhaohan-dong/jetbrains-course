public class ConcatenatingString {

    public static void main(String[] args) {
        int studentAge = 15;
        double studentGPA = 3.45;
        String studentFirstName = "Kayla";
        String studentLastName = "Hammon";

        System.out.println(studentAge);
        System.out.println(studentGPA);
        System.out.println(studentFirstName + " " + studentLastName
        + " has a GPA of " + studentGPA);

    }
}
