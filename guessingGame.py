import random 

print("Number Guessing Game")
number=random.randint(1,9)

chances=0
print("guess a nummber (between 1 and 9):")

while chances < 5:
    guess=int(input("Enter your guesses:- "))

    if guess==number:
        print("Congratulations You WON!!")
        break
    elif guess < number:
        print("Your guess was low :Guess a number higher then that" ,guess)
    else:
        print("Your guess was high :Guess a number lower then that" ,guess)  

chances += 1
if not chances < 5:
    print("You Loose!! The number is",number)
  