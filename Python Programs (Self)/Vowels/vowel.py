
num = []

def vowelcounter():

    global num
    
    num = []
    
    sen = str(input("Sentence: ")).lower()

    vowels = ["a", "e", "i", "o", "u"]

    for i in sen:
        if i in vowels:
            print(i)

            num += i

    print("The number of vowels are", len(num))

    replay()
    
def replay():
    rep = str(input("Repeat? (Y/N): ")).lower()
    
    if rep == "y":
        vowelcounter()

    elif rep == "n":
        print("Ok")
        quit()

    else:
        print("Seems like you typed something wrong")
        replay()

vowelcounter()






    

