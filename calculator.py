import math

# Idk what to explain for the functions below they're pretty self explanitory
def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def multiply(x, y):
    return x * y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error! Cannot take the square root of a negative number."
# Determines whether input is numbers or not
def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def run():
    #While true to have continous use of calculator
    while True:
        print("\nWhat operation would you like to do?")
        print("M/m : Multiplication | D/d : Division | A/a : Addition | S/s : Subtraction | Q/q : Quit")
        print("E/e : Exponentiation | Mod/mod : Modulus | SQ/sq : Square Root | Q/q : Quit")
        i = input("Choose an operation: ").strip()
        #get_number Gets the value of a numeric field in this sample 
        if i in ["M", "m"]:
            x = get_number("X = ")
            y = get_number("Y = ")
            print(f"{x} * {y} = {multiply(x, y)}")
            
        elif i in ["S", "s"]:
            x = get_number("X = ")
            y = get_number("Y = ")
            print(f"{x} - {y} = {subtract(x, y)}")
            
        elif i in ["A", "a"]:
            x = get_number("X = ")
            y = get_number("Y = ")
            print(f"{x} + {y} = {addition(x, y)}")
            
        elif i in ["D", "d"]:
            x = get_number("X = ")
            y = get_number("Y = ")
            print(f"{x} / {y} = {divide(x, y)}")
        
        elif i in ["E", "e"]:
            x = get_number("Enter the base number (X): ")
            y = get_number("Enter the exponent (Y): ")
            print(f"Result: {x} ^ {y} = {exponentiate(x, y)}")
        
        elif i.lower() in ["mod"]:
            x = get_number("Enter the first number (X): ")
            y = get_number("Enter the second number (Y): ")
            print(f"Result: {x} % {y} = {modulus(x, y)}")
        
        elif i.lower() in ["sq", "SQ"]:
            x = get_number("Enter the number to find the square root of (X): ")
            print(f"Result: √{x} = {square_root(x)}")
        
        elif i in ["Q", "q"]:
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid operation.")

        
run()