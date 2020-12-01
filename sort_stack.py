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

def sort_stack_2(s):
    s1 = s[:]
    s2 = []
    s2.append(s1.pop())
    
    while s1 != []:
        if s1[-1] <= s2[-1]:
            s2.append(s1.pop())
        else:
            a = s1.pop()
            b = s2.pop()
            
            if (s2 != []) and (a <= s2[-1]):
                s1.append(b)
                s2.append(a)
            else:
                s1.append(b)
                while (s2 != []) and (a > s2[-1]):
                    s1.append(s2.pop())
                s2.append(a)
    return s2
        
if __name__ == "__main__":
    
    tests = []
    for i in range(0,100):
        x = list(np.random.randint(-100,100,np.random.randint(1,50,1)))
        tests.append((x,list(reversed(sorted(x)))))
    
    results = np.array([sort_stack(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test sort_stack")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")

    results = np.array([sort_stack_2(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test sort_stack_2")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")