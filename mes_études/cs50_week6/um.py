import re
import sys

def main():
    print(count(input("Input:")))


def count(s):
    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    if match != None:
        return len(match)
    elif match == None:
        return 0

if __name__ == '__main__':
    main()

