#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:02:47 2019

@author: ankityadav
"""

numbers = []
def num(val, inc):
    i = 0
    while i < val:
        print("At the top i is {}".format(i))
        numbers.append(i)
        i = i + inc
        print("Numbers now", numbers)
        print("At the bottom i is {}".format(i))

num(5,3)

        
    
    
