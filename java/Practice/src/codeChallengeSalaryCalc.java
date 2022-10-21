public class codeChallengeSalaryCalc {
    public static double grossYearlySalary(double hoursPerWeek,
                                           double moneyPerHour,
                                           int vacationDays) {
        return hoursPerWeek * moneyPerHour * 52 - vacationDays * 8 * moneyPerHour;
    }
    public static void main(String[] args) {
    System.out.println(grossYearlySalary(40, 15, 0));
    }
}
