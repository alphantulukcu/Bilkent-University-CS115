#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:58:21 2021

@author: alphantulukcu
"""
"""
Write a program, that prompts the user for three names: displays the 
longest name (the name that contains the most characters) in the format 
as shown in the sample runs below.
"""
# enter the names
name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))
name3 = str(input("Enter third name: "))

# one of name is longer than others:

if (len(name1) > len(name2)) and (len(name1) > len(name3)):
    print (f"{name1}\'s name is the longest. ")
    
elif (len(name2) > len(name1)) and (len(name2) > len(name3)):
    print (f"{name2}\'s name is the longest. ")

elif (len(name3) > len(name1)) and (len(name3) > len(name2)):
    print (f"{name3}\'s name is the longest. ")

# two of name are equal and longer than other one or all of them are equal:
else:
    
    if (len(name1) == len(name2)) or (len(name1) == len(name3)):
        print (f"{name1}\'s name is the longest, but there is a tie! ") 

    elif (len(name1) == len(name2)) or (len(name2) == len(name3)):
        print (f"{name2}\'s name is the longest, but there is a tie! ") 

    elif (len(name1) == len(name3)) or (len(name2) == len(name3)):
        print (f"{name3}\'s name is the longest, but there is a tie! ") 
        
"""
In my opinion, when two or all names are equal, it should not be printed 
that "first name are longest" But samples do it this way. 

Sample Run 2:
Enter first name: Berk
Enter second name: Can
Enter third name: Doğa
Berk 's name is the longest, but there is a tie!

Sample Run 4:
Enter first name: Ali
Enter second name: Ece
Enter third name: Nil
Ali 's name is the longest, but there is a tie!

I think it should be printed "name_ and name_ are equal and name_ is 
shorter than others" or "all name are equal"
"""

