#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:26:24 2020

@author: nsage
"""

def fibonacci(n):
    return fibonacci_aux(n,[0 for i in range(0,n+1)])

def fibonacci_aux(n,memo):
    if (n == 0) or (n == 1):
        return n
    
    if memo[n] == 0:
        memo[n] = fibonacci_aux(n-1,memo) + fibonacci_aux(n-2,memo)
        
    return memo[n]

def fibonacci_2(n):
    if (n == 0):
        return 0
    
    memo = [0 for i in range(0,n+1)]
    memo[1] = 1
    
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]

def fibonacci_3(n):   
    if (n == 0):
        return 0
    
    a = 0
    b = 1
    
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        
    return a+b