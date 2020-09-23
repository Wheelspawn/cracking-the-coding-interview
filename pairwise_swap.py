#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:44:23 2020

@author: nsage
"""

def pairwise_swap(a):
    odd = 0   # 
    even = 0  # 
    c = 0
    while (odd < a) and (even < a):
        even += 2**c
        odd += 2**(c+1)
        c += 2
    return ((a & even) << 1) + ((a & odd) >> 1)

def pairwise_swap_2(a): # no iteration
    return ((a & 0x55555555) << 1) + ((a & 0xaaaaaaaa) >> 1)

if __name__ == "__main__":
    
    import numpy as np
    tests = [ ( 1,  2  ),
              ( 2,  1  ),
              ( 3,  3  ),
              ( 4,  8  ),
              ( 5,  10 ),
              ( 6,  9  ),
              ( 7,  11 ),
              ( 8,  4  ),
              ( 9,  6  ),
              ( 10, 5  ),
              ( 11, 7  ),
              ( 12, 12 ),
              ( 13, 14 ),
              ( 14, 13 ), 
              ( 15, 15 ),
              ( 644, 328 ),
              ( 45732, 29016 ) ]
    results = np.array([pairwise_swap(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test pairwise_swap")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results_2 = np.array([pairwise_swap_2(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test pairwise_swap_2")
    if results_2.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        