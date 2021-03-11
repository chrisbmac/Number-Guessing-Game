
import random
import time
import threading


# initial output of program to display random number to guess along with game name
def initial():

   #generate random num 1-100 and assign to num_toGuess
   num_toGuess = random.randint(1,100)
   print("-------------------------------------------")
   print("If at anytime you wish to end the game just type, end")
   print("%4d" % (num_toGuess)) 
   print("Number Guessing Game ----------------------")
   return num_toGuess

# user input and game exit input
def Input():
    
    user_guess = 0
    user_guess = (input())
    
    # if user wants to end the game at any time
    if user_guess == "end" or user_guess == "END":
        print("Okay Bye!")
        exit(0)
        
    return user_guess

# create the game with for loop and if statements, pass in variables from other functions
def main():
    #store users guesses
    used_numbers = set()
        
    # random number to guess
    num_toGuess = initial() 
        
    #guesses taken by user starting from one ending at 10. Total of 10 guesses
    guessesTaken = 1
            
    # loop through guess 10xs, can only have 10 guesses, unless guessed correctly
    while guessesTaken != 11:
        
        #print on before/on same line as user input using end=''
        print("Enter guess #",guessesTaken, "between 1 and 100: ", end="")
        
        #While user input is number
        while True:
            try:
                user_guess = int(Input())
                
                # error checking the users input
                if (user_guess < 1) or (user_guess > 100):
                    print("*** Incorrect Input : Must be in range from 1 to 100...")
                    print("Enter guess #",guessesTaken, "between 1 and 100: ", end="")
                elif user_guess in used_numbers:
                    print("*** Invalid Input : You already guessed that number..")
                    print("Enter guess #",guessesTaken, "between 1 and 100: ", end="")
                
                #if user enters num not in used nums then add and break
                elif user_guess not in used_numbers:
                    used_numbers.add(user_guess)
                    break
            #if user does not enter an int
            except ValueError:
                print("*** Invalid Input : Please try again....")
                print("Enter guess #",guessesTaken, "between 1 and 100: ", end="")
        
        # if user guesses the correct number, end prog
        if user_guess == num_toGuess:
            print("Guess #",guessesTaken, ":", user_guess, "- CORRECT!")
            print("YOU WIN!")
            # if user enter correct number stop and restart program in 2 secs
            time.sleep(2)     
            restart = threading.Thread(target=main())
            restart.start()
             
            
        #if statements to generate higher or lower
        elif (user_guess < num_toGuess) and (user_guess > 0) and (user_guess < 101) :
            print("Guess #",guessesTaken, ":", user_guess, "- Higher!")
            print("-------------------------------------------")
            guessesTaken = guessesTaken + 1
        elif (user_guess > num_toGuess) and (user_guess > 0) and (user_guess < 101) : 
            print("Guess #",guessesTaken, ":", user_guess, "- Lower!")
            print("-------------------------------------------")
            guessesTaken = guessesTaken + 1
    
    #if all guesses are used up , max 10 guesses .Then restart in 2 secs    
    else:
        print("YOU LOSE! The number to guess was", num_toGuess)
        time.sleep(2)     
        restart = threading.Thread(target=main())
        restart.start()
        
main()
