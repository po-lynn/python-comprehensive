
from enum import Enum
# from enum import Enum

class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def is_weekday(day):
    return day in (DayOfWeek.MONDAY, DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY, DayOfWeek.THURSDAY, DayOfWeek.FRIDAY)

today = DayOfWeek.TUESDAY
print(is_weekday(today))  # Output: True

weekend = (DayOfWeek.SATURDAY, DayOfWeek.SUNDAY)
print(is_weekday(weekend))  # Output: False



class Suite(Enum):
    """Suits (enumeration)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
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

    # https://symbl.cc/e

card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)    # ♠5 ♥K
