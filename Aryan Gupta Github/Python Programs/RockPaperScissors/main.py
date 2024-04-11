#22 Jan 2023 1:25 am, Aryan Gupta
#I rewrote the code with a working scoreboard

import time
import random
import pygame

pygame.mixer.init()
winsound = pygame.mixer.Sound("winsound1.wav")
losesound = pygame.mixer.Sound("losesound.wav")
yessound = pygame.mixer.Sound("yes.wav")

csc = 0
psc = 0

def playwinsound():
    pygame.mixer.Sound.play(winsound)

def playlosesound():
    pygame.mixer.Sound.play(losesound)

def playyessound():
    pygame.mixer.Sound.play(yessound)
    
    
def scoreboard(cpus, pls): #cpu score and player score
    print("CPU : " + str(cpus) + " | " + "Player: " + str(pls))

def rspgame():
    global csc
    global psc

    choice = input("Rock(R) Paper(P) or Scissors(S)? :").lower()

    choices = {1: "r", 2: "p", 3: "s"}

    cno = random.randint(1, 3)

    cpuchoice = choices[cno]

    if choice == "r":
        if cpuchoice == "s":
            playwinsound()
            print("You won! The CPU chose Scissors")
            time.sleep(1)
            scoreboard(csc, psc + 1)
            psc += 1
            time.sleep(2)
            restart()

        elif cpuchoice == "p":
            print("You lost! The CPU chose Paper")
            playlosesound()
            time.sleep(1)
            scoreboard(csc + 1, psc)
            csc = csc + 1
            time.sleep(2)
            restart()

        else:
            print("Tie! The CPU also chose Rock")
            time.sleep(1)
            scoreboard(csc, psc)
            time.sleep(2)
            restart()

    elif choice == "s":
        if cpuchoice == "p":
            playwinsound()
            print("You won! The CPU chose Paper")
            time.sleep(1)
            scoreboard(csc, psc + 1)
            psc = psc + 1
            time.sleep(2)
            restart()


        elif cpuchoice == "r":
            print("You lost! The CPU chose Rock")
            playlosesound()
            time.sleep(1)
            scoreboard(csc + 1, psc)
            csc = csc + 1
            time.sleep(2)
            restart()

        else:
            print("Tie! The CPU also chose Scissors")
            time.sleep(1)
            scoreboard(csc, psc)
            time.sleep(2)
            restart()

    elif choice == "gun":
        print("Seems like you found the secret weapon... You win, I guess")
        time.sleep(1)
        scoreboard(csc, psc + 1)
        psc = psc + 1
        time.sleep(2)
        restart()

    elif choice == "p":
        if cpuchoice == "r":
            playwinsound()
            print("You won! The CPU chose Rock")
            time.sleep(1)
            scoreboard(csc, psc + 1)
            psc = psc + 1
            time.sleep(2)
            restart()
        elif cpuchoice == "s":
            print("You lost! The CPU chose Scissors")
            playlosesound()
            time.sleep(1)
            scoreboard(csc + 1, psc)
            csc = csc + 1
            time.sleep(2)
            restart()
        else:
            print("Tie! The CPU also chose Paper")
            time.sleep(1)
            scoreboard(csc, psc)
            time.sleep(2)
            restart()

    else:
        print("Seems like you entered something wrong.")
        time.sleep(1)
        print("Restarting...")
        time.sleep(2)
        rspgame()


def restart():
    re = input("Do you want to play again (Y/N)").lower()

    if re == "y":
        print("Restarting...")
        playyessound()
        time.sleep(2)
        rspgame()

    elif re == "n":
        print("Ending...")
        quit()

    else:
        print("Seems like you entered something wrong.")
        restart()


print(""" |||Rock Paper Scissors|||""")

time.sleep(1)
scoreboard(0, 0)

time.sleep(2)

rspgame()
