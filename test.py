from numpy import array


def readFile(array, nickname):
    high = 0

    tfile = open("test.txt", "r")
    lines = tfile.readlines()

    """ for line in lines:
        array.append(line.strip().split()) """
    
    for i in range(len(lines)):
        array.append(lines[i].strip().split())
        array[i][1] = int(array[i][1])

    for i in range(len(array)):
        print(array[i][0])
        if nickname == array[i][0]:
            return array[i][1]
    
    tmpList = [nickname, 0]
    array.append(tmpList)
    
    return 0;
    
    

    

nick = input("Enter a nickname: ")

scoresArray = []

highscore = readFile(scoresArray, nick)
print(f'Your highscore is {highscore}')

print(scoresArray)