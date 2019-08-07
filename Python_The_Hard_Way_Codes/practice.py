#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 06:52:52 2019

@author: ankityadav
"""
import numpy
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))
          
nums = list(range(5))
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0 ]
print(even_squares)

animal_dict = {'cat': 'cute', 'dog': 'furry'}
print(animal_dict['cat'])

print('cat' in animal_dict)

animal_dict['fish'] = 'wet'

print(animal_dict['fish'])
print(animal_dict.get('moneky', 'N/A'))
print(animal_dict.get('fish', 'N/A'))
del animal_dict['fish']
print(animal_dict.get('fish', 'N/A'))


d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))

for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
    

even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)

animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)
animals.add('fish')
print('fish' in animals)
animals.add('cat')
print(len(animals))
animals.remove('cat')
print(len(animals))


animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

def solve(s):
    s.capitalize()
    return(s)
    
    
    
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
#print(numpy.prod(numpy.sum(A, axis=0), axis=0))








