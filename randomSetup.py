#!/usr/bin/env python3

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


def main():
    """Generate a random For Northwood! game setup"""

    rulers_init()


if __name__ == "__main__":
    main()
