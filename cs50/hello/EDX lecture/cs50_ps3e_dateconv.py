# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    months= [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]  
    
    
    while True:      
           try:
               date_input = input("Date in the following format {}/{}/{} or {} {}, {} : ".format("MM","DD","YYYY","January", "1", "2024"))
               date_parts = date_input.split("/") if "/" in date_input else date_input.split("")
               if len(date_parts) == 3:
                   m,d,y = map(int, date_parts)
                   if 1<=m<=12 and 1<=d<=31 and y>=0:
                        formatted_numbers(m,d,y)
                        break
               elif date_parts[0] in months:
                    number_month = date_parts[0]
                    m = months.index(number_month) + 1
                    d = int(date_parts[1].removesuffix(","))
                    y = int(date_parts[2])
                    formatted_numbers(m,d,y)
                    break
           except(KeyError,EOFError,ValueError):
                   pass         
                                              
def formatted_numbers(m,d,y):
        m = "{:0>2}".format(m)
        d = str(d).zfill(2) 
        y = "{:0>4}".format(y)
        print (f"{y}-{m}-{d}")
main()

