#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:46:30 2020

@author: nsage
"""

def triple_step(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
    
def triple_step_memo(n):
    if (n == 0) or (n == 1):
        return 1
    if (n == 2):
        return 2
    
    memo = [0 for i in range(0,n+1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
    return memo[-1]

def count_ways(n):
    memo = [-1 for i in range(0,n+1)]
    return count_ways_aux(n,memo)

def count_ways_aux(n,memo):
    if (n < 0):
        return 0
    elif (n == 0):
        return 1
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = count_ways_aux(n-1,memo) + count_ways_aux(n-2,memo) + count_ways_aux(n-3,memo)
    return memo[n]

import time
a = time.time()
for i in range(0,1000):
    triple_step_memo(i)
b = time.time()
print(b-a)

a = time.time()
for i in range(0,1000):
    count_ways(i)
b = time.time()
print(b-a)