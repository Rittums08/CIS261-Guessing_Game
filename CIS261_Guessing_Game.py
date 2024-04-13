import random

def display_title():
    print("Care for a game? Let's see if you are a Jedi!")
    print()

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking of a number between 1 and {limit}\n.")
    count = 1
    guess = int(input("What is your guess?:   "))
    
    while(guess != number):
        if guess < number:
            print("Hahaha! Too low, try again")
            count += 1
        elif guess > number:
            print("wow, and you thought you were a Jedi... Too High, try again")
            count += 1
        guess = int(input("Your guess?:  "))
    print(f"Wow, you guessed it and it only took you {count} tries.\n")
                         
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit: "))
        play_game(limit)
        again = input("Shall we have another go at it? Enter (yes/no)")
        print()
    print("I knew you did not have what it takes!")
   
if __name__ == "__main__":
    main()    