def calculator(operation, input1, input2):

    if operation == 'subtraction':
        x = input1 - input2
    elif operation == 'multiplication':
        x = input1 * input2
    elif operation == 'dividing':
        x = input1 // input2   
    elif operation == 'addition':
        x = input1 + input2        
        
    print(x)
    return x
    

input1_user = input("Enter a number: ")
input2_user = input("Enter a number: ")
int_input1_user = int(input1_user)
int_input2_user = int(input2_user)
operation_user = input("Enter an operation: addition, subtraction, multiplication or dividing: ")
calculator(operation_user, int_input1_user, int_input2_user)

