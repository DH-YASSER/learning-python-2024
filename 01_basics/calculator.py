# Simple CLI calculator
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: division by zero"

def main():
    print("=== Python Calculator ===")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Operator (+, -, *, /): ")
            b = float(input("Enter second number: "))
            ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
            if op in ops:
                print(f"Result: {ops[op](a, b)}")
            else:
                print("Invalid operator")
        except ValueError:
            print("Invalid input")
        if input("Continue? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()
