# calculator.py

# add two numbers and return result
def add(x, y):
    return x + y

#subtract two numbers and return result
def subtract(x, y):
    return x - y

# multiply two numbers and return result
def multiply(x, y):
    return x * y

# divide two numbers if second number is not 0, then return result
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
# Main program
while True:
    print("\nSelect operation: ")
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit program")

    choice = input("\nEnter your choice (1 / 2 / 3 / 4 / 5): ")
    
    if choice == '5':
        print("\nExiting program")
        break

    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("\nEnter the second number: "))

    if choice == '1':
        print("\nResult: ", add(num1,num2))
    elif choice == '2':
        print("\nResult: ", subtract(num1,num2))
    elif choice == '3':
        print("\nResult: ", multiply(num1,num2))
    elif choice == '4':
        print("\nResult: ", divide(num1,num2))
    else:
        print("\nInvalid input")