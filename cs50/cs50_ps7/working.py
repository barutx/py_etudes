import csv
import re
import sys

def main():
    print(convert(input("Hours: ")))




def convert(s):
    s = re.sub(r"[0](?=[1-9])","",s )
    s = re.sub(r"(?<=[1-9])\s",":00 ",s )

    if matches := re.search(r"^((?:[0-1]?[0-9])\s?(?:\:[0-5][0-9])?\s*?(?:AM|PM))\s*to\s*([0-1]?[0-9]\s*(?:\:[0-5][0-9])?\s*(?:AM|PM))$", s):
        pass
    else:
        return ("Expression does not match")
    conversion=[]
    first = matches.group(1)
    second = matches.group(2)

    with open("hours.csv") as hours:
        reader = csv.DictReader(hours)
        for row in reader:
            conversion.append({row["12-Hour"]:row["24-Hour"]})    
    for i in conversion:
        if i.get(first) != None:
            first = i.get(first)
        if i.get(second) != None:
            second = i.get(second)

    return f"{first} to {second}"


        


if __name__ == '__main__':
    main()