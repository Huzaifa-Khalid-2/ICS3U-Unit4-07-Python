#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program asks for a month and tells how many days it has


def main():
    # this function prints numbers in columns of 5
    counter = 1000
    # process & output
    print("")
    while counter <= 2000:
        print(counter, " ", end="")
        counter = counter + 1
        if counter % 5 == 0:
            print("\n")


if __name__ == "__main__":
    main()
    
