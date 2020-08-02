#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:44:16 2020

@author: nsage
"""

from tree import Node

def first_common_ancestor(x,y):
    if x == y:
        return x
    if x.parent == None:
        return x
    if y.parent == None:
        return y

    x_ancestor = x
    while x_ancestor != None:
        x_ancestor.marked = True
        x_ancestor = x_ancestor.parent
    y_ancestor = y
    while y_ancestor != None:
        if y_ancestor.marked == True:
            return y_ancestor
        y_ancestor = y_ancestor.parent
    return None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
j = Node('J')
k = Node('K')
l = Node('L')
m = Node('M')
n = Node('N')
o = Node('O')

a.add_children([b,c,d])
b.add_children([e,f])
d.add_children([g])
f.add_children([h,i,j,k])
h.add_children([m,n])
i.add_children([o])
g.add_children([l])

if __name__ == "__main__":
    import numpy as np
    tests = [ ( (b, c), a ),
              ( (b, d), a ), 
              ( (e, c), a ),
              ( (e, k), b ),
              ( (e, m), b ),
              ( (m, l), a ),
              ( (n, d), a ),
              ( (m, k), f ),
              ( (h, j), f) ]
    results = np.array([first_common_ancestor(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")




