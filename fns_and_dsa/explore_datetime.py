from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
        try:
            number_of_days = int(input("Enter the number of days to add to the current date: "))

            current_date =datetime.now()

            future_date = current_date + timedelta(days = number_of_days)

            formatted_future_date = future_date.strftime("%Y-%m-%d")

            print("Future Date:", formatted_future_date)

        except ValueError:
            print("Please enter a valid interger for the number of days.")
    display_current_datetime()
    calculate_future_date()
