#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:21:41 2024

@author: barut
"""
def main():
    print(f"Output: {remove_vowel()}")

def remove_vowel(word='selam'):
    vowel=["a","e","o","i","u"]
    for _ in word:
        if _ in vowel:
            word = word.replace(_,"")
    return word

if __name__ == '__main__':
    main()
