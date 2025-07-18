from random import randint
guesses =5
print("SIMPLE NUMBER GUESSING GAME")
print("GUESS THE CORRECT NUMBER IN 5 GUESSES")
answer = randint(1,50)
while guesses !=0:
    guess =int(input("Enter your guess between 1-50: "))
    if guess != answer:
        print("WRONG GUESS!  TRY AGAIN......")
        # print(answer)
        if answer < guess:
            print("YOUR GUESS IS GREATER")
            print("___________________________________")
        else:
            print("YOUR GUESS IS SMALLER")
            print("___________________________________")
        guesses =guesses-1
        if guesses == 0:
            print("YOU ARE OUT OF GUESSES......")
    else:
        print("YOU GUESSED IT CORRECTLY ....... CONGRATS")