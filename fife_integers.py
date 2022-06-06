#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program prints numbers in colums of 5


def main():
    # this function uses a nested loop

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 == 4:
            print("{}".format(counter))
        else:
            print("{} ".format(counter), end="")


if __name__ == "__main__":
    main()
