import time

def displayIntro():
    print ('You are stuck in ')
    print ('you see two caves. In one cave, the dragon is friendly')
    print ('and will share his treasure with you. The other dragon')
    print ('is greedy and hungry, and will eat you on sight.')
    print
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print ('You approach the cave...')
    time.sleep(2)
    print ('It is dark and spooky...')
   
    if chosenCave == "1":
        print ('you chose cave 1a')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('you chose cave 2a')
        elif chosenCave == "2":
            print ('you chose cave 2b')
    elif chosenCave == "2":
        print('you chose cave 1b')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('you chose cave 2c')
        elif chosenCave == "2":
            print ('you chose cave 2d')

def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()