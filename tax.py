#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 22nd, 2025
# This program will allow a user to enter
# a subtotal, and then display the tax and the
# total including tax.

import constants


def main():
    # get user input
    subtotal = float(input("Enter the subtotal: $"))

    # calculate the tax amount and the total with tax
    tax = subtotal * constants.TAX_RATE_NOVA_SCOTIA / 100
    total = subtotal + tax

    # display the tax amount and the total with
    # the tax
    print("")
    print("You entered a subtotal of ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()
