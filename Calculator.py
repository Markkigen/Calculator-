import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def calculator():
    print("\nAdvanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter choice (1-7): ")
        
        if choice == '7':
            print("Exiting Calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            operations = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': divide,
                '5': power
            }
            
            result = operations[choice](num1, num2)
            print(f"Result: {result}")
        
        elif choice == '6':
            num = float(input("Enter the number: "))
            print(f"Square root: {sqrt(num)}")
        
        else:
            print("Invalid choice. Please select a valid option.")

calculator()
