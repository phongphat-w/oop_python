# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:49:51 2021

@author: os
"""

class woman():

    def __init__(self, name=None, surname=None):
        self.local_name_woman = name
        self.local_surname_woman = surname
        
    def print_fullname_woman(self):		
        print ( "\n print_fullname() is activated...\n" )
        print ("woman full name =  ", self.local_name_woman, " ", self.local_surname_woman, "\n")