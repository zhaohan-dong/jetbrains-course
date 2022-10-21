public class constClass {
    public static void main(String[] args) {
        triangle triangleA = new triangle(15, 8, 15, 8, 17);
        triangle triangleB = new triangle(3, 2.598, 3, 3, 3);

        double triangleAArea = triangleA.findArea();
        System.out.println(triangleAArea);

        System.out.println(triangle.numOfSides);
    }
}
