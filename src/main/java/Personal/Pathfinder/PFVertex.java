package main.java.Personal.Pathfinder;

import java.util.HashSet;
import java.util.Set;

public class PFVertex<E> {
    private E value;
    private Set<PFVertex<E>> neighbors;

    public PFVertex(E value) {
        this.value = value;
        neighbors = new HashSet<>();
    }

    public E getValue() {return value;}
    public Set<PFVertex<E>> getNeighbors() {return neighbors;}

    public void connect(PFVertex<E> neighbor) {
        neighbors.add(neighbor);
    }

    public boolean connected(PFVertex<E> vertex) {
        return neighbors.contains(vertex);
    }
}
