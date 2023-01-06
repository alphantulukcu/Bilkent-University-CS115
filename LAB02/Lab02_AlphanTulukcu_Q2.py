#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:21:06 2021

@author: alphantulukcu
"""

"""
Write a program,that prompts the user to enter a string until an empty 
string is entered. For each input string, it displays a new string created 
by collecting even position letters followed by odd position letters from 
the input string.
"""

  
    
str0 = input("Enter a string: ")
if str0 == "":
    print("Done!")
else:
    mod_str1 = str0[::2]
    mod_str2 = str0[1::2]
    mod_str = mod_str1 + mod_str2 
    print("new string is ", mod_str)
    

while len(str0)!=0 :
    str0 = input("Enter a string: ")
    mod_str1 = str0[::2]
    mod_str2 = str0[1::2]
    mod_str = mod_str1 + mod_str2 
    
    if len(str0)==0 :
        print("done!")
    else:
        print("new string is ",mod_str)
        


    
   
    

