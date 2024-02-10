import random

def main():
    level = get_level()
    generate_integer(level)


def get_level():    
    while True:
        try:
            level = int(input("Pick up your level(1-3): "))
            if level in range(1,4):
                return level                
            elif level > 3 or level < 1:
                raise ValueError ("Not in range")
        except (TypeError):
            print("Not an integer")
        break

def generate_integer(level):
    if level == 1:
        for i in range(10):                    
            X = random.randint(1,9)
            Y = random.randint(1,9)
            correct_answer = X + Y 
            while True:
                try:
                    user_answer = int(input(f"{X} + {Y} = "))
                    if user_answer == correct_answer:
                        print("Congrats!!" + ascii_art)     
                        break
                    else:
                        print("EEE")
                except(TypeError):
                    print("Not an integer")
    elif level == 2:
        for i in range(10):
            X= random.randint(10,99)
            Y= random.randint(10,99)
            correct_answer = X + Y 
            while True:
                try:
                    user_answer = int(input(f"{X} + {Y} = "))
                    if user_answer == correct_answer:
                        print("Congrats!!" + ascii_art)     
                        break
                    else:
                        continue
                except(TypeError):
                    print("Not an integer")
    elif level == 3:
        for i in range(10):
            X = random.randint(100,999)
            Y = random.randint(100,999)
            correct_answer = X + Y 
            while True:
                try:
                    user_answer = int(input(f"{X} + {Y} = "))
                    if user_answer == correct_answer:
                        print("Congrats!!" + ascii_art)     
                        break
                    else:
                        continue
                except(TypeError):
                    print("Not an integer")
















global ascii_art
ascii_art = """
                                sexsexsexsexsexse
                              sexsesexsexsexsexsexs
                             sexsexsexsexsexsexsexse
                           sexsexsexsexsexsexsexsexsex
                         sexsexsexsexsexsexsexsexsexsex
                        sexsexsexsexsexsexsexsexsexsexs
                       sexsexsexsexsexsexsexsexsexsexsex
                      sexsexsexsexsexsexsexsexsexsexsexse
                     sexsexsexsexsexsexsexsexsexsexsexsex
                     exsexsexsexsexsexsexsex  sexsexsexsex
                    sexsexsexsexsexsexsexs     sexsexsexse
                    sexsexsexsexsexsexsex        sexsexsex
                    sexsexsexsexsexsex            sexsexsx
                    sexsexsexsexsexx              sexsexs x
                    sexsexsexsexsex-****.    .***-sexsexs sexs
                    sexsexsexsexsex               sexsex sexsexs
                    sexsexsexsexsex              sexsex sexsexsexs
                    sexsexsexsexsex              sexse sexsexsexse
                    sesexsexsexsexs   --sexsex- sexse sexsexsexse
                    xsexsexsexsexse      sexs  sexse sexsexsexs
                   sexsexsexsexsexse         sexse sexsexsexse
                 sexsexsexsexsexsexs       sexse    sexsexse
                sexsexse      sexsexs      ixx       sexse
                sexsex         sexsexs     i         sex
                sexs            sexsexs    i         x
                sex              sexsex        x   x
                 x               sexsex        x  x
                x                sexse          xx
              sex                sex                x
            sexsexs             xx                     x
           sexsexsex    x x                  x           x
         sexsexsexsexse                       x          (o
       sexsexsexsexse       x                            x
     sexsexsexsexse   x     x         (o)      x        x
   sexsexsexsexse     x      x                 x       x
  sexsexsexsex        x       x               x      x
sexsexsexsex          x        x             x    xx
sexsexsexse           x         x          x      x
 sexsexsexse           x           x x  x         x
   sexsexsexs          x                          x
    sexsexsexs          x                        x
     sexsexsex           x                       x
      sexsexsex           x                     x
       sexsexsex           x                    x
         sexsexse            x                 x
          sexsexse            x                x
            sexsexs           x                 x
              sexsex sexsexse x                  x
               sexsexsexsexsexs                   x
                 sexsexsexsexse                     x
                  sexsexsexsex               o       x
                       sexsex                        x
                        x                             x
                       x                              x
                      x                               x
                      x                      Y        x
                      x                      x        x
                      x                       x       x
                      x                        x      x
                      x                 sexsexsex     x
                      x            sexsexsexsexsx exsex
                      x          sexsexsexsexsexs sexx
                       x       sexsexsexsexsexsexs xx
                        x     sexsexsexsexsexsexse x
                         x   sexsexsexsexsexsexsexs
                          x sexsexsexsexsexsexsexse
                            sexsexsexsexsexsexsexsex
                             sexsexsexsexsexsexsexse
                            x sexsexsexsexsexsexsexs
                            xx sexsexsexsexsexsexsexs
                            sex sexsexsexsexsexsexsex
                             sex sexsexsexsexsexsexse
                             sexs sexsexsexsexsexsexs
                              sexse sexsexsexsexsexse
                              sexsex sexsexsexsexsexse
                               sexsex sexsexsexsexsexs
                               sexsexs sexsexsexsexsex
                                sexsexs sexsexsexsexse
                                sexsexse sexsexsexsexs
                                sexsexsex sexsexsexsex
                                sexsexsexs  sexsexsexse
                                sexsexsexs  sexsexsexse
                               sexsexsexse   sexsexsexs
                               sexsexsexs    sexsexsexse
                              sexsexsexse    sexsexsexse
                             sexsexsexse     sexsexsexse
                            sexsexsexse      sexsexsexs
                            sexsexsexse     sexsexsexse
                           sexsexsexsex     sexsexsexse
                           sexsexsexsex     sexsexsexse
                           sexsexsexsex     sexsexsexsex
                           sexsexsexse      sexsexsexsex
                           sexsexsexse      sexsexsexsex
                            sexsexsexs      sexsexsexsex
                            sexsexsexs       sexsexsexse
                            sexsexsex        sexsexsexse
                             sexsexse         sexsexsexs
                             sexsexse          sexsexsex
                              sexsexs           sexsexse
                              sexsex             sexsexs
                              sexsex              sexsexs
                              sexsex               sexsex
                               exsex                sexse
                              sexsex                sexsex
                              sexsex                sexsex
                              sexsexs               sexsexx
                             sexsexsex             sexsexse
                            sexsexsexse          sexsexsexse
                            sexsexsexsexs        sexsexsexsex
                            sexsexsexsexse       sexsexsexsex
                              sex    sexsexsex    sexsexsexsex
                               x        sexsexse   xx sexsexse
                                                   x    sexsex
                                                         sexse
                                                         sexse
                                                         sexse
                                                           sex
                                                            xx
                                                            xx






""" 



if __name__=="__main__":
    main()