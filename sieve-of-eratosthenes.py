#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:29:41 2020

@author: nsage
"""

import math
import numpy as np
import pandas as pd
import random

from enum import Enum

def soe(n):
    nums = np.arange(2,n+1)
    flags = [1 for i in range(1,n-1)]
    
    i = 0
    j = 2
    num = nums[i]
    while i < np.sqrt(len(nums)):
        while j*num < len(nums):
            flags[j*num-1] = 0
            j += 1
        
        i += 1
        j = 2
        num = nums[i]
    
    primes = []
    return flags

def indices_to_nums(l):
    
    nums = []
    
    for i in range(len(l)):
        if l[i] == True:
            nums.append(i+1)
            
    return nums

'''
n = 10**8
primes = indices_to_nums(soe(n))
p = pd.DataFrame(data={"Primes":primes})
p.to_csv("Primes.csv")
'''

from random import randint
from time import sleep
import numpy as np

def boys_and_girls():
    girls = 0
    boys = 0
    
    for i in range(1000000):
        birth = random.randint(0,1)
        if birth != 0:
            while birth != 0:
                boys += 1
                birth = random.randint(0,1)
            girls += 1
        else:
            girls += 1
            
    print("Girls:", girls)
    print("Boys:", boys)
    return boys,girls
            
        
def divide_into_groups():
    b = np.arange(1,100)
    
    c = 10
    index = len(b)//2
    while c > 0:
        
        c -= 1
        
    
    
def make_bottles():
    bottles = [False for i in range(100)]
    bottles[randint(1,100)] = True
    return bottles


class Graph(object):
    def __init__(self,v=[]):
        self.v = v
        self.State = Enum('State', 'visiting visited unvisited')
        for ve in v:
            ve.state = self.State.unvisited
        
    def bfs(self,s):
        s.marked = True
        q = [s]
        
        while q != []:
            for ve in q:
                for c in ve.nodes:
                    if c.marked == False:
                        c.pred = ve
                        q.append(c)
                ve.marked = True
                    
            if ve.marked:
                q.remove(ve)

    def check(self):
        for ve in self.v:
            if ve.pred != None:
                print(ve.name, " : ", ve.pred.name, " : ", ve.state)
            else:
                print(ve.name, " : ", None, " : ", ve.state)
        
    def path_between_nodes(self,s,e):
        self.reset()
        
        if s == e:
            return True
        
        visiting = self.State.visiting
        visited = self.State.visited
        unvisited = self.State.unvisited
        
        queue = [s]
        s.state = unvisited
        
        iter_number = 0
        
        while queue != []:
            q = queue[0]
            queue.remove(q)
            for v in q.nodes:
                if v == e:
                    print(iter_number)
                    return True
                if v.state == unvisited:
                    v.state = visiting
                    queue.append(v)
            q.state = visited
            
            self.check()
            print()
            iter_number += 1
            
        print(iter_number)
        return False
    
    def bidirectional_path_between_nodes(self,s,e):
        self.reset()
        
        if s == e:
            return True
        
        visiting = self.State.visiting
        visited = self.State.visited
        unvisited = self.State.unvisited
        
        queue_s = [s]
        queue_e = [e]
        s.state = unvisited
        e.state = unvisited
        
        visited_s = []
        visited_e = []
        
        iter_number = 0
        
        while (queue_e != []) and (queue_s != []):
            q1 = queue_e[0]
            queue_e.remove(q1)
            for v in q1.nodes:
                if (v == e) or (e in visited_e):
                    print(iter_number)
                    return True
                if v.state == unvisited:
                    v.state = visiting
                    queue_s.append(v)
            q1.state = visited
            visited_s.append(q1)
            
            q2 = queue_s[0]
            queue_s.remove(q2)
            for v in q2.nodes:
                if (v == s) or (s in visited_s):
                    print(iter_number)
                    return True
                if v.state == unvisited:
                    v.state = visiting
                    queue_e.append(v)
            q2.state = visited
            visited_e.append(q2)
            
            self.check()
            print()
            iter_number += 1
            
        print(iter_number)
        return False
        
    def backtrack(self,a):
        track = [a]
        p = a.pred
        while p != None:
            track.append(p)
            p = p.pred
        return track
            
        
    def reset(self):
        for ve in self.v:
            ve.state = self.State.unvisited
    
        
class Node(object):
    def __init__(self,name="",e=None,nodes=[],pred=None):
        self.name=name
        self.e=e
        self.nodes = nodes
        self.pred = pred
        
    def __repr__(self):
        return str(self.name)

class BSTNode(object):
    def __init__(self,name="",e=None,left=None,right=None,parent=None,marked=False):
        self.name=name
        self.e=e
        self.left=left
        self.right=right
        self.parent = parent
        self.marked = marked
        
    def __repr__(self):
        return str(self.name)
    
    def is_binary(self):
        if self.left != None:
            if (self.left.e > self.e):
                return False
            
            if self.left.is_binary() == False:
                return False
            
        if self.right != None:
            if (self.right.e < self.e):
                return False
            
            if self.right.is_binary() == False:
                return False
        return True
    
    def print_all(self):
        if self.left != None:
            self.left.print_all()
        print(self.name, end=" ")
        if self.right != None:
            self.right.print_all()


def minimal_tree(l):
    
    if len(l) == 1:
        return BSTNode(name=l[0],e=l[0])
    
    if len(l) == 2:
        return BSTNode(name=l[1],e=l[1],left=BSTNode(name=l[0],e=l[0]))
        
    if l != sorted(l):
        return False
    
    mid = len(l)//2
    return BSTNode(name=l[mid],e=l[mid], left=minimal_tree(l[:mid]), right=minimal_tree(l[(mid+1):]))


'''
o = Node("O")
p = Node("P")
q = Node("Q")
r = Node("R")
s = Node("S")
t = Node("T")
u = Node("U")
v = Node("V")
w = Node("W")
x = Node("X")
y = Node("Y")
z = Node("Z")

o.nodes = [p]
p.nodes = [q,s]
q.nodes = [r]
r.nodes = [s,t]
s.nodes = [o,p]
t.nodes = [r,q,u]
u.nodes = [t,v]
v.nodes = [w]
w.nodes = [x,u]
x.nodes = [w,y,z]
y.nodes = []
z.nodes = [u]

g = Graph(v=[o,p,q,r,s,t,u,v,w,x,y,z])

l0 = [1,3,4]
l1 = [1,1,3]
l2 = [3, 4, 5, 5, 7]
l3 = [1, 3, 4, 6, 7]
l4 = [3, 3, 3, 5, 5, 7]
l5 = [1, 3, 4, 5, 6, 7]
l6 = list(np.arange(1,28))

lists = [l0,l1,l2,l3,l4,l5]
for l in lists:
    print_all()
    print()
 '''

def get_depths(tree):
    
    depths = {  }
    
    def get_depths_aux(tree,d=0):
        if d in depths:
            depths[d].append(tree)
        else:
            depths[d] = [tree]
            
        if tree.left != None:
            get_depths_aux(tree.left,d+1)
        if tree.right != None:
            get_depths_aux(tree.right,d+1)
    
    get_depths_aux(tree)
    
    final = []
    
    for key in depths.keys():
        final.append(depths[key])
    
    return depths

def is_balanced(bst,d=0):
    
    if bst == None:
        return True
    
    def is_balanced_aux(bst):
        if (bst == None):
            return -1
        
        # return (is_balanced_aux(bst.left),is_balanced_aux(bst.right))+1
        
        left = is_balanced_aux(bst.left)
        right = is_balanced_aux(bst.right)
        if left == False:
            return False
        if right == False:
            return False
        if left > right + 1:
            return False
        if right > left + 1:
            return False
        return True
        
        # return max(left,right)+1
    
    return is_balanced_aux(bst)
    
    '''
    # return is_balanced_aux(bst.left),is_balanced_aux(bst.right)
    if abs(is_balanced_aux(bst.left) - is_balanced_aux(bst.right)) > 1:
        return False
    else:
        return is_balanced(bst.left) and is_balanced(bst.right)
    '''
    
def get_height(bst):
    if bst == None:
        return -1
    return max(get_height(bst.left),get_height(bst.right))+1



a = BSTNode(name="A")
b = BSTNode(name="B")
c = BSTNode(name="C")
d = BSTNode(name="D")
e = BSTNode(name="E")
f = BSTNode(name="F")
g = BSTNode(name="G")
h = BSTNode(name="H")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.left = h

i = BSTNode(name="I")
j = BSTNode(name="J")
k = BSTNode(name="K")
l = BSTNode(name="L")
m = BSTNode(name="M")
n = BSTNode(name="N")
o = BSTNode(name="O")
p = BSTNode(name="P")
q = BSTNode(name="Q")

i.left = j
i.right = k
k.left = l
k.right = m
m.left = n
m.right = o
o.left = p
o.right = q

a = BSTNode(name="A")
b = BSTNode(name="B")
c = BSTNode(name="C")
d = BSTNode(name="D")
e = BSTNode(name="E")
f = BSTNode(name="F")
g = BSTNode(name="G")

a.left = b
a.right = c
b.left = d
c.right = e
d.left = f
f.left = g
