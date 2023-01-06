#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:21:37 2021

@author: alphantulukcu
"""

"""
Write a program, that continually prompts the user for a desired sum until 
0 is entered. For each desired sum input value, it repeatedly rolls two 
six-sided dice until their sum is the desired sum and reports the number 
of rolls to achieve the desired sum. It should validate input for the 
desired sum. For example, 1 cannot be a valid desired sum.
"""
from random import randrange
i2 = 0
while i2 <1000:
    sum1 = int(input("Desired dice sum: "))
    
    if sum1 == 1 or sum1> 12 or sum1 < 0:
        print("Invalid dice sum! Try again...")
    if sum1 == 0:
        print("bye!")
        break
    else:
        i = 0
        while i < 1000:
            d1 = randrange(1,7)
            d2 = randrange(1,7)
            i += 1
            
            if sum1 == (d1 + d2):
                print(i,"rolls.")
                break
        