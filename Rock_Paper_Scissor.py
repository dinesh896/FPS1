# Make a game of rock, paper scissors against the computer. 

"""
Problem
    Tell the user about the Game Instruction
    Tell user to enter either rock,paper or scissors
    Get the response from the user     
    Generate a random choice from (rock, paper, scissors)
    Compare user selection and computer selection
    Display who wins.
    Addition of Scorebard for complete round of Game 
     
Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score    
Hint
  Rock  vs paper   -> paper wins
  Rock  vs scissor -> Rock wins
  paper vs scissor -> scissor wins
"""
# Algorithm  
"""
Print the Game Instruction to the User/Player

Add Counters with zero initial value for no of times game played,
user & computer win counts.
    
Infinite Loop 
    Tell User to enter either Rock, Paper, Scissor
    Get the response from the User and use counter
    Print the response from the User
    
    Computer chooses randomly between Rock, Paper and Scissor
    Print computers choice
    Print User Choice and Computer Choice
        
    Decide the condition of wining according to the Game Instructions
        
    Compare the result with user and computer 
    Printing either user or computer wins and count the game winner
        
    Get the response from User to Play Again
    Check the response from User and continue the loop
    Othewise break the loop to close the game

Print a Thanks Message to the user and Scoreboard
"""

"""
Final Version
"""
# Print the Game Instruction to the User/Player 
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n") 
n = 0   # No. of times game played
u = 0   # No. of times user wins
c = 0   # No. of Computer user wins
while True:

    # Tell User to enter either Rock, Paper, Scissor    
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n") 
    
    while True:
        n =n+1 
        # Get the response from the User 
        user_choice = input("User turn: > ") 
        user_choice = user_choice.lower()
        
        if user_choice not in ['rock','paper','scissor']:
            print ("Wrong input, please input again: ")
        else:
            break
 
    # Print the response from the User 
    print("User has choosen : " + user_choice + "\n") 
    

    
    # Computer chooses randomly between Rock, Paper and Scissor
    import random
    comp_choice = random.choice(['rock','paper','scissor']) 

    # Print computers choice
    print("Computer choice is: " + comp_choice + "\n") 
  
    # Print User Choice and Computer Choice
    print("\t" + user_choice + "\n V/s \n" + "\t"+ comp_choice) 
    

    # Decide the condition of wining according to the Game Instructions
    result = None
    
    if((user_choice == "rock" and comp_choice == "paper") or
      (user_choice == "paper" and comp_choice == "rock" )): 
        result = "paper"
    elif((user_choice == "rock" and comp_choice == "scissor") or
        (user_choice == "scissor" and comp_choice == "rock")): 
        result = "rock"
    else: 
        result = "scissor"
    
    # Compare the result with user and computer 
    # Printing either user or computer wins  
    if (user_choice == comp_choice): #additional
        print("<== Draw ==>")
#        x = x+1
    elif (result == user_choice): 
        print("<== User wins ==>") 
        u = u+1
    else: 
        print("<== Computer wins ==>") 
        c = c+1
    # Get the response from User to Play Again    
    ans = input("Do you want to play again ? (Y/N) > ") 
    ans = ans.lower()  
    # Check the response from User and continue the loop
    # Otherwise break the loop to close the game
    if ans == 'n': 
        break
        
# Print a Thanks Message to the user
     
print("\nThanks for playing Rock Paper Scissor Game")
print("\n***** SCORE BOARD *****")   
print("Game played:",n,"times")
print("Draw:",n-u-c,"times")
print("User Wins:",u,"times")
print("Computer Wins:",c,"times")
print("***********************")  