import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2 :
    print("Too few command-line arguments ")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit()
menu = []
try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append({"pizza": row["pizza"], "size0": row["size0"], "size1": row["size1"]})
except FileNotFoundError:
    print("Not a CSV file")
    sys.exit()
print(tabulate(menu, tablefmt="heavy_grid",headers="firstrow"))