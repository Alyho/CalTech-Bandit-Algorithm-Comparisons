# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:18:43 2019

@author: student-minecraft
"""

import random

class Pet :
    
    hunger_threshold = 10
    boredom_threshold = 5
    boredom_decrement = 2
    hunger_decrement = 2
    sounds = ["meow"]
    
    def __init__ (self, name) :
        self.name = name
        self.hunger = random.randrange(0, self.hunger_threshold)
        self.boredom = random.randrange(0, self.boredom_threshold)
        self.sounds = self.sounds[:]
        
    def time(self):
        self.boredom +=1
        self.hunger +=1
        
    def mood(self):
        if (self.boredom <= self.boredom_threshold or self.hunger <= self.hunger_threshold) :
            return "happy"
        elif (self.boredom >= self.boredom_threshold) :
            return "bored"
        elif (self.hunger >= self.hunger_threshold) :
            return "hungry"
        
    def __str__ (self):
        state = "My name is " + self.name + "."
        state += "I am " + self.mood() + "."
        return state
    
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
        
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
        
    def hi(self):
        self.reduce_boredom()
        print (self.sounds[random.randrange(0, len(self.sounds))])
       
    def teach(self, word):
        self.reduce_boredom()
        self.sounds.append(word)
        
    def feed(self):
        self.reduce_hunger()
        

p1 = Pet("mickey")

print(p1)

for i in range (10):
    p1.time()

print(p1)
p1.teach("merp")
p1.hi()
p1.teach("howdy")
p1.feed()

print(p1)
    