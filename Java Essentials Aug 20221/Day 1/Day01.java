class Student
{
    int roll;
    String name;
    float marks;
    void input(int rno, String nm, float mk)
    {
        roll = rno;
        name = nm;
        marks = mk;
    }
    void display()
    {
        System.out.println("\nRoll No: " + roll);
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
    }
}

class Day01
{
    public static void main(String[] args)
    {
        Student std1 = new Student();
        std1.input(1, "John", 83.5f);
        std1.display();

        Student std2 = new Student();
        std2.input(2, "Norman", 45.25f);
        std2.display();
    }
}