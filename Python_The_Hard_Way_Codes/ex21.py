#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:23:07 2019

@author: ankityadav
"""

def add(a, b):
    print("ADDING {} + {}".format(a,b))
    return(a + b)

def subtract(a,b):
    print("SUBTRACTING {} - {}".format(a, b))
    return(a - b)

def multiply(a, b):
    print("Multiplying {} * {}".format(a, b))
    return(a * b)

def divide(a, b):
    print("DIVIDING {} / {}".format(a, b))
    return(a / b)
    
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

# A puzzle for extra credit

print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

when = divide(add(24, 34), subtract(100, 1023))

print("That becomes: ", when, "Can you do it by hand?")