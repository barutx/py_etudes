def main():
    x= float(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return round(n * n, 3)
main()
