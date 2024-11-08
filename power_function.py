def power(x,y):
    if y== 0:
        return 1
    elif y > 0:
        return x * power(x, y-1)
    else:
        return 1 / power(x, -y)

def main():
    try:
        x = float(input("Enter the base (x): "))
        y = int(input("Enter the exponent (y): "))

        result = power(x, y)
        print(f"{x}^{y} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero encountered for x = 0 with a negative exponent.")


if __name__ == "__main__":
    main()
