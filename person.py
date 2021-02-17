# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:49:51 2021

@author: os
"""

class person():

    def __init__(self, name=None, surname=None):
        self.local_name_person = name
        self.local_surname_person = surname
        
    def print_fullname_person(self):
        print ( "\n print_fullname() is activated...\n" )
        print ("Person full name =  ", self.local_name_person, " ", self.local_surname_person, "\n")