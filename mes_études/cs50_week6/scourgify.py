import sys
import csv

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()
elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()

data0 = []
with open(f"{sys.argv[1]}") as file0:
    reader = csv.DictReader(file0)
    for row in reader: 
        data0.append({"name": row["name"], "house": row["house"]})

names_splt = []
for i in range(len(data0)):
    names_splt.append(data0[i]["name"].split(","))

fieldnames = ["first", "last", "house"]   
with open(f"{sys.argv[2]}", "a") as file1:
    writer = csv.DictWriter(file1, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(len(names_splt)):
        writer.writerow({"first": names_splt[_][1], "last": names_splt[_][0] , "house": data0[_]["house"]})
