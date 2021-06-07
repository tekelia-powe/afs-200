import random
a = random.randint(1,9)
guess_list = []


name = input("Hi! Please enter your name: ")
print("Hi " +name+"! We are going to play a guessing game. I am thinking of a number from 1 to 9.")

guess = int(input("Please enter your guess: "))
while a != guess:
    if guess>a:
        print("Your guess is too high!")
        guess = int(input("Please enter your guess: "))
        guess_list.append(guess)
    elif guess<a:
        print("Your guess is too low!")
        guess = int(input("Please enter your guess: "))
        guess_list.append(guess)
print("Congratulations! You guessed it in "+str(len(guess_list))+" tries!")
