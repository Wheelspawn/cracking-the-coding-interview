
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:05:26 2020

@author: nathaniellesage
"""

import numpy as np


def eight_queens():
    
    boards = []
    eight_queens_aux(boards,np.zeros((8,8)),0)
    
    for board in boards:
        
        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] == 1:
                    board[m][n] = 0
                    
        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] == 2:
                    board[m][n] = 1
        
    return boards

def eight_queens_aux(boards,board,row):
    
    if row >= 8:
        boards.append(board)
        return
    
    for col in range(0,8):
            if board[row][col] != 1:
                new_board = np.copy(board)
                new_board[row][col] = 2
                place_queen(new_board,row,col)
                eight_queens_aux(boards,new_board,row+1)
            
    return boards

def place_queen(arr,row,col):
    for i in range(8):
        
        arr[i][col] = 1
        arr[row][i] = 1
        
    for j in range(8):
        
        if ((j+(row)+(-col)) >= 0) and ((j+(row)+(-col)) < 8):
            arr[j+(row)+(-col)][j] = 1
            
        if ((row+col)-j >= 0) and ((row+col)-j < 8):
            arr[(row+col)-j][j] = 1
    
    arr[row][col] = 2

