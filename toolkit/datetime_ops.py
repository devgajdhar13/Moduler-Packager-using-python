from datetime import datetime
import time

def show_current_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    
def date_difference():
    date_format = "%Y-%m-%d"
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")
    
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        difference = abs((date2 - date1).days)
        print(f"The difference between {date1_str} and {date2_str} is {difference} days.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        
def custom_format_date():
    try:
        date_input = input("Enter a date (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, "%Y-%m-%d")
        
        print("Choose a format:")
        print("1.", date.strftime("%d-%m-%Y"))
        print("2.", date.strftime("%d/%m/%Y"))
        print("3.", date.strftime("%B %d, %Y"))
        print("4.", date.strftime("%A, %d %B %Y"))
        
    except ValueError:
        print("Invalid date.")
        
def stopwatch():
    print("\nstopwatch started.")
    print("press 'Enter' to stop the stopwatch.")

    start = time.time()
    input()
    end = time.time()
    elapsed_time = end - start
    print("Elapsed Time:",round(elapsed_time, 2),"seconds")
       
def countdown_timer():
    
    try:
        seconds = int(
            input("Enter countdown time in seconds: ")
        )

        if seconds < 0:
            print("Enter a positive number!")
            return

        print("\nCountdown started...")

        for i in range(seconds, 0, -1):

            print(i)

            time.sleep(1)

        print("Time's up!")

    except ValueError:
        print("Enter a valid number!")