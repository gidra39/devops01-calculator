def calculator(operation, float_num1, float_num2):

    if operation == '1':
        x = float_num1 + float_num2
        print(x) 
    elif operation == '2':
        x = float_num1 - float_num2
        print(x) 
    elif operation == '3':
        x = float_num1 * float_num2
        print(x)    
    elif operation == '4':
        x = float_num1 // float_num2    
        print(x)    
    else:
        print("Invalid operator. Please enter a valid operation")
        exit()
    
try:
    float_num1 = float(input("Enter first number: "))
    float_num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
operation_user = input("Enter an operation (1 - addition, 2 - subtraction, 3 - multiplication or 4 - dividing): ")
calculator(operation_user, float_num1, float_num2)

