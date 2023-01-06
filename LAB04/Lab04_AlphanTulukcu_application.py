#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:39:19 2021

@author: alphantulukcu
"""

from Lab04_AlphanTulukcu_Module import *



def searchcity_density():
    
    
    inputR = str(input("Enter city to search (quit to exit): "))
    inputC = inputR.capitalize()
    
    if inputC == 'Quit':
        print('Thank you - Goodbye')
        return True
    
    
    if inputC != "Ankara" and inputC != "Istanbul" and inputC != "Quit":
        print(f'{inputC} is not found...')
        return searchcity_density()
    else:
        num = float(input("Enter maximum density: "))
        # districts = str(find_districts(inputC, num))
        
        if find_districts(inputC, num) == True:
            print(f'Districts in {inputC} with population density below {num}: ')
            find_districts(inputC, num)
        
            file5 = open(f'{inputR}_density{num}.txt', 'r')
            next(file5)
            for line in file5:
                if line == '\n':
                    print(f'No districts in {inputC} with population density below {num}')
            
            
        
            # print(f'No districts in {inputC} with population density below {num}')
            
            
        while inputC != 'Quit':
            return searchcity_density()
        # if inputC == 'Quit':
        #     print('Thank you - Goodbye')
            
            
searchcity_density()

# f'Districts in {inputC} with population density below {num}: ' + str(a)