def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

print("Simple Calculator")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose operation (enter the corresponding number or symbol): ")

# Check if both numbers are integers
both_integers = num1.is_integer() and num2.is_integer()

# Calculation
result = None
if operation == '1' or operation == '+':
    result = add(num1, num2)
elif operation == '2' or operation == '-':
    result = subtract(num1, num2)
elif operation == '3' or operation == '*':
    result = multiply(num1, num2)
elif operation == '4' or operation == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation")

# Display result
if result is not None:
    if both_integers and result.is_integer():
        result = int(result)
    print("Result:", result)

