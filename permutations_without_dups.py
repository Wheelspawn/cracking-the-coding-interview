#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:25:41 2020

@author: nathaniellesage
"""

import itertools
import random
import string

def perms_without_dups(s):
    if len(s) <= 1:
        return set(s)
    else:
        p = []
        c = s[0]
        for perm in perms_without_dups(s[1:]):
            for i in range(len(perm)+1):
                p.append(perm[:i]+c+perm[(i):])
        return p

if __name__ == "__main__":
    import numpy as np
    tests = []
    chars = list(string.ascii_uppercase + string.ascii_lowercase)
    for i in range(0,50):
        random.shuffle(chars)
        test = ''.join(chars[0:random.randint(1,8)])
        tests.append( ( test, sorted([''.join(p) for p in itertools.permutations(test)]) ) )
    
    results = np.array([sorted(perms_without_dups(tests[i][0])) == tests[i][1] for i in range(len(tests))])
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")