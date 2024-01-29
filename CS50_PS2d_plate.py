#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:18:00 2024

@author: barut
"""

def main():
    if is_valid(): 
        print("Valid")
    else:
        print("Invalid")
def is_valid():
    s = str(input("Plate: ")).upper().strip()
    letters=[alph for alph in s if alph.isalpha()]
    num=[num for num in s if num.isdigit()]
    punc=[punc for punc in s if not (punc.isalpha() or punc.isdigit())]
    if punc:
        return False 
    elif len(s)<=6 and len(s)>=2 and len(letters)>=2:     
        if num:
            if num[0]=="0":
                return False
            elif True:           
                j=s.index(num[0])
                for char in letters:
                    if char in s[j:(len(s))]:
                        return False
                    else:
                        return True
        else:            
            return True
            
    else:
        return False
main()


