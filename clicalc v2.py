# Made by Alex Osterrieth 
# Second attempt at CLICalc

from re import L


print("Welcome to CLICalc")

def addition():
    print("Please use the following formula: a + b = c")
    num1 = float(input("Please type the value of a: "))
    num2 = float(input("Please type the value of b: "))
    print(num1, " + ", num2, " = ", num1+num2)
    ending()

def multiplication():
    print("Please use the following formula: a x b = c")
    num1 = float(input("Please type the value of a: "))
    num2 = float(input("Please type the value of b: "))
    print(num1, " x ", num2, " = ", num1*num2)
    ending()

def subtraction():
    print("Please use the following formula: a - b = c")
    num1 = float(input("Please type the value of a: "))
    num2 = float(input("Please type the value of b: "))
    print(num1, " - ", num2, " = ", num1-num2)
    ending()

def division():
    print("Please use the following formula: a / b = c")
    num1 = float(input("Please type the value of a: "))
    num2 = float(input("Please type the value of b: "))
    print(num1, " / ", num2, " = ", num1/num2)
    ending()

# Exit closes the program after the user choses to quit.
def exit():
    print("Thanks for using this calculator")

# Ending() appears after a calculation result is shown to allow the user to perform another calculation if desired
def ending():
    calmake = input("Do you have more calculations to make (yes/no)? ")
    if calmake == "yes":
        main()
    elif calmake == "Yes":
        main()
    elif calmake == "y":
        main()
    elif calmake == "Y":
        main()
    else:
        print("Thanks for chosing to use this calculator.")

# Main is the operation selector.
def main():
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    selection = float(input("Please make your choice: "))

    if selection == 1:
        addition()
    elif selection == 2:
        subtraction()
    elif selection == 3:
        multiplication()
    elif selection == 4:
        division()
    else:
        print("error, please try again")
        main()

# Execution order of the program
main()