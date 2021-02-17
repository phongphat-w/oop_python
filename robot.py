# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:49:51 2021

@author: os
"""

from person import person as parent_person
from superman import superman as parent_superman
from woman import woman as parent_woman

class robot(parent_person, parent_superman, parent_woman):
    
    def __init__(self):
        
        #Get member from First parent class
        super().__init__() 
        
        #Get member from Second parent class
        super(parent_person, self).__init__() 
        
        #Get member from Third parent class
        super(parent_superman, self).__init__()
               