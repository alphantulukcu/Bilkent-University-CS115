#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:09:23 2021

@author: alphantulukcu
"""
"""
Write a program, that inputs three integers from the 
user and reports the largest even input and the sum of even inputs.
"""

x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))
z = int(input('Enter third integer: '))

# all of them are even number:

if (x % 2 == 0) and (y % 2 == 0) and (z % 2 == 0):
    sum = x + y + z
    print(f'Sum of evens is {sum}')
    if (x >= y) and (x >= z):
        print (f'even max is {x}')
    elif (y >= x) and (y >= z):
        print (f'even max is {y}')
    elif (z >= y) and (z >= x):
        print (f'even max is {z}')
    
        
        
# two of them are even number but one of them are not:

elif (x % 2 == 0) and (y % 2 == 0) and (z % 2 != 0):
    sum = x + y
    print(f'Sum of evens is {sum}')
    if (x >= y):
        print (f'even max is {x}')
    elif (y >= x):
        print (f'even max is {y}')

elif (x % 2 == 0) and (y % 2 != 0) and (z % 2 == 0):
    sum = x + z
    print(f'Sum of evens is {sum}')
    if  (x >= z):
        print (f'even max is {x}')
    elif (z >= x):
        print (f'even max is {z}')
        

elif (x % 2 != 0) and (y % 2 == 0) and (z % 2 == 0):
    sum = y + z
    print(f'Sum of evens is {sum}')
    if (y >= z):
        print (f'even max is {y}')
    elif (z >= y):
        print (f'even max is {z}')
        

# one of them are even number but others are not: 
    
elif (x % 2 == 0) and (y % 2 != 0) and (z % 2 != 0):
    sum = x
    print(f'Sum of evens is {sum}')
    print (f'even max is {x}')
        
elif (x % 2 != 0) and (y % 2 == 0) and (z % 2 != 0):
    sum = y
    print(f'Sum of evens is {sum}')
    print (f'even max is {y}')
        
elif (x % 2 != 0) and (y % 2 != 0) and (z % 2 == 0):
    sum = z
    print(f'Sum of evens is {sum}')
    print(f'even max is {z}')
        
# none of them are even number:
    
elif (x % 2 != 0) and (y % 2 != 0) and (z % 2 != 0):
    print('No even integer is entered. ')


    
    
    
