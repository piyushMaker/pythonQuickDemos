# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:48:13 2023

@author: supep
"""

#List comprehension

my_list = [x for x in range (0,10)]
print(my_list)

my = [[x for x in range(0,4)] for c in range(0,3)]
print(my)


my_dict = {k:v for k,v in zip(['a', 'b'], [1,2])}
print(my_dict)


my_dict = {d : {k:v for k,v in zip(["a", "b"], [1,2])} for d in range(0,10)}
print(my_dict)

my_dict = {k+"m":v**2 for k,v in zip(["a", "b"], [1,2])}
print(my_dict)


my_tuple = (x for x in range(1,10))
print(next(my_tuple))


