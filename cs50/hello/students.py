##LISTS##
students = ["Hermione", "Harry", "Ron"]
print(students[0])
#square bracket inside the list enables us to index into the list
#lists are zero indexed
students=["Hermione","Harry","Ron"]
for student in students:
    print(student)

students=["Hermione","Harry","Ron"]
for i in range(len(students)):
    print (i+1, students[i]) 
# i+1 is for ranking starting from 1

###DICTIONARIES##### in addition to str, int, floating points, bools
studentss={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron": "Gryffindor",
    }
for student in studentss:
    print(student)
##### for student iterates over a dictionary, iterates over all keys
##### so what we can do:
studentss={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron": "Gryffindor",
    }

for student in studentss:
        print(student, studentss[student],sep=", ")
####### for the sake of discussion, each student has a patronus
        #making each student a dictionary, so we list dictionaries.

studentz=[
     {"name":"Hermione", "house":"Gryffindor","patronus":"Otter"},
     {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
     {"name": "Draco", "house":"Slytherin", "patronus":None}]
for student in studentz:
     print(student["name"], student["house"], student["patronus"], sep=", ")


