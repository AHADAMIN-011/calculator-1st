def calculator():
    print("WELCOME TO THE CALCULATOR")
    print("PLEASE SELECT AN OPRATION")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")

    operation = input("SELECT AN OPERATION 1,2,3,4:")

    var1 = float(input("ENTER FIRST NUMBER :"))
    var2 = float(input("ENTER SECOND NUMBER :"))

    if operation == '1':
        print(f"Output: {var1} + {var2} = {var1 + var2}")
    elif operation == '2':
        print(f"Output: {var1} - {var2} = {var1 - var2}")
    elif operation == '3':
        print(f"Output: {var1} * {var2} = {var1 * var2}")
    elif operation == '4':
        if var2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Output: {var1} / {var2} = {var1 / var2}")
    else:
        print("Invalid operation selected. Please choose a valid option.")

# we used calculator function to perform the operation
calculator()