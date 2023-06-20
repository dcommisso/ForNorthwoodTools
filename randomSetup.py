#!/usr/bin/env python3

from random import shuffle

suits = ["artigli",
        "fiori",
        "occhi",
        "foglie"]

royal_titles = ["Fante",
          "Regina",
          "Re",
          "Principe",
          "Marchesa",
          "Barone"]


def rulers_init():
    """This function initialize the rulers array"""

    rulers = {}

    for suit in suits:
        rulers[suit] = []
        for title in royal_titles:
            rulers[suit].append(title + " di " + suit.capitalize())
    return rulers


def random_setup(rulers):
    """Return 4 random allies and 8 random neutral rulers"""

    allies = []
    neutrals = []
    for suit in rulers.keys():
        shuffle(rulers[suit])
        allies.append(rulers[suit][0])
        neutrals.append(rulers[suit][1])
        neutrals.append(rulers[suit][2])
    shuffle(neutrals)
    return allies, neutrals


def pretty_print_allies(allies):
    """Print allies in human-readable format"""
    print("I tuoi alleati sono: " + ', '.join(allies))


def pretty_print_neutrals(neutrals):
    """Print neutrals in human-readable format"""

    print("I sovrani neutrali sono:\n")
    for fief, ruler in enumerate(neutrals):
        print(f'Feudo {fief:d} -> {ruler:s}')


def main():
    """Generate a random For Northwood! game setup"""

    rulers = rulers_init()
    allies, neutrals = random_setup(rulers)
    pretty_print_allies(allies)
    print("--------")
    pretty_print_neutrals(neutrals)


if __name__ == "__main__":
    main()
