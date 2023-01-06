#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:54:31 2021

@author: alphantulukcu
"""

class Instructor( object ):
    def __init__(self, Id, NameSurname, status, hours):
        self.__Id = Id
        self.__NameSurname = NameSurname
        self.__status = status
        self.__hours = hours
        self.__salary = 0
        
# the following 4 functions get a parameters self and return each object        
    def get_Id(self):
        return self.__Id
    
    def get_NameSurname(self):
        return self.__NameSurname
       
    def get_status(self):
        return self.__status
      
    def get_hours(self):
        return self.__hours
    
# calculate and get the salary with hours        
    def calculate_salary(self):
        if self.__status == 'F':
            self.__salary = 5000 + self.__hours * 500
        if self.__status == 'P':
            self.__salary = self.__hours * 400
        return self.__salary
    
    def get_salary(self):
        return self.__salary
    

# str and repr methods    
    def __str__(self):
        return f'Name: {self.__NameSurname}\nStatus: {self.__status}\nSalary: {self.__salary} TL'
    
    def __repr__(self):
        return f'Id: {self.__Id}\nName: {self.__NameSurname}\nSalary: {self.__salary} TL'
    
    
        