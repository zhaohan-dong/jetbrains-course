public class student {
    String firstName;
    String lastName;
    int expectedYearToGraduate;
    double GPA;
    String declaredMajor;

    public student(String firstName, String lastName,
                   int expectedYearToGraduate,
                   double GPA, String declaredMajor) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.expectedYearToGraduate = expectedYearToGraduate;
        this.GPA = GPA;
        this.declaredMajor = declaredMajor;
    }

    public void incrementExpectedGraduationYear() {
        this.expectedYearToGraduate = this.expectedYearToGraduate + 1;
    }

    public void printProfile() {
        System.out.println(this.firstName + " " + this.lastName + "\n" +
                "Expected Graduation Year: " + this.expectedYearToGraduate + "\n" +
                "GPA: " + this.GPA + "\n" +
                "Declared Major: " + this.declaredMajor);
    }
}
