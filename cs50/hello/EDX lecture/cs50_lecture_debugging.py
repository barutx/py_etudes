#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:54:31 2024

@author: barut
"""

def main():
    height = int(input("Height: "))
    pyramid(height)
    
def pyramid(n):
    for i in range(n):        
        print("#"*i)
        
if __name__ == "__main__":
    main()
    
#########DEBUGGING######
#####Let's say that it's rather "i" is problematic, so we will print i 
# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print(i, end=" ")
#         print("#"*i)
main()
##### WE ADDED PRINT(i) SO THAT WE CAN SEE OUR STEPS. AND i STARTS WITH ZERO !!!!
##### SO print("#" * (i+1))
##### PRINT CAN BE PRETTY TEDIOUS, SO WE HAVE A DEBUGGER
#### A BREAKPOINT IS A MECHANISM THAT HELPS YOU TO SPECIFY AT WHICH LINE OF PROGRAM YOU WANT TO STOP
#### SO THAT YOU CAN POKE AROUND 