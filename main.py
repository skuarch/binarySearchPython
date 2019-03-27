#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:31:18 2019
""@author: skuarch
"""

array = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12, 13, 14, 15]
key = 13
size = len(array)
half = int(size / 2)
result = 0
found = False
i = 0

print("half {}".format(half))
print("key {}".format(key))

if half == key:
    result = key

while i < 10:
    print("comparing")
    if key > half:
        i = i + 1
        s = array[half:size]
        print("s {}".format(s))
        size = len(s)
        print("size {}".format(size))
        half = int(size / 2)
        print("half {}".format(half))
        if key == half:
            found == True
    else:
         s = array[0:half]
          
         for e in s:
             print(e)
        
    

print("result {}".format(result))    