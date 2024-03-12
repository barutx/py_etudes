#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:10:10 2024

@author: barut
"""

######EXHAUSTIVE ENUMERATION########
##### The code below prints the integer cube root, if it exists, of an integer.
# If the input is not a perfect cube, it prints a message to that effect.

#Find the cube root of a perfect cube:
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print (x, 'is not a perfect cube')
else: 
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)

##### WHENEVER WE WRITE A LOOP, A DECREMENTAL FUNCTION MUST BE THERE:
    # 1.IT MAPS A SET OF PROGRAM VARIABLES INTO AN INTEGER
    # 2. WHEN THE LOOP IS ENTERED, ITS VALUE IS NONNEGATIVE
    # 3. WHEN ITS VALUE IS <=0 LOOP TERMINATES.
    # 4 ITS VALUE IS DECREASED EVERY TIME THROUGH THE LOOP
    # THE DECREMENTING FUNCTION FOR THE LOOP ABOVE IS : abs(x) - ans**3
### THIS ALGORITHMIC TECHNIQUE IS A VARIANT OF GUESS AND CHECK CALLED EXHAUSTIVE ENUMERATION.
### WE ENUMERATE ALL POSSIBILITIES UNTIL WE GET TO THE RIGHT ANSWER OR EXHAUST THE SPACE OF POSSIBILITIES.

#### IT TAKES A NANOSECOND TO EXECUTE AN ORDER (LIGHT TRAVELS ONE METER FOR MORE THAN A NANOSECOND)
## JUST FOR FUN TRY: 
max = int(input("An integer: "))
i = 0
while i < max:
    i = i + 1
print (i)

# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

def get_root_power(integer):
    root_pwr = {}
    for root in range(abs(integer) + 1):
        for pwr in range(1,6):
            if root ** pwr == integer:
                pwr = root_pwr.get(root,pwr)
                root_pwr[root] = pwr
    if len(root_pwr) != 0:
        return root_pwr
    else:
        return None

if __name__ == "__main__":
    user_input = int(input("Give a fucking integer: "))
    result = get_root_power(user_input)
    
    if result:
        for i in result.keys():
            pw = result[i]       
            print (f"Root: {i}, Power: {pw} ")
    else:
        print("No such pairs of integers exist")

######### FOR LOOPS and RANGE #######3
#### We use for loops and range function which returns a sequence containing an arithmetic progression.
#range(5, 40, 10) = [5, 15, 25, 25]
#range(40, 5, -10)= [40, 30, 20, 10]
#range(0,3) = range(3)

### Think about the code
x = 4
for i in range (0, x):
    print (i) 
    x = 5
##Whether changing the value of x inside the loop affects the number of iterations? IT DOES NOT CHANGE.
## RANGE FUNCTION IN THE LINE IIN THE LINE WITH FOR IS EVALUATED JUST BEFORE THE FIRST ITERATION OF THE LOOP

x = 4
for j in range(x):
    for i in range(x):
        print (i) 
        x = 2
### FOR THAT ONE, OUTER LOOP IS EVALUATED ONLY ONCE, KEEPING X = 4, BUT INNER LOOP IS REEVALUATED EACH TIME
# ENDORSING THE VALUE X = 2, SO THE RESULT IS 0 1 2 3 0 1 0 1 0 1

#### FOR THE SAME EXAMPLE OF CUBE ROOT :
x = int(input('Enter an integer:'))
for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != (x):
        print (x, 'x is not a perfect cube')
else:
    if x < 0:
        ans = -ans
        print ("Cube root of", x, 'is, ans')
    
###  FOR LOOP CAN BE ALSO USED TO ITERATE OVER CHARACTERS OF STRING ? ## I did not know that
total = 0 
for c in '123456789':
    total += int(c)
print (total)


# #######   Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
# the sum of the numbers in s.


def get_numbers(s):
    numbers = s.split(',')
    
    total_sum = sum(float(number) for number in numbers)
    return total_sum

s = '1.23, 2.4, 3.57, 4.36, 8.27, 9.18'
result = get_numbers(s)
print (f"the sum of numbers {s}: {result}")


######   APPROXIMATING ######
x = 12
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0
ans = 0.0
while abs((ans**2)-x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print ('numGuesses = ', numGuesses)
if abs((ans**2) - x) >= epsilon:
    print('Failed on square rooth of', x)
else: 
    print (f"{ans:.2f}", 'is close to square root of', x)
    

# LEZ GO FOR BISECTION SEARCH METHOD

x = 25
epsilon = 0.01
numGuesses= 0
low = 0
high = x
ans = (high+low)/2
while abs((ans**2)-x) >= epsilon:
    print('low =',low, 'high =', high, 'ans = ', ans)
    numGuesses += 1
    if abs(ans**2 < x ):
        low = ans
    else:
        high = ans
    ans = (high+low)/2
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x) 

#### THERE IS A FINGER EXERCISE TO MODIFY THE CODE ABOVE SO THAT IT PRINTS FOR NEGATIVE AND POSITIVE VALUES BUT I PASS THAT FOR THE MOMENT.

###  BELOW CODE TO CLARIFY ON FLOATS:
x = 0.0
for i in range(10):
    x += 0.1
if x == 1.0:
    print(x, '=1.0')
else: 
    print(x, 'is not 1.0')
#### X NEVER CAN BE EQUAL EXACTLY TO 1.0, BECAUSE OF THE WAY DECIMAL NUMBERS ARE REPRESENTED IN BINARY FORMS
x = 0.0
for i in range(10):
    x += 0.1
if x == 1.0:
    print(x, '=1.0')
else: 
    print(x == 10.0 * 0.1)
#### ABOVE CODE WILL PRINT FALSE BECAUSE ... ADDING TEN TIMES 0.1 IS NOT EQUAL TO MULTIPLYING 0.1 BY 10
#### WE CAN EXPLICITLY USE ROUND FUNCTION WHICH IS... ROUND(X, numDigits) so:
round(2 ** 0.5, 3)
### It gives us square root of 2, rounded to 3 step decimal number.
####  THIS IS IMPORTANT BECAUSE TWO FLOATING NUMBERS MAY NOT BE EQUAL TO ONE ANOTHER SO: 
# (x-y) < 0.0001 rather than  x == y

### NEWTON-RAPHSON APPROXIMATION METHOD FOR SQUARE ROOT:
    ## FIND X SUCH THAT X**2 - 24 IS WITHIN EPSILON OF 0
epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess- (((guess**2) - k)/(2*guess))
print ('Square root of', k, 'is about', guess)
#### LET'S ADD A COUNTER FOR THE NUMBER OF STEPS TO ABOVE CODE 
epsilon = 0.01
k = 24.0
guess = k/2.0
step = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2)- k)/(2*guess))
    step += 1
print ('Square root of', k, 'is about', guess)
print('Steps= ', step)
#### ABOVE CODE PROVES THAT NEWTON-RAPHSON METHOD IS MORE EFFICIENT IN FINDING THE SQUARE ROOT. 













