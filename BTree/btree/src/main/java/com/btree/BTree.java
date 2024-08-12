package com.btree;

import java.util.HashSet;

public class BTree<E extends Comparable<E>> {
    private final int maxNodeSize;
    private final int minNodeSize;
    private HashSet<E> values;
    private Node<E> root;

    public BTree(int maxNodeSize) {
        this.maxNodeSize = maxNodeSize;
        this.minNodeSize = maxNodeSize/2;
        this.values = new HashSet<E>();
        this.root = new Node<E>(maxNodeSize);
    }

    public int getMaxNodeSize() {
        return maxNodeSize;
    }

    public int getMinNodeSize() {
        return minNodeSize;
    }

    public void insert(E value) {
        if(!values.contains(value)) {
            root.add(value);
        }
    }
}