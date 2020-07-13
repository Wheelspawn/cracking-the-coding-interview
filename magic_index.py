#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:10:04 2020

@author: nsage
"""

def magic_index(l):
    return magic_index_indistinct(l,0,len(l)-1)

def magic_index_aux(l,lo,hi):
    mid = (hi+lo)//2
    if l[mid] == mid:
        return mid
    else:
        if hi<lo:
            return None
        if l[mid] > mid:
            return magic_index_aux(l,lo,mid-1)
        else:
            return magic_index_aux(l,mid+1,hi)

def magic_index_indistinct(l,lo,hi):
    mid = (hi+lo)//2
    mid_val = l[mid]
    if mid_val == mid:
        return mid
    else:
        if hi<lo:
            return None
        if mid_val > mid:
            return magic_index_aux(l,lo,min(mid-1,mid_val))
        else:
            return magic_index_aux(l,max(mid+1,mid_val),hi)


