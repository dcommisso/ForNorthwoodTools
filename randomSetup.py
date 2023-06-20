#!/usr/bin/env python3

semi = ["artigli",
        "fiori",
        "occhi",
        "foglie"]

figure = ["Fante",
          "Regina",
          "Re",
          "Principe",
          "Marchesa",
          "Barone"]

# rulers = {}
#
# for seme in semi:
#     rulers[seme] = []
#     for figura in figure:
#         rulers[seme].append(figura + " di " + seme)
#


def rulers_init():
    """This function initialize the rulers array"""

    rulers = {}

    for seme in semi:
        rulers[seme] = []
        for figura in figure:
            rulers[seme].append(figura + " di " + seme.capitalize())
    print(rulers)


def main():
    """Generate a random For Northwood! game setup"""

    rulers_init()


if __name__ == "__main__":
    main()
