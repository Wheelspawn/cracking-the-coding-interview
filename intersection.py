#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:12:58 2020

@author: nsage
"""

from linkedlist import DoublyLinkedList, DoublyLinkedListNode

def intersection(a,b):
    a_next = a
    while a_next != None:
        b_next = b
        while b_next != None:
            if a_next is b_next:
                return a_next
            b_next = b_next.nextnode
        a_next = a_next.nextnode
    return None

def intersection_2(a,b):
    
    len_a = get_length(a)
    len_b = get_length(b)
    
    if len_b > len_a:
        return intersection_2(b,a)
    
    if get_tail(a) != get_tail(b):
        return None
    
    a_node = a
    b_node = b
    
    for i in range(len_a-len_b):
        a_node = a_node.nextnode
        
    while (a_node != None) and (b_node != None):
        
        if a_node is b_node:
            return a_node
        
        a_node = a_node.nextnode
        b_node = b_node.nextnode

def get_length(l):
    node = l
    count = 1
    while node.nextnode != None:
        node = node.nextnode
        count += 1
    return count
    
def get_tail(l):
    node = l
    while node.nextnode != None:
        node = node.nextnode
    return node

if __name__ == "__main__":
    
    a = DoublyLinkedListNode('A')
    b = DoublyLinkedListNode('B')
    c = DoublyLinkedListNode('C')
    d = DoublyLinkedListNode('D')
    e = DoublyLinkedListNode('E')
    f = DoublyLinkedListNode('F')
    
    a.nextnode = b
    b.nextnode = e
    c.nextnode = d
    d.nextnode = e
    e.nextnode = f
    
    g = DoublyLinkedListNode('G')
    h = DoublyLinkedListNode('H')
    i = DoublyLinkedListNode('I')
    j = DoublyLinkedListNode('J')
    k = DoublyLinkedListNode('K')
    
    g.nextnode = h
    i.nextnode = j
    j.nextnode = k
    
    l = DoublyLinkedListNode('L')
    m = DoublyLinkedListNode('M')
    n = DoublyLinkedListNode('N')
    
    l.nextnode = m
    m.nextnode = n
    
    import numpy as np
    tests = [ ( ( a, c ), e ),
              ( ( c, a ), e ),
              ( ( g, i ), None ),
              ( ( l, a ), None ) ]
    results = np.array([intersection(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test intersection")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")

    results = np.array([intersection_2(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test intersection_2")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")