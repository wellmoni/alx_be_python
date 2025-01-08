def perform_operation(num1, num2, operation):
    
    """
    this is going to perform a basic arithmetic operation: addition, subtraction, multiplication or division.
    Parameter:
        num1 (float): First number.
        num2 (floa): second number.
        operation (str): This operation to perform ('add', 'substract', 'multiply', 'divide')
    Returns:
        Float or srt:
    """
    if operation == "add":
        return num1 + num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif opeartion == "divide":
        if num2 == 0:
            return "Error: Zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid Operation."
