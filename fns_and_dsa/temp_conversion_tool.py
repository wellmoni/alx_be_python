FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main()

    try:
        temp = float(input("Enter the temperature to convert:"))
        unit = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
                converted_temp = convert_to_fahrenheit(temp)
                print (f"{temp}°C is equal to {converted_temp:.2f}°F")
        elif unit =="F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        except ValueError as e:
            print("error:", e)

    if __name__ == "__main__":
        main()
