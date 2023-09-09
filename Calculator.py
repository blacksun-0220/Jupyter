# Greetings
while True:
    print("Welcome to the Simple Calculator!")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")
    print("\n")
# Get user's choice
    choice = input("Enter your choice: ")
# exit the program if choosing exit
    if choice in ("exit"):
        print("Thank you for using the Simple Calculator!")
        break
# Check if choice is not one of the four options
    if choice not in ("add","subtract","multiply","divide"):
        print("Invalid input. Please enter a valid operation.")
        continue
        
# Get user's numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
# Calculator functions
    if choice == "add":
        sum_result= num1 + num2
        print(f"Result: {num1} + {num2} = {sum_result}")
    elif choice == "substract":
        sub_result = num1 - num2
        print(f"Result: {num1} - {num2} = {sub_result}")
    elif choice == "multiple":
        mul_result = num1 * num2
        print(f"Result: {num1} * {num2} = {mul_result}")
    elif choice == "divide":
        div_result = int(num1 / num2)
        print(f"Result: {num1} / {num2} = {div_result}")
