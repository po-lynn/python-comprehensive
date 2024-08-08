from enum import Enum


class Suite(Enum):
    """Suits (enumeration)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


# from enum import Enum
# class Color(Enum):
#    RED = 1
#    GREEN = 2
#    BLUE = 3

# for color in Color:
#     print(f'{color}: {color.value}')



class Card:
    """Card"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # Get the corresponding characters according to the suits and points of the cards
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    def __lt__(self, other):
        # Compare the size of points with the same suit
        if self.suite == other.suite:
            return self.face < other.face
        # Compare the values corresponding to different suits
        return self.suite.value < other.suite.value
    

card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)    # ♠5 ♥K



import random


class Poker:
    """poker"""

    def __init__(self):
        # Create a list of 52 cards through the generative grammar of lists
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # The current attribute indicates the position where the cards are dealt
        self.current = 0

    def shuffle(self):
        """shuffle"""
        self.current = 0
        # The random random order of the list is realized by the shuffle function of the random module
        random.shuffle(self.cards)

    def deal(self):
        """Licensing"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """Are there any cards left?"""
        return self.current < len(self.cards)
    

poker = Poker()
poker.shuffle()
print(poker.cards)


class Player:
    """player"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """draw cards"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


poker = Poker()
poker.shuffle()
players = [Player('John'), Player('Doe'), Player('Steve'), Player('Maung')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)


    