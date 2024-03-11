#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:33:31 2024

@author: barut
"""

def main():
    my_grocery_list={}
        
    while True:
        try:
            item = input("Item:").strip().lower()
            if item not in my_grocery_list:
                count = my_grocery_list.get(item,0)
                my_grocery_list[item] = count+1
            elif item in my_grocery_list:
                my_grocery_list[item] += 1         
        except EOFError:
            return list_display(my_grocery_list)

def list_display(my_grocery_list):
    for i in sorted(my_grocery_list.keys()):
        count = my_grocery_list[i]
        print(f"{count} {i.upper()}")
        
    

    
if __name__=="__main__":
    main()
##########  I REALLY TOOK HELP FROM CHATGPT THIS TIME. BECAUSE I DID NOT KNOW
########## THAT get(item,default) creates an item in the dictionary and assigns it a value.


