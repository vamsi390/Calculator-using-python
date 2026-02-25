🧮 Simple Python Calculator

This is a basic command-line calculator built using Python.
It allows users to perform simple arithmetic operations:

-Addition

-Subtraction

-Multiplication

-Division

📌 Features

-Interactive user input

-Continuous calculations using a loop

-Handles invalid numeric inputs

-Prevents division by zero

-Displays results formatted to 2 decimal places

🛠️ Technologies Used

Python 3

Basic Functions

While Loop

Conditional Statements

Exception Handling (try-except)

📂 File Structure
calculator.py
README.md
▶️ How to Run

Make sure Python 3 is installed.

Save the file as calculator.py.

Open terminal or command prompt.

Run the program:

python calculator.py
📖 How It Works

The program displays a menu:

1. Add
2. Subtract
3. Multiply
4. Divide

User selects an operation.

User enters two numbers.

The selected function performs the calculation.

The result is displayed.

User can continue or exit.

🧠 Functions Used
➕ add(x, y)

Returns the sum of two numbers.

➖ subtract(x, y)

Returns the difference of two numbers.

✖️ multiply(x, y)

Returns the product of two numbers.

➗ divide(x, y)

Returns the division of two numbers.

⚠️ Error Handling

If the user enters non-numeric input → Shows error message.

If division by zero is attempted → Displays warning.

If invalid menu option is selected → Shows "Invalid Input".

📸 Sample Output
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide

Enter choice(1/2/3/4): 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.00
Let's do next calculation? (yes/no): no
Thanks for using the calculator!
