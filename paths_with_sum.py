#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:12:23 2020

@author: nsage
"""

from tree import BSTNode

def paths_with_sum(root,d,n):
    l = []
    for e in d:
        if d[e] == n:
            m = [e[1]]
            parent = m[0].parent
            while (parent != e[0].parent):
                m.append(parent)
                parent = parent.parent
            l.append(list(reversed(m)))
    return l

def compute_path_sums(node,d):
    
    if node.parent != None:
        d[(node.parent,node)] = node.e + node.parent.e
        
        if node.parent.parent != None:
            path_dist = d[(node.parent,node)]
            
            parent = node.parent
            while parent.parent != None:
                path_dist += d[(parent.parent,parent)] - parent.e
                d[(parent.parent,node)] = path_dist
                parent = parent.parent
            
    if node.left != None:
        compute_path_sums(node.left,d)
    if node.right != None:
        compute_path_sums(node.right,d)

if __name__ == "__main__":
    
    a = BSTNode(e=4)
    a.insert(2)
    a.insert(5)
    a.insert(-1)
    a.insert(3)
    a.insert(-5)
    a.insert(-3)
    a.insert(7)
    a.insert(10)
    
    d={}
    compute_path_sums(a,d)
    for thing in d:
        print(thing, d[thing])
    
    