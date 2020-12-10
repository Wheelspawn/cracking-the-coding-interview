#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:38:26 2020

@author: nathaniellesage
"""

def hanoi(disks):
    try:
        h1(disks)
    except RecursionError:
        pass

def h1(disks):
    if len(disks[0]) == 0:
        pass
    elif len(disks[0]) == 1:
        move(disks,0,2)
    elif len(disks[0]) == 2:
        move(disks,0,1)
        move(disks,0,2)
        move(disks,1,2)
    else:
        biggest = disks[0][0]
        disks[0].remove(biggest)
        # print(disks," ",biggest)
        h1(disks)
        disks[1].append(biggest)
        # print(disks)
        h2(disks)
        disks[1].remove(biggest)
        # disks[2].append(biggest)
        # print(disks)
        h1(disks)
        disks[2].insert(0,biggest)

def h2(disks):
    if len(disks[2]) == 0:
        pass
    elif len(disks[2]) == 1:
        move(disks,2,0)
    elif len(disks[2]) == 2:
        move(disks,2,1)
        move(disks,2,0)
        move(disks,1,0)
    else:
        biggest = disks[2][0]
        disks[2].remove(biggest)
        # print(disks," ",biggest)
        h2(disks)
        disks[1].append(biggest)
        # print(disks)
        h1(disks)
        disks[1].remove(biggest)
        # disks[0].append(biggest)
        # print(disks)
        h2(disks)
        disks[0].insert(0,biggest)

# h1: moves stack from left to right
#  | | |    | | |    | | |    | | |    | | |    | | |
#  1 | |    | | |    | | |    | | |    | | |    | | 1
#  2 | |    | | 1    | | 1    1 | |    1 | |    | | 2
#  3 | | -> | | 2 -> | | 2 -> 2 | | -> 2 | | -> | | 3
#  . | |    | | 3    | | 3    3 | |    3 | |    | | .
#  m | |    | | .    | | .    . | |    . | |    | | m
#  n | |    n | m    | n m    m n |    m | n    | | n
# d[0]==n  h1(d)    d[1]==n  h2(d)    d[2]==n  h1(d)

# h2: moves stack from right to left
#  | | |    | | |    | | |    | | |    | | |    | | |
#  | | 1    | | |    | | |    | | |    | | |    1 | |
#  | | 2    1 | |    1 | |    | | 1    | | 1    2 | |
#  | | 3 -> 2 | | -> 2 | | -> | | 2 -> | | 2    3 | |
#  | | .    3 | |    3 | |    | | 3    | | 3    . | |
#  | | o    . | |    . | |    | | .    | | .    o | |
#  | | m    o | m    o m |    | m o    m | o    m | |
# d[2]==m  h2(d)    d[1]==m  h1(d)    d[0]==m  h2(d)


def move_back(disks):
    pass

def is_valid_move(disks,tower_from,tower_to):
    try:
        if disks[tower_from][-1] < disks[tower_to][-1]:
            return True
        else:
            return False
    except IndexError:
        if (tower_to >= 3) or (tower_from >= 3):
            return False
        if disks[tower_to] == []:
            return True
        else:
            return False

def move(disks,tower_from,tower_to):
    disks[tower_to].append(disks[tower_from].pop())
    # print(disks)

def get_test_disks(n):
    return [[i for i in range(n,0,-1)],[],[]], [[],[],[i for i in range(n,0,-1)]]

if __name__ == "__main__":
    import numpy as np
    tests = [ get_test_disks(n) for n in range(0,15) ]
    results = []
    for test in tests:
        hanoi(test[0])
        if test[0] == test[1]:
            results.append(True)
        else:
            results.append(False)
    results = np.array(results)
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")


