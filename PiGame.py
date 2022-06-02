from time import sleep
import os
import msvcrt as m


pi = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'


def wait():
    m.getch()

def rememberHighScore(array, nickname):
    
    tfile = open("highscores.txt", "r")
    lines = tfile.readlines()

    """ for line in lines:
        array.append(line.strip().split()) """
    
    for i in range(len(lines)):
        array.append(lines[i].strip().split())
        array[i][1] = int(array[i][1])

    for i in range(len(array)):
        """ print(array[i][0]) """
        if nickname == array[i][0]:
            return array[i][1]
    
    tmpList = [nickname, 0]
    array.append(tmpList)

    """ print(array) """
    
    return 0;

def writeHighScore(array):
    myFile = open("highscores.txt", "w")
    for line in array:
        myFile.write(line[0] + " " + str(line[1]) + "\n")
    myFile.close()

def checkInput(nickname, array, pi, high):
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
            
            for i in range(len(array)):
                if array[i][0] == nickname:
                    array[i][1] = high

            return

        score += 1

        if score > high: 
            high = score

        os.system('cls')

    for i in range(len(array)):
        if array[i][0] == nickname:
            array[i][1] = high

    

    tmpList = [nickname, high]
    array.append(tmpList)

    print(array)

    writeHighScore(array)
    
    print(f'Congrats! You completed the challenge and your score was {score}')

    return


print("I will show you the number Pi by portions and you'll have to remember that portion and type it....\nGood Luck!\nPress any key to continue: ", end="")

wait()
os.system('cls')

nick = input("Enter a nickname: ")

scoresArray = []

high = rememberHighScore(scoresArray, nick)
checkInput(nick, scoresArray, pi, high)
writeHighScore(scoresArray)

""" print(high) """