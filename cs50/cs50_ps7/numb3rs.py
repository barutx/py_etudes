import re
import sys

def main():
    print(validate(input("IPv4 Adress: ")))

def validate(ip):
    if match := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for i in match.groups():
            if int(i) > 255:
                print("Not a valid IPv4 adress")
                return False
        return ip    

if __name__ == "__main__":
    main()