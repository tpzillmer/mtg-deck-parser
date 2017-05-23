from mtgsdk import Card
from operator import itemgetter

Creature = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Planeswalker = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Sorcery = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Instant = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Enchantment = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Artifact = [[[[] for rarity in range(5)] for costs in range(16)] for colors in range(32)]
Land = []


All = [Creature, Planeswalker, Sorcery, Instant, Enchantment, Artifact, Land]

typeMapping = {'Creature': Creature, 'Planeswalker': Planeswalker, 'Sorcery': Sorcery, 'Instant': Instant, 'Enchantment': Enchantment, 'Artifact': Artifact, 'Land': Land}

colorMapping = {'White': 0, 'Blue': 1, 'Black': 2, 'Red': 3, 'Green': 4, 'WhiteBlue': 5, 'BlueBlack': 6, 'BlackRed': 7, 'RedGreen': 8, 'GreenWhite': 9, 'WhiteBlack': 10, 'BlueRed': 11,
                'BlackGreen': 12, 'RedWhite': 13, 'GreenBlue': 14, 'WhiteBlueGreen': 15, 'WhiteBlueBlack': 16, 'BlueBlackRed': 17, 'BlackRedGreen': 18, 'RedGreenWhite': 19,
                'WhiteBlackRed': 20, 'BlueRedGreen': 21, 'WhiteBlackGreen': 22, 'WhiteBlueRed': 23, 'BlueBlackGreen': 24, 'BlueBlackRedGreen': 25, 'WhiteBlackRedGreen': 26,
                'WhiteBlueRedGreen': 27, 'WhiteBlueBlackGreen': 28, 'WhiteBlueBlackRed': 29, 'WhiteBlueBlackRedGreen': 30, 'Colorless': 31}

rarityMapping = {'Mythic Rare':0, 'Rare': 1, 'Uncommon': 2, 'Common': 3, 'Basic Land': 4}

def parseDeck(deck):

    for cardsInDeck in deck:
        if(cardsInDeck[0].isdigit()):
            i = 0
            while(cardsInDeck[i].isdigit()):
                i+=1
            cardName = '"'+cardsInDeck[i+1:]+'"'
            card = getCard(cardName)
            cardType = getType(card)
            cardColor = getColors(card)
            cardCost = card.cmc
            
            if(card.rarity == 'Special'):
                cardRarity = 'Mythic Rare'
            else:
                cardRarity = card.rarity

            addToList(cardsInDeck, cardType, cardColor, cardCost, cardRarity)
            

def getCard(cardName):
    BasicLands = ['Swamp', 'Plains', 'Forest', 'Island', 'Mountain']
    try:
        if cardName in BasicLands:
            card = Card.where(name=cardName).where(setName='Alpha').all()[0]
        else:
            card = Card.where(name=cardName).all()[0]
        return card
    except IndexError:
        print("{} has not been printed or does not exist.".format(cardName))
        
def getType(card):
    cardTypes = card.types
    
    if(len(cardTypes) == 1):
       cardType = cardTypes[0]
       
    else:
        if cardTypes[0] == 'Land':
           cardType = cardTypes[0]
        else:
            cardType = cardTypes[1]
            
    return cardType

def getColors(card):
    colors = card.colors
    if(colors):
        return ''.join(colors)
    else:
        return 'Colorless'

def addToList(cardInDeck, cardType, cardColor, cardCost, cardRarity):
    if(cardType == "Land"):
        Land.append(cardInDeck)
    else:
        typeMapping[cardType][colorMapping[cardColor]][cardCost][rarityMapping[cardRarity]].append(cardInDeck)

def printCards():
    print("\n//Creatures")
    for colors in Creature:
        for costs in colors:
            for rarities in costs:
                rarities.sort()
                for card in rarities:
                    print(card)
    print("")
    print("//Planeswalkers")
    for colors in Planeswalker:
        for costs in colors:
            for rarities in costs:
                rarities.sort()
                for card in rarities:
                    print(card)
    print("")
    print("//Sorceries")
    for colors in Sorcery:
        for costs in colors:
            for rarities in costs:
                rarities.sort()
                for card in rarities:
                    print(card)
    print("")
    print("//Instants")
    for colors in Instant:
        for costs in colors:
            for rarities in costs:
                rarities.sort()
                for card in rarities:
                    print(card)
    print("")
    print("//Enchantments")
    for colors in Enchantment:
        for costs in colors:
            for rarities in costs:
                for card in rarities:
                    print(card)
    print("")
    print("//Artifacts")
    for colors in Artifact:
        for costs in colors:
            for rarities in costs:
                rarities.sort()
                for card in rarities:
                    print(card)
    print("")
    print("//Lands")
    for land in Land:
        print(land)

if __name__ == "__main__":
    deck = []
    print("Please enter a deck list, press enter and then Ctrl-D.")
    while True:
        try:
            deckInput = input()
            if(deckInput):
                deck.append(deckInput)
        except EOFError:
            break
    parseDeck(deck)
    printCards()
        
