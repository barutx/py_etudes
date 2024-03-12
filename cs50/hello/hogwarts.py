##### Write a program that examines three variables—x, y, and z—
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.

# def main(): 
    x=int(input("What's x? "))
    y=int(input("What's y? "))
    z=int(input("What's z? "))
    if is_odd(x) and is_odd(y) and is_odd(z):
            print(max(x,y,z))
    elif is_odd(x) and is_odd(y):
            print(max(x,y))
    elif is_odd(y) and is_odd(z):
          print(max(y,z))
    elif is_odd(x) and is_odd(z):
          print(max(x,z))
    elif is_odd(x):
        print(x)
    elif is_odd(y):
          print(y)
    elif is_odd(z):
        print(z)
    else:
        print("None of them is even")
# def is_odd(a):
    return a%2==1
#main()
    
    

  