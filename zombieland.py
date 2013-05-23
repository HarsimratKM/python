import time

def displayIntro():
    print ('You are driving on a lonely road on your roadtrip')
    time.sleep(2)
    print ('The fog starts to thickens.......')
    time.sleep(2)
    print ('You slow down since you cant see anything')
    time.sleep(2)
    print ('the last thing you remember is your car crashing into a weird figure')
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
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you chose cave 3a')
            elif chosenCave == "2":
                print ('you chose cave 3b')
        elif chosenCave == "2":
            print ('you chose cave 2b')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you chose cave 3c')
            elif chosenCave == "2":
                print ('you chose cave 3d')
                
    elif chosenCave == "2":
        print('you chose cave 1b')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('you chose cave 2c')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you chose cave 3e')
            elif chosenCave == "2":
                print ('you chose cave 3f')
        elif chosenCave == "2":
            print ('you chose cave 2d')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you chose cave 3g')
            elif chosenCave == "2":
                print ('you chose cave 3h')

def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()