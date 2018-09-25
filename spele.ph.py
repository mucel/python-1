from random import randint
secret = randint(0, 100)
minejums = -1 #kaut kas tads, kas nav iespejams ka secret


while minejums  != secret:
    secret = 45
    minejums = int(input("Ludzu miniet skaitli: "))

    if secret > minejums:
        print("Istais skaitlis ir liekaks")
    elif secret < minejums:
        print("Istais skaitlis ir mazaks")
    else:
        print("Apsveicu, skaitlis ir pareizs!")