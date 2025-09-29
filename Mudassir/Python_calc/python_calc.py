def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        return "ERROR!"
    else:
        return x/y
    
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is EVEN"
    else:
        return f"{num} is ODD"
    
def percentage(part, whole):
    if whole == 0:
        return "ERROR!"
    else:
        return (part/whole) * 100

while True:  

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Check Even/Odd")
    print("6. Percentage")
    print("7. Exit")


    choice = input("Enter your CHOICE (1-7):")

    if choice == "1":
        x = float(input("Enter 1st Number:"))
        y = float(input("Enter 2nd Number:"))
        print("Result:", add(x,y))

    elif choice == "2":
        x = float(input("Enter 1st Number:"))
        y = float(input("Enter 2nd Number:"))
        print("Result:", subtract(x,y))

    elif choice == "3":
        x = float(input("Enter 1st Number:"))
        y = float(input("Enter 2nd Number:"))
        print("Result:", multiply(x,y))

    elif choice == "4":
        x = float(input("Enter 1st Number:"))
        y = float(input("Enter 2nd Number:"))
        print("Result:", divide(x,y))

    elif choice == "5":
        num = int(input("Enter a Number:"))
        print(even_odd(num))

    elif choice == "6":
        part = float(input("Enter Part:"))
        whole = float(input("Enter Whole:"))
        print("Result:", percentage(part,whole), "%" )

    elif choice == "7":
        print("Thanks!")
        break

    else:
        print("Error! Try Again")