num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = str(input("Choose the operation(+, -, *, /"):)

match operation

case "+":
    result = num1 + num2
    print(f"The result is {result}.")
case "-":
    result = num1 -num1
    print(f"The result is {result}.")
case "*":
    result = num1 * num2
    print (f"The result is {result}.")
case "/":
            if num2 == 0:
                print("Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
case "_":
    print("Invalid operator")

