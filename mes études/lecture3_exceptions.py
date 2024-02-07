#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:44:26 2024

@author: barut
"""

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")    

#####ELSE is USED to print if other conditions are true. 
#####If user do not prompt correctly, the question is reposed. 
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
#this feature allows us to ask the prompt again until we get a response
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}")
## THESE TWO ARE THE SAME.
##############################
##TRY TO GET AN INTEGER FROM THE USER
def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
main()

#### WE CREATE OUR OWN FUNCTION. WE CAN MAKE IT LOOK BETTER BY REPLACING BREAK:
def main():
    x = get_integer()
    print(f"x is {x}")
def get_integer():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError: 
            print("x is not an integer")
        else:
            return x   ####THIS PART !!!!
main()        
        ############ WHAT CAN WE DO TO TIGHTEN UP THE CODE?????
def main():
    x = get_intt()
    print(f"x is {x}")
def get_intt():
    while True:
        try:
            return int(input("What's x? "))  ###WHY DEFINE SAME VARIABLE TWO TIMES?
        except ValueError:
            print("x is not an integer")
main()
        
 # TO HANDLE THE ERROR NICER, WITHOUT PROMPTING. WE CAN USE *pass*

def main():
    x = gett_int()
    print(f"x is {x}") 
def gett_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
main()
        
 ############ INSTEAD OF USING X, WE MAKE THE FUNCTION MORE REUSABLE:
def main():
    x = get_innt("What's x? ")
    print(f"x is {x}")
def get_innt(prompt): #### BY ADDING PROMPT AS ARGUMENT, WE MAKE IT REUSABLE BY OTHERS!!!!
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
       
        
        
        
        
        