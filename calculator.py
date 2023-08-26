try:
    input1 = float(input("Enter first number: "))
    input2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

operation = input("Enter an operation (1 - addition, 2 - subtraction, 3 - multiplication or 4 - division): ")

def calculator(operation, input1, input2):

    if operation in ["1", "2", "3", "4"]:
        if operation == '1':
            calc_result = input1 + input2
        elif operation == '2':
            calc_result = input1 - input2
        elif operation == '3':
            if input1 == 0 or input2 == 0:
                calc_result = 0
            else:
                calc_result = input1 * input2
        elif operation == '4':
            if input1 == 0 or input2 == 0:
                calc_result = 0
            else:
                calc_result = input1 // input2
    else:
        print("Invalid operator. Please enter a valid operation")
        exit()

    print("Result is: ", calc_result)

calculator(operation, input1, input2)