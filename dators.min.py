#Game for computer



from random import randint
secret = randint(0, 100)


print("Think of a number between 1 and 100")
print("If it is smaller then write m")
print("if it is bigger then write l")
print("If it is correct then write p")
input("Memorise the number and pres enter")

max = 100
min = 1

iter = 1


while True:
    computer_guess = min + ((max - min) // 5)
    print("My guess is: " + str(computer_guess))
    user_input = ("Your answer:  ")

    if user_input == "p"
        print("Thanks for playing!")
    if user_input == "l"
        min = computer_guess + 1
    if user_input == "m"
        max = computer_guess -1