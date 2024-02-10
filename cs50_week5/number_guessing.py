
import random 

### Two versions, one with main, second with command line
ascii_art ="""
    .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
    LGB      ||_.-.   ||_.-.
            (_.--__) (_.--__)

"""
def main():  
    while True:
        try:
            level = int(input("Level: "))
            target = random.choice(range(level))
            while True:
                try:        
                    guess = int(input("Guess: "))          
                    if guess < target:
                            print("Too small ")
                    elif guess == target:
                            print("That's it!", ascii_art, sep="\n")
                            break
                    elif level > guess > target: 
                         print("Too large")  
                    else:
                         print("Choose an integer under level")
                except ValueError:
                    print("Not an integer")
            break
        except ValueError:
            print("Not an integer")
if __name__ =='__main__':
     main()

#### WITH SYSTEM COMMAND-LINE

# import sys
# import random

# if len(sys.argv) != 2:
#     sys.exit()
# while True:
#     try:
#         level = int(sys.argv[1])
#         target = random.choice(range(level))
#         while True:
#             try:
#                 guess = int(input("Guess "))
#                 if guess < target:
#                     print("Too small!")
#                 elif guess > target:
#                     print("Too large!")
#                 elif guess == target:
#                     print(f"That's it! Number is {target}")
#                     break
#                 else:
#                     print("Choose an integer under level")
#             except (TypeError,ValueError):
#                 print("Not an integer")
#         break                
#     except (TypeError, ValueError):
#             print("Not an integer")        
        

