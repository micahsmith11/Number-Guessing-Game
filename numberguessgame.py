import random
print("Welcome to the Number Guessing Game! What is the lowest possible number you want in your game?")
a = int(input())
print("What is the highest possible number that you want in your game?")
x = int(input())
correct_number = random.randint(a, x)
#correct_number = 56
attempts_number = 1
print("Guess the number between " + str(a) + " and " + str(x)) 
number_Guess = int(input())
if number_Guess == correct_number:
	print("correct it took you " + str(attempts_number) + " time to solve")
else:
	while number_Guess != correct_number:
            if number_Guess > correct_number:
                    print("too high")
                    attempts_number += 1
            elif number_Guess < correct_number:
                attempts_number += 1
                print("too low")
            number_Guess = int(input())
            if number_Guess == correct_number:        
                print("correct it took you " + str(attempts_number) + " times to solve")    