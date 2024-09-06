def input_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            num = float(user_input)
            return num
        except ValueError:
            print("Invalid input. Please enter a real number.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by 0!"
    return x / y

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

print("Select calculation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Greatest Common Divisor")

choice = input("Enter your selection (1/2/3/4/5): ")

num1 = input_number("Enter the first number: ")
num2 = input_number("Enter the second number: ")

if choice == '1':
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
    print(f"Result: GCD({num1}, {num2} = {gcd(num1, num2)}")   
else:
    print("Invalid selection!")
