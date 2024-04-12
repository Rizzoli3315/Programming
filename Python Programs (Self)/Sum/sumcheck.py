import time

def numberf():
    x = float(input("First number: "))
    y = float(input("Second number: "))
    z = float(input("Third number: "))
    sumf = x+y+z
    print("The sum of the three given numbers is")
    time.sleep(1)
    print(sumf)
    time.sleep(1)
    if sumf == 0:
        print("zero")
    if sumf%2 == 0:
        print("even")
    elif (sumf).is_integer() and sumf%2 != 0:
        print("odd")
    else:
        print("float")

    time.sleep(1)

    if sumf<0:
        print("negative")
    else:
        print("positive")
        
    restart()
    
def restart():
    re = input("Restart (Y/N): ").lower()

    if re == "y":
        print("Restarting...")
        numberf()
    elif re == "n":
        print("Ending...")
        quit()
    else:
        print("Seems like you typed something wrong")
        restart()
      
numberf()

