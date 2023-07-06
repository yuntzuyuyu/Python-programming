from random import random

def main():
    printIntro()
    probA , porbB , n = getInputs()
    winsA , winsB = simNGame(n,probA, porbB)
    printSummary(n,winsA, winsB)


def printIntro():
    print("This progra sumulate a game of racquetball between two")
    print("player called A and B , the ability of each other is")
    print("indicated by a probability that")
    print("The player wins the point when serving, Player A always")
    print("has the first serve.")
def getInputs():
    a = eval(input("What is the prob player A wins  a serve?"))
    b = eval(input("What is the prob player B wins  a serve?"))
    n = eval(input("How many game to simulate ?"))
    return a, b ,n

def simNGame(n,probA, porbB):

    winsA =0
    winsB = 0

    for i in range(n):
        scoreA ,scoreB = simOneGame(probA, porbB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
            
    return winsA , winsB




#Simulate a single game
def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    

    
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
     
        else :
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA ,scoreB

            
                              
        


def gameOver(a,b) :
    return a == 15 or b ==  15


def printSummary(n,winsA, winsB):
    

    print("Games simulation {}".format(n))
    print("Wins for A :{0},{1:0.1%}".format(winsA, winsA/n))
    print("Wins for B :{0},{1:0.1%}".format(winsB, winsB/n))
