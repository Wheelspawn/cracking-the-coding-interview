#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:43:11 2020

@author: nsage
"""

def add_without_plus(a,b):
    if a > b:
        return add_without_plus_aux(a,b)
    else:
        return add_without_plus_aux(b,a)

def add_without_plus_aux(a,b):
    
    if (a == 0) and (b == 0):
        return 0
    
    l = []
    n = 1
    final = 0
    carry = 0
    carry_bit = None
    
    while (a != 0) or (b != 0):
        if (a%2==1) and (b%2==1):
            if carry == 0:
                carry = 1
                carry_bit = (n << 1)
            elif carry == 1:
                final = final | carry_bit
                carry_bit = (n << 1)
        elif (a%2==0) and (b%2==0):
            if carry == 0:
                pass
            elif carry == 1:
                final = final | carry_bit
                carry = 0
        else: # ( ( a%2==1 ) and ( b%2==0 ) ) or ( ( a%2==0 ) and ( b%2==1 ) )
            if carry == 0:
                final = final | n
                carry_bit = 0
            elif carry == 1:
                carry_bit = (n << 1)
        
        a //= 2
        b //= 2
        n = n << 1
    
    final = final | carry_bit
    
    return final

def add_without_plus_2(a,b):
    if (b == 0):
        return a
    s = a ^ b
    c = (a & b) << 1
    print(a,"  ",b,"  ",s,"  ",c)
    return add_without_plus_2(s,c)

def add_without_plus_3(a,b):
    while b != 0:
        s = a ^ b
        c = (a & b) << 1        
        print(a,"  ",b,"  ",s,"  ",c)
        a = s
        b = c
        
    return a

if __name__ == "__main__":
    import numpy as np
    tests = [ (add_without_plus_3(i,j), i+j) for i in range(0,10) for j in range(1,10)]
    results = np.array(list(map((lambda x:x[0]==x[1]),tests)))
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
