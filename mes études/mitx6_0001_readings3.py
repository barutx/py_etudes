#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:34:33 2024

@author: barut
"""

#### FUNCTIONS #### 

def max(x, y) :
    if x > y:
        return x
    else:
        return y
### THE SEQUENCE OF NAMES (X,Y) ARE COLLED FORMAL PARAMETERS
### WHEN THE FUNCTION IS CALLED, FORMAL PARAMETERS ARE BOUND TO ACTUAL PARAMETS OR ARGUMENTS.
### A FUNCTION CALL IS AN EXPRESSION, AND LIKE ALL EXPRESSIONS IT HAS A VALUE.
### THAT VALUE IS THE VALUE RETURNED BY THE INVOKED FUNCTION.
#### IF NO EXPRESSION FOLLOWS THE RETURN OR THERE ARE NO STATEMENTS TO EXECUTE, THE VALUE OF INVOCATION IN None.

### Write a function isIn that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other, and False
# otherwise. Hint: you might want to use the built-in str operation in.

def isIn(x ,y):
    if str(x) in str(y) or str(y) in str(x):
        return True
    else:
        return False

isIn("selam", "aselam")

##### POSITIONAL ARGUMENTS... FIRST FORMAL PARAMETER BOUND TO THE FIRST ACTUAL, THE SECOND IS TO THE SECOND ETC.
##### KEYWORD ARGUMENTS... FORMALS ARE BOUND TO ACTUALS USING THE NAME OF THE FORMAL PARAMETER.

def  printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ',' + firstName )
    else:
        print (firstName, lastName)
printName('Olga', 'ACıdere', False)
printName('Olga', 'Acıdere', reverse = False)
printName(lastName='Acıdere',firstName='Olga',reverse=False)

#### They will all print out the same thing.
#### KEYWORD ARGUMENTS CAN APPEAR IN ANY ORDER, BUT A KEYWORD ARGUMENT CANNOT BE FOLLOWED BY A NON-KEYWORD ARGUMENT:
printName('Olga', lastName = 'Acıdere', False) ### PRODUCES ERROR RIGHT?

### KEYWORD ARGUMENTS ARE COMMONLY USED IN CONJUCTION WITH DEFAULT PARAMETER VALUES. WE CAN WRITE :
def printName(firstName, lastName, reverse = False):
    if reverse:
        print (lastName + ',' + firstName )
    else:
        print (firstName, lastName)
     ### DEFAULT VALUES ALLOW US TO CALL A FUNCTION WITH FEWER ARGUMENTS :
printName('Olga', 'Acıdere')
printName('Olga', 'Acıdere', True)
printName('Olga', 'Acıdere', reverse = True)


#### SCOPING #####
# At top level, i.e., the level of the shell, a symbol table keeps track of all names defined at that level and
# their current bindings.
# When a function is called, a new symbol table is called (a stack frame). This table keeps track of all names
# defined within the function (including the formal parameters ) and their current bindings. If a function is called
# from within the function body, another stack frame is called to that effect.

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g 
x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()

### CONSIDER THIS EXAMPLE for scope:
def f():
    print (x)
def g():
    print (x)
    x = 1
x = 3
f()
x = 3
g()

######  SPECIFICATION OF A FUNCTION CAN BE GIVEN:
def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
        epsilon > 0 & power >= 1
        Returns float y such that y**power is within epsilon of x."""
        if x < 0 and power%2 == 0:
            return None
            low = min(-1.0, x)
            high = max(1.0, x)
            ans = (high + low)/2.0
        return ans
        
    
#########    ITERATIVE AND A RECURSIVE IMPLEMENTATION OF FACTORIAL: 
def factI(n):
    """
    Assumes that n is an int > 0
    Returns n! """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    """
    Assumes that n is an int > 0
    Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n-1)
    
###### USING A GLOBAL VARIABLE ######

def fib(x):
    """Assumes x an int >= 0
    Returns Fibonacci of x"""
    global numFibCalls 
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print ('fib of', i, '=', fib(i))
        print ('fib called', numFibCalls, 'times.')

testFib(30)
 
#### Apparently, the piece of code above takes many steps, we can use MEMOIZATION BY STORING RESULTS IN DICT !!!
def fib(x, memo = {}):
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1 
    elif x in memo:
        return memo[x]
    else:
        result = fib(x-1, memo) + fib(x-2, memo)
        memo[x] = result
        return result
def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print ('fib of', i, '=', fib(i))
        print ('fib called', numFibCalls, 'times.')
        
testFib(30)
        
        
        
        
        
        
        
        




