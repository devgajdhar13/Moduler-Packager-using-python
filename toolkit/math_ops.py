import math

def calculate_factorial():
    
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial cannot be negative!")
            return

        result = math.factorial(number)

        print("Factorial:", result)

    except ValueError:
        print("Enter a valid integer!")
        
def compound_interest():
    
    try:
        principal = float(input("Enter principal amount: "))

        rate = float(input("Enter rate of interest (in %): "))

        years = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** years

        interest = amount - principal

        print("Compound Interest:",round(interest, 2))

        print("Final Amount:",round(amount, 2))

    except ValueError:
        print("Enter valid numbers!")
        
    def trigonometric_calculations():
    
        try:
            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:",round(math.sin(radians), 4))

            print("Cos:",round(math.cos(radians), 4))

            print("Tan:",round(math.tan(radians), 4))

        except ValueError:
            print("Enter a valid angle!")
            
    def area_of_shapes():
    
        print("\nArea of Geometric Shapes:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                radius = float(input("Enter radius: "))

                area = math.pi * radius ** 2

                print("Area of Circle:",round(area, 2))

            elif choice == "2":

                length = float(input("Enter length: "))

                width = float(input("Enter width: "))

                area = length * width

                print("Area of Rectangle:",round(area, 2))
                
            elif choice == "3":
    
                base = float(input("Enter base: "))

                height = float(input("Enter height: "))

                area = 0.5 * base * height

                print("Area of Triangle:",round(area, 2))

            elif choice == "4":

                side = float(input("Enter side: "))

                area = side ** 2

                print("Area of Square:",round(area, 2))

            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter valid numbers!")