#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:48:57 2020

@author: nsage
"""

import numpy as np

def sort_stack(s):
    
    bottom = 0
    top = len(s)
    s1 = s[:]
    s2 = []
    
    for i in range(bottom,top):
        flag = False
        max_ = -np.inf
        for j in range(i,top):
            c = s1.pop()
            if c > max_:
                max_ = c
            s2.append(c)
        s1.append(max_)
        while s2 != []:
            c = s2.pop()
            if c == max_:
                if flag == False:
                    flag = True
                else:
                    s1.append(c)
            else:
                s1.append(c)
    return s1

if __name__ == "__main__":
    
    tests = []
    for i in range(0,1000):
        x = list(np.random.randint(-100,100,np.random.randint(1,50,1)))
        tests.append((x,list(reversed(sorted(x)))))
    
    results = np.array([sort_stack(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test conversion")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
