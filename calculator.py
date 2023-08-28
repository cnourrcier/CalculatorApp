# calculator.py

def add(x, y):
    # add two numbers and return result
    return x + y

def subtract(x, y):
    #subtract two numbers and return result
    return x - y

def multiply(x, y):
    # multiply two numbers and return result
    return x * y

def divide(x, y):
    # divide two numbers if second number is not 0, then return result
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
# Main program
while True:
    # Displays the options for the user to choose from
    print("\nSelect operation: ")
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit program")

    # Prompt the user for choice from list of options
    choice = input("\nEnter your choice (1 / 2 / 3 / 4 / 5): ")
    
    if choice == '5':
        print("\nExiting program")
        break # Exit the program if the user chooses option 5

    # Prompt the user for two values
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