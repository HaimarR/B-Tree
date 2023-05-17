package main.java.Personal.Pathfinder;

import java.util.LinkedList;

public class Pathfinder<E> {
    private PFAdjGraph<PFVertex<E>> graph;

    public Pathfinder(Graph<PFVertex<E>> map) {
        this.graph = new PFAdjGraph<>();
    }
    
    public LinkedList<PFVertex<E>> pathfind(PFVertex<E> initial, PFVertex<E> goal) throws PathfinderException {
        if(initial.isOpen() && goal.isOpen()) {
            return (LinkedList<PFVertex<E>>)graph.BFPath(initial, goal);
        } else {
            throw new PathfinderException("Either the initial or the goal vertices are inaccessible.");
        }
    }

    public static void main(String[] args) {
        Tablemaker tablemaker = new Tablemaker(10, 10);
         
    }
}