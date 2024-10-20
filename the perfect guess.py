#we are going to write a program that generates a random number and ask the user to guess it. 
# if the player's guess is higher than the acutal number, the program displays "lower number please". Similarly, if the user's guess is too low, the program prints "higher number please", when the user guess the number correctly the program displays the number of gusses reuqired to guess the number 
#hint use random modules.
import random
n = random.randint(1,100)
a = -1
guesses = 0 
while (a != n ):
    guesses += 1
    a = int(input ("enter the number please"))
    if (a>n):
        print("lower number please")
    else:
        print("higher number please")

print(f'you have guessed the number i.e. {n} corretly in {guesses}')
