import java.util.Scanner;

class Cab
{
    int fare;
    int distance;

    public Cab(int initialDistance, int distance)
    {
        fare = 50 + (initialDistance + distance) * 10;
        /*
            Fare has a base cost of 50
            initial distance is the distance between cab & user initially
            distance is the distance travelled by the user in the cab
        */
    }

    void cost()
    {
        System.out.println("Total Fare: ₹" + fare);
    }
}

class Day03
{
    public static void main(String[] args)
    {
        int initialDistance, distance;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Distance from Cab: ");
        initialDistance = scanner.nextInt();
        System.out.println("Enter Distance: ");
        distance = scanner.nextInt();

        // initial distance is only considered if it is more than 5
        if(initialDistance > 5)
            initialDistance -= 5;
        else
            initialDistance = 0;
        
        Cab myCab = new Cab(initialDistance, distance);
        myCab.cost();

        scanner.close();
    }
}