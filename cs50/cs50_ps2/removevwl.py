#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:21:41 2024

@author: barut
"""
def main():
    remove_vowel()

def remove_vowel():
    x=(input("Input: "))
    vowel=["a","e","o","i","u"]
    for _ in x:
        if _ in vowel:
            x=x.replace(_,"")
        else:True
    print("Output:",x)

if __name__ == '__main__':
    main()
