#Zombieland.py
# Author: Harsimrat Kaur
# Last Modified by: Hrsimrat Kaur
#Date last Modified: 23rd May 2013
#Program description: Zombieland game, 3 level decision, 7 negative outcomes, 1 positive

import time

def displayIntro():
    #introductory text that sets the storyline for the game
    print ('You are driving on a lonely road on your roadtrip')
    time.sleep(2)
    print ('The fog starts to thickens.......')
    time.sleep(2)
    print ('You slow down since you cant see anything')
    time.sleep(2)
    print ('the last thing you remember is your car crashing into a weird figure')
    time.sleep(2)
def chooseCave():
    #First level decision, lets the player choose the first cave, also sets more of the story
    cave = ''
    while cave != 'left' and cave != 'right':
        print ('You wake up in cave, the walls are all covereg in human skulls and bones, its the Catacombs')
        time.sleep(2)
        print ('You look around to make sense of the place, you see a piece of paper and try reading whats written on it')
        time.sleep(2)
        print ('GET OUT OF HERE! FOLLOW THE CAVES, THERE IS ONLY ONE WAY OUT')
        time.sleep(2)
        print ('You see two way out of the room, which door do you go though? left or right?')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    
    if chosenCave == "left":
        print ('You enter the next cave, theres a torch on the wall, you take it')
        time.sleep(2)
        print ('You see another two exits from the room, which room do you go to? left or right?')
        chosenCave = raw_input()
        if chosenCave == "left":
            #nested if and elif statements take care of each decision making level
            print ('You enter another room and yet again, there are two doors in front of you, left or right?')
            chosenCave = raw_input()
            if chosenCave == "left":
                print ('You go into the room......Its a dead end!')
                time.sleep(2)
                print ('Just as you think about turning back, the walls start crumbling down on you and you......')
            elif chosenCave == "right":
                print ('You enter a room way bigger than the ones before, you go in deeper')
                time.sleep(2)
                print ('Suddenly, you hear a sound behind you, before you get the chance to turn back, you feel the hands that are about to snap your neck')
        elif chosenCave == "right":
            print ('You enter another room with another pile of bones in the center, there are right doors, left or right?')
            chosenCave = raw_input()
            if chosenCave == "left":
                print ('You enter the room and get eaten to death by Zombies')
            elif chosenCave == "right":
                print ('The room is narrow and long, you go deeper....')
                time.sleep(2)
                print ('You hear the sound of a car, you start running towards it')
                time.sleep(2)
                print ('You found the way out of the catacombs!!!!!!')
                time.sleep(2)
                print ('Congratulations, you win :)')

                
    elif chosenCave == "right":
        print('You chose to go through the second door, the next room also has two exits, which door do you choose? left or right?')
        chosenCave = raw_input()
        if chosenCave == "left":
            print ('You enter another room, you hear something, Its a ZOMBIE!')
            print ('you pick up one of the broken bones on the floor and stab it in its head left0 times')
            time.sleep(2)
            print ('You try to catch your breath but you know you cant stay for long in this place')
            print ('You see two caves, which one do you go into left or right?')
            chosenCave = raw_input()
            if chosenCave == "left":
                print ('You go into the room and see its swarmed by zombies')
                print ('They sense you there, and get o you before you had the chance to turn back')
            elif chosenCave == "right":
                print ('The room is narrow and long, you go deeper....')
                print ('All of a sudden, a zombie jumps on you and bites you!')
                print ('You manage to kill the zombie, but you lost so much blood in th process that your body gives up')
        elif chosenCave == "right":
            print ('You enter the next room, theres a reek of rotten flesh all around the place')
            print ('You see another two exits, which one do you choose this time? left or right?')
            chosenCave = raw_input()
            if chosenCave == "left":
                print ('You go left, and you see the night sky!!!!!')
                print ('Suddenly you feel your feet sinking into the ground')
                print ('Its a Marsh.....you get trapped and die')
            elif chosenCave == "right":
                print ('You find yoursef back in the room you started')
                print ('Only this time, you are not alone')
                print ('There are 4 zombie dogs in the room, you try to fight them but fail')

def main():
    
    #calling the main function, let's the use choose whether he wants to play again or not
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()