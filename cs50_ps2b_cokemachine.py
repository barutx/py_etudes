#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:57:08 2024

@author: barut
"""
def main():
    get_coke()
    
def get_coke():
    due=50 
    while True:
        coin=int(input("Insert your coin: "))
        if coin == 50 or coin == 25 or coin==10 or coin==5:   
            due=due-coin                                    
            if due==0:              
                return print("Change Owed:0")
            elif due<0:             
                return print("Change Owed:",abs(due))
            else:
                print("The amount due:",due )
main()