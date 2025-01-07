# Arithmetic Operations Function Tasks

def perform_operation(num1, num2, operation):
    """Perform condition statement on operations"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by Zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"