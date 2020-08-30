#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:49:00 2020

@author: nsage
"""

from tree import BSTNode

def check_subtree(t1,t2):
    if (t1 == None) or (t2 == None):
        return False
    else:
        return (are_trees_identical(t1,t2) or check_subtree(t1.left,t2) or check_subtree(t1.right,t2))

def are_trees_identical(t1,t2):
    if (t1 == None and t2 != None) or (t1 != None and t2 == None):
        return False
    if t1.e != t2.e:
        return False
    if t1.right == None and t1.left == None and t2.left == None and t2.right == None:
        return True
    else:
        return (are_trees_identical(t1.left,t2.left) and are_trees_identical(t1.right,t2.right))

if __name__ == "__main__":
    
    a = BSTNode(e=4)
    b = BSTNode(e=2)
    c = BSTNode(e=5)
    d = BSTNode(e=1)
    e = BSTNode(e=3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    
    f = BSTNode(e=2)
    g = BSTNode(e=1)
    h = BSTNode(e=3)
    f.left = g
    f.right = h
    
    import numpy as np
    tests = [ ( (a, a), True ),
              ( (b, f), True ), 
              ( (f, b), True ),
              ( (a, b), False ),
              ( (b, a), False ),
              ( (d, c), False ) ]
    results = np.array([are_trees_identical(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test are_trees_identical")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
        
    tests = [ ( (a, a), True ),
              ( (a, f), True ),
              ( (a, b), True ), 
              ( (b, f), True ),
              ( (f, a), False ),
              ( (b, a), False ) ]
    results = np.array([check_subtree(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test check_subtree")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
    
    
    