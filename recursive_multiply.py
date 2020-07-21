#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:25:25 2020

@author: nsage
"""

def recursive_multiply(a,b,i=0):
    if a > b:
        return recursive_multiply(b,a,i)
    if (1 << i) > b:
        return 0
    if (b | (1 << i)) != b:
        return 0 + recursive_multiply(a,b,i+1)
    else:
        # print(i)
        return (a << i) + recursive_multiply(a,b,i+1)

def recursive_multiply_2(a,b):
    if a > b:
        return recursive_multiply_aux(b,a)
    else:
        return recursive_multiply_aux(a,b)

def recursive_multiply_aux(a,b):
    if a == 0:
        return 0
    if a == 1:
        return b
    if a%2 == 1:
        return b + (recursive_multiply_aux((a-1)//2,b) << 1)
    else:
        return recursive_multiply_aux(a//2,b) << 1
        

if __name__ == "__main__":
    import numpy as np
    tests = [ (recursive_multiply(i,j), i*j) for i in range(0,60) for j in range(1,60)]
    

