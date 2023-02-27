package main.java.Personal.ElevatorProject;

public class Person{
    private int currentLevel;
    private Elevator elevator;

    public Person(int currentLevel) {
        this.currentLevel = currentLevel;
        elevator = new Elevator(10);
    }

    public int getCurrentLevel() {return currentLevel;}
    public Elevator getElevator() {return elevator;}

    public int call(Elevator elevator) {
        elevator.goTo(currentLevel);
        return currentLevel;
    }

    public int goTo(Integer goTo) {
        currentLevel = elevator.goTo(goTo);
        return currentLevel;
    }

    @Override
    public String toString() {
        return "Person {level=" + currentLevel + "}";
    }

    public static void main(String[] args) {
        Elevator elevator = new Elevator(10, 0);
        Person person = new Person(5);

        System.out.println(elevator);
        System.out.println(person);

        person.call(elevator);
        System.out.println(elevator);
        System.out.println(person);

        elevator.goTo(0);
        System.out.println(elevator);
        System.out.println(person);
    }
}