def add_numbers(a, b):
    return a + b

while True:
    # Ask for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Call the function with the numbers
    result = add_numbers(num1, num2)

    # If the result is 20, do something and break the loop
    if result == 20:
        print("The result is 20. Doing something...")
        break
    else:
        print("The result is not 20. Asking again...")