#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:17:25 2020

@author: nsage
"""

from linkedlist import DoublyLinkedList, DoublyLinkedListNode, Result


def palindrome(l_1):
    # assumption: singly or doubly linked list
    
    if l_1 == []:
        return None
    
    l_2 = []
    it_1 = iter(l_1)
    size = 0
    
    while True:
        try:
            head = next(it_1)
            l_2.insert(0,head)
            size += 1
        except StopIteration:
            break
    
    it_1 = iter(l_1)
    it_2 = iter(l_2)
    
    for i in range(size//2):
        head_1 = next(it_1)
        head_2 = next(it_2)
        if head_1 != head_2:
            return False
        
    return True
        
def palindrome_2(dll):
    stack = []
    
    slowrunner = dll.head
    fastrunner = dll.head
    
    while (fastrunner != None and fastrunner.nextnode != None):
            stack.append(slowrunner.e)
            slowrunner = slowrunner.nextnode
            fastrunner = fastrunner.nextnode.nextnode
            
    if fastrunner != None:
        slowrunner = slowrunner.nextnode
            
    while stack != []:
        p = stack.pop()
        if p != slowrunner.e:
            return False
        slowrunner = slowrunner.nextnode
    return True

def palindrome_3(dll):
    length = len(dll.l)
    return palindrome_3_recurse(dll.head,length).result

def palindrome_3_recurse(head,length):
    if length == 0:
        return Result(head,True)
    if length == 1:
        return Result(head.nextnode,True)
    
    res = palindrome_3_recurse(head.nextnode,length-2)
    
    if (not res.result) or (res.node == None):
        return res
    
    res.result = (head.e == res.node.e)
    res.node = res.node.nextnode
    
    return res
    

if __name__ == "__main__":
    
    import numpy as np
    tests = [ ([1,2,1], True),
              (["A","B","B","A"], True),
              ([5,6,5,1,2,2,3,2,2,1,5,6,5], True),
              ([0,0], True),
              ([1,6,5,3,2], False),
              ([1,3,5,7,6,4,7,5,3,1], False),
              (["A","A","A","B"], False),
              ([0,1], False) ]
    results = np.array([palindrome(tests[i][0]) == tests[i][1] for i in range(len(tests))])
    print("Test palindrome")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results = np.array([palindrome_2(DoublyLinkedList(tests[i][0])) == tests[i][1] for i in range(len(tests))])
    print("Test palindrome_2")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")
        
    results = np.array([palindrome_3(DoublyLinkedList(tests[i][0])) == tests[i][1] for i in range(len(tests))])
    print("Test palindrome_3")
    if results.all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")