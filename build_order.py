#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:01:34 2020

@author: nsage
"""

import numpy as np
from tree import Graph, Node, BSTNode

def build_order(projects,dependencies):
    
    projects = projects[:]
    dependencies = dependencies[:]
    
    d = {}
    
    for project in projects:
        d[project] = []
        
    for dependency in dependencies:
        d[dependency[1]].append(dependency[0])
        
    l_0 = []
    
    # print(projects)
    # print(dependencies)
    # print(d)
    
    for project in d:
        if d[project] == []:
            l_0.append(project)
            projects.remove(project)
    
    if l_0 == []:
        return False
    
    while projects != []:
        old_project = projects[:]
        for project in projects:
            if set( l_0 ) == set.union( set( d[project] ), set( l_0 ) ):
                # print("I")
                l_0.append(project)
                projects.remove(project)
            
            
            '''
            print(project)
            print(projects)
            print(set(d[project]))
            print(set(l_0))
            print()
            '''
            
        if old_project == projects:
            return False
        else:
            old_project = projects[:]
            
    return l_0
    
    '''
    g = Graph()
    d = {}
    
    for project in projects:
        d[project] = Node(name=project)
        g.v.append(d[project])
        
    for dependency in dependencies:
        d[dependency[0]].nodes.append(dependency[1])
    
    output = []
    
    return g
    '''
    
# solution 2
def build_order_2(v,e):
    g=Graph(v)
    
def func(self,a):
    return a+a

from types import MethodType
Node.func = MethodType(func,Node)

# solution 3
def build_order_3():
    pass

tests = [ (['a','b','c','d','e','f'],
           [('a','d'),
            ('f','b'),
            ('b','d'),
            ('f','a'),
            ('d','c')],
            True),
          (['a','b','c','d','e'],
           [('a','e'),
            ('b','e'),
            ('c','e'),
            ('d','e')],
            True),
          (['a','b','c','d','e','f','g','h','i'],
           [('a','c'),
            ('b','c'),
            ('c','d'),
            ('c','e'),
            ('e','f'),
            ('f','g'),
            ('b','g')],
            True),
          (['a','b','c','d','e','f','g'],
           [('f','c'),
            ('f','a'),
            ('f','b'),
            ('c','a'),
            ('b','a'),
            ('a','e'),
            ('b','e'),
            ('d','g')],
           True),
          (['a','b'],
           [('a','b'),
            ('b','a')],
            False),
          (['a','b','c'],
           [('a','b'),
            ('b','c'),
            ('c','a')],
            False),
          (['a','b','c','d'],
           [('a','b'),
            ('b','c'),
            ('c','a'),
            ('c','d')],
            False),
          (['a','b','c','d','e'],
           [('a','b'),
            ('a','c'),
            ('b','d'),
            ('c','d'),
            ('d','e'),
            ('e','a')],
            False),
          (['a','b','c','d','e','f','g','h'],
           [('a','c'),
            ('b','c'),
            ('c','d'),
            ('c','e'),
            ('d','f'),
            ('e','f'),
            ('f','b')],
            False),
          (['a','b','c','d','e','f','g','h'],
           [('a','c'),
            ('b','c'),
            ('c','d'),
            ('c','e'),
            ('d','f'),
            ('e','f'),
            ('f','e')],
            False)]

'''
for test in tests:
    if test[0] == test[1]:
        print("Pass")
    else:
        print("Fail")
        '''