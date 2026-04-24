def calculator():
    print("Simple Error-Safe Calculator")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)

        elif op == "-":
            print("Result:", num1 - num2)

        elif op == "*":
            print("Result:", num1 * num2)

        elif op == "/":
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed!")
            else:
                print("Result:", num1 / num2)

        else:
            print("❌ Error: Invalid operator!")

    except ValueError:
        print("❌ Error: Please enter valid numbers!")

    except Exception as e:
        print("❌ Unexpected Error:", e)


# Run calculator
calculator()