#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:30:33 2020

@author: nsage
"""

def conversion(a,b):
    
    bits = 0
    if b < a:
        return conversion(b,a)
    else:
        while b != 0:
            a_part = a%2
            b_part = b%2
            a //= 2
            b //= 2
            if a_part != b_part:
                bits += 1
    return bits

def conversion_2(a,b):
    
    c = a ^ b
    bits = 0
    while c != 0:
        bits += c & 1
        c //= 2
    return bits

def conversion_3(a,b):
    
    c = a ^ b
    bits = 0
    while c != 0:
        c = c & (c-1)
        bits += 1
    return bits

if __name__ == "__main__":
    
    import numpy as np
    tests = [ ( (0, 0), 0 ),
              ( (1, 1), 0 ),
              ( (2, 3), 1 ),
              ( (3, 2), 1 ), 
              ( (4, 5), 1 ),
              ( (4, 8), 2 ),
              ( (467, 19), 3),
              ( (4375, 4575), 3 ),
              ( (30, 96), 6 ),
              ( (12, 867 ), 8 ) ]
    results = np.array([conversion(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test conversion")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results = np.array([conversion_2(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test conversion_2")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results = np.array([conversion_3(tests[i][0][0],tests[i][0][1]) == tests[i][1] for i in range(len(tests))])
    print("Test conversion_3")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        