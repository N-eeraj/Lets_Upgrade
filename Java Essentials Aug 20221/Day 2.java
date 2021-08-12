import java.util.Scanner;

class Day02
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int num1, num2;

        System.out.println("Enter First Number: ");
        num1 = scanner.nextInt();
        System.out.println("Enter Second Number: ");
        num2 = scanner.nextInt();
        
        System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));

        scanner.close();
    }
}