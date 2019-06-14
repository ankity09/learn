#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:03:20 2019

@author: ankityadav
"""

from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file {}".format("filename"))
print (txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print (txt_again.read())