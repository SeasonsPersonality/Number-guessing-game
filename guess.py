import random

print("Select your range of numbers to start the game")


#get numbers from user
lower_num = int(input("Enter the lower number: "))
upper_num = int(input("Enter the upper number: "))
if upper_num < lower_num:
    raise ValueError("Please run again and enter a number greater than your first choice")
#make a random number from random library
random_num = (random.randint(lower_num , upper_num + 1))

count = 0
while True:
    # user guess
    guess = int(input("What is your guess? "))
    if guess == random_num:
        count += 1
        print("Congratulations! you did it in",count,"try.")
        #print(f"{count}")
        ask = input("Do you want to keep playing?(Y/N) ",)
        if ask == 'Y':
            # get numbers from user
            lower = int(input("Enter the lower number: "))
            upper = int(input("Enter the upper number: "))
            # make a random number from random library
            random_num = (random.randint(lower, upper + 1))
            continue
    if guess > random_num:
        print("Try again! You guessed too hight")
    elif guess < random_num:
        print("Try again! you guessed too small")
    else:
        print("Better Luck Next Time")
