package com.btree;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Objects;

public class SortedList<E extends Comparable<E>>{
    private List<E> values;

    public SortedList() {
        this.values = new ArrayList<E>();
    }
    
    public int size() {
        return values.size();
    }

    
    public boolean isEmpty() {
        return values.isEmpty();
    }

    
    public boolean contains(Object o) {
        return values.contains(o);
    }

    
    public Iterator<E> iterator() {
        return values.iterator();
    }

    
    public Object[] toArray() {
        return values.toArray();
    }

    
    public <T> T[] toArray(T[] a) {
        return values.toArray(a);
    }

    
    public boolean add(E e) {
        int index = 0;
        for (E value : values) {
            if (e.compareTo(value) < 0) {
                break;
            }
            index++;
        }
        values.add(index, e);
        return true;
    }

    
    public boolean remove(E value) {
        return values.remove(value);
    }

    public E pop(int index) {
        return values.remove(index);
    }

    
    public boolean containsAll(Collection<?> c) {
        return values.containsAll(c);
    }

    
    public boolean addAll(Collection<? extends E> c) {
        return values.addAll(c);
    }

    
    public boolean addAll(int index, Collection<? extends E> c) {
        return values.addAll(index, c);
    }

    
    public boolean removeAll(Collection<?> c) {
        return values.removeAll(c);
    }

    
    public boolean retainAll(Collection<?> c) {
        return values.retainAll(c);
    }

    
    public void clear() {
        values.clear();
    }

    
    public E get(int index) {
        return values.get(index);
    }

    
    public E set(int index, E element) {
        return values.set(index, element);
    }

    
    public void add(int index, E element) {
        values.add(index, element);
    }

    // 
    // public E remove(int index) {
    //     return values.remove(index);
    // }

    
    public int indexOf(Object o) {
        return values.indexOf(o);
    }

    
    public int lastIndexOf(Object o) {
        return values.lastIndexOf(o);
    }

    
    public ListIterator<E> listIterator() {
        return values.listIterator();
    }

    
    public ListIterator<E> listIterator(int index) {
        return values.listIterator(index);
    }

    
    public List<E> subList(int fromIndex, int toIndex) {
        return values.subList(fromIndex, toIndex);
    }

    
    public boolean equals(Object obj) {
        if(this == obj) {
            return true;
        }
        if(obj == null || getClass() != obj.getClass()) {
            return false;
        }
        SortedList<?> other = (SortedList<?>) obj;
        return Objects.equals(values, other.values);
    }
}
