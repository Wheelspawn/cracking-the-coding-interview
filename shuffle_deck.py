#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:15:47 2020

@author: nsage
"""

import random
import numpy as np

def shuffle_deck(l):
    for i in range(len(l)):
        j = random.randint(0,len(l)-1)
        p = l[i]
        l[i] = l[j]
        l[j] = p
        
a = [1,2,3,4,5,6,7,8,9,10]
r = []
for i in range(200000):
    shuffle_deck(a)
    r.append(a[:])

# all should be ~5.5
print(list(np.mean(r,0)))


