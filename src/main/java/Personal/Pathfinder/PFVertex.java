package main.java.Personal.Pathfinder;

import java.util.HashSet;
import java.util.Set;

public class PFVertex<E> {
    private E value;
    private Set<PFVertex<E>> neighbors;
    private boolean isOpen;

    public PFVertex(E value, boolean isOpen) {
        this.value = value;
        neighbors = new HashSet<>();
        this.isOpen = isOpen;
    }

    public PFVertex(E value) {
        this(value, true);
    }

    public E getValue() {return value;}
    public Set<PFVertex<E>> getNeighbors() {return neighbors;}
    public boolean isOpen() {return isOpen;}

    public void switchOpen() {
        isOpen = !isOpen;
    }

    public void connect(PFVertex<E> neighbor) {
        neighbors.add(neighbor);
    }

    public boolean connected(PFVertex<E> vertex) {
        return neighbors.contains(vertex);
    }
}
