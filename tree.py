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

class Graph(object):
    def __init__(self,v=[],e=[]):
        self.v = v[:]
        self.d = {}
        self.State = Enum('State', 'visiting visited unvisited')
        for vert in v:
            vert_obj = Node(name=vert)
            vert_obj.state = self.State.unvisited
            self.d[vert_obj.name] = vert_obj
        for parent, child in e:
            self.d[parent].add_child(self.d[child])
            
    def get(self,ve_name):
        return self.d[ve_name]
        
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
    def __init__(self,name="",e=None,nodes=[],pred=None,parent=None,marked=False):
        self.name=name
        self.e=e
        self.nodes = nodes[:]
        self.pred = pred
        self.parent = parent
        self.marked = marked
        
    def __repr__(self):
        return str(self.name)
    
    def add_children(self,cs):
        for c in cs:
            self.add_child(c)
    
    def add_child(self,c):
        self.nodes.append(c)
        c.parent = self

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
    
    def size(self):
        if (self.left != None) and (self.right != None):
            return 1 + self.left.size() + self.right.size()
        elif (self.left == None) and (self.right != None):
            return 1 + self.right.size()
        elif (self.left != None) and (self.right == None):
            return 1 + self.left.size()
        else:
            return 1
        
    def assign(self,l):
        self.left = l[0]
        self.right = l[1]
        if l[0] != None:
            l[0].parent = self
        if l[1] != None:
            l[1].parent = self
    
    def print_all(self):
        if self.left != None:
            self.left.print_all()
        print(self.name, end=" ")
        if self.right != None:
            self.right.print_all()
            
    def __repr__(self):
        return str(self.e)
