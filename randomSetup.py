#!/usr/bin/env python3

from random import shuffle
import argparse


class RulersDeck:
    """A deck of For Northwood! ruler cards"""

    def __init__(self):

        self.undrawn_cards = {}
        self.allies = []
        self.neutrals = []

        suits = ["artigli",
                 "fiori",
                 "occhi",
                 "foglie"]

        royal_titles = ["fante",
                        "regina",
                        "re",
                        "principe",
                        "marchesa",
                        "barone"]

        for suit in suits:
            self.undrawn_cards[suit] = []
            for title in royal_titles:
                self.undrawn_cards[suit].append(title + " di " + suit)

    def __shuffle_by_suits(self):
        """Shuffle each suit separately"""

        for suit in self.undrawn_cards.keys():
            shuffle(self.undrawn_cards[suit])

    def __remove_card_from_deck(self, card):
        suit_of_card_to_remove = card.split()[2].lower()
        self.undrawn_cards[suit_of_card_to_remove].remove(card.lower())

    def draw_neutral_rulers(self):
        """Draw 8 neutral rulers, 2 per suit"""

        self.__shuffle_by_suits()
        for suit in self.undrawn_cards:
            for _ in range(2):
                self.neutrals.append(self.undrawn_cards[suit][0])
                self.__remove_card_from_deck(self.undrawn_cards[suit][0])
        shuffle(self.neutrals)

    def draw_allies(self, allies_to_draw=None):
        """Draw specified allies from the deck or 4 random allies if no card
        has been specified"""

        if allies_to_draw:
            for ally in allies_to_draw:
                self.allies.append(ally.lower())
                self.__remove_card_from_deck(ally)
        else:
            self.__shuffle_by_suits()
            for suit in self.undrawn_cards:
                self.allies.append(self.undrawn_cards[suit][0])
                self.__remove_card_from_deck(self.undrawn_cards[suit][0])

    def pretty_print_allies(self):
        """Print allies in human-readable format"""

        print("I tuoi alleati sono: " + ', '.join(self.allies).title())

    def pretty_print_neutrals(self):
        """Print neutrals in human-readable format"""

        print("I sovrani neutrali sono:\n")
        for fief, ruler in enumerate(self.neutrals):
            print(f'Feudo {fief:d} -> {ruler:s}'.title())


def main():
    """Generate a random For Northwood! game setup"""

    parser = argparse.ArgumentParser(description='Random setup generator for\
    "For Northwood!" game')

    parser.add_argument('--allies', type=str,
                        help='Allies to draw separated by comma')
    args = parser.parse_args()

    deck = RulersDeck()
    deck.draw_allies(args.allies.split(','))
    deck.draw_neutral_rulers()
    deck.pretty_print_allies()
    deck.pretty_print_neutrals()


if __name__ == "__main__":
    main()
