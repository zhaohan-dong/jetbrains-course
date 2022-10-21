public class Main {

    public static void main(String[] args) {
        student studentA = new student("Billy", "King", 2020, 3.9, "Biology" );
        student studentB = new student("Martha", "Scorsese", 2022, 3.88, "Film");
        studentA.printProfile();
        studentB.printProfile();
        studentB.incrementExpectedGraduationYear();
        studentB.printProfile();
    }
}
