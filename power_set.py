#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:12:45 2020

@author: nsage
"""

global s
s = []

def power_set(l):
    subsets = []
    for i in range(0,2**len(l)):
        subset = []
        k = i
        pos = len(l)-1
        while k != 0:
            if k%2 == 1:
                subset.append(l[pos])
            k = k//2
            pos -= 1
        subsets.append(set(subset))
    return subsets

def power_set_2(n):
    if n == 0:
        return [ set([]) ]
    else:
        return power_set_2(n-1) + add_num(power_set_2(n-1),n)
    
def add_num(l,n):
    m = []
    for s in l:
        g = s.copy()
        g.add(n)
        m.append(g)
    return m

def power_set_3(n):
    max_ = 1 << len(n)
    subsets = []
    for i in range(0,max_):
        subsets.append(convert_int_to_set(i,n))
    return subsets

def convert_int_to_set(x, s):
    i = 0
    k = x
    l = []
    while k > 0:
        if k%2 == 1:
            l.append(s[i])
        i += 1
        k //= 2
    return l

tests = [ ( set([1]),
           [set([]),set([1])] ),
          ( set([1,2]),
           [set([]),set([1]),set([2]),set([1,2])] ),
          ( set([1,2,3]),
           [set([]),set([1]),set([2]),set([3]),set([1,2]),set([1,3]),set([2,3]),set([1,2,3]) ] ) ]


