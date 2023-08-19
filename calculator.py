def calculator(operation, input1, input2):

    if operation == 'subtraction':
        x = input1 - input2
        print(x) 
    elif operation == 'multiplication':
        x = input1 * input2
        print(x) 
    elif operation == 'dividing':
        x = input1 // input2
        print(x)    
    elif operation == 'addition':
        x = input1 + input2    
        print(x)    
    else:
        print("Invalid operator. Please enter a valid operation")
        exit()
    
try:
    input1_user = input("Enter a number: ")
    input2_user = input("Enter a number: ")
    int_input1_user = float(input1_user)
    int_input2_user = float(input2_user)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
operation_user = input("Enter an operation: addition, subtraction, multiplication or dividing: ")
calculator(operation_user, int_input1_user, int_input2_user)

