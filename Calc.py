# This function adding two numbers
def add(x, y):
    return x + y

# This function subtracting two numbers
def subtract(x, y):
    return x - y

# This function multiplying two numbers
def multiply(x, y):
    return x * y

# This function dividing two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choose = input("Enter choice(1/2/3/4): ")
    if choose in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choose == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result:.2f}")  
        elif choose == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result:.2f}")
        elif choose == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result:.2f}")
        elif choose == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result:.2f}")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            print("Thanks for using the calculator!")
            break
    else:
        print("Invalid Input")
