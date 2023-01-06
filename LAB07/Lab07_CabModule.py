#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:36:40 2021

@author: alphantulukcu
"""

class Cab(object):
    
    def __init__(self, typeOfCab, kms, year):
        self.__typeOfCab = typeOfCab
        self.__kms = kms
        self.__year = year
        
    def get_typeOfCabs(self):
        return self.__typeOfCab
    
    def get_kms(self):
        return self.__kms
    
    def get_year(self):
        return self.__year
    
    def __gt__(self, other):
        return int(self.__year) > int(other.__year)
    
    def __eq__(self, other):
        return int(self.__year) == int(other.__year)
    
    def __repr__(self):
        return f'{self.__typeOfCab}, {self.__kms}, {self.__year}'
    
class Sedan(Cab):
    def __init__(self, typeOfCab, kms, year):
        Cab.__init__(self, typeOfCab, kms, year)
        self.__price_per_km = int(kms)
        
    def calculate_fare(self):
        self.__price_per_km *= 2.5
        return self.__price_per_km
        
    def get_price_per_km(self):
        return self.__price_per_km
    
    def __repr__(self):
        return Cab.__repr__(self) +', '+ f'{self.__price_per_km}'
        
    
    
class Hatchback(Cab):
    def __init__(self, typeOfCab, kms):
        Cab.__init__(self, typeOfCab, kms)
        self.__price_per_km = int(kms)
        
    def calculate_fare(self):
        self.__price_per_km *= 2.2
        return self.__price_per_km
        
    def get_price_per_km(self):
        return self.__price_per_km
    
    def __repr__(self):
        return Cab.__repr__(self) +', '+ f'{self.__price_per_km}'
    
    
# p1 = Sedan('Sedan', 200, 2021)
# Sedan.calculate_fare(p1)
        
# print(p1)