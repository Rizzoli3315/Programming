import random
import time
thenumber = int(random.randint(1, 101))
theother = int(random.randint(1, 101))

def numberchoose(number1, number2):
        number1 = number1+int(random.randint(1, 101))
        number2 = number2+int(random.randint(1, 101))
        thegamestart()

def thegamestart(): 
    
    if theother == thenumber:
        print("\033[1;32m ~SOMETHING WENT WRONG...STARTING AGAIN~  \n")
        time.sleep(3)
        numberchoose(thenumber, theother)
        
    else:
        print(""" ||| HIGHER OR LOWER |||

                  You will be given a number from
                  1 to 100. There is another mystery
                  number. You have to guess whether it
                  is higher or lower than the number
                  you are given.

                  have fun!""")

        time.sleep(2)

        choosestart = input("Enter anything to start: ").lower()

        if choosestart == "end":
            print("Alright then...")
            time.sleep(3)
            print("\033[1;32m ~GAME HAS ENDED~  \n")
            quit()

        else:
            thenumbershow()

 
def thenumbershow():

    print("The number you are given is ",theother)

    time.sleep(2)

    thegame()


def thegame():

    guess = input("Now guess whether the mystery number is higher or lower : ").lower()

    time.sleep(2)

    if guess == "higher":
        if thenumber>theother:
            print("You are correct! The mystery number was ",thenumber)

            playagain()

        else:
            print("You are incorrect! The mystery number was ",thenumber)

            playagain()
            
    elif guess == "lower":
        if thenumber<theother:
            print("You are correct! The mystery number was ",thenumber)

            playagain()
            
        else:
            print("You are incorrect! The mystery number was ",thenumber)

            playagain()

    elif guess == "end":
        print("Alright then...")
        time.sleep(3)
        print("\033[1;32m ~GAME HAS ENDED~  \n")
        quit()
  
    else:
        print("Hmm... Seems like you typed something wrong. You can guess again or type 'end' to end the game")

        time.sleep(2)

        thegame()
                    

def playagain():
    playagain1 = input("Do you want to play again? (Yes/No): ").lower()

    if playagain1 == "yes":
        time.sleep(1)
        print("Nice!")
        time.sleep(2)
        print("\033[1;32m ~INITIATING PROCESS~  \n")
        time.sleep(2)
        print("\033[1;32m ~STARTING GAME.... \n")
        time.sleep(2)
        
        numberchoose(thenumber, theother)
        
    elif playagain1 == "no":
        time.sleep(1)
        print("Ok!")
        time.sleep(3)
        print("\033[1;32m ~GAME HAS ENDED~  \n")
        quit()
            
    elif playagain1 == "end":
        time.sleep(1)
        print("Alright then...")
        time.sleep(3)
        print("\033[1;32m ~GAME HAS ENDED~  \n")
        quit()
             
    else:
        time.sleep(1)
        print("Hmm... Seems like you typed something wrong. You can enter or type 'end' to end the game")
        time.sleep(1)
        playagain()


numberchoose(thenumber, theother)
























         
