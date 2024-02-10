import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
list_fonts = figlet.getFonts()
try: 
    if len(sys.argv) == 1:
        s = input("Your string: ")
        f = random.choice(list_fonts)
        figlet.setFont(font=f)
        print(f"{f}" , figlet.renderText(s), sep='\n')  ## Set the font before rendering test

    elif len(sys.argv) == 3:
        if (sys.argv[1] != '-f'):
            print(sys.argv[1], end=" ")
            print("Command not found")
            sys.exit()
        elif sys.argv[2] not in list_fonts:
            print("Font not found")
            sys.exit()
        s = input("Your string: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))  
except: 
    print("Invalid input")
    sys.exit()