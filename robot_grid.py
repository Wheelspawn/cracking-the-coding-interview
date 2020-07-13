#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:56:58 2020

@author: nsage
"""

from tree import BSTNode

def robot_grid(mat):
    tree=BSTNode()
    global end
    end=tree

    def robot_grid_aux(tree,m,n,aux):
        global end
        tree.e = (m,n)
        # end = tree
        # end.e = (m,n)
        # print(tree.e)
        
        if (m == len(aux)-1) and (n == len(aux[0])-1):
            print(m,n)
            for a in aux:
                print(a)
            end = tree
            return # return tree
        
        if (aux[m][n] != 0):
            pass
        
        if (m+1 < len(aux)) and (aux[m+1][n] == 0):
            tree.left = BSTNode()
            tree.left.parent = tree
            aux[m][n] = -1
            robot_grid_aux(tree.left,m+1,n,aux)
            # aux[m][n] = -1
        
        if (n+1 < len(aux[0])) and (aux[m][n+1] == 0):
            tree.right = BSTNode()
            tree.right.parent = tree
            aux[m][n] = -1
            robot_grid_aux(tree.right,m,n+1,aux)
            # aux[m][n] = -1
     
    # return tree
            
    robot_grid_aux(tree,0,0,mat)
    path = [end]
    p = end.parent
    while p != None:
        path.append(p)
        p = p.parent
        
    return path[::-1]

# second method
def robot_grid_2(maze):
    if (maze == None) or (len(maze)) == 0:
        return None
    path = []
    failed_points = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    if get_path(maze, len(maze)-1, len(maze[0])-1, path, failed_points):
        return path
    return None

def get_path(maze, m, n, path, failed_points):
    if (m < 0) or (n < 0) or (maze[m][n] == 1):
        return False
    if failed_points[m][n] == True:
        return False
    
    is_at_origin = (m == 0) and (n == 0)
    
    if (is_at_origin or (get_path(maze,m,n-1,path,failed_points))
        or (get_path(maze,m-1,n,path,failed_points))):
        path.append((m,n))
        print((m,n))
        return True
    
    failed_points[m][n] == False
    return False
    

grid_0 = [ [ 0,0,0 ],
           [ 0,1,0 ],
           [ 0,0,0 ] ]

grid_1 = [ [ 0,0,0,0,0 ],
           [ 0,0,1,1,0 ],
           [ 0,1,0,0,0 ],
           [ 0,1,0,0,0 ],
           [ 0,0,0,0,0 ] ]

grid_2 = [ [ 0,0,0,1,0,0 ],
           [ 1,1,0,1,0,0 ],
           [ 0,1,0,1,0,0 ],
           [ 0,0,0,0,0,0 ],
           [ 0,0,1,0,0,0 ],
           [ 0,0,0,0,1,0 ] ]

grid_3 = [ [ 0,0,0,0,0,0,0,0,0,0 ],
           [ 1,0,0,1,0,0,0,0,0,0 ],
           [ 0,1,0,1,1,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0,0,0,0 ],
           [ 0,1,1,1,1,1,1,0,1,0 ],
           [ 0,0,0,0,0,0,0,0,1,0 ],
           [ 0,0,0,0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0,1,0,0 ],
           [ 0,0,0,0,0,0,1,0,1,0 ],
           [ 0,0,0,0,0,0,0,0,0,0 ] ]
