#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:31:47 2024

@author: barut
"""

def main():
    get_fuel('jhjh')

def get_fuel(fraction):
    fraction = fraction.split('/')  
    while True:
        try:  
            x = int(fraction[0])
            y = int(fraction[1])
            fuel = float((x/y)*100)
            if fuel>=99:
                print("F")
                return "F"
            elif fuel<=1:
                print("E")
                return "E"
            else:
                    print(round(fuel),"%", sep="")
                    a = round(fuel)                        
                    return f"{a}%"              
        except (ValueError):
            print("pick some integers")
            break
    fraction = input("What is fraction?  ")
    get_fuel(fraction)
    

        
if __name__ == '__main__':
    main()


####CHECK CHATGPT IF WE CAN TIGHTEN THIS UP, ESPECIALLY INPUT PART
#### CHATGPT IS A GREAT HELP !!!!!! ##### 
# def main():
#     get_fuell()
# def get_fuell():
#     while True:
#         try:
#             fraction = input("Enter the fuel fraction in the following format: {}/{}".format("X","Y"))
#             x,y = parse_fraction(fraction)
#             fuel= calculate_fuel_percentage(x,y)
#             print_result(fuel)
#             break 
#         except(ValueError, ZeroDivisionError,IndexError):
#             pass
# def parse_fraction(fraction):
#     x,y = map(int, fraction.split("/"))
#     return x,y
# def calculate_fuel_percentage(x,y):
#     fuel = round((x/y)*100)
#     return fuel
# def print_result(fuel):
#     if fuel <= 1:
#         print("E")
#     elif fuel >= 99:
#         print("F")
#     else:
#         print("{}%".format(fuel))
# if __name__ == '__main__':
#     main()
        
        
        
        
        
        
        
        
        
        