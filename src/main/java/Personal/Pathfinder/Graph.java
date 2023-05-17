package main.java.Personal.Pathfinder;

import java.util.List;

public interface Graph<E> {
    void add(E value);
    boolean contains(E value);
    int size();
    void connect(E a, E b);
    boolean connected(E a, E b);
    boolean BFSearch(E start, E goal);
    List<E> BFPath(E start, E goal);
}
