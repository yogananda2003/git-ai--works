def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if op not in operations:
        print("Invalid operator")
        return

    result = operations[op](a, b)
    print(f"Result: {a} {op} {b} = {result}")

if __name__ == "__main__":
    calculator()
