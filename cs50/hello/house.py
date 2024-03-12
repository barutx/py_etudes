name = input("What's your name?")
match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryffindor")
    case _:
        print ("who?")
        