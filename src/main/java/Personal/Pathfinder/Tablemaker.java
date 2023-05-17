package main.java.Personal.Pathfinder;

public class Tablemaker {
    private int rows;
    private int cols;

    public Tablemaker(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
    }
    public int getRows() {return rows;}
    public int getCols() {return cols;}

    public PFTuple[][] make() {
        PFTuple[][] table = new PFTuple[rows][cols];
        PFTuple tuple = new PFTuple();
        for (int i = 0; i < rows; i++) {
            tuple.setRow(i);
            for (int j = 0; j < cols; j++) {
                tuple.setCol(j);
                table[i][j] = tuple;
            }
        }

        return table;
    }
}
