#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:15:22 2021

@author: alphantulukcu
"""

def load_movies(file):
    file2 = open(file, 'r')
    d = {}

    for line in file2:
        line = line.strip()
        line1 = line.split(',')

        year = line1[0]
        mName = line1[1]


        if int(year) in d:
            d[int(year)].append(mName)
        else:    
            d[int(year)] = [mName]
        
    file2.close()        
    return d


def get_movies_by_year(d,years):
    l1 = []
    for i in d.keys():
        if years == i:
            l1.append(d[i])
        else: 
            continue
        return l1 
        
    
def get_movies_by_keyword(file,kw):
    l2 = []
    file2 = open(file, 'r')
    
    list_mix = []
    for line in file2:
        line = line.strip()
        line1 = line.split(',')
        
        year = line1[0]
        mName = line1[1]
        
        mix = [year, mName]
        list_mix.append(mix)
    
    for k in list_mix:
        
        s = k[1][0:].split(' ')
        
        if kw in s:
            l2.append(k)
        else:
            continue
    return l2 
            
    
def print_list(l):
    for i in l:
        print(", ".join(i))
    
   
        
file = 'movie_data.csv'

d = load_movies(file)

y = int(input('Enter year to search: '))

l = get_movies_by_year(d,y)


if get_movies_by_year(d,y) is None:
    print(f'No movie from {y} found')
else:
    ls = []
    for i in range(0,len(l[0])):
        ls.append(l[0][i])
    print(f'Movie made in {y}: ')    
    print(*ls, sep = '\n')
    
    
kw = input('Enter keyword to search: ')

if not get_movies_by_keyword(file,kw):
    print(f'No movie from "{kw}" found')
else:    
    print_list(get_movies_by_keyword(file,kw))
