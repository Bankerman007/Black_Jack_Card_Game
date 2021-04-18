"""Program that is a Black Jack Card game"""

"""Import module that will randomize card deck"""
import random


class Card:
        def __init__(self, value, suit):
            self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] [value - 1]
            self.suit = '♥♦♣♠' [suit]

        def card_image(self):
            print('┌───────┐')
            print(f'| {self.value:<2}    |')
            print('|       |')
            print(f'|   {self.suit}   |')
            print('|       |')
            print(f'|    {self.value:>2} |')
            print('└───────┘') 

        def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost
