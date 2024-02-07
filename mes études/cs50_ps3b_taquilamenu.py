#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:39:15 2024

@author: barut
"""
# def main():      
#     place_order()




# def place_order():
#     menu = {
#              "Baja Taco": 4.25,
#              "Burrito": 7.50,
#              "Bowl": 8.50,
#              "Nachos": 11.00,
#              "Quesadilla": 8.50,
#              "Super Burrito": 8.50,
#              "Super Quesadilla": 9.50,
#              "Taco": 3.00,
#              "Tortilla Salad": 8.00,
#              }    
#     Total=0
#     while True:
#         try:
           
#             item =  input("Place your order: ").title()                     
#             if item in menu:        
#                 Total+=menu[item]        
#                 print("Total: $",Total, sep="")
#         except(EOFError):
#             break
# main()
############## WHAT CHATGPT SUGGESTS TO IMPROVE THE SCRIPT ABOVE: 
MENU =  {
         "Baja Taco": 4.25,
         "Burrito": 7.50,
         "Bowl": 8.50,
         "Nachos": 11.00,
         "Quesadilla": 8.50,
         "Super Burrito": 8.50,
         "Super Quesadilla": 9.50,
         "Taco": 3.00,
         "Tortilla Salad": 8.00,
         }    
#####  MENU AS GLOBAL VARIABLE ######
def main():
    place_order()

def get_item_price(item, menu):
    return menu.get(item,None)

def display_total(total):
    total = print("Total: ${: .2f}".format(total))

def place_order():
    total = 0
    while True:
        try:
            item =  input("Place your order: ").title()
            if item in MENU:
                total += get_item_price(item,MENU)
                display_total(total)
            else:
                print("Invalid item, please choose from the menu.")
        except EOFError:
            return display_total(total)
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    