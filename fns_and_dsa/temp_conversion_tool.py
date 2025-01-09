# Defining the two Global variables

FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9) # F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) # C to F

# function to convert the temperatures from Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """convert temperature in Fahrenheit to Celsius function"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# function to convert the temperatures from Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """convert temperature in Celsius to Fahrenheit function"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# main function
def main():
    try:

        """users temperature value to be converted prompt"""
        user_temp = float(input("Enter the temperature to convert: "))

        """unit of user temperature value prompt"""
        user_temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        """control statement"""

        if user_temp_unit == "C":
            converted_temp = convert_to_fahrenheit(user_temp)
            print(user_temp, '', chr(176), 'C', ' ', 'is', ' ', converted_temp, chr(176), 'F', sep='')

        elif user_temp_unit == "F":
            converted_temp = convert_to_celsius(user_temp)
            print(user_temp, '', chr(176), 'F', ' ', 'is', ' ', converted_temp, chr(176), 'C', sep='')

        else:
            print("Invalid temperature unit. Please enter 'C' for Celsius and 'F' for Fahrenheit")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()


