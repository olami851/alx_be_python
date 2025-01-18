def safe_divide(numerator, denominator):
    try:
        # convert inputs to float
        num = float(numerator)
        deno = float(denominator)

        # perform division
        result = num/deno
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # handling zero division
        return f"Error: Cannot divide by zero."

    except ValueError:
        # handling value error division
        return f"Error: Please enter numeric values only."

