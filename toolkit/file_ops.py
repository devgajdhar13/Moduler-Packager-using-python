from pathlib import Path


def create_file():

    filename = input("Enter file name: ")

    try:

        file = Path(filename)

        file.touch(exist_ok=False)

        print("File created successfully!")

    except FileExistsError:

        print("File already exists!")

    except Exception as error:

        print("Error:", error)


def write_file():

    filename = input("Enter file name: ")

    data = input("Enter data to write: ")

    try:

        with open(filename,"w",encoding="utf-8") as file:

            file.write(data)

        print("Data written successfully!")

    except Exception as error:

        print("Error:", error)


def read_file():

    filename = input("Enter file name: ")

    try:

        with open(filename,"r",encoding="utf-8") as file:

            content = file.read()

        print("\nFile Content:")
        print(content)

    except FileNotFoundError:

        print("File not found!")

    except Exception as error:

        print("Error:", error)


def append_file():

    filename = input("Enter file name: ")

    data = input("Enter data to append: ")

    try:

        with open(filename,"a",encoding="utf-8") as file:

            file.write("\n" + data)

        print("Data appended successfully!")

    except Exception as error:

        print("Error:", error)