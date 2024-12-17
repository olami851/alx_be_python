# Prompt the user's inputs

num1 = int(input("Enter the first number: ")) # first user's inputted number

num2 = int(input("Enter the second number: ")) # second user's inputted number

operation = input("Choose the operation (+, -, *, /): ") # user's desired inputted operator

#Perform the Calculation Using Match Case:

match operation:
    case "+":
        result = num1 + num2  # Performing addition operation on the numbers

    case "-":
        result = num1 - num2 # Performing subtraction operation on the numbers

    case "*":
        result = num1 * num2 # Performing multiplication operation on the numbers

    case "/":
        if num2 != 0: # Performing non-zero denominator division operation on the numbers
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed." # Performing zero denominator division operation on the numbers

    case _:
        result = "invalid operator" # invalid operator selector case
# Output the Result
print(f"The result is {result}.")

