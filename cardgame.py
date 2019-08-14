""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random               #TA told us to do it this way

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def clearDeck():                                            #defining a function clearDeck with no arguments
    for i in range(NUMCARDS):                               #using a for loop to set values equal to zero in cardLoc
        cardLoc[i] = 0

def assignCard(cardHolder):                                 #defining a function assignCard with argument cardHolder
    keepGoing = True                                        #creating a boolean variable and setting equal to True
    while(keepGoing):                                       #while loop begins
        placement = random.randint(0, 51)                   #getting random integers by random.randint function
        if cardLoc[placement] == DECK:
            keepGoing = False                               #these three lines assigning the card to cardHolder if its in the DECK
    cardLoc[placement] = cardHolder

def showDeck():                                             #defining a new function showDeck
    print(" Location of all cards")
    print(" #       Card         Location")                 #printing some stuff to the window
    for i in range(NUMCARDS):                               #for loop begins on NUMCARDS
        print("{:2}  {:17}  {}".format(i, showName(i), playerName[cardLoc[i]]))             #:2, :17 adding appropriate spaces between content

def showName(loc):                                                      #this function showName contains one argument loc
    cardname = rankName[loc % 13] + " of " + suitName[int(loc / 13)]    #this line basically gives card names according to suitName and rankName
    return cardname                                                     #returning the value so I can use it in other functions

def showHand(cardHolder):                                               #this whole function displays player and
    print("\nDisplaying {} hand:".format(playerName[cardHolder]))        #computer cards in the end
    for i in range(NUMCARDS):
        if cardLoc[i] == cardHolder:
            print(showName(i))

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)
main()

