#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:55:39 2021

@author: alphantulukcu
"""
"""
Write a program, Lab01_yourname_Q1.py, that prompts the user to enter three 
float values for x, y and z from the user. Calculate and display the result 
of the following equation. The output should be formatted as shown in the 
sample run below.

"""

x = float(input('Enter the value x: '))
y = float(input('Enter the value y: '))
z = float(input('Enter the value z: '))

ans = (x + y*z) * (x*y + z) / (x*y*z)
print(f'f({x},{y},{z}) = {ans: .2f}')

#done