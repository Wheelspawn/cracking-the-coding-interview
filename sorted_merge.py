#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:21:49 2020

@author: nsage
"""

import random
import numpy as np

def sorted_merge(a,b):
    for e in b:
        i = len(a)-1
        while (a[i] == None):
            i -= 1
        a[i+1] = e
        while (i >= 0) and (a[i] > a[i+1]):
            swap(a,i,i+1)
            i -= 1
    return a
            
def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    
def two_random_lists():
    x = sorted([random.randrange(0,50) for i in range(1,random.randrange(5,10))])
    z = [None for i in range(random.randrange(5,10))]
    y = sorted([random.randrange(0,50) for i in range(0,len(z))])
    
    return (x+z,y,sorted(x+y))

if __name__ == "__main__":
    import numpy as np
    tests = []
    for i in range(0,50000):
        x,y,z = two_random_lists()
        tests.append( ( sorted_merge(x,y), z ) )
        
    results = np.array(list(map((lambda x:x[0]==x[1]),tests)))
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")


