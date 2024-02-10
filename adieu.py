
import sys
import inflect
p = inflect.engine()

def main():    
    if len(sys.argv) >= 1:
        names=[]
        while True:
            try:                                   
                names.append(input("Name?: "))        
            except EOFError:
                mylist= p.join(names)
                
                print("Adieu, adieu to ",end=" ")  
                
                print(mylist.title())
                
                sys.exit()
    else:
        sys.exit()

if __name__=="__main__":
    main()






