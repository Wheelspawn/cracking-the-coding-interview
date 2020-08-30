#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:32:40 2020

@author: nsage
"""

from tree import BSTNode

def bst_sequences(root):
    return bst_sequences_aux(root)

def bst_sequences_aux(root):
    if root.left != None and root.right != None:
        left = bst_sequences_aux(root.left)
        right = bst_sequences_aux(root.right)
        
        l_all = []
        
        for l in left:
            for r in right:
                for i in insert_all(l[:],r[:]):
                    l_all.append([root]+i)
        return l_all
        
    elif root.left != None and root.right == None:
        left = bst_sequences_aux(root.left)
        
        l_all = []
        
        for l in left:
            l_all.append([root]+l)
        return l_all
        
    elif root.left == None and root.right != None:
        right = bst_sequences_aux(root.right)
        
        l_all = []
        
        for r in right:
            l_all.append([root]+r)
        return l_all
    
    else:
        return [[root]]
    
def insert_all(a,b):
    '''
    insert_all([1,2],[3,4]) should return
    [3,4,1,2],
    [3,1,4,2],
    [3,1,2,4],
    [1,3,4,2],
    [1,3,2,4],
    [1,2,3,4]
    
    insert_all([1],[3,4,5]) should return
    [3,4,5,1],
    [3,4,1,5],
    [3,1,4,5],
    [1,3,4,5]
    
    '''
    l_0 = []
    l_1 = []
    pos = 1
    while b != []:
        if l_0 == []:
            e = b.pop(0)
            l_0 = insert_all_aux(a,e)
        
        if b == []:
            return l_0
        
        e = b.pop(0)
        inc = pos
        for c in l_0:
            for d in insert_all_aux(c[inc:],e):
                l_1.append(c[:inc] + d)
                
            inc += 1
        pos += 1
        inc = pos
                
        l_0 = l_1
        l_1 = []
        
    return l_0
    
def insert_all_aux(a,e):
    l = []
    for i in range(len(a)+1):
        new_a = a[:]
        new_a.insert(i,e)
        l.append(new_a)
    return l

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
    
    for e in bst_sequences(a):
        print(e)
    