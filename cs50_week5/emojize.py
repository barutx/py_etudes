import sys
import emoji 

if len(sys.argv) != 2:
    sys.exit()

try:
    response = emoji.emojize(sys.argv[1])
except:
    sys.exit()  
print(response)
