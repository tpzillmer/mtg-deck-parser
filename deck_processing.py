from mtgsdk import Card
from operator import itemgetter

def createTypeList(TypeList, cardColor, card, cardCost):
    
    if cardColor == None:
        TypeList[31][card] = cardCost
        
    elif len(cardColor) == 1:
        if cardColor[0] == 'White':
            TypeList[0][card] = cardCost
        elif cardColor[0] == 'Blue':
            TypeList[1][card] = cardCost
        elif cardColor[0] == 'Black':
            TypeList[2][card] = cardCost
        elif cardColor[0] == 'Red':
            TypeList[3][card] = cardCost
        elif cardColor[0] == 'Green':
            TypeList[4][card] = cardCost
            
    elif len(cardColor) == 2:
        if "White" in cardColor and "Blue" in cardColor:
            TypeList[5][card] = cardCost
        elif "Blue" in cardColor and "Black" in cardColor:
            TypeList[6][card] = cardCost
        elif "Black" in cardColor and "Red" in cardColor:
            TypeList[7][card] = cardCost
        elif "Red" in cardColor and "Green" in cardColor:
            TypeList[8][card] = cardCost
        elif "Green" in cardColor and "White" in cardColor:
            TypeList[9][card] = cardCost
        elif "White" in cardColor and "Black" in cardColor:
            TypeList[10][card] = cardCost
        elif "Blue" in cardColor and "Red" in cardColor:
            TypeList[11][card] = cardCost
        elif "Black" in cardColor and "Green" in cardColor:
            TypeList[12][card] = cardCost
        elif "Red" in cardColor and "White" in cardColor:
            TypeList[13][card] = cardCost
        elif "Green" in cardColor and "Blue" in cardColor:
            TypeList[14][card] = cardCost

    elif len(cardColor) == 3:
        if "Black" and "Red" not in cardColor:
            TypeList[15][card] = cardCost
        elif "Red" and "Green" not in cardColor:
            TypeList[16][card] = cardCost
        elif "Green" and "White" not in cardColor:
            TypeList[17][card] = cardCost
        elif "White" and "Blue" not in cardColor:
            TypeList[18][card] = cardCost
        elif "Blue" and "Black" not in cardColor:
            TypeList[19][card] = cardCost
        elif "Blue" and "Green" not in cardColor:
            TypeList[20][card] = cardCost
        elif "White" and "Black" not in cardColor:
            TypeList[21][card] = cardCost
        elif "Blue" and "Red" not in cardColor:
            TypeList[22][card] = cardCost
        elif "Black" and "Green" not in cardColor:
            TypeList[23][card] = cardCost
        elif "White" and "Red" not in cardColor:
            TypeList[24][card] = cardCost

    elif len(cardColor) == 4:
        if "White" not in cardColor:
            TypeList[25][card] = cardCost
        if "Blue" not in cardColor:
            TypeList[26][card] = cardCost
        if "Black" not in cardColor:
            TypeList[27][card] = cardCost
        if "Red" not in cardColor:
            TypeList[28][card] = cardCost
        if "Green" not in cardColor:
            TypeList[29][card] = cardCost

    else:
        TypeList[30][card] = cardCost


def parseDeck(deck):
    deckList = deck.split('\n')
    deckList = list(filter(None, deckList))
    
    BasicLands = ['Swamp', 'Plains', 'Forest', 'Island', 'Mountain']

    Creature = [{} for colors in range(32)]
    Planeswalker = [{} for colors in range(32)]
    Sorcery = [{} for colors in range(32)]
    Instant = [{} for colors in range(32)]
    Enchantment = [{} for colors in range(32)]
    Artifact = [{} for colors in range(32)]
    Land = []

    All = [Creature, Planeswalker, Sorcery, Instant, Enchantment, Artifact]

    
    for card in deckList:
        if card[0].isdigit():
            cardName = ''
            cardType = ''
            if card[1].isdigit():
                cardName = '"' + card[3:] + '"'
            else:
                cardName = '"' + card[2:] + '"'
            try:
                if cardName in BasicLands:
                    cards = Card.where(name=cardName).where(setName='Alpha').all()[0]
                else:
                    cards = Card.where(name=cardName).all()[0]
                cardTypes = cards.types
                if(len(cardTypes)==1):
                    cardType = cardTypes[0]
                else:
                    if cardTypes[0] == 'Land':
                        cardType = 'Land'
                    else:
                        cardType = cardTypes[1]

                cardColor = cards.colors
                cardCost = cards.cmc
                
                if(cardType == 'Creature'):
                    createTypeList(Creature, cardColor, card, cardCost)
                elif(cardType == 'Planeswalker'):
                    createTypeList(Planeswalker, cardColor, card, cardCost)
                elif(cardType == 'Sorcery'):
                    createTypeList(Sorcery, cardColor, card, cardCost)
                elif(cardType == 'Instant'):
                    createTypeList(Instant, cardColor, card, cardCost)
                elif(cardType == 'Enchantment'):
                    createTypeList(Enchantment, cardColor, card, cardCost)
                elif(cardType == 'Artifact'):
                    createTypeList(Artifact, cardColor, card, cardCost)        
                elif(cardType == 'Land'):
                    Land.append(card)
                    Land = sorted(Land)
            except:
                print("{} may not be released yet!\n".format(cardName))

    for types in All:
        for i in range(len(types)):
            types[i] = sorted(types[i].items(), key=itemgetter(1))

            
    print("//Creatures")
    for colors in Creature:
        for cards, cost in colors:
            print(cards)
    print("\n//Planeswalkers")
    for colors in Planeswalker:
        for cards, cost in colors:
            print(cards)
    print("\n//Sorceries")
    for colors in Sorcery:
        for cards, cost in colors:
            print(cards)
    print("\n//Instants")
    for colors in Instant:
        for cards, cost in colors:
            print(cards)
    print("\n//Enchantments")
    for colors in Enchantment:
        for cards, cost in colors:
            print(cards)
    print("\n//Artifacts")
    for colors in Artifact:
        for cards, cost in colors:
            print(cards)
    print("\n//Lands")
    for cards in Land:
        print(cards)


