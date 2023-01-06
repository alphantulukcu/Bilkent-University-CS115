#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:23:12 2021

@author: alphantulukcu
"""


"""
Summary or Description of the Function
Parameters:
file1: txt
file2: txt
Returns:
file3: txt
file4: txt
"""

def district_density():
    file1 = open('city_districts.txt' ,'r')
    file2 = open('city_values.txt' ,'r')
    file3 = open('ankara_density.txt' ,'w')
    file4 = open('istanbul_density.txt' ,'w')    
    
    next(file1)
    next(file2)
    
    for line1 in file1:
        line1R = line1.strip()
        line2 = file2.readline()
        line2R = line2.replace(',','')
        
    #get numeric values
        pos1 = line1R.find('\t')
        pos2 = line2R.find('\t')
    
    #get districts
        if 'Ankara' in line1R:
            districtA = line1R[pos1+1:len(line1)]
        
    #get population
            pop = float(line2R[0:pos2])
        
    #get area
            area = float(line2R[pos2+1:len(line2)])
        # print(pop, area, end='')
        
    #calculate density
            density = pop / area
    
    #write to the output file
    
            file3.write(districtA + " " + str(density)+'\n')
            
        if 'Istanbul' in line1R:
            districtI = line1R[pos1+1:len(line1)]
        
    #get population
            pop = float(line2R[0:pos2])
        
    #get area
            area = float(line2R[pos2+1:len(line2)])
        # print(pop, area, end='')
        
    #calculate density
            density = pop / area
    
    #write to the output file
    
            file4.write(districtI + " "  + str(density)+'\n')   
            

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    
district_density()


"""
Summary or Description of the Function
Parameters:
imputD: str
s: float
Returns:
print: str
"""


def find_districts(inputD, s):
    file3 = open('ankara_density.txt' ,'r')
    file4 = open('istanbul_density.txt' ,'r')
    file5 = open(f'{inputD}_density{s}.txt', 'w')    
    name = inputD.capitalize()
    file5.write(f'Districts in {name} with population density below {s}: \n')
    
    if name == "Ankara":
        # print(file3.readlines())
        
        for line3 in file3:
            pos3 = line3.find(' ')
            density = float(line3[pos3+1:])
            if density < s:
                print(line3[0:pos3+1])
                districtsA = str(line3[0:pos3+1])
                
                file5.write( districtsA + '\n')
                
    if name == "Istanbul":
        # print(file3.readlines())
        
        for line4 in file4:
            pos4 = line4.find(' ')
            density = float(line4[pos4+1:])
            if density < s:
                print(line4[0:pos4+1])
                districtsI = str(line4[0:pos4+1])
            
                file5.write(districtsI + '\n')
            
    
        


    


