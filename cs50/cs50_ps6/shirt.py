import sys
from PIL import Image, ImageOps
import os



def is_valid_extension(file_name):
    valid_extensions = [".jpg", ".jpeg", ".png"]
    _,extension = os.path.splitext(file_name)
    return extension.lower() not in valid_extensions

def get_extension(file_name):
    _,extension = os.path.splitext(file_name)
    return extension.lower()

if len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many arguments")

if is_valid_extension(sys.argv[1]) or is_valid_extension(sys.argv[2]):
    print("Invalid format.")
elif get_extension(sys.argv[1]) != get_extension(sys.argv[2]):
    print("Input format does not match output format")

try:   
    with Image.open(f"{sys.argv[1]}") as serlok:
        shirt =  Image.open("shirt.png")
        serlok = ImageOps.fit(serlok,size=shirt.size)
        serlok.paste(shirt,shirt)
        serlok.show()
        serlok.save(f"{sys.argv[2]}")
except FileNotFoundError:
    print("File could not be found")
    sys.exit()