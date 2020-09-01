#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:41:03 2020

@author: nsage
"""

def coins(n):
    l = []
    coins_aux(n,l,[])
    return l

def coins_aux(n,l,way):
    if sum(way) < n:
        coins_aux(n,l,way+[25])
        coins_aux(n,l,way+[10])
        coins_aux(n,l,way+[5])
        coins_aux(n,l,way+[1])
    elif sum(way) == n:
        l.append(way)
    else:
        pass
    
if __name__ == "__main__":
    # do something
    coins_0  = [[]]
    coins_1  = [[1]]
    coins_5  = [[5],[1,1,1,1,1]]
    coins_6  = [[5,1],[1,5],[1,1,1,1,1,1]]
    coins_7  = [[5,1,1],[1,5,1],[1,1,5],[1,1,1,1,1,1,1]]
    coins_10 = [[10],
                [5, 5],
                [5, 1, 1, 1, 1, 1],
                [1, 5, 1, 1, 1, 1],
                [1, 1, 5, 1, 1, 1],
                [1, 1, 1, 5, 1, 1],
                [1, 1, 1, 1, 5, 1],
                [1, 1, 1, 1, 1, 5],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    coins_11 = [[10, 1],
                [5, 5, 1],
                [5, 1, 5],
                [5, 1, 1, 1, 1, 1, 1],
                [1, 10],
                [1, 5, 5],
                [1, 5, 1, 1, 1, 1, 1],
                [1, 1, 5, 1, 1, 1, 1],
                [1, 1, 1, 5, 1, 1, 1],
                [1, 1, 1, 1, 5, 1, 1],
                [1, 1, 1, 1, 1, 5, 1],
                [1, 1, 1, 1, 1, 1, 5],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    coins_true = [coins_0,coins_1,coins_5,coins_6,coins_7,coins_10,coins_11]
    coins_test = [coins(0),coins(1),coins(5),coins(6),coins(7),coins(10),coins(11)]
    
    passes = []
    for i in range(0,6):
        for e in coins_test[i]:
            if e in coins_true[i]:
                passes.append(True)
            else:
                passes.append(False)
    
    if False in passes:
        print("All tests did not pass")
    else:
        print("All tests passed")
        