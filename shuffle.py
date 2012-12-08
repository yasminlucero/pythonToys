## Card Shuffler
##

def shuffleDeck(startDeck):
# input should be a list with integers 1-52 arranged in any order without repeats
    try:
        import random
    except: ImportError
    shuffledDeck = []
    for j in range(52):
        currentDraw = random.randint(0,51-j)
        shuffledDeck.append(startDeck[currentDraw])
        tmp = startDeck.pop(currentDraw)
    return shuffledDeck
    