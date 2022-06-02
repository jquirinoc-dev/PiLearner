from time import sleep
import os
import msvcrt as m


pi = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'


def wait():
    m.getch()

def rememberHighScore():
    myFile = open("highscore.txt", "r")
    high = int(myFile.read())
    """ print(f'{high} is type {type(high)}') """
    myFile.close()
    return high;

def writeHighScore(high):
    myFile = open("highscore.txt", "w")
    myFile.write(str(high))
    myFile.close()

def checkInput(pi, high):
    score = 0

    for i in range(3, len(pi), 2):
        sleep(0.25)
        print("Wait for you turn to type...")
        print(f'Pi: {pi[:i + 1]}')
        sleep(3)
        os.system('cls')

        print(f'Current score: {score}')
        print(f'Highscore: {high}')
    
        inpt = input("\nEnter the Pi portion I just showed you: ")

        if inpt != pi[:i + 1]:
            print(f'INCORRECT! You could just try from the beggining\nThe score you got was {score}')
            return high

        score += 1

        if score > high: 
            high = score

        

        os.system('cls')
    
    print(f'Congrats! You completed the challenge and your score was {score}')

    return high;


print("I will show you the number Pi by portions and you'll have to remember that portion and type it....\nGood Luck!\nPress any key to continue: ", end="")

wait()
os.system('cls')

high = rememberHighScore()
high = checkInput(pi, high)
writeHighScore(high)

""" print(high) """