#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:05:05 2020

@author: nsage
"""

from datetime import date

class AnimalShelter(object):
    def __init__(self,d=[],c=[]):
        self.dog = d
        self.cat = c
    
    def select_oldest(self):
        if self.dog == [] or self.cat == []:
            return None
        if self.dog == [] and self.cat != []:
            return self.dequeue_cat()
        if self.dog != [] and self.cat == []:
            return self.dequeue_dog()
        if self.peek_dog().age < self.dequeue_cat().age:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()
    
    def select_species(self,species):
        if species.lower() == "dog":
            return self.dequeue_dog()
        elif species.lower() == "cat":
            return self.dequeue_cat()
        else:
            print("Animal type not recognized")
    
    def enqueue(self,animal):
        if type(animal) == Dog:
            self.dog.insert(0,animal)
        elif type(animal) == Cat:
            self.cat.insert(0,animal)
        else:
            print("Animal type not recognized")
    
    def dequeue_any(self,species):
        if species == "dog":
            return self.dequeue_dog()
        elif species == "cat":
            return self.dequeue_cat()
        else:
            print("Animal type not recognized")
    
    def dequeue_dog(self):
        if self.dog == []:
            return None
        d = self.dog[-1]
        self.dog.remove(d)
        return d
    
    def dequeue_cat(self):
        if self.cat == []:
            return None
        c = self.cat[-1]
        self.cat.remove(c)
        return c
    
    def peek_dog(self):
        if self.dog == []:
            return None
        return self.dog[-1]
    
    def peek_cat(self):
        if self.cat == []:
            return None
        return self.cat[-1]
    
        
class Animal(object):
    def __init__(self,age):
        self.age = age
        
    def __eq__(self,other):
        return (type(self) == type(other)) and (self.age == other.age)

class Dog(Animal):
    def __init__(self,age):
        self.age = age

class Cat(Animal):
    def __init__(self,age):
        self.age = age
        
if __name__ == "__main__":
    
    a = AnimalShelter()
    a.enqueue(Dog(date(2020,1,1)))
    a.enqueue(Dog(date(2020,1,3)))
    a.enqueue(Cat(date(2020,1,15)))
    a.enqueue(Cat(date(2020,2,1)))
    a.enqueue(Dog(date(2020,2,3)))
    a.enqueue(Cat(date(2020,5,10)))
    
    import numpy as np
    tests = [ ( a.dequeue_dog(), Dog(date(2020,1,1) ) ),
              ( a.dequeue_any("dog"), Dog(date(2020,1,3) ) ),
              ( a.peek_dog(), Dog(date(2020,2,3) ) ),
              ( a.peek_cat(), Cat(date(2020,1,15) ) ),
              ( a.select_species('Cat'), Cat(date(2020,1,15) ) ),
              ( a.dequeue_cat(), Cat(date(2020,2,1) ) ),
              ( a.select_oldest(),Dog(date(2020,2,3) ) ),
              ( a.peek_dog(), None ) ]
    results = []
    for i in range(len(tests)):
        results.append(tests[i][0] == tests[i][1])
    print("Test loop_detection")
    if np.array(results).all() == True:
        print("All tests passed")
    else:
        print("All tests did not pass")