#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:46:55 2024

@author: barut
"""

total_cost=1000000
portion_down_payment=0.25
semi_annual_raise=0.07
r=0.04
nmb_months=36
annual_salary=float(input("Enter your initial salary: "))
payment=float(total_cost*portion_down_payment)
def savings(annual_salary,saved_portion):
    savings=0
    for i in range(1,37):
        if i%6==0:
            annual_salary+=annual_salary*semi_annual_raise
            savings+=((annual_salary*saved_portion/10000)/12)+(savings*r/12)
        else:
            savings+=((annual_salary*saved_portion/10000)/12)+(savings*r/12)
    return float(savings)


def bisectional_best_rate(annual_salary,payment):
    epsilon=100
    low=0
    high=10000
    best_rate=(low+high)/2
    steps=0
    while abs(savings(annual_salary,best_rate)-payment)>=epsilon:
        if savings(annual_salary,best_rate)<=payment and steps<=30:
            low=best_rate            
        elif savings(annual_salary,best_rate)>=payment and steps<=30:
            high=best_rate
        else:
            break
        best_rate=(low+high)/2    
        steps+=1
    if abs(savings(annual_salary,best_rate)-payment)<=epsilon:
        return best_rate,steps
    else:
        return None,None
result,steps=bisectional_best_rate(annual_salary, payment)
if result is not None:
    print("Your initial annual salary is: ", annual_salary)
    print("The cost of your dream house is: ", total_cost)
    print(f"Best saving rate is: {result/10000:.4f}")
    print(f"The number of steps is: {steps}")
else:
    print("It is not possible for these parameters to have a saving rate")
    

