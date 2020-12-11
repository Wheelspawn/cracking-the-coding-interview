#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:37:43 2020

@author: nathaniellesage
"""

import itertools
import random
import string

def perms_with_dups(s):
    d = {}
    return perms_with_dups_aux(s,d)

def perms_with_dups_aux(s,d):
    # first solution: generate every permutation, hash table checks for duplicates
    if len(s) <= 1:
        return set(s)
    else:
        p = []
        c = s[0]
        for perm in perms_with_dups_aux(s[1:],d):
            for i in range(len(perm)+1):
                if perm[:i]+c+perm[(i):] not in d:
                    d[perm[:i]+c+perm[(i):]] = True
                    p.append(perm[:i]+c+perm[(i):])
        return p

def perms_with_dups_2(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return perms_with_dups_aux_2(d)

def perms_with_dups_aux_2(d):
    # second solution: add char counts to a hash table and process dynamically
    if sum(d.values()) == 0:
        return ['']
    else:
        p = []
        for c in d:
            d_c = d.copy()
            if d_c[c] > 0:
                d_c[c] -= 1
                # print(c)
                for perm in perms_with_dups_aux_2(d_c):
                    # print(perm)
                    p.append(c+perm)
        return p

if __name__ == "__main__":
    import numpy as np
    tests = []
    chars = list(string.ascii_uppercase + string.ascii_lowercase)
    for i in range(0,50):
        test=''
        for j in range(random.randint(1,8)):
            test = test + random.choice(chars)
        tests.append((test, sorted(set(([''.join(p) for p in itertools.permutations(test)])))))
    
    results = np.array([sorted(perms_with_dups(tests[i][0])) == tests[i][1] for i in range(len(tests))])
    if results.all() == True:
        print("1: All tests passed")
    else:
        print("1: All tests did not pass")

    results = np.array([sorted(perms_with_dups_2(tests[i][0])) == tests[i][1] for i in range(len(tests))])
    if results.all() == True:
        print("2: All tests passed")
    else:
        print("2: All tests did not pass")