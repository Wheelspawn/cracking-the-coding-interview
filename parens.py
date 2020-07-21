#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:08:49 2020

@author: nsage
"""

def parens(n):
    s = parens_aux([],n,n)
    s_valid = []
    for e in s:
        if check_valid(e[:]):
            s_valid.append(''.join(e))
    return s_valid

def parens_aux(s,l,r):
    s = s[:]
    if s == []:
        return parens_aux([['(']],l-1,r) + parens_aux([[')']],l,r-1)
    if (l == 0) and (r == 0):
        return s[:]
    else:
        if (l > 0) and (r > 0):
            return parens_aux([s[-1][:]+['(']], l-1, r) + parens_aux([s[-1][:]+[')']], l, r-1)
        else:
            if (l > 0):
                return parens_aux([s[-1][:]+['(']], l-1, r)
            if (r > 0):
                return parens_aux([s[-1][:]+[')']], l, r-1)
    return s[:]

def check_valid(s):
    if s == ['']:
        return False
    parens_stack = [s.pop(0)]
    while len(s) > 0:
        e = s.pop(0)
        if e == '(':
            parens_stack.append(e)
        else:
            if len(parens_stack) > 0:
                parens_stack.pop(-1)
            else:
                return False
    if parens_stack == []:
        return True
    else:
        return False


if __name__ == "__main__":
    import numpy as np
    tests = [ ([''], False),
              ([')'], False),
              (['('], False),
              ([')'], False),
              ([')','('], False),
              (['(',')','('], False),
              ([')','(',')'], False),
              (['(','(',')',')',')'], False),
              (['(',')'], True),
              (['(',')','(',')'], True),
              (['(','(',')',')'], True),
              (['(','(',')','(',')',')'], True),
              (['(','(',')',')','(',')'], True),
              (['(','(',')','(',')',')','(',')'], True),
              (['(','(',')','(','(',')',')',')'], True),
              (['(','(','(','(',')','(',')',')',')',')'], True)]
    results = np.array(list(map((lambda x:check_valid(x[0])==x[1]),tests)))
    if results.all() == True:
        print("All check_valid tests passed")
    else:
        print("All check_valid tests did not pass")
        
    tests = [ (0, []),
              (1, ['()']),
              (2, ['(())','()()']),
              (3, ['((()))','(()())','(())()','()(())','()()()']) ]
    results = np.array(list(map((lambda x:parens(x[0])==x[1]),tests)))
    if results.all() == True:
        print("All parens tests passed")
    else:
        print("All parens tests did not pass")


