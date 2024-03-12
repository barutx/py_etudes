for _ in range(3):
    print("#")

#####instead
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
main()

####another version of print_column
def print_column(height):
    print("#\n" * height, end="")

###### for the coin, horizontal bricks
def main():
    print_row(4)

def print_row(width):
    print("?" * width)
main()

###### if it was a block of squares like the walls in mario
def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each break in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()
main()
######instead of nesting loops we can
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#"* (size))
main()
