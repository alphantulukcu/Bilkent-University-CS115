#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:37:28 2021

@author: alphantulukcu
"""

def is_neat_reversible(s):
    
    len1 = len(s)
    
    s_new = ""
    i1 = 1
    for i in s:
        s_new = s_new + s[i1%(len1)]
        i1 += 1
    
    s_new_reverse = ""
    i2 = -1
    for i in s_new:
        s_new_reverse = s_new_reverse + s_new[i2]
        i2 -= 1
    return s_new_reverse == s
    
    
""" 
Parameters: 
s (str): inputting string
s_new (str): moving first character to the end for s
s_new_reverse (str): reverse the s_new

Returns:(bool) 
return s_new_reverse == s  

"""
    
def uppercase_word_at(s, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = s[0:index]
    count = 0
    for i in s[index:len(s)]:
        if i == " ":
            break
        else:
            if i not in alphabet or alphabet.index(i)>=26:
                result += i
                count += 1
            else:
                result += alphabet[alphabet.index(i)+26]
                count += 1

    result = result + s[(index+count):len(s)]
    return result

""" 
Parameters: 
s (str): inputting string
index (int): inputting integer as requiring initial letter of queque

Returns: (str)
takes a string s and an integer index as parameters and returns a string which 
is identical to s except the letters in s starting from the specified index up 
to the first space character are capitalized.
    
"""





def capitalize_neat_reversibles(s):
    if s == " ":
        print("bye! ")
    if s == "":
        print("bye! ")
    
    final_string = s
    i0=0
    i_word=0
    
    while i0 < len(s):
        
        i_word = 0
        while (i0 + i_word) < len(s) and s[i0 + i_word] != " ":
            i_word += 1
        
        if is_neat_reversible( s[i0:i0+i_word] ) :
            
            final_string = uppercase_word_at(final_string, i0)    
        
        i0 += (i_word+1)
    
    return final_string



"""
Parameters:
s (str): inputting sentence

Returns: (str)
takes a string s as a parameter,and using the functions defined in parts a) 
    and b), creates and returns a new string in which all neat reversible 
    words are capitalized.
"""
strinput = input('Enter a string: ')
print(capitalize_neat_reversibles(strinput))
while strinput != "":
    strinput = input('Enter a string: ')
    print(capitalize_neat_reversibles(strinput))

            
   
    
    
    
    
