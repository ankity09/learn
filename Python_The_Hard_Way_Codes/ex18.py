#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:35:32 2019

@author: ankityadav
"""

def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_one(arg1):
    print("arg1: {}".format(arg1))

def print_none():
    print("I get nothin.")
    
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()