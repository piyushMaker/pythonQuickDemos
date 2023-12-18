# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:25:03 2023

@author: supep
"""

import numpy as np
from math import sqrt

'''
ip_embd = np.random.random(size= (10,))
ip_embd = np.round(ip_embd, decimals=2)
print(np.shape(ip_embd))
print(ip_embd)
ll = ip_embd.tolist()
print(ll)

embd = np.random.random(size= (5,10))
embd = np.round(embd, decimals=2)
print(embd)
'''

ip_embd = [[0.73,0.06,0.99,0.97,0.89,0.93,0.55,0.96,0.81,0.96]]

embd = [[0.48,0.03,0.27,0.5,0.73,0.8,0.82,0.38,0.79,0.45],
[0.19,0.37,0.64,0.22,0.19,0.24,0.97,0.85,0.48,0.75],
[0.08,0.35,0.97,0.66,0.7,0.43,0.58,0.28,0.5,0.83],
[0.13,0.29,0.95,0.05,0.73,0.15,0.25,0.06,0.78,0.74],
[0.87,0.85,0.51,0.54,0.07,0.64,0.78,0.18,0.26,1.]]

print(len(ip_embd[0]))


def euclidean_distance(inp, embding):
    if 10 != len(inp):
        print("IP Dimension missmatch")
        return 1
    dist = []
    dist_squared = 0
    for row in embding:
        for elems in range(0, len(inp)):
            dist_squared += (inp[elems] - row[elems])**2
        
        dist2 =  sqrt(dist_squared)
        dist2 = round(dist2,3)
        #print(dist_squared, " sq ---sqrt ",dist2 )
        dist.append(dist2)
        dist_squared = 0
    
    
    return dist
    
x = euclidean_distance(ip_embd[0], embd)
sorte = np.argsort(x)
print(sorte)
print(x)

best_match = 3

for cl in range(0, best_match):
    print("closest ", embd[sorte[cl]])



    
    


