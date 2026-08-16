from toolkit import datetime_ops, math_ops, random_ops, uuid_ops, file_ops, dir_explorer
 

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            datetime_ops.show_current_datetime()
        elif choice == "2":
            datetime_ops.date_difference()
        elif choice == "3":
            datetime_ops.custom_format_date()
        elif choice == "4":
            datetime_ops.stopwatch()
        elif choice == "5":
            datetime_ops.countdown_timer()
        elif choice == "6":
            break
        else:
            print("Please enter a valid choice!")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            math_ops.calculate_factorial()
        elif choice == "2":
            math_ops.compound_interest()
        elif choice == "3":
            math_ops.trigonometric_calculations()
        elif choice == "4":
            math_ops.area_of_shapes()
        elif choice == "5":
            break
        else:
            print("Please enter a valid choice!")
 
def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            random_ops.generate_random_number()
        elif choice == "2":
            random_ops.generate_random_list()
        elif choice == "3":
            random_ops.generate_random_password()
        elif choice == "4":
            random_ops.generate_random_otp()
        elif choice == "5":
            break
        else:
            print("Please enter a valid choice!")

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            file_ops.create_file()
        elif choice == "2":
            file_ops.write_file()
        elif choice == "3":
            file_ops.read_file()
        elif choice == "4":
            file_ops.append_file()
        elif choice == "5":
            break
        else:
            print("Please enter a valid choice!")

def main_menu():
    while True:
       
        print("Welcome to Multi-Utility Toolkit")
      
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_ops.generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            dir_explorer.explore_module()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Please enter a valid choice!")

if __name__ == "__main__":
    main_menu()