package main.java.Personal.Pathfinder;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class PFAdjGraph<E> implements Graph<E> {
    private Map<E, PFVertex<E>> vertices;
    
    public PFAdjGraph() {
        vertices = new HashMap<>();
    }

    @Override
    public void add(E value) {
        PFVertex<E> vertex = new PFVertex<>(value);
        vertices.put(value, vertex);
    }

    @Override
    public boolean contains(E value) {
        return vertices.containsKey(value);
    }

    @Override
    public int size() {
        return vertices.size();
    }

    @Override
    public void connect(E a, E b) {
        PFVertex<E> vertexA = vertices.get(a);
        PFVertex<E> vertexB = vertices.get(b);
        vertexA.connect(vertexB);
        vertexB.connect(vertexA);
    }

    @Override
    public boolean connected(E a, E b) {
        PFVertex<E> vertexA = vertices.get(a);
        PFVertex<E> vertexB = vertices.get(b);
        return vertexA.connected(vertexB);
    }

    @Override
    public boolean BFSearch(E start, E goal) {
        PFVertex<E> s = vertices.get(start);
        PFVertex<E> e = vertices.get(goal);

        Queue<PFVertex<E>> queue = new LinkedList<>();
        Set<PFVertex<E>> visited = new HashSet<>();

        queue.add(s);
        visited.add(s);

        while(!queue.isEmpty()) {
            PFVertex<E> v = queue.poll();
            if(v == e) {
                return true;
            } else {
                for(PFVertex<E> n : v.getNeighbors()) {
                    if(!visited.contains(n) && n.isOpen()) {
                        visited.add(n);
                        queue.add(n);
                    }
                }
            }
        }

        return false;
    }

    @Override
    public List<E> BFPath(E start, E goal) {
        PFVertex<E> s = vertices.get(start);
        PFVertex<E> e = vertices.get(goal);

        Queue<PFVertex<E>> queue = new LinkedList<>();
        Map<PFVertex<E>, PFVertex<E>> predecessors = new HashMap<>();

        queue.add(s);
        predecessors.put(s, null);

        while(!queue.isEmpty()) {
            PFVertex<E> v = queue.poll();
            if(v == e) {
                break;
            } else {
                for(PFVertex<E> n : v.getNeighbors()) {
                    if(!predecessors.containsKey(n) && n.isOpen()) {
                        predecessors.put(n, v);
                        queue.add(n);
                    }
                }
            }
        }

        return makePath(predecessors, e);
    }

    private List<E> makePath(Map<PFVertex<E>, PFVertex<E>> predecessors,
        PFVertex<E> end) {
            if(predecessors.containsKey(end)) {
                List<E> path = new LinkedList<>();
                PFVertex<E> current = end;
                while(current != null) {
                    path.add(0, current.getValue());
                    current = predecessors.get(current);
                }
                return path;
            } else { 
                return null;
            }
    }
}
