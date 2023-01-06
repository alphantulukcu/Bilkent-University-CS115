#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:30:37 2021

@author: alphantulukcu
"""

from Lab06_Tulukcu_Alphan_Q2 import Instructor as im


"""
Summary or Description of the read_file(file)
    Parameters:
        file (str): Description of file name
    Returns:
        dict: return dictionary created by given file
"""


def read_file(file):
    
    d = {}
    infile = open(file, 'r')
    for line in infile:
        l = line.strip().split(';')
        d[int(l[0])] = [l[1], l[2], float(l[3])]     
    return d


#input searchId and find an Instructor
d = read_file('instructor.txt')
searchId = int(input('Enter instructor id: '))
found = False
for k in d.keys():
    f = im(k, d[k][0], d[k][1], d[k][2])
    if searchId == im.get_Id(f):
        im.calculate_salary(f)
        found = True
        print(im.__str__(f))
        
if not found: 
    print('No Instructor is found')
        
        
#input searchstatus and find Instructors    
searchstatus = input('Enter status (F - Full-time / P - Part-time): ')
found = False
print('Part-time Instructors: ')
for k in d.keys():
    f = im(k, d[k][0], d[k][1], d[k][2])
    if searchstatus == im.get_status(f):
        im.calculate_salary(f)
        found = True          
        print(im.__repr__(f) + '\n')
        
if not found:
    print('invalid status')








#this part is not important!!!

# searchstatus = input('Enter status (F - Full-time / P - Part-time): ')
# found = False

# F = [
#      ]
# P = [
#      ]
# for k in d.keys():
#    f = im(k, d[k][0], d[k][1], d[k][2])
#    # ID = Id: im.get_Id (f)
#    # Name = im.get_NameSurname(f)
#    # Status = im.get_status(f)
#    im.calculate_salary(f)
#    # Salary  = im.get_salary(f)
#    if im.get_status(f) == 'F':
#        F.append(im.__repr__(f))
                 
#    if im.get_status(f) == 'P':
#        P.append(im.__repr__(f))


# if searchstatus == 'F':
#     found = True
#     print('Part-time Instructors: ')
#     print(F, sep = '\n')
# if searchstatus == 'P':
#     found = True
#     print('Part-time Instructors: ')
#     print(P)

# if not found:
#     print('invalid status')
        
    

        


        
        