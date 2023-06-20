#!/usr/bin/env python3

from random import shuffle

suits = ["artigli",
        "fiori",
        "occhi",
        "foglie"]

figure = ["Fante",
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
        for figura in figure:
            rulers[suit].append(figura + " di " + suit.capitalize())
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


def main():
    """Generate a random For Northwood! game setup"""

    rulers = rulers_init()
    allies, neutrals = random_setup(rulers)


if __name__ == "__main__":
    main()
