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
def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def run():
    while True:
        print("\nWhat operation would you like to do?")
        print("M/m : Multiplication | D/d : Division | A/a : Addition | S/s : Subtraction | Q/q : Quit")
        i = input("Choose an operation: ").strip()
        
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
        
        elif i in ["Q", "q"]:
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid operation.")

        
run()