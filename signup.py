#!/usr/bin/python3

def signup():
    firstName = input("Enter your first name:\n")
    lastName = input("Enter your last name:\n")
    password = input("Enter your password:\n")

    try:
        if firstName.isdigit() or lastName.isdigit():
            raise TypeError("Invalid first name or last name")
        if not firstName or not lastName:
            raise ValueError("You must provide both \
your first name and last name!")
        if not password:
            raise ValueError("Please enter a password")

    except Exception as e:
        print(e)
    else:
        count = 0
        userName = firstName[0] + lastName
        file = open("usernames.txt", "r")
        for line in file:
            data = line.split(",")
            if firstName == data[2] and lastName == data[3]:
                count = count + 1
        file.close()

        if count > 0:
            text = userName + str(count) + "," + password + "," + firstName + "," + lastName + ",\n"
        else:
            text = userName + "," + password + "," + firstName + "," + lastName + ",\n"

        file = open("usernames.txt", "a")
        file.write(text)
        print("Signed up")
        if count > 0:
            userName = userName + str(count)
        print("Your username is {}".format(userName))
        file.close()
