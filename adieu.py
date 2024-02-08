
import sys
import inflect
p = inflect.engine()
global names
names=[]
def main():
    global names
    names=[]
    if len(sys.argv) >= 1:
        try:
            name_list = ["Name:" for i in range(0,5)]                       
            names = names.append([input(f"{name} ") for name in name_list])         
        except EOFError:
            mylist= p.join(names)
            print("Adieu, adieu to ", end=" ")  
            print(mylist)
            
            sys.exit()
    else:
        sys.exit()

if __name__=="__main__":
    main()






