#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:14:58 2020

@author: nsage
"""

import numpy as np
from tree import Graph, Node, BSTNode

# first solution
'''
def find_succ(n):
    root = n
    while root.parent != None:
        root = root.parent
    
    global succ_
    succ_ = None
    
    def find_succ_aux(root):
        global succ_
        if root == None:
            return
        find_succ_aux(root.left)
        if succ_ == None:
            succ_ = root
            root.succ = succ_
        else:
            succ_.succ = root
            succ_ = root
        find_succ_aux(root.right)
    
    find_succ_aux(root)
    return n.succ
'''

# second (better) solution
def find_succ(n):
    if n == None:
        return None
    
    if n.right != None:
        leftmost = n.right
        while leftmost.left != None:
            leftmost = leftmost.left
        return leftmost
    
    if n.parent != None:
        if n == n.parent.left:
            return n.parent
        
    p = n
    while p.parent != None:
        if p == p.parent.left:
            return p.parent
        p = p.parent
        
    return None
    
    

a = BSTNode("A")
b = BSTNode("B")
c = BSTNode("C")
d = BSTNode("D")
e = BSTNode("E")
f = BSTNode("F")
g = BSTNode("G")
h = BSTNode("H")
i = BSTNode("I")
j = BSTNode("J")
k = BSTNode("K")
l = BSTNode("L")
m = BSTNode("M")
n = BSTNode("N")

a.assign((b,c))
b.assign((d,e))
c.assign((f,g))
f.assign((h,i))
g.assign((j,None))
h.assign((k,l))
l.assign((m,n))

d.e = 1
b.e = 2
e.e = 3
a.e = 4
k.e = 5
h.e = 6
m.e = 7
l.e = 8
n.e = 9
f.e = 10
i.e = 11
c.e = 12
j.e = 13
g.e = 14

tests = [ ( find_succ(d), b ),
          ( find_succ(b), e ),
          ( find_succ(e), a ),
          ( find_succ(a), k ),
          ( find_succ(k), h ),
          ( find_succ(h), m ),
          ( find_succ(m), l ),
          ( find_succ(l), n ),
          ( find_succ(n), f ),
          ( find_succ(f), i ),
          ( find_succ(i), c ),
          ( find_succ(c), j ),
          ( find_succ(j), g ),
          ( find_succ(g), None ) ]

for test in tests:
    if test[0] == test[1]:
        print("Pass")
    else:
        print("Fail")
