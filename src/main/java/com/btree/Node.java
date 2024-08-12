package com.btree;

import java.util.List;

public class Node<E extends Comparable<E>> {
    private SortedList<E> values;
    private Integer maxSize;
    private Integer minSize;
    private List<Node<E>> children;
    private Node<E> parent;

    public Node(Integer maxSize) {
        this.maxSize = maxSize;
        this.minSize = maxSize/2;
    }

    public SortedList<E> getValues() {
        return values;
    }

    public Node<E> getParent() {
        return parent;
    }

    public List<Node<E>> getChildren() {
        return children;
    }

    public int getMaxSize() {
        return maxSize;
    }

    public int getMinSize() {
        return minSize;
    }

    // Only to be used by addChild()
    public void setParent(Node<E> parent) {
        this.parent = parent;
    }

    public void addChild(Node<E> child) {
        children.add(child);
        child.setParent(this);
    }

    public void addChild(Node<E> child, int index) {
        children.add(index, child);
        child.setParent(this);
    }

    public int getOwnIndex() {
        if(this.parent == null) {
            return 0;
        } else {
            List<Node<E>> siblings = this.parent.getChildren();
            return siblings.indexOf(this);
        }
    }

    public void add(E value) {
        if(values.size() <= maxSize) {
            values.add(value);
        } else {
            split();
        }
    }

    public void split() {
        // Values less than the middle index stay in node
        // No code required for this step

        // Middle index goes to parent
        int middleIndex = maxSize/2;
        if (this.parent == null) {
            this.parent = new Node<E>(maxSize);
        }
        E newParentValue = values.pop(middleIndex);
        this.parent.add(newParentValue);

        // Values more than middle index get added to a new node right to current (add a child to the parent on index <current +1>)º
        int ownIndex = getOwnIndex();
        this.parent.addChild(parent, ownIndex+1);
        Node<E> newChild = this.parent.getChildren().get(ownIndex+1);
        for(int i = middleIndex+1; i <= maxSize; i++) {
            newChild.add(values.pop(i));
        }

        // Now we need to split the children of the node we just split
        // A node that needs to be split will always have <maxSize + 2> children
        // This means there is always one more child than the number of values required for the split
        // Therefore, no need to check for children, but let's do it anyways just in case I broke something
        if(this.children.size() != maxSize+2) {
            try {
                throw new Exception("The number of children is not maxSize + 2");
            } catch (Exception e) {
                e.printStackTrace();
            }
            return;
        }

        // The first half of the children stay on the current node, so no code needed
        // The second half is adopted by the new node we just created
        for(int i = (maxSize+2)/2; i < (maxSize+2); i++) {
            this.children.get(i).setParent(newChild);
        }

    }
}
