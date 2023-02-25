package main.java.Personal.Elevator;

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
}