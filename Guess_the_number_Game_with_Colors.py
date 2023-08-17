import random
from colorama import init, Fore, Back,Style

init() # Initialize colorama

def guess_the_number():
    print("Welcome to " + Fore.CYAN + Back.GREEN + "Guess a Number!" + Style.RESET_ALL)
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    life_line = 5
    
    while True:
        guess = int(input("Take a guess: "))
        if guess > 0 and guess < 101:
            attempts += 1
        
            if guess < secret_number:
                print(Fore.YELLOW + "Too low. Try again!")
                #print("Life Line Left:",life_line)
                life_line -=1
                print("Life Line Available Now:",life_line)
                if life_line == 0:
                    print("Game Over!!!")
                    print("Secret Number: ", secret_number)
                    break
            elif guess > secret_number:
                print(Fore.YELLOW + "Too high. Try again!" + Style.RESET_ALL)
                #print("Life Line Left:",life_line)
                life_line -= 1
                print("Life Line Available Now:",life_line)
                if life_line == 0:
                    print("Game Over!!!")
                    print("Secret Number: ", secret_number)
                    break
            else:
                print(Fore.GREEN + f"Congratulations! You guessed the number in {attempts} attempts!" + Style.RESET_ALL)
                life_line += 1
                print("Available Life Lines are: ", life_line)
                
        else:
            print("Please choose number between 1-100 ....")
            
guess_the_number()