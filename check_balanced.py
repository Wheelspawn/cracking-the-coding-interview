#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:59:15 2020

@author: nsage
"""

import numpy as np
from tree import Graph, Node, BSTNode

# first method: n * log n

'''
def get_height(root):
    global op
    if root == None:
        return -1
    op += 1
    return max(get_height(root.left),get_height(root.right))+1

def is_balanced(root):
    global op
    if root == None:
        return True
    
    op += 1
    if abs( get_height(root.left) - get_height(root.right) ) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)
'''

# second method
def get_height(root):
    if root == None:
        return -1
    
    a = get_height(root.left)
    b = get_height(root.right)
    
    if (a == -np.inf):
        return -np.inf
    if (b == -np.inf):
        return -np.inf4
    
    if abs(a-b) > 1:
        return -np.inf
    else:
        return max(a,b)+1

def is_balanced(root):
    return get_height(root) != -np.inf

a = BSTNode("A")
b = BSTNode("B")
c = BSTNode("C")
d = BSTNode("D")
e = BSTNode("E")

a.left = b
a.right = c
b.left = d
b.right = e

print(is_balanced(a))
print(is_balanced(b))
print(is_balanced(d))

f = BSTNode("F")
g = BSTNode("G")

d.left = f
f.left = g

print(is_balanced(a))
print(is_balanced(b))

h = BSTNode("H")
i = BSTNode("I")
j = BSTNode("J")

c.right = h
h.right = i
i.right = j

print(is_balanced(a))
print(is_balanced(c))
print(is_balanced(h))
print(is_balanced(i))


