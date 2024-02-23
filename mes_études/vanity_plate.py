#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:18:00 2024

@author: barut
"""

def main():
    x= str(input("Plate:")).upper().strip()
    if is_valid(x): 
        print("Valid: ",x)
    else:
        print("Invalid: ", x)

def is_valid(s):
    s = list(s)
    letters=[alph for alph in s if alph.isalpha()]
    num=[num for num in s if num.isdigit()]
    punc=[punc for punc in s if not (punc.isalpha() or punc.isdigit())]
   
    if punc:
        return False 
    elif not (letters[0:2] == s[0:2]):
        return False
    elif len(s)<=6 and len(s)>=2 and len(letters)>=2:     
        if num:
            if num[0]=="0":
                return False          
            j=s.index(num[0])
            for char in letters:
                if char in s[j:(len(s))]:
                    return False
            return True
        else:            
            return True
            
    else:
        return False

if __name__ == '__main__':
    main()


