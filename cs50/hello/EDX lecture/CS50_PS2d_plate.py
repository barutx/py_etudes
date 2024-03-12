#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:18:00 2024

@author: barut
"""



# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
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


