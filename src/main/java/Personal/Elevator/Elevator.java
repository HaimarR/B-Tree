package main.java.Personal.Elevator;

import java.util.Arrays;

public class Elevator{

    private int totalLevels;
    private int currentLevel; 
    private int goingTo;
    private boolean onCall;
    private int[] calls;

    public Elevator(int totalLevels) {
        currentLevel = 0;
        goingTo = -2147483648;
        onCall = false;
        calls = new int[totalLevels];
    }

    public Elevator(int totalLevels, int currentLevel) {
        this(totalLevels, currentLevel, -2147483648, false, new int[totalLevels]);
    }

    public Elevator(int totalLevels, int currentLevel, int goingTo) {
        this(totalLevels, currentLevel, goingTo, false, new int[totalLevels]);
    }

    public Elevator(int totalLevels, int currentLevel, int goingTo, boolean onCall) {
        this(totalLevels, currentLevel, goingTo, onCall, new int[totalLevels]);
    }

    public Elevator(int totalLevels, int currentLevel, int goingTo, boolean onCall, int[] calls) {

    }

    public int getTotalLevels() {return totalLevels;}
    public int getCurrentLevel() {return currentLevel;}
    public int getGoingTo() {return goingTo;}
    public boolean getOnCall() {return onCall;}
    public int[] getCalls() {return calls;}

    public void goTo(int goingTo) {
        if (currentLevel < goingTo) {
            for (int i = currentLevel; i <= goingTo; i++ ) {
                currentLevel++;
            }
        } else if (currentLevel < goingTo) {
            for (int i = currentLevel; i <= goingTo; i++ ) {
                currentLevel++;
            }
        } else if (currentLevel == goingTo) {
            throw new IllegalArgumentException("");
        }
        
    }

    @Override
    public String toString() {
        return "Elevator{total=" + totalLevels + "; current=" + currentLevel + 
                "; goingTo=" + goingTo + "; onCall=" + onCall + "; calls=" + Arrays.toString(calls);  
    }
    public static void main(String[] args) {
        Elevator elevator = new Elevator(10);

        elevator.goTo(5);
        System.out.println(elevator);
    }
}