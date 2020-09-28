#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:13:21 2020

@author: nsage
"""

class DoublyLinkedList(object):
    def __init__(self,l):
        self.l = l
        self.build(l)
        
    def build(self,l):
        self.head = DoublyLinkedListNode(l[0])
        iter_node = self.head
        for i in range(1,len(l)):
            iter_node.nextnode = DoublyLinkedListNode(l[i])
            iter_node.nextnode.prevnode = iter_node
            iter_node = iter_node.nextnode
    
    def __repr__(self):
        return str(self.l)
    
class DoublyLinkedListNode(object):
    def __init__(self,e,prevnode=None,nextnode=None,visited=False):
        self.e = e
        self.prevnode = prevnode
        self.nextnode = nextnode
        self.visited = visited
        
    def reset(self):
        self.visited = False
        if (self.nextnode != None) and (self.nextnode.visited==True):
            self.nextnode.reset()
    
    def __repr__(self):
        return str(self.e)

class Result(object):
    def __init__(self,node,result):
        self.node = node
        self.result=result