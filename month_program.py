#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program asks for a month and tells how many days it has


def main():
    # This program asks for a month and tells how many days it has
    print("This program asks you for a month and tells how many days it has.")
    print("")

    # input
    user_month = input("Insert any month: ")
    print("")

    # process and output
    if user_month == "January":
        print("31 days")
    elif user_month == "February":
        print("28 days (unless its a leap year)")
    elif user_month == "March":
        print("31 days")
    elif user_month == "April":
        print("30 days")
    elif user_month == "May":
        print("31 days")
    elif user_month == "June":
        print("30 days")
    elif user_month == "July":
        print("31 days")
    elif user_month == "August":
        print("31 days")
    elif user_month == "September":
        print("30 days")
    elif user_month == "October":
        print("31 days")
    elif user_month == "November":
        print("30 days")
    elif user_month == "December":
        print("31 days")
    else:
        print("Bro what is that answer (・_・ヾ I asked for a month.")
    print("\nDone")


if __name__ == "__main__":
    main()
