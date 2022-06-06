#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program prints numbers in colums of 5


def main():
    # This program prints numbers in colums of 5
    print("")
    counter = 1000
    while counter <= 2000:
        print(counter, "", end="")
        counter = counter + 1
        if counter % 5 == 0:
            print("\n")


if __name__ == "__main__":
    main()
