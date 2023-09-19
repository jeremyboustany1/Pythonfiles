def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def circle_area(radius):
    return 3.14159 * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("Area of the circle:", area)

    x = float(input("Enter the first numeric value: "))
    y = float(input("Enter the second numeric value: "))

    addition_result = add(x, y)
    subtraction_result = subtract(x, y)
    multiplication_result = multiply(x, y)
    division_result = divide(x, y)

    print("Addition result:", addition_result)
    print("Subtraction result:", subtraction_result)
    print("Multiplication result:", multiplication_result)
    print("Division result:", division_result)

if __name__ == "__main__":
    main()
