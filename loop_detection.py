#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:03:00 2020

@author: nsage
"""

from linkedlist import DoublyLinkedList, DoublyLinkedListNode

def loop_detection(head):
    node_to_check = head
    while node_to_check.nextnode != None:
        node_to_check.visited = True
        if node_to_check.nextnode.visited == True:
            return node_to_check.nextnode
        node_to_check = node_to_check.nextnode
    return None

def loop_detection_2(head):
    fastrunner = head
    slowrunner = head
    
    while fastrunner != None and slowrunner != None:
        slowrunner = slowrunner.nextnode
        fastrunner = fastrunner.nextnode.nextnode
        
        if slowrunner is fastrunner:
            break
    
    if fastrunner == None or slowrunner == None:
        return None
    
    slowrunner = head
    
    while slowrunner != fastrunner:
        slowrunner = slowrunner.nextnode
        fastrunner = fastrunner.nextnode
        
    return slowrunner
    
    
if __name__ == "__main__":
    
    a = DoublyLinkedListNode('A')
    b = DoublyLinkedListNode('B')
    c = DoublyLinkedListNode('C')
    d = DoublyLinkedListNode('D')
    e = DoublyLinkedListNode('E')
    f = DoublyLinkedListNode('F')
    
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    e.nextnode = b
    
    g = DoublyLinkedListNode('G')
    h = DoublyLinkedListNode('H')
    i = DoublyLinkedListNode('I')
    j = DoublyLinkedListNode('J')
    
    g.nextnode = h
    h.nextnode = i
    i.nextnode = j
    
    import numpy as np
    tests = [ ( a, b ),
              ( b, b ),
              ( g, None ),
              ( h, None ),
              ( j, None ) ]
    results = []
    for i in range(len(tests)):
        results.append(bool(loop_detection(tests[i][0]) == tests[i][1] for i in range(len(tests))))
        tests[i][0].reset()
    print("Test loop_detection")
    if np.array(results).all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results = []
    for i in range(len(tests)):
        results.append(bool(loop_detection_2(tests[i][0]) == tests[i][1] for i in range(len(tests))))
        tests[i][0].reset()
    print("Test loop_detection_2")
    if np.array(results).all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        