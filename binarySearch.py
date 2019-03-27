#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:19:46 2019

@author: skuarch
"""

def printArray(start, end):
    r = array[start:end]
    for e in r:
        print("[{}, ]".format(e)) 
#                                !
#        0  1  2  3  4   5   6   7   8   9   10  11  12  13  14 
array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
key = 120
size = len(array) -1
half = int(size / 2)
result = 0
found = False
i = 0
start = 0
end = size
index = 0

while found == False:   
    
    print("--------------------------")
    print("start {} half {} end {} size {}".format(start, half, end, size))
    printArray(start, end + 1)
    if array[start] == key:
        found = True
        index = start
        break
    elif array[half] == key:
        found = True
        index = half 
        break
    elif array[end] == key:        
        found = True
        index = end
        break
    
    print("key {} > {}".format(key, array[half]))
    if key > array[half]:
        start = half
        end = size
        half = int(end / 2) 
        size = int(((end - start) / 2)) + start
    else:        
        end = half
        half = int(end / 2)
        size = end + 1
        
    i = i + 1
    
    if half == 0:
        break

if found == False:
    print("not found")
else:
    print("found on position: {}".format(index))

print("iterations: {}".format(i + 1))


