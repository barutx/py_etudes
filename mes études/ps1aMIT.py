#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:27:25 2024

@author: barut
"""

total_cost=float(input("Enter the cost of your dream house: "))
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
portion_down_payment= 0.25
current_savings= 0
r=0.04

a=float(total_cost*portion_down_payment)
c=annual_salary*portion_saved/12
i=0
while current_savings<a:
    current_savings+=c+current_savings*r/12
    i=i+1
if current_savings >=a:
    print("Your annual salary: ", annual_salary)
    print("The percent of your salary to save, as a decimal: ",portion_saved)
    print("The cost of your dream house: ",total_cost)
    print("Number of months:",i)