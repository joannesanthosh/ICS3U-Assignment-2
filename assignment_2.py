#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program calculates the area of a triangle

import math


def main():
    # This function calculates the area of a triangle

    # input
    base_of_triangle = int(input("Enter the base of the triangle (cm): "))
    height_of_triangle = int(input("Enter the height of the triangle (cm): "))

    # process
    area_of_triangle = (base_of_triangle * height_of_triangle) / 2

    # output
    print("")
    print("The area is {0} cm².".format(area_of_triangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
