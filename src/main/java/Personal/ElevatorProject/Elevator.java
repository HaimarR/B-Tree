package main.java.Personal.ElevatorProject;

import java.util.Arrays;

public class Elevator{

    private int totalLevels;
    private int currentLevel;
    private boolean onCall;
    private int[] calls;
    public boolean doorsOpened = false;

    public Elevator(int totalLevels) {
        currentLevel = 0;
        onCall = false;
        calls = new int[totalLevels];
    }

    public Elevator(int totalLevels, int currentLevel) {
        this(totalLevels, currentLevel, false, new int[totalLevels]);
    }

    public Elevator(int totalLevels, int currentLevel, boolean onCall) {
        this(totalLevels, currentLevel, onCall, new int[totalLevels]);
    }

    public Elevator(int totalLevels, int currentLevel, boolean onCall, int[] calls) {

    }

    public int getTotalLevels() {return totalLevels;}
    public int getCurrentLevel() {return currentLevel;}
    public boolean getOnCall() {return onCall;}
    public int[] getCalls() {return calls;}
    public boolean getOpenDoors() {return doorsOpened;}

    public int goTo(Integer goingTo) {

        System.out.println(currentLevel);
        System.out.println(goingTo);

        if (currentLevel < goingTo) {
            for (int i = currentLevel; i <= goingTo; i++ ) {
                currentLevel = i;
                System.out.println("UP, " + currentLevel);
                
            }
            openDoors(goingTo);
        } else if (currentLevel > goingTo) {
            for (int i = currentLevel; i >= goingTo; i-- ) {
                currentLevel = i;
                System.out.println("DOWN, " + currentLevel);
                
            }
            openDoors(goingTo);
        } else if (currentLevel == goingTo) {
            throw new IllegalArgumentException("Elevator is already at level " + goingTo + ".");
        }

        return currentLevel;
        
    }

    public void openDoors(int goingTo) {
        System.out.println(currentLevel);
        System.out.println(goingTo);
        if (currentLevel == goingTo) {
            doorsOpened = true;
        } else {
            throw new IllegalArgumentException("Can't open doors. Elevtor is moving.");
        }
    }

    @Override
    public String toString() {
        return "Elevator{total=" + totalLevels + "; current=" + currentLevel + 
                "; onCall=" + onCall + "; calls=" + Arrays.toString(calls)+ "}";  
    }

    public static void main(String[] args) {
        Elevator elevator = new Elevator(10);

        elevator.goTo(5);
        System.out.println(elevator);
    }
}