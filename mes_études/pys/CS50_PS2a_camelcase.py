#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:23:37 2024

@author: barut
"""

prompt=input("camelCase: ")
for i in prompt:
        if i.isupper():
             prompt=prompt.replace(i,"_"+i)
        else:
            True
print("snake_case:",prompt.lower())
        
####OLLLLLLEEEEEEYYY           
            
        



