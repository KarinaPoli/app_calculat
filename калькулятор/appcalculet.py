def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: Ділення на нуль!"
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Простий CLI-калькулятор")
    parser.add_argument("operation", choices=["add", "subtract"], help="Операція: add (додавання) або subtract (віднімання)")
    parser.add_argument("a", type=float, help="Перше число")
    parser.add_argument("b", type=float, help="Друге число")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = multiply(args.a, args.b)
    elif args.operation == "divide":
        result = divide(args.a, args.b)

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
