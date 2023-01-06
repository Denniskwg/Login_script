#!/usr/bin/python3
#My login script
def login():
    print("#####################")
    print("#   Login Screen   ##")
    print("#####################")

    i = 3
    j = 0
    while i > 0:
        username = input("Username? ")
        password = input("password? ")

        file = open("usernames.txt", "r")
        for line in file:
            data = line.split(",")
            if username == data[0] and password == data[1]:
                j = 1
                break;
        if j == 1:
            print("You are logged in")
            break
        else:
            print("Wrong username or password")
            i = i - 1
            if i != 0:
                print("{:d} attempts left".format(i))
