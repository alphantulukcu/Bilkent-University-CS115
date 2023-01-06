#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:37:38 2021

@author: alphantulukcu
"""

from Lab07_CabModule import Cab, Sedan, Hatchback

def read_file(filename):
    """
    Parameters
    ----------
    filename : str.

    Returns
    -------
    CabL : list.

    """
    file = open(filename, 'r')
    CabL = []
    for line in file:
        l = line.strip().split(';')
        CabL.append([l[0],l[1],l[2]])
    return CabL

def find_greater(CabL, obj):
    """
    Parameters
    ----------
    CabL : list
        
    obj : class object
        
    Returns
    -------
    Cabyear : int
        the number of cabs which year is bigger than year of obj.

    """
    
    Cabyear = 0
    for i in CabL:
        cab = Cab(i[0],i[1],i[2])
        if Cab.get_typeOfCabs(cab) == Cab.get_typeOfCabs(obj):
            if Cab.__gt__(cab, obj):
                Cabyear += 1
    return Cabyear
                


#separate sedan and hatchback and create new lists
SedanL = []
HatchbackL = []
CabL = read_file('cabs.txt')
for i in CabL:
    if i[0] == 'Sedan':
        SedanL.append(i)
    elif i[0] == 'Hatchback':
        HatchbackL.append(i)

#calculate fare for each sedan and print it        
num = 1
for i in SedanL:
    cab = Sedan(i[0],i[1],i[2])
    Sedan.calculate_fare(cab)
    print(f'Sedan {num} will pay {Sedan.get_price_per_km(cab)} TL')
    num += 1
    
print()
    
# calculate total km for required car and year    
"""
trv = 0
for a in HatchbackL:
    if a[2] == '2020':
        trv += int(a[1])
"""
trv = 0
obj1 = Cab('Hatchback',0,2020)
for a in HatchbackL:
    caba = Cab(a[0],a[1],a[2])
    if Cab.__eq__(caba, obj1):
        trv += int(Cab.get_kms(caba))

#find the number of car which is bigger than year of obj2        
CabL = read_file('cabs.txt')
obj2 = Cab('Sedan',0,2015)
res = find_greater(CabL, obj2)

print(f'There are {res} {Cab.get_typeOfCabs(obj2)} cars newer than {Cab.get_year(obj2)} \n')
        
print(f'All Hatchback cars of year 2020 have travelled {trv} kms')
        