# 1. Get numbers and operation from the user
num1 = float(input("Enter the first number: ")) # Using float() to handle decimals
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# 2. Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation entered!"

# 3. Print the result using an f-string
print(f"{num1} {operation} {num2} = {result}")