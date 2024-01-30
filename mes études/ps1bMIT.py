#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:05:40 2024

@author: barut
"""
annual_salary=float(input("Enter your starting annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream house: "))
semi_annual_raise=float(input("Enter semi annual raise, as a decimal: "))

portion_down_payment= 0.25
current_savings= 0
r=0.04

payment=float(total_cost*portion_down_payment)
salary=annual_salary
monthly_saving=float((salary*portion_saved)/12) 
i=1

while current_savings<payment:
    if i%6==0:
        salary+=salary*semi_annual_raise
        monthly_saving=float((salary*portion_saved)/12) 
        current_savings+=float(monthly_saving+(current_savings*r/12))
        i=i+1    
    else:
         current_savings+=float(monthly_saving+(current_savings*r/12))
         i=i+1  
    
if current_savings>=payment:
    print("Your starting annual salary: ", annual_salary)
    print("The percent of your salary to save, as a decimal: ",portion_saved)
    print("The cost of your dream house: ",total_cost)
    print("Number of months:",i)
    print("Total savings in: ", i ," months:", current_savings)
    print("The amount of down payment: ",payment)
    print("Final salary: ",salary)
