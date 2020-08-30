#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:12:23 2020

@author: nsage
"""

from tree import BSTNode

def paths_with_sum(root,n):
    pass

def compute_paths(node,root,d,n):
    
    if node.parent != None:
        if node.parent.parent != None:
            d[(root.e,node.e)] = node.e + d[(root.e,node.parent.e)]
        else:
            d[(root.e,node.e)] = node.e + node.parent.e
    
    if (node.left == None) and (node.right == None):
        pass
    if node.left != None:
        compute_paths(node.left,root,d,n)
    if node.right != None:
        compute_paths(node.right,root,d,n)

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
    compute_paths(a,a,d,0)
    for thing in d:
        print(thing, d[thing])
    