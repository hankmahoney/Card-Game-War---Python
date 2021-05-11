from random import shuffle, randint

def getValue(card):
    if(card[1:] == 'J'):
        value = 11
    elif(card[1:] == 'Q'):
        value = 12
    elif(card[1:] == 'K'):
        value = 13
    elif(card[1:] == 'A'):
        value = 14
    else:
        value = card[1:]
    return int(value)

# Deck class - 3 methods - create - shuffle - deal
class Deck():
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    DECK = []

    def create(self):
        for suite in range(len(Deck.SUITE)):
            for rank in range(len(Deck.RANKS)):
                Deck.DECK.append(f"{Deck.SUITE[suite]}{Deck.RANKS[rank]}")
        return Deck.DECK

    def shuffle(self):
        shuffle(Deck.DECK)

    def deal(self,arr1,arr2):
        for i in range(len(Deck.DECK)):
            if i%2 == 0:
                arr1.append(Deck.DECK.pop())
            else:
                arr2.append(Deck.DECK.pop())

# Hand class - 2 methods - add cards - remove cards
class Hand():
    def __init__(self,hand):
        self.hand = hand

    def add(self,cards):
        self.hand.extend(cards)

    def remove(self,cards):
        self.hand.remove(cards)

    def __str__(self):
        return (f"{self.hand}")

# Player class - 2 methods - play: to drwa a card to play - cards: to view the deck that is left
class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play(self):
        return getValue(self.hand.hand[0])

    def cards(self):
        return self.hand.hand

# Create - SHuffle - Deal the cards
deck = Deck()
deck = deck.create()
Deck.shuffle(deck)
deal1 = []
deal2 = []
Deck.deal(deck,deal1,deal2)

#Create the hadns with the Hand class
hand1 = Hand(deal1)
hand2 = Hand(deal2)

# Create players - assign the hands to players
p1 = Player("Hannu",hand1)
p2 = Player("Computer",hand2)

#Boolean to evaluate if the conditions for gameplay are still met
true = True

#Game play logic
while(true):
    #List of cards which will be allocated to the winner of the round
    cardsForWinner = []

    #First card from each players hand
    card1 = p1.hand.hand[0]
    value1 = int(p1.play())

    print(f"Player: {p1.name} Card: {card1}")

    card2 = p2.hand.hand[0]
    value2 = int(p2.play())

    print(f"Player: {p2.name} Card: {card2}")

    #Check which card wins
    if(value1>value2):
        #Remove dealt cards from each players deck and allocated the cards into the winners deck
        p1.hand.hand.remove(card1)
        p2.hand.hand.remove(card2)
        p1.hand.add([card1,card2])

        print(f"Player: {p1.name} wins this hand!")

    elif(value1<value2):
        #Remove dealt cards from each players deck and allocated the cards into the winners deck
        p1.hand.hand.remove(card1)
        p2.hand.hand.remove(card2)
        p2.hand.add([card1,card2])

        print(f"Player: {p2.name} wins this hand!")

    #Logic for the gameplay if the first round produces a drwa
    else:
        #Remove dealt cards from each players deck and allocated the cards into the winners deck
        p1.hand.hand.remove(card1)
        p2.hand.hand.remove(card2)

        #Allocate the cards that produces the draw into the cardsForWinner List
        cardsForWinner.append(card1)
        cardsForWinner.append(card2)

        print("DRAW")

        #3 cards will be dealt from each player for additional round if each players have enough cards to be played
        while(len(p1.cards()) >= 4 or len(p2.cards()) >= 4):

            #list for each player to allocate the 3 cards to dealt
            p1DeckOf3 = []
            p2DeckOf3 = []

            #If one of the players has less than 4 cards in the deck then the game will finish
            if(len(p1.cards())<=4 or len(p2.cards())<=4):
                if(p1.cards()>p2.cards()):
                    print(f"Player: {p2.name} does not have enough cards to play!")
                    print(f"Player {p1.name} WINS")
                    true = False
                    break
                elif(p1.cards()<p2.cards()):
                    print(f"Player: {p1.name} does not have enough cards to play!")
                    print(f"Player {p2.name} WINS")
                    true = False
                    break

            #Loop to deal the 4 cards from each players deck
            for i in range(4):
                card1 = p1.hand.hand[0]
                card2 = p2.hand.hand[0]
                p1DeckOf3.append(card1)
                p2DeckOf3.append(card2)
                p1.hand.hand.remove(card1)
                p2.hand.hand.remove(card2)

            #Draw one card from each of the newlt created decks
            p1Index = randint(0,3)
            p2Index = randint(0,3)
            card1 = p1DeckOf3[p1Index]
            card2 = p2DeckOf3[p2Index]
            value1 = getValue(p1DeckOf3[p1Index])
            value2 = getValue(card2)

            print(f"Player: {p1.name} Card: {p1DeckOf3[p1Index]}")
            print(f"Player: {p2.name} Card: {p2DeckOf3[p2Index]}")

            #Game logic for a extra round after the draw
            if(value1>value2):
                cardsForWinner.extend(p1DeckOf3)
                cardsForWinner.extend(p2DeckOf3)
                p1.hand.add(cardsForWinner)
                print(f"Player: {p1.name} wins this hand!")
                break
            elif(value1<value2):
                cardsForWinner.extend(p1DeckOf3)
                cardsForWinner.extend(p2DeckOf3)
                p2.hand.add(cardsForWinner)
                print(f"Player: {p2.name} wins this hand!")
                break
            else:
                cardsForWinner.append(p1DeckOf3.pop(p1Index))
                cardsForWinner.append(p2DeckOf3.pop(p2Index))

        if not true:
            break

    print(f"Player: {p1.name} Current deck: {p1.cards()}")
    print(f"Player: {p2.name} Current deck: {p2.cards()}")
    input("Press Enter to continue...")

    #Logic to check if one of the players have lost all the cards
    if(p1.cards() == [] or p2.cards() == []):
        if(p1.cards() == []):
            print(f"{p2.name} is the winner!")
        elif(p2.cards() == []):
            print(f"{p1.name} is the winner!")
        break
