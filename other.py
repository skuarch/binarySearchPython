#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:25:27 2019

@author: skuarch
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:19:46 2019

@author: skuarch
"""
#                                !
#        0  1  2  3  4   5   6   7   8   9   10  11  12  13  14  15 
array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 90]
key = 12
size = len(array) -1
half = int(size / 2)
result = 0
found = False
i = 0
start = 0
end = size
index = 0

while i < size:   
    
    print("--------------------------")
    print("start {} half {} end {}".format(start, half, end))
    
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
        size = end - start
    else:        
        end = half
        half = int(end / 2)
        
    i = i + 1
    
    if half == 0:
        break

if found == False:
    print("not found")
else:
    print("found on position: {}".format(index))

print("iterations: {}".format(i + 1))