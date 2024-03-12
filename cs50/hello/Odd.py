###Finger exercise: Write a program that asks the user to input 10 integers, and
###then prints the largest odd number that was entered. If no odd number was
###entered, it should print a message to that effect.
def main():
    i = 0
    integers = []
    while i < 5:
        integers +=[int((input(f"{i+1}. integer = " )))]
        i= i + 1
    largest_odd = find_largest(integers)
    if largest_odd is not None:
         print(f"The largest odd is {largest_odd} ")
    else:
         return None
    
def is_odd(n):
        return n%2 == 1
def find_largest(integers):
     odd_numbers = [ints for ints in integers if is_odd(ints)]
     if odd_numbers:
          return max(odd_numbers)
     else:
          return None
main()

#####Finger exercise: Write a program that examines three variables—x, y, and z—
#### and prints the largest odd number among them. If none of them are odd, it
#### should print a message to that effect.     
def main():
    variables = [int(input(f"What's {var}? ")) for var in ['x', 'y', 'z']]
    largest_odd = find_largest_odd(variables)

    if largest_odd is not None:
        print(f"The largest odd number is: {largest_odd}")
    else:
        print("None of them is odd")


def is_odd(a):
    return a % 2 == 1

def find_largest_odd(variables):
    odd_numbers = [var for var in variables if is_odd(var)]

    if odd_numbers:
        return max(odd_numbers)
    else:
        return None
main()

###########
def main():
    i = 0
    integers = []
    largest_odd = None

    while i < 10:
        num = int(input(f"{i + 1}. integer = "))
        integers += [num]

        if num % 2 == 1 and (largest_odd is None or num > largest_odd):
            largest_odd = num

        i += 1

    print("Entered integers:", integers)

    if largest_odd is not None:
        print(f"The largest odd number is: {largest_odd}")
    else:
        print("No odd number was entered")
main()
