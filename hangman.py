# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # step1: import external libraries
    # Step2: make a list of words

    # Step3: Show message to start the game or quite. This should be a loop.

    # Step4: pick a random word

    # Step5: add condition of win or loose
    # Step6: draw  spaces,  draw guessed letters, spaces and strikes
    # Step7: take guess
    # Step8: Check the input from user for boundary conditions
   
    # Step9: print out win / lose
    # Step10: Print the right word if player looses

"""
#####################
#   FInal Version   #
#####################

# Step1: import external libraries
import random 

# Step2: make a list if word
#words = ['orange','lime','lemon','melon','grape','mango']

words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

# find length of biggest word
n=0
for item in words:
    m=len(item)
    if(m>n):
        n=m
print("length of biggest word is:",n)  

    #Step 3
while True:
    start = input("Press enter / return to start, or enter Q to quit")
    if start.lower() == 'q':
        break

    #Step4: pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
        
    #Step5: add contition of win or loose
    
    
    while len(bad_guesses) < n+1 and len(good_guesses) != len (list( secret_word)):
        # Step 6: draw  spaces
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
            else:
                print('_', end=' ')
                #print ('')

        print('\nStrikes : {} /'.format(len(bad_guesses)),n+1)

        print ('')

        # Step 7: take guess
        guess = input ("Guess a letter : ").lower()

        # Step8: Check the input from user for boundary conditions
        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        
        # Step9: print out win / lose

        if guess in secret_word:
            good_guesses.append(guess)

        if len (good_guesses) == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break
        else:
            bad_guesses.append(guess)
    
    else:   # else for the while, if you win, it will never be executed
        print ("You didn't guess it: my secret word was {}". format(secret_word))
