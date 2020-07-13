#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:40:35 2020

@author: nsage
"""

import numpy as np
from tree import Graph, Node, BSTNode

def validate_bst(root,min_=-np.inf,max_=np.inf):
    if root == None:
        return True
    
    if root.e < min_:
        return False
    if root.e > max_:
        return False
    
    return validate_bst(root.left,min_,root.e) and validate_bst(root.right,root.e,max_)
    
    

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
o = BSTNode("O")

a.left = b
a.right = c

b.left = d
b.right = e

e.left = h
e.right = i

i.left = k
i.right = l

k.left = n
k.right = o

c.left = f
c.right = g

f.right = j
j.right = m

d.e = 1
b.e = 2
h.e = 3
e.e = 4
n.e = 5
k.e = 6
o.e = 7
i.e = 8
l.e = 9
a.e = 10
f.e = 11
j.e = 12
m.e = 13
c.e = 14
g.e = 15

print(validate_bst(a))
print(validate_bst(b))
print(validate_bst(c))
print(validate_bst(e))
print(validate_bst(i))
print(validate_bst(f))
print(validate_bst(j))
print(validate_bst(m))
print()

e.e = 17
f.e = 13
print(validate_bst(a))
print(validate_bst(b))
print(validate_bst(c))

e.e = 4
f.e = 11
n.e = -1
print(validate_bst(a))

e.e = 5
g.e = 9
print(validate_bst(a))

g.e = 15
o.e = 12
print(validate_bst(a))