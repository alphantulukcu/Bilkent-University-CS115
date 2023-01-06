#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:31:45 2021

@author: alphantulukcu
"""

from Country import Country as co

def readCountries(l,filename):
    infile = open(filename, 'r')
    for line in infile:
        c = line.strip().split(',')
        obj = co(c[0], c[1], float(c[2]), float(c[3]))
        l.append(obj)
    return l
        
def searchCountries(listC, sVal, endInd, l):
    
    if endInd == -1:
        return l
    else:
        if co.getContinent(listC[endInd]) == sVal.capitalize():
            l.append(listC[endInd])
            return searchCountries(listC, sVal, endInd-1,l)
        else:
            return searchCountries(listC, sVal, endInd-1,l)
        
            
def selectionSort(L):
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i].getContinent() < L[suffixStart].getContinent():
                L[suffixStart], L[i] = L[i], L[suffixStart]
            elif L[i].getContinent() == L[suffixStart].getContinent():
                if L[i].getCountry() < L[suffixStart].getCountry():
                    L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    
        
    



#search countries for input continent (I add message for empty list)
continent = input('Enter continent to search: ')
file = 'country.txt'
countries = []
readCountries(countries,file)
l = []
searchCountries(countries,continent,len(countries)-1, l)
if l != []:
    print(f'List of countries in {continent}: ')
    for obj in l[::-1]:
        print(obj)
else:
    print('No country was found')
    
#add new country in list
inpc = input('Enter county name, continent, life expectany for Men and life expectany for Women: ')
inpc = inpc.strip().split(', ')
newobj = co(inpc[0], inpc[1], float(inpc[2]), float(inpc[3]))

found = False
for a in countries:
    if co.__eq__(a, newobj):
        found = True

if found == False:
    countries.append(newobj)
    print('New country added \n')
elif found == True:
    print(f'{co.getCountry(newobj)} is already on the list \n')
    
#print sorted list
print('Countries by Continent and Name: ')
selectionSort(countries)

print(countries)

    
    
    
        