# Made by Alex Osterrieth
# Don't judge this too hard, it's my first program made. ever.

# Strings of text used throughout the program:
textresult = "The result is: "

# In case of an error encountered
def error():
    print("Error, try again")
    main()

# Code of main body, aka main()
def main():
    # Get the user to select the type of operation they would like to perform
    print("What operation would you like to perform?")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    operation = int(input("Make your choice: "))

    # selection of numbers
    num1= int(input("Enter your first number: "))
    num2= int(input("Enter your second number: "))

    numadd = num1+num2
    numsub = num1-num2
    nummul = num1*num2
    numdiv = num1/num2

    # Opeation selection
    if operation == 1:
        print(textresult, numadd)
    elif operation == 2:
        print(textresult, numsub)
    elif operation == 3:
        print(textresult, nummul)
    elif operation == 4:
        print(textresult, numdiv)
    else:
        error()
    
    finalstep()

# End
def end():
    print("Thanks for using this calculator")
    print("Goodbye!")

#define final step
def finalstep():
    endtest = (input("Do you have additional calculations to make (yes/no): "))

    if endtest == "yes":
        main()
    elif endtest == "Yes":
        main()
    elif endtest == "y":
        main()
    elif endtest == "Y":
        main()
    else:
        end()

# Program execution order
main()