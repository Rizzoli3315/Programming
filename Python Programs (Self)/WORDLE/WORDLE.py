import random
from spellchecker import SpellChecker

def play_wordle():
    print("Welcome to the WORDLE game!\n")
    print("The rules are simple:")
    print("1. The computer will choose a 5 letter word from the English dictionary.")
    print("2. You have to guess the word within 6 attempts.")
    print("3. With each guess, the computer will tell you how many letters are in the right position and how many letters are in the wrong position.")
    print("4. The letters that are in the right position will be in UPPER CASE and letters that are in the wrong position will be in lower case.")
    print("5. Good luck!\n")
    # Choose a word at random from the list
    word_list = ["python", "apple", "table", "swift", "world", "month", "fruit", "happy", "light", "smile", "tiger", "lion", "swim", "lemon", "pilot", "dream", "guard", "flood", "adult", "sight", "alarm", "force", "wound", "brave", "cable", "panic", "study", "faith", "equal", "grade", "award", "bully", "voice", "drive", "Flirt", "fifth", "gamer", "mouse"]
    # filter the word_list with only 5 letters words
    word_list = [word for word in word_list if len(word) == 5 ]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    word_guessed = ["_"] * len(word)
    spell = SpellChecker()
    attempts = 0
    while "_" in word_guessed and attempts < 6:
        guess = input("Enter a 5 letter word as the guess: ").lower()
        if len(guess) != 5:
            print("The word should have 5 letters")
        elif set(guess).issubset(alphabet):
            if spell.correction(guess) == guess:
                if guess == word:
                    print(f"Congratulations, you have guessed the word {word} in {attempts + 1} attempts!")
                    break
                else:
                    correct_letter_count_right = 0
                    correct_letter_count_wrong = 0
                    correct_letter_pos_right = []
                    correct_letter_pos_wrong = []
                    for i in range(5):
                        if guess[i] == word[i]:
                            correct_letter_count_right += 1
                            correct_letter_pos_right.append(guess[i].upper())
                        elif guess[i] in word:
                            correct_letter_count_wrong += 1
                            correct_letter_pos_wrong.append(guess[i])
                    print("Incorrect guess!")
                    print(f"Correct letters in right position: {correct_letter_count_right} {correct_letter_pos_right}")
                    print(f"Correct letters in wrong position: {correct_letter_count_wrong} {correct_letter_pos_wrong}")
                    attempts += 1
            else:
                print("Invalid input, enter only a valid 5 letter word in English")
        else:
            print("Invalid input, enter only a 5 letter word")
            
            
    if attempts == 6:
        print("You reached the maximum number of attempts, the word was: ", word)

play_wordle()
        
