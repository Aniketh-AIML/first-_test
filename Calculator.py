# calculator 

user_input = input("Enter the operation you want to perform  ")

if user_input == "add":
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    result = num1 + num2
    print("The result is ", result)

elif user_input == "subtract":
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    result = num1 - num2
    print("The result is ", result)

elif user_input == "multiply":
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    result = num1 * num2
    print("The result is ", result)

elif user_input == "divide":
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    if num2 != 0:
        result = num1 / num2
        print("The result is ", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation. Please choose add, subtract, multiply, or divide.")



        