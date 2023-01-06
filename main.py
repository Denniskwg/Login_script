#!/usr/bin/python3
from login import login
from signup import signup

def main():
    option = input("For Login enter 'l' for Signup enter 's'\n")
    try:
        if type(option) != str:
            raise TypeError("Please Enter valid option")
        if not option == 's' and not option == 'l':
            raise ValueError("Please Enter valid option")
    except Exception as e:
        print(e)
    else:
        if option == 'l':
            login()
        else:
            print("###########################")
            print("#### Welcome to signup ####")
            print("###########################")
            signup()

main()
