# Explore datetime in python

from datetime import datetime, timedelta

def display_current_datetime():
    """creating a variable named current_date"""
    current_date = datetime.now()

    """formatting the current date and time in readable format"""
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    """output the current date in readable format using f-string"""
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    """prompt user for number of days to be added to current date"""
    number_of_day = int(input("Enter the number of days to add to the current date: "))

    """get the current date"""
    current_date = datetime.now()

    """creating a variable named future_date"""
    future_date = current_date + timedelta(days=number_of_day)

    """creating a formatted and readable future date form"""
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    """print a formatted future date using f-string """
    print(f"Future date: {formatted_future_date}")

display_current_datetime()
calculate_future_date()


