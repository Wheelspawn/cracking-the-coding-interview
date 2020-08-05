#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:20:55 2020

@author: nsage
"""

def paint_fill(m,p,c):
    
    orig = m[p[0]][p[1]]
    m[p[0]][p[1]] = c
    
    if (p[0] > 0) and (m[p[0]-1][p[1]] == orig):
        paint_fill(m,(p[0]-1,p[1]),c)
    if (p[0] < len(m)-1) and (m[p[0]+1][p[1]] == orig):
        paint_fill(m,(p[0]+1,p[1]),c)
    if (p[1] > 0) and (m[p[0]][p[1]-1] == orig):
        paint_fill(m,(p[0],p[1]-1),c)
    if (p[1] < len(m)-1) and (m[p[0]][p[1]+1] == orig):
        paint_fill(m,(p[0],p[1]+1),c)
    
    
if __name__ == "__main__":
    import numpy as np
    
    m_0 = [ [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1], 
            [1,1,1,1,1] ]
    
    t_0 = [ [1,1,1,1,1],
            [1,2,2,2,1],
            [1,2,1,2,1],
            [1,2,2,2,1], 
            [1,1,1,1,1] ]
    
    m_1 = [ [1,3,1,3,1,3],
            [1,3,3,3,1,4],
            [3,3,1,2,1,4],
            [1,3,3,3,3,3], 
            [3,1,1,1,0,0] ]
    
    t_1 = [ [1,9,1,9,1,3],
            [1,9,9,9,1,4],
            [9,9,1,2,1,4],
            [1,9,9,9,9,9], 
            [3,1,1,1,0,0] ]
    
    m_2 = [ [1,1],
            [1,1] ]
    
    t_2 = [ [5,5],
            [5,5] ]
    
    m_3 = [ [1,2,3],
            [4,5,6],
            [7,8,9] ]
    
    t_3 = [ [1,2,3],
            [4,5,6],
            [7,8,1] ]
    
    paint_fill(m_0,(1,1),2)
    paint_fill(m_1,(3,5),9)
    paint_fill(m_2,(0,1),5)
    paint_fill(m_3,(2,2),1)
    
    tests = [ (m_0,t_0),
              (m_1,t_1),
              (m_2,t_2),
              (m_3,t_3) ]
        
    results = np.array(list(map((lambda x:x[0]==x[1]),tests)))
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
