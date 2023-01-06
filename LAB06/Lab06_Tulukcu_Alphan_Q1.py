#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:34:23 2021

@author: alphantulukcu
"""


"""
Summary or Description of the formSentence(inlist, searchChr)
    Parameters:
        inlist (list): Description of arg1
    Returns:
        str: return l created in function
"""

def formSentence(inlist, searchChr):
    
    l = ''
    for i in inlist:
        for k in i:
            if k[0].lower() == searchChr.lower():
                # l.append(k)
                l += k + ' '
    return l


tlist = [['This', 'is', 'lab', 'Script'],
         ['We', 'should', 'finish', 'it'],
         ['we', 'solve', 'some', 'questions']]

searchChr = input('Enter search character: ')

print('Two Dimensional List: ')
for s in tlist:
    print(s)
print('Sentence:', formSentence(tlist, searchChr))
    