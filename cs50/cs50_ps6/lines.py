import sys 
print(len(sys.argv))
if len(sys.argv) > 2 :
    print("Too many command line arguments")
    sys.exit()
elif len(sys.argv) < 2 :
    print("Too few arguments")
    sys.exit()
try:
    with open(f"{sys.argv[1]}") as file:
        lines = file.readlines() 
except (FileNotFoundError, IndexError):
    print("File not found, try another")
    sys.exit()

number_lines = 0
for line in lines:
    line = line.lstrip()
    if line.startswith("#"):        
        continue
    elif line == '':
        continue
    else:
        number_lines += 1
print(f"Number of lines in your programme number: {number_lines}")

