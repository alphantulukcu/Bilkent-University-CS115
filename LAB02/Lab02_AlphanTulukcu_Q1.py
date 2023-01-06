#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:19:45 2021

@author: alphantulukcu
"""

"""
Write a program, that inputs an integer number from the user and prints 
the factors of that number, as shown in the sample runs below.
"""

x = int(input("Enter an integer: "))

if x <= 0:
    print(f"{x} is invalid")
else:
    print(f"Factors of {x}: ")
    for i in range(1, x + 1):
           if x % i == 0:
               
               if i < x:
                   print(i,",", end= "")
               else:
                   print(i, end= " ")
                   
           