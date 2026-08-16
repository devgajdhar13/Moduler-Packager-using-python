import random
import string


def generate_random_number():

    try:
        minimum = int(input("Enter minimum value: "))
        maximum = int(input("Enter your maximum value: "))

        number = random.randint(minimum, maximum)

        print("Generated random number:", number)

    except ValueError:
        print("Enter valid numbers!")


def generate_random_list():

    try:
        length = int(input("Enter list length: "))

        minimum = int(input("Enter minimum number: "))
        maximum = int(input("Enter maximum number: "))

        random_list = []

        for i in range(length):random_list.append(random.randint(minimum, maximum))

        print("Generated Random List:", random_list)

    except ValueError:
        print("Enter valid numbers!")


def generate_random_password():

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password should have at least 4 characters.")
            return

        characters = (string.ascii_letters+ string.digits+ string.punctuation)

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Random Password:", password)

    except ValueError:
        print("Enter a valid password length!")


def generate_random_otp():

    try:
        length = int(input("Enter OTP length: "))

        if length <= 0:
            print("OTP length must be greater than 0.")
            return

        otp = ""

        for i in range(length):
            otp += random.choice(string.digits)

        print("Generated OTP:", otp)

    except ValueError:
        print("Enter a valid OTP length!")